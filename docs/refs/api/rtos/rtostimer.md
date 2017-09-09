#### RtosTimer

<span class="warnings">**Deprecated**: The EventQueue has superseded the RtosTimer. The RtosTimer and EventQueue duplicate the functionality of timing events outside of interrupt context; however, the EventQueue has additional features to handle deferring other events to multiple contexts.</span>

Use the [`RtosTimer`](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classrtos_1_1RtosTimer.html) class to create and control timer functions in the system. A timer function is called when a time period expires, so both one-shot and periodic timers are possible. You can start, restart or stop a timer.

The thread `osTimerThread` handles timers. Callback functions run under the control of this thread and may use CMSIS-RTOS API calls.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/rtos_timer.png)</span>

##### RtosTimer class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classrtos_1_1RtosTimer.html)

##### RtosTimer example

Control the timing of four LEDs.

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed/code/rtos_timer/)](https://developer.mbed.org/teams/mbed/code/rtos_timer/file/tip/main.cpp)
