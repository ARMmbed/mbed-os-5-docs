### Timer

Use the Timer interface to create, start, stop and read a timer for measuring small times (between microseconds and seconds).

You can independently create, start and stop any number of Timer objects.

<span class="warnings">**Warning:** Timers are based on 32-bit int microsecond counters, so they can only time up to a maximum of 2^31-1 microseconds (30 minutes). They are designed for times between microseconds and seconds. For longer times, you should consider the `time()` real time clock. </span>

#### Timer class reference

[![View code](https://www.mbed.com/embed/?type=library)](/docs/v5.4/mbed-os-api-doxy/classmbed_1_1_timer.html)

#### Timer Hello World!

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/Timer_HelloWorld/)](https://developer.mbed.org/teams/mbed_example/code/Timer_HelloWorld/file/485b7e68874c/main.cpp)
