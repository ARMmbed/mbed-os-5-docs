# Kernel interface functions

The Kernel namespace implements interfaces to attach a function to some kernel events and also to read the kernel tick count.

## Kernel namespace reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/namespacertos_1_1_kernel.html)

## Kernel::Clock example

The nested class `Clock` can be used to read the current RTOS kernel millisecond tick count as a C++11 Chrono time point. The below code snippet demonstrates use of `Kernel::Clock` to calculate the elapsed time:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_RTOS/Kernel_get_ms_count)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_RTOS/Kernel_get_ms_count/main.cpp)


## Kernel hooks example

You can use the function `attach_idle_hook()` to attach a function to be called by the RTOS idle task. You can use the function `attach_thread_terminate_hook()` to attach a function to be called when a thread terminates. The below code snippet demostrates the usage of these hooks.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_RTOS/Kernel_hooks)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_RTOS/Kernel_hooks/main.cpp)
