### Ticker

Use the Ticker interface to set up a recurring interrupt; it calls a function repeatedly and at a specified rate.

You can create any number of Ticker objects, allowing multiple outstanding interrupts at the same time. The function can be a static function, or a member function of a particular object.

#### API

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classmbed_1_1Ticker.html)

#### Hello World!

Try this program to set up a Ticker to repeatedly invert an LED:

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/Ticker_HelloWorld/)](https://developer.mbed.org/teams/mbed_example/code/Ticker_HelloWorld/file/5dc3a82c48f6/main.cpp)

##### Warnings and notes

* Timers are based on 32-bit int microsecond counters, so they can only time up to a maximum of 2^31-1 microseconds (30 minutes). They are designed for times between microseconds and seconds. For longer times, you should consider the time() real time clock.

* No blocking code in ISR: avoid any call to wait, infinite while loop or blocking calls in general.

* No printf, malloc or new in ISR: avoid any call to bulky library functions. In particular, certain library functions (such as printf, malloc and new) are not re-entrant, and their behavior could be corrupted when called from an ISR.

* RTOS Timer: Consider using the [mbed RTOS Timer](Timer.md) instead of a Ticker. In this way your periodic function will not be executed in an ISR, giving you more freedom and safety in your code. </span>

#### Examples

Use this example to attach a member function to a ticker:

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/Ticker_Example/)](https://developer.mbed.org/teams/mbed_example/code/Ticker_Example/file/fa1a6e600bdb/main.cpp)
