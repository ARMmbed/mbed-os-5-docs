### RTC

By implementing RTC you will enable Mbed OS to keep track of current time. RTC API is not mandatory, but by implementing it you will be able to use standard library time keeping functions like `time`.

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

##### Potential bugs

- Incorrect overflow handling.
- Glitches due to ripple counter.

#### Depenndencies

Hardware RTC capabilities.

#### Implementing the RTC API

You can find the API and specification for the RTC in following header file:

[![View code](https://www.mbed.com/embed/?type=library)](https://github.com/ARMmbed/mbed-os/blob/feature-hal-spec-rtc/hal/rtc_api.h)

To enable RTC support in Mbed OS, you need to add the `RTC` label in the `device_has` option of the target's section in the `targets.json` file.

#### Validation

Mbed OS HAL provides set of conformance tests for RTC, which you can use to validate correctness of your implementation. You can read more about the test cases here:

 [![View code](https://www.mbed.com/embed/?type=library)](https://github.com/ARMmbed/mbed-os/blob/feature-hal-spec-rtc/TESTS/mbed_hal/rtc/rtc_test.h)

 [![View code](https://www.mbed.com/embed/?type=library)](https://github.com/ARMmbed/mbed-os/blob/feature-hal-spec-rtc/TESTS/mbed_hal/rtc_reset/rtc_reset_test.h)
