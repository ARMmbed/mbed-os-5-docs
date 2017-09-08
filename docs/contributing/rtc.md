# RTC HAL API

The RTC HAL API provides a low level interface to the Real Time Counter (RTC) of a target.

## Assumptions

### Defined behavior

- The function `rtc_init` is safe to call repeatedly
- RTC accuracy is at least 10%
- `Init`/`free` doesn't stop RTC from counting
- Software reset doesn't stop RTC from counting
- Sleep modes don't stop RTC from counting
- Shutdown mode doesn't stop RTC from counting

### Undefined behavior

- Calling any function other than `rtc_init` before the initialization of the RTC

### Potential bugs

- Incorrect overflow handling
- Glitches due to ripple counter

## Implementing the RTC API

RTC HAL API is located in [hal/rtc_api.h](). Following functions need to be implemented to support RTC:


To enable sleep support in mbed OS `RTC` label needs to be added in `device_has` option of target's section in `targets.json` file.

## Testing

The [RTC HAL API test suite]() validates:

- `rtc_init` is safe to call repeatedly - Verified by test `rtc_init_test`
- `Init`/`free` doesn't stop RTC from counting - Verified by test `rtc_persist_test`
- Software reset doesn't stop RTC from counting - Verified by `rtc_reset_test`
- Sleep modes don't stop RTC from counting - Verified by `rtc_sleep_test`
- Overflow handling - Verified by `rtc_range_test`
- No backward glitches - Verified by `rtc_glitch_test`
