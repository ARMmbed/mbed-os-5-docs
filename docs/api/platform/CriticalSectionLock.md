# CriticalSectionLock

The CriticalSectionLock class provides a mechanism to access a resource without interruption. With the `CriticalSectionLock::enable` API, you can enter critical section with interrupts disabled. The `CriticalSectionLock::disable()` API is the exit from critical section, and the last exit call restores the state of interrupts.

CriticalSectionLock class is based on RAII approach. In other words, the constructor acquires the lock, and the destructor destroys it automatically when it is out of scope. We do not recommend you use CriticalSectionLock as global or a member of a class because you will enter critical section on object creation, and all interrupts will be disabled.

Mbed OS supports nesting of critical section, and the destructor enables interrupts only when you exit from the last nested critical section.

<span class="notes">**Note:** You must not use time-consuming operations, standard library and RTOS functions inside critical section.</span>

## CriticalSectionLock class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_critical_section_lock.html)

## CriticalSectionLock example

Here is an example that demonstrates a race condition issue and how CriticalSectionLock helps resolves it.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/mbed-os-example-critical-section/)](https://os.mbed.com/teams/mbed_example/code/mbed-os-example-critical-section/file/a88acbffd78b/main.cpp)
