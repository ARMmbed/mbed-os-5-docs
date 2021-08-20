# Low Power Ticker

Implementing the low power ticker enables Mbed OS to perform power efficient timing operations that only request millisecond accuracy. You can use this API to schedule events, record elapsed time and drive the tickless OS scheduler.

## Assumptions

### Defined behavior
- Has a reported frequency between 8KHz and 64KHz.
- Has a counter that is at least 12 bits wide.
- Continues operating in deep sleep mode.
- The function `ticker_init` is safe to call repeatedly.
- The function `ticker_init` allows the ticker to keep counting and disables the ticker interrupt.
- Ticker frequency is nonzero and the counter is at least 8 bits.
- The ticker rolls over at (1 << bits) and continues counting starting from 0.
- The ticker counts at the specified frequency plus or minus 10%.
- The ticker increments by 1 each tick.
- The ticker interrupt fires only when the ticker time increments to or past the value that `ticker_set_interrupt` sets.
- It is safe to call `ticker_set_interrupt` repeatedly before the handler is called.
- The function `ticker_fire_interrupt` causes `ticker_irq_handler` to be called immediately from interrupt context.
- The ticker operations `ticker_read`, `ticker_clear_interrupt`, `ticker_set_interrupt` and `ticker_fire_interrupt` take less than 20us to complete.

### Undefined behavior

- Calling any function other than `ticker_init` before the initialization of the ticker.
- Whether `ticker_irq_handler` is called a second time if the time wraps and matches the value that `ticker_set_interrupt again` sets.
- Calling `ticker_set_interrupt` with a value that has more than the supported number of bits.
- Calling any function other than `lp_ticker_init` after calling `lp_ticker_free`.

### Notes

Be careful around these common trouble areas when implementing this API:

- The ticker cannot drift when rescheduled repeatedly
- The ticker keeps counting when it rolls over
- The ticker interrupt fires when the compare value is set to 0 and and overflow occurs

### Handling synchronization delay

Some low power tickers require multiple low power clock cycles for the compare value that `ticker_set_interrupt` sets to take effect. Further complicating this issue, a new compare value typically cannot be set until the first has taken effect. Because of this, when you make back-to-back calls to `ticker_set_interrupt` without a delay, the second call blocks and violates the above requirement that `ticker_set_interrupt` completes in 20us.

To meet this timing requirement, targets that have this synchronization delay must set `LPTICKER_DELAY_TICKS` to the number of low power clock cycles it takes for a call to `ticker_set_interrupt` to take effect. When the targets set this value, the timer code prevents `lp_ticker_set_interrupt` from being called twice within that number of clock cycles. It does this by using the microsecond time to schedule the write to happen at a future date.

## Dependencies

Hardware low power ticker capabilities.

## Implementing the low power ticker API

You can find the API and specification for the low power ticker API in the following header file:

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.14/mbed-os-api-doxy/group__hal__lp__ticker.html)

To enable low power ticker support in Mbed OS, add the `LPTICKER` label in the `device_has` option of the target's section in the `targets.json` file.

## Testing

The Mbed OS HAL provides a set of conformance tests for the low power ticker. You can use these tests to validate the correctness of your implementation. To run the low power ticker HAL tests, use the following command:

```
mbed test -t <toolchain> -m <target> -n tests-mbed_hal-common_ticker*,tests-mbed_hal-lp_ticker*
```

You can read more about the test cases:

 [![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.14/mbed-os-api-doxy/group__hal__lp__ticker.html)

 [![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.14/mbed-os-api-doxy/group__hal__ticker__tests.html)

 [![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.14/mbed-os-api-doxy/group__hal__lp__ticker__tests.html)
