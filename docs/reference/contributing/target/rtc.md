### RTC

Implementing RTC enables Mbed OS to keep track of current time. It backs the standard library time keeping functions, such as `time`.

#### Assumptions

##### Defined behavior

- The function `rtc_init` is safe to call repeatedly.
- RTC accuracy is at least 10%.
- `Init`/`free` doesn't stop RTC from counting.
- Software reset doesn't stop RTC from counting.
- Sleep modes don't stop RTC from counting.
- Shutdown mode doesn't stop RTC from counting.

##### Undefined behavior

- Calling any function other than `rtc_init` before the initialization of the RTC.

##### Things to look out for

- Incorrect overflow handling.
- Glitches due to ripple counter.

#### Dependencies

Hardware RTC capabilities.

#### Implementing the RTC API

You can find the API and specification for the RTC in the following header file:

[![View code](https://www.mbed.com/embed/?type=library)](https://github.com/ARMmbed/mbed-os/blob/feature-hal-spec-rtc/hal/rtc_api.h)

To enable RTC support in Mbed OS, add the `RTC` label in the `device_has` option of the target's section in the `targets.json` file.

#### Testing

The Mbed OS HAL provides a set of conformance tests for RTC. You can use these tests to validate the correctness of your implementation. To run the RTC HAL tests use the following command:
```
mbed test -t <toolchain> -m <target> -n "tests-mbed_hal-rtc*"
```

You can read more about the test cases:

 [![View code](https://www.mbed.com/embed/?type=library)](https://github.com/ARMmbed/mbed-os/blob/feature-hal-spec-rtc/TESTS/mbed_hal/rtc/rtc_test.h)

 [![View code](https://www.mbed.com/embed/?type=library)](https://github.com/ARMmbed/mbed-os/blob/feature-hal-spec-rtc/TESTS/mbed_hal/rtc_reset/rtc_reset_test.h)
