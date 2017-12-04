## Sleep manager

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

<span class="notes">**Note:** Mbed OS handles sleep for you automatically when you call any of the wait functions. You do not need to call `sleep()` directly unless you are overriding the default sleep handling of Mbed OS.</span>

### Sleep modes

There are two available sleep modes:

1. Sleep mode

The system clock to the core stops until a reset or an interrupt occurs. This eliminates dynamic power that the processor, memory systems and buses use. This mode maintains the processor, peripheral and memory state, and the peripherals continue to work and can generate interrupts.

You can wake up the processor by any internal peripheral interrupt or external pin interrupt.

2. Deep sleep mode

This mode is similar to sleep but saves more power and has a longer wakeup time. It saves power by turning off the high-speed clocks. Because of this, you can only enter this mode when peripherals relying on high-speed clocks are not in use. Peripherals that do not rely on high-speed clocks include the LowPowerTicker, RTC and InterruptIn APIs. This mode maintains all state.

### Sleep manager

The sleep manager provides an API to control sleep modes. Deep sleep might introduce some power savings that can affect an application, for instance high speed clock dependent drivers.

These Mbed OS drivers contain locking deep sleep:

- `Ticker`.
- `Timeout`.
- `Timer`.
- `SPI`.
- `I2C`.
- `CAN`.
- `SerialBase`.

### Sleep manager function reference

<a href="https://github.com/ARMmbed/mbed-os/blob/master/platform/mbed_sleep.h" target="_blank">https://github.com/ARMmbed/mbed-os/blob/master/platform/mbed_sleep.h</a>

### Example

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/SleepManager_Example_1/)](https://os.mbed.com/teams/mbed_example/code/SleepManager_Example_1/file/e85412b4147e/main.cpp)
