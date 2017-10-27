### Tickless

#### Tickless mode

Tickless mode is an optimization mechanism available in RTOS for suspending the SysTick. You can use it in situations when RTOS is idle for multiple ticks, so you can achieve power savings by entering uninterrupted sleep. Target implementing tickless mode disables the SysTick, sets up wake-up timers and enters sleep mode when idle. It then exits sleep mode and re-enables the SysTick when the timer expires or some event occurs (like external interrupt).

##### Enabling tickless mode

To support tickless mode in Mbed OS, your target needs to meet two requirements:

- Support for Sleep HAL API
- Support for Low Power Ticker HAL API

To enable tickless mode support in Mbed OS, you need to add the `MBED_TICKLESS` macro in the `macros` option of the target's section in the `targets.json` file.

Targets supporting tickless mode override the default SysTick mechanism and use [RtosTimer](https://github.com/ARMmbed/mbed-os/blob/master/rtos/TARGET_CORTEX/mbed_rtx_idle.cpp) implementation based on [low power ticker](https://github.com/ARMmbed/mbed-os/blob/master/drivers/LowPowerTicker.h). This change is necessary to avoid drift connected with using two different timers to measure time. It should be mostly invisible for users, except that users must not change the low power ticker interrupt handler when tickless mode is in use.

##### Testing

There are no dedicated tests validating tickless mode. Running all Mbed OS tests suits, with particular focus on HAL sleep and HAL low power ticker tests, provides sufficient coverage.
