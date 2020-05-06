# ThisThread

Use the ThisThread class to control the current thread. 

Unlike the [Thread](../apis/thread.html) API, which allows you to create, join and end threads, ThisThread lets you control the thread that's currently running. A thread may not have a corresponding Mbed Thread object because you can create a thread directly with CMSIS-RTOS APIs, or it might be main's thread. You can't manipulate those with Thread methods, but ThisThread functions still work from inside them.

## ThisThread class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/namespacertos_1_1_this_thread.html)

## ThisThread example

Spawn a thread to blink for 5 seconds before setting a flag to trigger the thread to terminate.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-thisthread/)](https://github.com/ARMmbed/mbed-os-example-thisthread/blob/master/main.cpp)

## Related content

- [Thread](../apis/thread.html) API reference.
