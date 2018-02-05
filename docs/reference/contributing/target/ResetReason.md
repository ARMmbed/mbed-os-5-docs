### Reset Reason

The Reset Reason API provides a platform-independent method of checking the cause of the last system reset. Implementing the Reset Reason API is not mandatory, but by implementing it, you can check for erroneous system resets at boot time.

#### Assumptions

##### Defined behavior

- The function `hal_reset_reason_clear` clears the reset reason registers for the next system boot.
- The function `hal_reset_reason_get` will get the reset reason currently in the reset reason registers. This may not necessarily be the value of the reset reason registers that were set at boot time if they have been cleared since.

##### Undefined behavior

- The function `hal_reset_reason_get` is not guaranteed to return the same value when called repeatedly. The user should store the value for later use instead of calling the function repeatedly.
- The function `hal_reset_reason_clear` may not clear the reset reason register in time for the next system boot.

##### Things to look out for

- The contents of the targets reset reason register may be cleared by some subsystem before it first gets called. This returns a `RESET_REASON_UNKNOWN` value to the user. To avoid this, the user should call the reset reason API as early as possible at boot time.
- If the target doesn't support clearing reset registers, `hal_reset_reason_get` seems to erroneously return a reset reason even after clearing.

#### Dependencies

Hardware Reset Reason registers.

#### Implementing Reset Reason

You can find the API and specification for the Reset Reason API in the following header file:

[![View code](https://www.mbed.com/embed/?type=library)](https://github.com/ARMmbed/mbed-os/blob/feature-watchdog/hal/reset_reason_api.h)

To enable Reset Reason support in Mbed OS, add the `RESET_REASON` label in the `device_has` option of the target's section in the `targets.json` file.

#### Testing

The Mbed OS HAL provides a set of conformance tests for ResetReason. You can use these tests to validate the correctness of your implementation. To run the ResetReason HAL tests use the following command:

```
mbed test -t <toolchain> -m <target> -n "tests-mbed_hal-reset_reason"
```

[![View code](https://www.mbed.com/embed/?type=library)](https://github.com/ARMmbed/mbed-os/blob/feature-watchdog/TESTS/mbed_hal/reset_reason/reset_reason_api_tests.h)

[![View code](https://www.mbed.com/embed/?type=library)](https://github.com/ARMmbed/mbed-os/blob/feature-watchdog/TESTS/host_tests/reset_reason.py)
