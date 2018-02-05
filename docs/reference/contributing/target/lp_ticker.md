### Low Power Ticker

Implementing Low Power Ticker enables Mbed OS to perform power efficient timing operations which only request millisecond accuracy. It is used to shedule events, record elapsed time and drive the tickless OS scheduler.

<span class="warnings">**Warning:** We are changing the Low Power Ticker HAL API in an upcoming release of Mbed OS. You can find details on how it may affect you in the [Implementing the Low Power Ticker API](#Implementing-the-Low-Power-Ticker-API) section.

#### Assumptions

##### Defined behavior
- Has a reported frequency between 8KHz and 64KHz
- Has a counter that is at least 12 bits wide
- Continues operating in deep sleep mode
- The function ticker_init is safe to call repeatedly
- The function ticker_init allows the ticker to keep counting and disables the ticker interrupt
- Ticker frequency is non-zero and counter is at least 8 bits
- The ticker rolls over at (1 << bits) and continues counting starting from 0
- The ticker counts at the specified frequency +- 10%
- The ticker increments by 1 each tick
- The ticker interrupt fires only when the ticker times increments to or past the value set by ticker_set_interrupt.
- It is safe to call ticker_set_interrupt repeatedly before the handler is called
- The function ticker_fire_interrupt causes ticker_irq_handler to be called immediately from interrupt context
- The ticker operations ticker_read, ticker_clear_interrupt, ticker_set_interrupt and ticker_fire_interrupttake less than 20us to complete

##### Undefined behavior

- Calling any function other than ticker_init before the initialization of the ticker
- Whether ticker_irq_handler is called a second time if the time wraps and matches the value set by ticker_set_interrupt again
- Calling ticker_set_interrupt with a value that has more than the supported number of bits
- Calling any function other than lp_ticker_init after calling lp_ticker_free

##### Things to look out for

- Drift due to reschedule
- Incorrect overflow handling of timers
- Interrupting at a time of 0
- Interrupt triggered more than once

#### Dependencies

Hardware Low Power Ticker capabilities.

#### Implementing the Low Power Ticker API

We are working on the new HAL Low Power Ticker API, which will replace current version in an upcoming release of Mbed OS. You will need to implement the Low Power Ticker API in both variants. Firstly you need to implement the current API, you can find it on master branch:

[![View code](https://www.mbed.com/embed/?type=library)](https://os-doc-builder.test.mbed.com/docs/v5.7/mbed-os-api-doxy/lp__ticker__api_8h_source.html)

To make sure your platform is ready for the upcoming changes, you will need to implement the future API and submit it in a separate pull request against `feature-hal-spec-ticker` branch. You can find the API and specification for the new Low Power Ticker API in the following header file:

[![View code](https://www.mbed.com/embed/?type=library)](https://github.com/ARMmbed/mbed-os/blob/feature-hal-spec-ticker/hal/lp_ticker_api.h)

To enable Low Power Ticker support in Mbed OS, add the `LOWPOWERTIMER` label in the `device_has` option of the target's section in the `targets.json` file.

#### Testing

The Mbed OS HAL provides a set of conformance tests for the Low Power Ticker. You can use these tests to validate the correctness of your implementation. To run the Low Power Ticker HAL tests use the following command:
```
mbed test -t <toolchain> -m <target> -n tests-mbed_hal-lp_us_ticker*,tests-mbed_hal-lp_ticker*
```

You can read more about the test cases:

 [![View code](https://www.mbed.com/embed/?type=library)](https://github.com/ARMmbed/mbed-os/blob/feature-hal-spec-ticker/hal/lp_ticker_api.h)

 [![View code](https://www.mbed.com/embed/?type=library)](https://github.com/ARMmbed/mbed-os/blob/feature-hal-spec-ticker/TESTS/mbed_hal/lp_us_tickers/ticker_api_tests.h)

 [![View code](https://www.mbed.com/embed/?type=library)](https://github.com/ARMmbed/mbed-os/blob/feature-hal-spec-ticker/TESTS/mbed_hal/lp_ticker/lp_ticker_api_tests.h)
