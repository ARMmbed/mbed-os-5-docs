#### Thread

The [`Thread`](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classrtos_1_1Thread.html) class allows defining, creating and controlling thread functions in the system.

A `Thread` can be in the following states:

* `Running`: The currently running thread. Only one thread at a time can be in this state.
* `Ready`: Threads that are ready to run. Once the ``running`` thread has terminated or is `waiting`, the `ready` thread with the highest priority becomes the `running` thread.
* `Waiting`: Threads that are waiting for an event to occur.
* `Inactive`: Threads that are not created or terminated. These threads typically consume no system resources.

<span class="images">![](Images/Thread/thread_status.png)</span>

##### The main() function

The function `main` is a special thread function that is started at system initialization and has the initial priority `osPriorityNormal`; it is the first thread the RTOS schedules.

##### Thread example

The code below uses two separate threads to blink two LEDs. The first thread is automatically created and executes the `main` function; the second thread is created explicitly inside `main`.

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/rtos_basic/)](https://developer.mbed.org/teams/mbed_example/code/rtos_basic/file/dc33cd3f4eb9/main.cpp)

##### Thread example with callbacks

The Callback API provides a convenient way to pass arguments to spawned threads.  

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/rtos_threading_with_callback/)](https://developer.mbed.org/teams/mbed_example/code/rtos_threading_with_callback/file/d4b2a035ffe3/main.cpp)

##### Thread class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classrtos_1_1Thread.html)

<span class="images">![](Images/Thread/thread_priority.png)</span>
