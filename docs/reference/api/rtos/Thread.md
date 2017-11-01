## Thread

The <a href="https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/classrtos_1_1_thread.html" target="_blank">Thread</a> class allows defining, creating and controlling parallel tasks.

<span class="notes">**Note:** The function `main` is a special thread function that is started at system initialization.</span>

### Thread class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/classrtos_1_1_thread.html)

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/thread_priority.png)</span>

### Thread example

The code below uses two separate threads to blink two LEDs. The first thread is automatically created and executes the `main` function; the second thread is created explicitly inside `main`.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/rtos_basic/)](https://os.mbed.com/teams/mbed_example/code/rtos_basic/file/dc33cd3f4eb9/main.cpp)

### Thread example with callbacks

The Callback API provides a convenient way to pass arguments to spawned threads.  

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/rtos_threading_with_callback/)](https://os.mbed.com/teams/mbed_example/code/rtos_threading_with_callback/file/d4b2a035ffe3/main.cpp)
