## Timeout

Use the Timeout interface to set up an interrupt to call a function after a specified delay.

You can create any number of Timeout objects, allowing multiple outstanding interrupts at the same time.

### Warnings and notes

* Timers are based on 32-bit int microsecond counters, so they can only time up to a maximum of 2^31-1 microseconds (30 minutes). They are designed for times between microseconds and seconds. For longer times, you should consider the time() real time clock.

* No blocking code in ISR: avoid any call to wait, infinite while loop or blocking calls in general.

* No printf, malloc or new in ISR: Avoid any call to bulky library functions. In particular, certain library functions (such as printf, malloc and new) are not re-entrant, and their behavior could be corrupted when called from an ISR.

### Timeout class reference

[![View code](https://www.mbed.com/embed/?type=library)](/docs/v5.4/mbed-os-api-doxy/classmbed_1_1_timeout.html)

### Timeout Hello World!

Set up a Timeout to invert an LED after a given timeout:

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/Timeout_HelloWorld/)](https://developer.mbed.org/teams/mbed_example/code/Timeout_HelloWorld/file/46d33a0cb1b1/main.cpp)

### Timeout example

Try this example to attach a member function:

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/Timeout_Example/)](https://developer.mbed.org/teams/mbed_example/code/Timeout_Example/file/00cc01bd2e75/main.cpp)
