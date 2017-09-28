## Execution

You can use the same RTOS API in ISR. The only two warnings are:

* You cannot use `Mutex`.
* Wait in ISR is not allowed; all the timeouts in method parameters have to be set to 0.

**ISR example**

This example uses a message from the queue to trigger an interrupt.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/rtos_isr/)](https://os.mbed.com/teams/mbed_example/code/rtos_isr/file/40078e697304/main.cpp)
