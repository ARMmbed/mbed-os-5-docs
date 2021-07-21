# RTC

The RTC (Real-Time Clock) provides mechanisms to set the current time of the hardware RTC with `set_time` API. The time is set as an offset measured in seconds from the time epoch (Unix Epoch - January 1, 1970). [Time](../apis/time.html) provides more information about C `date` and `time` standard library functions.

<span class="notes">**Note:** If your MCU does not have an RTC nor an LPTICKER, you need to provide hooks to the external RTC you are using to the `attach_rtc` API. See the [platform RTC API](https://os.mbed.com/docs/mbed-os/v6.13/mbed-os-api-doxy/group__platform__rtc__time.html) for more details about that function.</span>

RTC class APIs are thread safe.

RTC can keep track of time even in a powered down state if the secondary source of power (battery) is connected.

## RTC function reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.13/mbed-os-api-doxy/mbed__rtc__time_8h_source.html)

## RTC Time example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-time_HelloWorld/tree/v6.13)](https://github.com/ARMmbed/mbed-os-snippet-time_HelloWorld/blobl/v6.13/main.cpp)
