# SysTick and tickless mode

## SysTick

System tick timer (SysTick) is a standard timer available on most Cortex-M cores. Its main purpose is to rise an interrupt with set frequency (usually 1ms). You can use it to perform any task in the system, but for platforms using RTOS, including Mbed OS, it provides an interval for the OS for counting the time and scheduling tasks.

Mbed OS uses default SysTick source for most targets, but you can override that using the [Tick API](http://arm-software.github.io/CMSIS_5/RTOS2/html/group__CMSIS__RTOS__TickAPI.html) that CMSIS-RTOS2 provides.

## Tickless mode

Tickless mode is an optimization mechanism available in RTOS for suspending the SysTick. You can use it in situations when RTOS is idle for multiple ticks, so you can achieve power savings by entering uninterrupted sleep. Targets implementing tickless mode disable the SysTick, set up wake-up timers and enter sleep mode when idle. It then exits sleep mode and re-enables the SysTick when the timer expires or some event occurs (like external interrupt).

Mbed OS supports the tickless mode on multiple targets. [`targets/targets.json`](https://github.com/ARMmbed/mbed-os/blob/master/targets/targets.json) defines the `MBED_TICKLESS` macro.

Targets supporting tickless mode override the default SysTick mechanism and use [RtosTimer](https://github.com/ARMmbed/mbed-os/blob/master/rtos/TARGET_CORTEX/mbed_rtx_idle.cpp) implementation based on [low power ticker](https://github.com/ARMmbed/mbed-os/blob/master/drivers/LowPowerTicker.h). This change is necessary to avoid drift connected with using two different timers to measure time. It should be mostly invisible for users, except that users must not change the low power ticker interrupt handler when tickless mode is in use.
