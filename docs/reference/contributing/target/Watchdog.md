### Watchdog

The Watchdog HAL API provides a low-level interface to the Independent Watchdog Timer of a target. Implementing the Watchdog API is not mandatory, but by implementing it, you can use the hardware watchdog timer to detect and recover from computer malfunctions.

The Reset Reason API should ideally also be implemented when implementing the Watchdog API, the Reset Reason API will allow you to detect at boot time whether a watchdog caused the last reset.

#### Assumptions

##### Defined behavior

* Sleep and Debug modes don't stop the watchdog from counting down.
* The function `hal_watchdog_init` is safe to call repeatedly, it must not do anything if the watchdog timer is already initialized.
* Maximum supported timeout is `UINT32_MAX` milliseconds, minimum timeout is 1ms.
* The timeout must be accurate to the nearest millisecond.

##### Undefined behavior

* Calling any function other than `hal_watchdog_init` or `hal_watchdog_get_platform_features` before the watchdog has been initialized.

##### Potential bugs

- Watchdog timer may not be stopped by a Software Reset, the behaviour is platform specific.
- Timings on most platforms are calculated based on the timeout registers and a prescaler value, they should be accurate to the nearest millisecond, but may be off my a several µs.

#### Dependencies

Hardware Independent Watchdog support.

#### Implementing Watchdog

You can find the API and specification for the Watchdog API in the following header file:

[![View code](https://www.mbed.com/embed/?type=library)](https://github.com/ARMmbed/mbed-os/blob/feature-watchdog/hal/watchdog_api.h)

To enable Watchdog support in Mbed OS, add the `WATCHDOG` label in the `device_has` option of the target's section in the `targets.json` file.


#### Testing

The Mbed OS HAL provides a set of conformance tests for Watchdog. You can use these tests to validate the correctness of your implementation.

You can read more about the test cases here:


 [![View code](https://www.mbed.com/embed/?type=library)](https://github.com/ARMmbed/mbed-os/blob/feature-watchdog/TESTS/mbed_hal/watchdog/watchdog_api_tests.h)

[![View code](https://www.mbed.com/embed/?type=library)](https://github.com/ARMmbed/mbed-os/blob/feature-watchdog/TESTS/mbed_hal/watchdog/watchdog_reset_tests.h)