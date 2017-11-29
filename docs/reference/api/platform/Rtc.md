## RTC

The RTC (Real-Time Clock) class provides mechanisms to set the current time of the hardware RTC with `set_time` API. The time is set as an offset measured in seconds from the time epoch (Unix Epoch - January 1, 1970). 

You can use the `attach_rtc` API to hook external RTC for using C time functions. It provides you with `init()`, `read()`, `write()` and `isenabled()` functions to be attached. <a href="/docs/v5.6/reference/time.html" target="_blank">Time</a> provides more information about C `date` and `time` standard library functions.

RTC class APIs are thread safe.

RTC can keep track of time even in a powered down state if the secondary source of power (battery) is connected.

### RTC Time class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/mbed__rtc__time_8h_source.html)

### RTC Time example

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/time_HelloWorld/)](https://os.mbed.com/teams/mbed_example/code/time_HelloWorld/file/8593c9813840/main.cpp)
