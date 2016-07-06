# TimeOut

The Timeout interface is used to setup an interrupt to call a function after a specified delay.

Any number of Timeout objects can be created, allowing multiple outstanding interrupts at the same time.

## Hello World!

A simple program to setup a Timeout to invert an LED after a given timeout:

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/users/mbed_official/code/Timeout_HelloWorld/)](https://developer.mbed.org/users/mbed_official/code/Timeout_HelloWorld/file/8a555873b7d3/main.cpp) 

## API

API summary

[![View code](https://www.mbed.com/embed/?type=library)](https://developer.mbed.org/users/mbed_official/code/mbed/docs/tip/classmbed_1_1Timeout.html) 

<span class="warnings">**Warning**: Timers are based on 32-bit int microsecond counters, so can only time up to a maximum of 2^31-1 microseconds i.e. 30 minutes. They are designed for times between microseconds and seconds. For longer times, you should consider the time()/Real time clock. </span> 

<span class="warnings">**Warning**: No blocking code in ISR </br>In ISR you should avoid any call to wait, infinitive while loop, or blocking calls in general. </span> 

<span class="warnings">**Warning**: No printf, malloc, or new in ISR </br>In ISR you should avoid any call to bulky library functions. In particular, certain library functions (like printf, malloc and new) are non re-entrant and their behaviour could be corrupted when called from an ISR. </span> 

<span class="notes">**Note**: RTOS Timer </br>Consider using the [mbed RTOS Timer](https://developer.mbed.org/handbook/RTOS) instead of a Timeout. In this way your callback function will not be executed in a ISR, giving you more freedom and safety in your code. </span>

## Examples

Attaching a member function

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/users/mbed_official/code/Timeout_Example/)](https://developer.mbed.org/users/mbed_official/code/Timeout_Example/file/f24282a2495f/main.cpp) 
