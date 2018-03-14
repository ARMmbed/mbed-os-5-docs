## Power management

### Sleep

There is only one sleep function in Mbed OS:

```c++
void sleep();
```

This function invokes sleep manager, which selects the most appropriate sleep mode.

<span class="notes">**Note:** In most cases, you don't need to call `sleep()` directly. Mbed OS enters sleep mode automatically any time the system is idle. That is when all your threads are in a waiting state, for example waiting for an event or a timeout.</span>

#### Sleep modes

There are two available sleep modes:

1. Sleep mode

The system clock to the core stops until a reset or an interrupt occurs. This eliminates dynamic power that the processor, memory systems and buses use. This mode maintains the processor, peripheral and memory state, and the peripherals continue to work and can generate interrupts.

You can wake up the processor by any internal peripheral interrupt or external pin interrupt.

2. Deep sleep mode

This mode is similar to sleep but saves more power and has a longer wakeup time. It saves additional power by turning off the high-speed clocks. Because of this, you can only enter this mode when peripherals relying on high-speed clocks are not in use. Peripherals that do not rely on high-speed clocks include the LowPowerTicker, RTC and InterruptIn APIs. This mode maintains all state.

#### Sleep manager

The sleep manager provides an API and logic to control device sleep mode selection. Although standard sleep doesn't affect application execution, deep sleep might introduce some additional power savings that can affect the application, for instance high-speed clock-dependent drivers. To ensure correct operation of your application, sleep manager may disable deep sleep, in which case your board enters normal sleep, instead. This mechanism is mostly invisible to the user, but you should be aware that it may affect the power consumption of your hardware.

These Mbed OS drivers can lock the deep sleep:

- `Ticker`.
- `Timeout`.
- `Timer`.
- `SPI`.
- `I2C`.
- `CAN`.
- `SerialBase`.

#### Example

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/SleepManager_Example_1/)](https://os.mbed.com/teams/mbed_example/code/SleepManager_Example_1/file/e85412b4147e/main.cpp)

### Function reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/group__platform__power__mgmt.html)

### Idle loop

Idle loop is a background system thread, which scheduler executes when no other threads are ready to run. That may happen when your application is waiting for an event to happen. By default, the idle loop invokes sleep manager to enter a sleep mode. You can overwrite this behavior by providing a different handler:

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

#### Function reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.7/mbed-os-api-doxy/group__rtos___idle.html)

### Example

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/SleepManager_Example_1/)](https://os.mbed.com/teams/mbed_example/code/SleepManager_Example_1/file/e85412b4147e/main.cpp)

