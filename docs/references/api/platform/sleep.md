#### Sleep

There is only one sleep function in Mbed OS 5.6:

```c++
void sleep();
```

This function invokes sleep manager, which we introduce below.

The idle loop invokes sleep manager by default. You can overwrite this default behavior by attaching a different idle hook function pointer.

```c++
void new_idle_loop()
{
    // do nothing
}

void main()
{
    rtos_attach_idle_hook(&new_idle_loop);
}
```

##### Sleep modes

There are two available sleep modes:

1. Sleep mode

    The system clock to the core stops until a reset or an interrupt occurs. This eliminates dynamic power that the processor, memory systems and buses use. This mode maintains the processor, peripheral and memory state, and the peripherals continue to work and can generate interrupts.

    You can wake up the processor by any internal peripheral interrupt or external pin interrupt.

2. Deep sleep mode 

    This processor is set up ready for deep sleep, and sent to sleep. This mode has the same sleep features as sleep, and it also powers down peripherals and high speed clocks. This mode maintains all state. You can only wake up the processor by lp ticker, RTC, an external interrupt on a pin or a watchdog timer.

##### Sleep manager

The sleep manager provides an API to control sleep modes. Deep sleep might introduce some power savings that can affect an application, for instance high speed clock dependent drivers.

The `DeepSleepLock` class provides an RAII object for disabling sleep, or explicit lock/unlock methods. To prevent an application from entering deep sleep, invoke the `DeepSleepLock()::lock()` method. As soon as an application is ready for the deep sleep, allow it by invoking the `DeepSleepLock::unlock()` method.

These Mbed OS drivers contain locking deep sleep:

- `Ticker`.
- `Timeout`.
- `Timer`.
- `SPI`.
- `I2C`.
- `CAN`.
- `SerialBase`.

##### `Sleep Manager` class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.6/api/mbed__sleep_8h_source.html)

##### `Deep Sleep Lock` class reference

[![View code](https://www.mbed.com/embed/?type=library)](/docs/v5.4/mbed-os-api-doxy/classmbed_1_1_deep_sleep_lock.html)

##### Example

This example shows SPI asynchronous transfer with deep sleep locking.

```c++

SPI::transfer(const Type *tx_buffer, int tx_length, Type *rx_buffer, int rx_length, const event_callback_t& callback, int event = SPI_EVENT_COMPLETE)
{
    if (spi_active(&_spi)) {
        return queue_transfer(tx_buffer, tx_length, rx_buffer, rx_length, sizeof(Type)*8, callback, event);
    }
    // This driver requires high speed clock, needs to wait for complete flag set via a callback to unblock the deep sleep
    sleep_manager_lock_deep_sleep();
    start_transfer(tx_buffer, tx_length, rx_buffer, rx_length, sizeof(Type)*8, callback, event);
    return 0;
}


void SPI::irq_handler_asynch(void)
{
    int event = spi_irq_handler_asynch(&_spi);
    if (_callback && (event & SPI_EVENT_ALL)) {
        _callback.call(event & SPI_EVENT_ALL);
    }
    if (event & (SPI_EVENT_ALL | SPI_EVENT_INTERNAL_TRANSFER_COMPLETE)) {
        // all data should be written now, unlock the deep sleep
        sleep_manager_unlock_deep_sleep();
#if TRANSACTION_QUEUE_SIZE_SPI
        // SPI peripheral is free (event happend), dequeue transaction
        dequeue_transaction();
#endif
    }
}
```
