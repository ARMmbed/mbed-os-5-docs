## CriticalSectionLock

CriticalSectionLock class provides a mechanism to access a resource without interruption. With the `lock` API, you can enter critical section with interrupts disabled. The `unlock` API is the exit from critical section, and the state of interrupts is restored upon exit. Nesting of critical section is supported, and interrupts are enabled only when we exit from last nested critical section.

CriticalSectionLock class is based on RAII approach i.e. lock is acquired in constructor and destroyed automatically when out of scope as part of destructor. Usage of CriticalSectionLock as global or member of class is not recommended, as you will enter critical section on object creation and all interrupts will be disabled.


<span class="notes">**Note:** You must not use time consuming operations, standard library and RTOS functions inside critical section.</span>

## CriticalSectionLock class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/classmbed_1_1_critical_section_lock.html)

## CriticalSectionLock example

Here is an example that demonstrates a race condition issue and how CriticalSectionLock helps resolves it.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/mbed-os-example-critical-section/)](https://os.mbed.com/teams/mbed_example/code/mbed-os-example-critical-section/file/a88acbffd78b/main.cpp)
