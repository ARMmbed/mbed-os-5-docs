# Watchdog

<span class="images">![](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/classmbed_1_1_watchdog.png)<span>Watchdog class hierarchy</span></span>

You can use the Watchdog interface to set up a hardware watchdog timer that resets the system in the case of system failures or malfunctions.

<span class="notes">**Note:** There is only one instance in the system. Use `Watchdog::get_instance()` to obtain a reference. </span>

If you fail to refresh the watchdog periodically, it resets the system after a set period of time.

<span class="notes">**Note:** The maximum amount of time you can set as the Watchdog timeout varies depending on the target hardware. You can check the maximum value by calling `Watchdog::get_instance().get_max_timeout()`.</span>

## Watchdog class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/classmbed_1_1_watchdog.html)

## Watchdog example

This example creates a watchdog timer that expires after five seconds and that you can refresh by pushing BUTTON1 on the target board:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Watchdog_ex_1/tree/v6.5)](https://github.com/ARMmbed/mbed-os-snippet-Watchdog_ex_1/blob/v6.5/main.cpp)

