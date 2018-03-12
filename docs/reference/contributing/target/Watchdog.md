### Watchdog

The Watchdog HAL API provides a low-level interface to the Independent Watchdog Timer of a target. Implementing the Watchdog API is not mandatory, but by implementing it, you can use the hardware watchdog timer to detect and recover from computer malfunctions.

Implement the ResetReason API when implementing the Watchdog API. The ResetReason API allows you to detect at boot time whether a watchdog caused the last reset.

#### Assumptions

##### Defined behavior

- Sleep and debug modes don't stop the watchdog timer from counting down.
- The function `hal_watchdog_init` is safe to call repeatedly. The function's implementation must not do anything if `hal_watchdog_init` has already initialized the hardware watchdog timer.
- Maximum supported timeout is `UINT32_MAX` milliseconds; minimum timeout is 1ms.
- The timeout must be accurate to the nearest millisecond.

##### Undefined behavior

- Calling any function other than `hal_watchdog_init` or `hal_watchdog_get_platform_features` before you have initialized the watchdog.

##### Notes

- A software reset may not stop the watchdog timer; the behavior is platform specific.
- Timing on most platforms is based on the timeout registers and a prescaler value. They should be accurate to the nearest millisecond but may be off my a several µs.

#### Dependency

Hardware Independent Watchdog support.

#### Implementing Watchdog

You can find the API and specification for the Watchdog API in the following header file:

[![View code](https://www.mbed.com/embed/?type=library)](https://github.com/ARMmbed/mbed-os/blob/feature-watchdog/hal/watchdog_api.h)

To enable Watchdog support in Mbed OS, add the `WATCHDOG` label in the `device_has` option of the target's section in the `targets.json` file.

#### Testing

The Mbed OS HAL provides a set of conformance tests for Watchdog. You can use these tests to validate the correctness of your implementation. To run the Watchdog HAL tests use the following command:

```
mbed test -t <toolchain> -m <target> -n "tests-mbed_hal-watchdog*"
```

You can read more about the test cases here:

 [![View code](https://www.mbed.com/embed/?type=library)](https://github.com/ARMmbed/mbed-os/blob/feature-watchdog/TESTS/mbed_hal/watchdog/watchdog_api_tests.h)

[![View code](https://www.mbed.com/embed/?type=library)](https://github.com/ARMmbed/mbed-os/blob/feature-watchdog/TESTS/mbed_hal/watchdog_reset/watchdog_reset_tests.h)
