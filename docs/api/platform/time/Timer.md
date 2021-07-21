# Timer

<span class="images">![](../../../images/classmbed_1_1_timer.png)<span>Timer class hierarchy</span></span>

Use the Timer interface to create, start, stop and read a stopwatch-like timer for measuring precise times (better than millisecond precision).

You can independently create, start and stop any number of Timer objects.

## Warnings and notes

- Timers are based on 64-bit signed microsecond counters, giving a range of over 250,000 years.
- While a Timer is running, deep sleep is blocked to maintain accurate timing. If you don't need microsecond precision, consider using the LowPowerTimer or Kernel::Clock classes instead because these do not block deep sleep mode.

## Timer class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.13/mbed-os-api-doxy/_timer_8h_source.html)

## Timer hello, world

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Timer_HelloWorld/tree/v6.13)](https://github.com/ARMmbed/mbed-os-snippet-Timer_HelloWorld/blob/v6.13/main.cpp)
