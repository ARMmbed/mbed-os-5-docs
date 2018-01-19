### RTC

Implementing RTC enables Mbed OS to keep track of current time. It is used by the standard library time keeping functions, such as `time`.

#### Deprecation warning

**All of the following informations are intended for the new RTC HAL API, available on a feature branch, but not yet part of the master branch. We are planning to replace the API on master in time for the Mbed OS 5.9 realease. If you intend for your port to be part of the Mbed OS before May 2019, you will need to implemnt both of the APIs. In this case you need to submit your main port as a pull request against master, implementing the old API. Additionaly you need to rise another pull request against `feature-hal-spec-rtc` branch, implementing the new API described below.**

You can find the old RTC HAL API in the following header file:

[![View code](https://www.mbed.com/embed/?type=library)](https://os-doc-builder.test.mbed.com/docs/v5.7/mbed-os-api-doxy/rtc__api_8h_source.html)

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
