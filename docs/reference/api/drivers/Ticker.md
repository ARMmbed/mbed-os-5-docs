## Ticker

Use the Ticker interface to set up a recurring interrupt; it calls a function repeatedly and at a specified rate.

You can create any number of Ticker objects, allowing multiple outstanding interrupts at the same time. The function can be a static function, or a member function of a particular object.

### Warnings and notes

* Timers are based on 32-bit int microsecond counters, so they can only time up to a maximum of 2^31-1 microseconds (30 minutes). They are designed for times between microseconds and seconds. For longer times, you should consider the time() real time clock.

* No blocking code in ISR: avoid any call to wait, infinite while loop or blocking calls in general.

* No printf, malloc or new in ISR: avoid any call to bulky library functions. In particular, certain library functions (such as printf, malloc and new) are not re-entrant, and their behavior could be corrupted when called from an ISR.

### Ticker class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/classmbed_1_1_ticker.html)

### Ticker Hello World!

Try this program to set up a Ticker to repeatedly invert an LED:

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/Ticker_HelloWorld/)](https://os.mbed.com/teams/mbed_example/code/Ticker_HelloWorld/file/5dc3a82c48f6/main.cpp)

### Ticker examples

Use this example to attach a member function to a ticker:

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/Ticker_Example/)](https://os.mbed.com/teams/mbed_example/code/Ticker_Example/file/fa1a6e600bdb/main.cpp)
