# SysTick and tickless mode

## SysTick

System tick timer (SysTick) is a standard timer available on most Cortex-M cores. Its main purpose is to rise an
interrupt with set frequency (usually 1ms). It can be used to perform any task in the system, but for platforms
utilizing RTOS, including mbed OS, it provides an interval for the OS for counting the time and scheduling tasks.

mbed OS uses default SysTick source for most targets, but that can be overridden using the
[Tick API](http://arm-software.github.io/CMSIS_5/RTOS2/html/group__CMSIS__RTOS__TickAPI.html) provided by CMSIS-RTOS2.

## Tickless mode

Tickless mode is an optimization mechanism available in RTOS for suspending the SysTick. It can be used in situations
when RTOS will be idle for multiple ticks, allowing to achieve power savings by entering uninterrupted sleep. Targets
implementing tickless mode will disable the SysTick, set up wake-up timer and enter sleep mode when idle. It will then exit
sleep mode and re-enable the SysTick, when the timer expires or some event occurs (like external interrupt).

mbed OS supports the tickless mode on multiple targets, they will define `MBED_TICKLESS`
macro in [targets/targets.json](https://github.com/ARMmbed/mbed-os/blob/master/targets/targets.json).

Targets supporting tickless mode will override the default SysTick mechanism and use
[RtosTimer](https://github.com/ARMmbed/mbed-os/blob/master/rtos/TARGET_CORTEX/mbed_rtx_idle.cpp) implementation based on
[low power ticker](https://github.com/ARMmbed/mbed-os/blob/master/drivers/LowPowerTicker.h).
This change is necessary to avoid drift connected with using two different timers to measure time. It should be mostly
invisible for users, except that the low power ticker interrupt handler shouldn't be changed when tickless mode is in use.
