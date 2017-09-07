#### Sleep

There is only one sleep function in the Mbed OS 5.6

```c++
void sleep();
```

This function invokes Sleep manager that is introduced below.

It is invoked in the idle loop by default. This default behaviour can be overwritten by attaching a different the idle hook function pointer.


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

    The system clock to the core is stopped until a reset or an interrupt occurs. This eliminates dynamic power used by the processor, memory systems and buses. The processor, peripheral and memory state are maintained, and the peripherals continue to work and can generate interrupts.

    The processor can be woken up by any internal peripheral interrupt or external pin interrupt.

    The wake-up time should be less than 10 us.

2. Deep sleep mode 

    This processor is setup ready for deep sleep, and sent to sleep. This mode
    has the same sleep features as sleep plus it powers down peripherals and high speed clocks. All state is still maintained. 
    The processor can only be woken up by lp ticker, RTC, an external interrupt on a pin or a watchdog timer.

    The wake-up time should be less than 10 ms.

##### Latency

The sleep modes introduce some interrupt + wake-up latencies that might affect the application. The times are as follows:

Sleep latency - up to 10 microseconds
Deep sleep latency - up to 10 milliseconds

##### Sleep manager

The sleep manager provides API to control sleep modes. Deep sleep might introduce some power savings that can affect an application, for instance high speed clock dependent drivers.

`DeepSleepLock` class provides RAII object for disabling sleep, or explicit lock/unlock methods. To not let an application to enter deep sleep, invoke `DeepSleepLock()::lock()` method. As soon as an application is ready for the deep sleep, allow it by invoking `DeepSleepLock::unlock()` method.

These mbed OS drivers contain locking deep sleep:

- `Ticker`
- `Timeout`
- `Timer`
- `SPI`
- `I2C`
- `CAN`
- `SerialBase`

### Example

SPI asynchronous transfer with deep sleep locking

```c++

SPI::transfer(const Type *tx_buffer, int tx_length, Type *rx_buffer, int rx_length, const event_callback_t& callback, int event = SPI_EVENT_COMPLETE)
{
    if (spi_active(&_spi)) {
        return queue_transfer(tx_buffer, tx_length, rx_buffer, rx_length, sizeof(Type)*8, callback, event);
    }
    // This driver requires high speed clock, needs to waits for complete flag set via a callback to unblock the deep sleep
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
