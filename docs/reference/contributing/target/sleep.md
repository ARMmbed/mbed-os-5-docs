### Sleep

<span class="warnings">**Warning:** We are changing the Sleep HAL API in an upcoming release of Mbed OS. You can find details on how it may affect you in the [Implementing the Sleep API](#implementing-the-sleep-api) section.

Implement the Sleep HAL API to enable your device to go into a low power state when you are not actively using it.

#### Assumptions

##### Defined behavior

There are two power-saving modes available in Mbed OS:

###### Sleep

The core system clock is disabled. You can use both the low- and high-frequency clocks and retain RAM.

1. Wake-up sources - Any interrupt must wake up the MCU.
1. Latency - The MCU must wake up within 10 us.

###### Deep sleep

The core system clock is disabled. You can only enable the low-frequency clocks and retain RAM.

1. Wake-up sources - RTC, low power ticker or GPIO must wake up the MCU.
1. Latency - The MCU must wake up within 10 ms.

#### Implementing the Sleep API

We are working on the new HAL Sleep API, which will replace the current version in an upcoming release of Mbed OS. You need to implement the Sleep API in both variants. First, you need to implement the current API. You can find it on the master branch:

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/sleep__api_8h_source.html)

To make sure your platform is ready for the upcoming changes, you need to implement the future API and submit it in a separate pull request against the `feature-hal-spec-sleep` branch. You can find the API and specification for the new Sleep API in the following header file:

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/feature-hal-spec-sleep-doxy/group__hal__sleep.html)

To enable sleep support in Mbed OS, you need to add the `SLEEP` label in the `device_has` option of the target's section in the `targets.json` file.

#### Testing

The Mbed OS HAL provides a set of conformance tests for Sleep. You can use these tests to validate the correctness of your implementation. To run the Sleep HAL tests, use the following command:

```
mbed test -t <toolchain> -m <target> -n "tests-mbed_hal-sleep*"
```

You can read more about the test cases:

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/feature-hal-spec-sleep-doxy/group__hal__sleep__tests.html)
