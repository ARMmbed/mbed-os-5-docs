## CriticalSectionLock

CriticalSectionLock class provides a mechanism to access a resource uniterrupted. With the `lock` API, you can enter critical section with interrupts disabled. The `unlock` API is the exit from critical section, and the state of interrupts is restored upon exit. Nesting of critical section is supported, and interrupts are enabled only when we exit from last nested critical section.

<span class="notes">**Note:** You must not use time consuming operations, standard library and RTOS functions inside critical section.</span>

## CriticalSectionLock class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/classmbed_1_1_critical_section_lock.html)

## CriticalSectionLock example

Here is an example that demonstrates a race condition issue and how critical section helps resolves it.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/users/deepikabhavnani/code/mbed-os-example-criticalsection/)](https://os.mbed.com/users/deepikabhavnani/code/mbed-os-example-criticalsection/main.cpp)
