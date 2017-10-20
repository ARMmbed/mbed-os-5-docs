## CriticalSectionLock

CriticalSectionLock class provides mechanism to access a resource uinterrupted. `lock` API is provided to enter critical section with interrupts disabled. `unlock` API is the exit from critical section and the state of interrupts is restored upon exit.
Nesting of critical section is supported and interrupts are enabled only when we exit from last nested critical section.
Note: Time consuming operations, standard library and RTOS functions must not be used inside critical section.

## CriticalSectionLock class reference
[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/classmbed_1_1_critical_section_lock.html)

## CriticalSectionLock example

Here is an example to demonstrate race condition issue and how critical section helps in resolving that.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/users/deepikabhavnani/code/mbed-os-example-criticalsection/)](https://os.mbed.com/users/deepikabhavnani/code/mbed-os-example-criticalsection/main.cpp)