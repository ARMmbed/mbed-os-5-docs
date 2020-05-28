When writing an Mbed OS program, in whichever development tool you use, you may need to:

* Set up a serial connection to your board so you can flash and debug your program.
    * You won't usually need a serial driver for Mbed enabled boards, but if you're on Windows you [may need to install one](../program-setup/windows-serial-driver.html).
    * Mbed CLI has a built-in serial terminal to display output from your program.
* Select or create a build profile.
* Use build rules to include or exclude files and directories from your build.
* Use the configuration system to define how your board uses features and the bootloader.
* Modify or set up a new target.

# Execution

Most embedded systems are dedicated to performing a single duty, although some can be very complex. They are typically constrained in resources and contain only the necessary components to perform that duty. Most embedded systems are powered by a single microcontroller chip, which is typically limited in resources such as memory. Software for an embedded system must be carefully designed to make the best use of these limited resources. Mbed OS in the default full profile is often too large for constrained systems, but has a bare metal profile that is targeted to those systems.

## Threads

In single-microcontroller embedded systems, a thread is an independent segment of the program that executes within the single process running on the microcontroller. Threading is a fundamental technique in software development, which allows multiple tasks to run concurrently using schedulers, either standalone or included in a real time operating system (RTOS). Threads provide a lot of flexibility to the developer but come at the cost of resources for the scheduler. Mbed OS, in its default full profile, provides an RTOS for applications where resources are not critical. The bare metal profile does not include the RTOS or threading capabilities.

There are two types of schedulers:

* Preemptive
    * A scheduler (a central piece of software) is responsible for piking and running the threads. Schedulers can use different algorithms:
        * Priority based round robin is used by Mbed OS
        * Threads are executed in equal time slots according to their priority
* Cooperative
    * Active thread needs to yield execution for another thread to run
    * Not supported by Mbed OS

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

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Isr/tree/v6.0)](https://github.com/ARMmbed/mbed-os-snippet-Isr/blob/v6.0/main.cpp)
