# Microsecond ticker

Implementing the microsecond ticker enables Mbed OS to perform operations that require precise timing. You can use this API to schedule events, record elapsed time and perform submillisecond delays.

## Assumptions

### Defined behavior

- Has a reported frequency between 250 KHz and 8 MHz for counters that are less than 32 bits wide.
- Has a reported frequency up to 100 MHz for counters that are 32 bits wide.
- Has a counter that is at least 16 bits wide.
- The function `ticker_init` is safe to call repeatedly.
- The function `ticker_init` allows the ticker to keep counting and disables the ticker interrupt.
- Ticker frequency is nonzero, and the counter is at least 8 bits.
- The ticker rolls over at (1 << bits) and continues counting starting from 0.
- The ticker counts at the specified frequency plus or minus 10%.
- The ticker increments by 1 each tick.
- The ticker interrupt fires only when the ticker time increments to or past the value set by `ticker_set_interrupt`.
- It is safe to call `ticker_set_interrupt` repeatedly before the handler is called.
- The function `ticker_fire_interrupt` causes `ticker_irq_handler` to be called immediately from interrupt context.
- The ticker operations `ticker_read`, `ticker_clear_interrupt`, `ticker_set_interrupt` and `ticker_fire_interrupt` take less than 20 us to complete.
- The ticker operations `ticker_init` and `ticker_read` are atomic.

### Undefined behavior

- Calling any function other than `ticker_init` before the initialization of the ticker.
- Whether `ticker_irq_handler` is called a second time if the time wraps and matches the value set by `ticker_set_interrupt` again.
- Calling `ticker_set_interrupt` with a value that has more than the supported number of bits.
- Calling any function other than `us_ticker_init` after calling `us_ticker_free`.

### Notes

Be careful around these common trouble areas when implementing this API:

- The ticker cannot drift when rescheduled repeatedly.
- The ticker keeps counting when it rolls over.
- The ticker interrupt fires when the compare value is set to 0 and overflow occurs.

## Dependencies

To implement this API, the device must have a hardware counter that has a count value at least 16 bits wide and can operate between 250 KHz and 8 MHz.

## Implementing the microsecond ticker API

You can find the API and specification for the microsecond ticker API in the following header file:

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/group__hal__us__ticker.html)

To enable microsecond ticker support in Mbed OS, add the `USTICKER` label in the `device_has` option of the target's section in the `targets.json` file.

### Optimizing the microsecond ticker API

The generic ticker API uses the `ticker_info_t` structure to determine each hardware counter's frequency and width. This then requires runtime calculations to convert between the hardware counter and the 64-bit microsecond count used by the generic API.

In addition to the generic `ticker_info_t`, the target can also provide compile-time information about the microsecond ticker by defining the macros `US_TICKER_PERIOD_NUM`, `US_TICKER_PERIOD_DEN` and `US_TICKER_MASK`. If provided, these permit greatly optimized versions of APIs such as `wait_us`. See the header file for full details.

## Testing

The Mbed OS HAL provides a set of conformance tests for the microsecond ticker. You can use these tests to validate the correctness of your implementation. To run the microsecond ticker HAL tests, use the following command:

```
mbed test -t <toolchain> -m <target> -n tests-mbed_hal-common_ticker*,tests-mbed_hal-us_ticker*
```

You can read more about the test cases:

 [![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/group__hal__us__ticker.html)

 [![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/group__hal__ticker__tests.html)

 [![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/group__hal__us__ticker__tests.html)
