# Timer

The Timer interface is used to create, start, stop and read a timer for measuring small times (between microseconds and seconds).

Any number of Timer objects can be created, and can be started and stopped independently

## Hello World!

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/users/mbed_official/code/Timer_HelloWorld/)](https://developer.mbed.org/users/mbed_official/code/Timer_HelloWorld/file/27e1de20d3cb/main.cpp) 

## API

API summary

[![View code](https://www.mbed.com/embed/?type=library)](https://developer.mbed.org/users/mbed_official/code/mbed/docs/tip/classmbed_1_1Timer.html) 

<span class="warnings">**Warning:** Timers are based on 32-bit int microsecond counters, so can only time up to a maximum of 2^31-1 microseconds i.e. 30 minutes. They are designed for times between microseconds and seconds. For longer times, you should consider the time()/Real time clock. </span> 

<span class="notes">**Note:** Implementation </br> The timer used to implement this functionality is:
</br>On the **LPC1768**: ``Timer 3 (LPC_TIM3)``
</br>On the **LPC11U24**: ``32-bit Counter/Timer B1 (LPC_CT32B1)`` </span>
