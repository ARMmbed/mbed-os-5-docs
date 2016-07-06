# Ticker

The Ticker interface is used to setup a recurring interrupt to repeatedly call a function at a specified rate.

Any number of Ticker objects can be created, allowing multiple outstanding interrupts at the same time. The function can be a static function, or a member function of a particular object.

## Hello World!

A simple program to setup a Ticker to invert an LED repeatedly:

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/users/mbed_official/code/Ticker_HelloWorld/)](https://developer.mbed.org/users/mbed_official/code/Ticker_HelloWorld/file/5014bf742e9b/main.cpp) 

## API

API summary

[![View code](https://www.mbed.com/embed/?type=library)](https://developer.mbed.org/users/mbed_official/code/mbed/docs/tip/classmbed_1_1Ticker.html) 

<span class="warnings">**Warning:** Timers are based on 32-bit int microsecond counters, so can only time up to a maximum of 2^31-1 microseconds i.e. 30 minutes. They are designed for times between microseconds and seconds. For longer times, you should consider the time()/Real time clock. </span> 

<span class="warnings">**Warning:** No blocking code in ISR </br>In ISR you should avoid any call to wait, infinitive while loop, or blocking calls in general. </span> 

<span class="warnings">**Warning:** No printf, malloc, or new in ISR </br>In ISR you should avoid any call to bulky library functions. In particular, certain library functions (like printf, malloc and new) are non re-entrant and their behaviour could be corrupted when called from an ISR. </span> 

<span class="notes">**Note:** RTOS Timer </br> Consider using the [mbed RTOS Timer](../RTOS/mbed_RTOS.md) instead of a Ticker. In this way your periodic function will not be executed in a ISR, giving you more freedom and safety in your code. </span>

## Examples

Example attaching a member function to a ticker: 

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/users/mbed_official/code/Ticker_Example/)](https://developer.mbed.org/users/mbed_official/code/Ticker_Example/file/14eb5da7a9a3/main.cpp) 
