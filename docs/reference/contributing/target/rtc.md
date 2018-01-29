### RTC

Implementing RTC enables Mbed OS to keep track of current time. It is used by the standard library time keeping functions, such as `time`.

<span class="warnings">**Warning:** We are changing the RTC HAL API in an upcoming release of Mbed OS. You can find details on how it may affect you in the [Implementing the RTC API](#Implementing-the-RTC-API) section.

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

We are working on the new HAL RTC API, which will replace current version in an upcoming release of Mbed OS. You will need to implement the RTC API in both variants. Firstly you need to implement the current API, you can find it on master branch:

[![View code](https://www.mbed.com/embed/?type=library)](https://os-doc-builder.test.mbed.com/docs/v5.7/mbed-os-api-doxy/rtc__api_8h_source.html)

To make sure your platform is ready for the upcoming changes, you will need to implement the future API and submit it in a separate pull request against `feature-hal-spec-rtc` branch. You can find the API and specification for the new RTC API in the following header file:

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
