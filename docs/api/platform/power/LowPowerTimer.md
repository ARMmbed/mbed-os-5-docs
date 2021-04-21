# LowPowerTimer

<span class="images">![](https://os.mbed.com/docs/mbed-os/v6.10/mbed-os-api-doxy/classmbed_1_1_low_power_timer.png)<span>LowPowerTimer class hierarchy</span></span>

LowPowerTimer inherits from the Timer Class. The timer in this case continues operating even in deep sleep mode. It relies on `lp_ticker`, which is the low power ticker.

You can use the LowPowerTimer interface to create, start, stop and read a timer for measuring small times (between microseconds and seconds). You can independently create, start and stop any number of LowPowerTimer objects. For more information about power management, please see our [power management APIs](power-management-sleep.html).

## LowPowerTimer class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.10/mbed-os-api-doxy/classmbed_1_1_low_power_timer.html)

## LowPowerTimer example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-lowpowerTimer_ex_1/tree/v6.10)](https://github.com/ARMmbed/mbed-os-snippet-lowpowerTimer_ex_1/blob/v6.10/main.cpp)

## Related content

- [Power management APIs](power-management-sleep.html).
