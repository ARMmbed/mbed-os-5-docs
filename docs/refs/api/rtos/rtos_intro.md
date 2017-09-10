### RTOS

The Arm Mbed RTOS is a C++ wrapper over the Keil RTX code. For more information about Keil RTX, check [the Keil CMSIS-RTOS tutorial](https://github.com/ARM-software/CMSIS/raw/master/CMSIS/Documentation/RTX/CMSIS_RTOS_Tutorial.pdf) and [the element14 introduction to Keil RTX](https://www.element14.com/community/docs/DOC-46650/l/arm-keil-rtx-real-time-operating-system-overview). You can use these resources as a general introduction to RTOS principles; it is important to be familiar with the concepts behind an RTOS in order to understand this guide.

The code of the Mbed RTOS can be found in the [`mbed-os`](https://github.com/ARMmbed/mbed-os) repository, in the [rtos subdirectory](https://github.com/ARMmbed/mbed-os/tree/master/rtos). The Doxygen is [available here](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.6/api/group__rtos.html).

##### RTOS APIs

The RTOS APIs handle creation and destruction of threads in Arm Mbed OS 5, as well as mechanisms for safe interthread communication. Threads are a core component of Mbed OS 5 (even your `main` function starts in a thread of its own), so understanding how to work with them is an important part of developing applications for Mbed OS 5.

* [Thread](/docs/v5.4/reference/api-references.html#thread): The class that allows defining, creating and controlling parallel tasks.
* [Mutex](/docs/v5.4/reference/api-references.html#mutex): The class used to synchronize the execution of threads.
* [Semaphore](/docs/v5.4/reference/api-references.html#semaphore): The class that manages thread access to a pool of shared resources of a certain type.
* [Queue and Memory Pool](/docs/v5.4/reference/api-references.html#queue-and-memorypool): Classes used to queue pointers and to define and manage fixed-size memory pools.
* [RtosTimer](/docs/v5.4/reference/api-references.html#rtostimer): A deprecated class used to control timer functions in the system.
* [Event](/docs/v5.4/reference/api-references.html#events): The queue to store events, extract them and excute them later.
* [EventFlag](https://os-doc-builder.test.mbed.com/docs/v5.4/reference/api-references.html#eventflags): 

##### Default Timeouts

The Mbed RTOS API has made the choice of defaulting to `0` timeout (no wait) for the producer methods, and `osWaitForever` (infinite wait) for the consumer methods.

A typical scenario for a producer could be a peripheral triggering an interrupt to notify an event; in the corresponding interrupt service routine you cannot wait (this would deadlock the entire system). On the other side, the consumer could be a background thread waiting for events; in this case the desired default behaviour is not using CPU cycles until this event is produced, hence the `osWaitForever`.

<span class="warnings">**Warning**: No wait in ISR </br> When calling an RTOS object method in an ISR, all the timeout parameters must be set to 0 (no wait); waiting in ISR is not allowed. </span>

##### The main() function

The function `main` is a special thread function that is started at system initialization and has the initial priority `osPriorityNormal`; it is the first thread the RTOS schedules.

A `Thread` can be in the following states:

* `Running`: The currently running thread. Only one thread at a time can be in this state.
* `Ready`: Threads that are ready to run. Once the ``running`` thread has terminated or is `waiting`, the `ready` thread with the highest priority becomes the `running` thread.
* `Waiting`: Threads that are waiting for an event to occur.
* `Inactive`: Threads that are not created or terminated. These threads typically consume no system resources.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/thread_status.png)</span>

##### Signals

Each `Thread` can wait for signals and be notified of events:

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/rtos_signals/)](https://developer.mbed.org/teams/mbed_example/code/rtos_signals/file/476186ff82cf/main.cpp)


##### Status and error codes

The CMSIS-RTOS functions will return the following statuses:

* `osOK`: function completed; no event occurred.
* `osEventSignal`: function completed; signal event occurred.
* `osEventMessage`: function completed; message event occurred.
* `osEventMail`: function completed; mail event occurred.
* `osEventTimeout`: function completed; timeout occurred.
* `osErrorParameter`: a mandatory parameter was missing or specified an incorrect object.
* `osErrorResource`: a specified resource was not available.
* `osErrorTimeoutResource`:  a specified resource was not available within the timeout period.
* `osErrorISR`: the function cannot be called from interrupt service routines (ISR).
* `osErrorISRRecursive`: function called multiple times from ISR with same object.
* `osErrorPriority`: system cannot determine priority or thread has illegal priority.
* `osErrorNoMemory`: system is out of memory; it was impossible to allocate or reserve memory for the operation.
* `osErrorValue`: value of a parameter is out of range.
* `osErrorOS`: unspecified RTOS error - runtime error but no other error message fits.

