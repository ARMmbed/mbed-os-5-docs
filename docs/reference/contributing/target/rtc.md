### RTC HAL API

TODO: embed API
TODO: how to test

The RTC HAL API provides a low-level interface to the Real Time Counter (RTC) of a target.

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

#### Implementing the RTC API

RTC HAL API is in [hal/rtc_api.h](/docs/v5.4/mbed-os-api-doxy/rtc__api_8h_source.html). You need to implement the following functions to support RTC:

To enable sleep support in Mbed OS, you need to add the `RTC` label in the `device_has` option of the target's section in the `targets.json` file.
