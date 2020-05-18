# Execution

Embedded systems are systems that are built for performing a sole dedicated duty. They are typically constrained in resources and contain only the necessary components to perform their duty. Most embedded systems are powered by a single microcontroller chip. That microcontroller is typically also limited in resources such as memory. Software for an embedded system must be carefully designed to make the best use of such limited resources. Mbed OS is often too large for such systems in its default configuration, but it supports additional modes that might be a better option depending on your target system.

Threading is a fundamental technique in software development, which allows multiple tasks to run concurrently. As microcontrollers become more capable, it has become possible to use threading in embedded systems, using schedulers, either standalone or included in a real time operating system (RTOS). In single-microcontroller embedded systems, a thread is an independent segment of the program which executes within the single process runnning on the microcontroller. Threads provide a lot of flexibility to the developer but come at the cost of resources for the scheduler. Mbed, in its default configuration, provides an RTOS to enable threading in applications where resources are not critical. There is also a bare metal profile which is optimized for constained targets and does not include the RTOS or threading capabilities.

## Threads

Your application (`main` function) starts execution in the main thread, but it's not the only thread running in Mbed OS. There are many threads running system services, such as:
* Main - The default thread that executes the application's `main` function. The main thread has 4kB of stack space by default. The application can configure it in `mbed_app.json` by defining the `MAIN_STACK_SIZE` parameter.
* Idle - The thread that's run by the scheduler when there's no other activity in the system (e.g. all other threads are waiting for some event). It's used to make sure the board is not burning empty processor cycles, but is put to sleep for as long as possible.
* Timer - The thread that handles system and user timer objects. *Note: The user timer class RtosTimer is deprecated. You should not use it for new designs. Use EventQueue instead.*

On top of the standard system threads, some drivers may use additional threads. Users can create threads using the [Thread class](../apis/thread.html).

## Modes

Mbed OS executes in two modes:

* Thread mode - Default application mode. All user threads execute in this mode. It uses dedicated thread specific stack memory.
* Handler mode - Interrupt mode, system code and interrupt handlers execute in this mode. It uses static system ISR stack memory.

### Handler mode

All the ISR handlers execute in this mode. You can use the same RTOS API in ISR handlers. The important difference between the modes is that code written for the handler mode can't wait; it executes as fast as possible and returns to the thread mode. Therefore:

* You cannot use `Mutex`.
* Wait in ISR is not allowed; all the timeouts in method parameters have to be set to 0.

**ISR example**

This example uses a message from the queue to trigger an interrupt.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_RTOS/Isr/)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_RTOS/Isr/main.cpp)
