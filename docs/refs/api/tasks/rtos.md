<h3 id="rtos">RTOS</h3>


The mbed RTOS is a C++ wrapper over the Keil RTX code. For more information about Keil RTX, check [the Keil CMSIS-RTOS tutorial](https://github.com/ARM-software/CMSIS/raw/master/CMSIS/Documentation/RTX/CMSIS_RTOS_Tutorial.pdf) and [the element14 introduction to Keil RTX](https://www.element14.com/community/docs/DOC-46650/l/arm-keil-rtx-real-time-operating-system-overview). You can use these resources as a general introduction to RTOS principles; it is important to be familiar with the concepts behind an RTOS in order to understand this guide.

The code of the mbed RTOS can be found in the [mbed-os](https://github.com/ARMmbed/mbed-os) repository, in the [rtos subdirectory](https://github.com/ARMmbed/mbed-os/tree/master/rtos). The Doxygen is [available here](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/group__rtos.html).

<h4 id="thread">Thread</h4>

The [``Thread``](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classrtos_1_1Thread.html) class allows defining, creating and controlling thread functions in the system.

A ``Thread`` can be in the following states:

* ``Running``: The currently running thread. Only one thread at a time can be in this state.
* ``Ready``: Threads that are ready to run. Once the ``running`` thread has terminated or is ``waiting``, the ``ready`` thread with the highest priority becomes the ``running`` thread.
* ``Waiting``: Threads that are waiting for an event to occur.
* ``Inactive``: Threads that are not created or terminated. These threads typically consume no system resources.

<span class="images">![](Images/Thread/thread_status.png)</span>

<h5 id="thread-main">The main() function</h5>

The function ``main`` is a special thread function that is started at system initialization and has the initial priority ``osPriorityNormal``; it is the first thread the RTOS schedules.

<h5 id="thread-example">Thread example</h5>

The code below uses two separate threads to blink two LEDs. The first thread is automatically created and executes the `main` function; the second thread is created explicitly inside `main`.

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/rtos_basic/)](https://developer.mbed.org/teams/mbed_example/code/rtos_basic/file/dc33cd3f4eb9/main.cpp)

<h5 id="thread-example-callback">Thread example with callbacks</h5>

The Callback API provides a convenient way to pass arguments to spawned threads.  

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/rtos_threading_with_callback/)](https://developer.mbed.org/teams/mbed_example/code/rtos_threading_with_callback/file/d4b2a035ffe3/main.cpp)

<h5 id="thread-class">Thread class reference</h5>

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classrtos_1_1Thread.html)

<span class="images">![](Images/Thread/thread_priority.png)</span>

<h4 id="mutex">Mutex</h4>

A [``Mutex``](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classrtos_1_1Mutex.html) is used to synchronize the execution of threads, for example to protect the access to a shared resource.

<span class="warnings"> **Warning - ISR:** The ``Mutex`` methods cannot be called from interrupt service routines (ISR). In the current version of mbed OS, if you attempt to use a mutex from within an ISR, nothing happens; attempts to lock a mutex succeed immediately, regardless of whether the lock is actually free. In other words, if you acquire a mutex lock in an ISR, you can break the thread safety mechanisms and introduce race-conditions into an otherwise safe piece of code. Future versions of mbed OS will provide warnings and ultimately prevent this from happening. </span>

<span class="images">![](Images/Thread/Mutex.png)</span>

<h5 id="mutex-example">Mutex example</h5>

Use Mutex to protect printf().

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/rtos_mutex/)](https://developer.mbed.org/teams/mbed_example/code/rtos_mutex/file/1ae0d86d2020/main.cpp)

<span class="notes">**Note:** C standard library Mutexes</br>The ARM C standard library already has Mutexes in place to protect the access to ``stdio``, so on the LPC1768 the above example is not necessary. On the other hand, the LPC11U24 does not provide default ``stdio`` Mutexes, making the above example a necessity. </span>
<span class="warnings">**Warning:** ``stdio``, ``malloc`` and ``new`` in ISR</br>Because of the mutexes in the ARM C standard library, you cannot use ``stdio`` (``printf``, ``putc``, ``getc`` and so on), ``malloc`` and ``new`` in ISR. </span>

<h5 id="mutex-class">Mutex class reference</h5>

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classrtos_1_1Mutex.html)

<h4 id="semaphore">Semaphore</h4>

A [``Semaphore``](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classrtos_1_1Semaphore.html) manages thread access to a pool of shared resources of a certain type.

<span class="images">![](Images/Thread/Semaphore.png)</span>

<h5 id="semaphore-example">Semaphore example</h5>

Use Semaphore to protect printf().

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/rtos_semaphore/)](https://developer.mbed.org/teams/mbed_example/code/rtos_semaphore/file/574f47121e8e/main.cpp)

<h5 id="semaphore-class">Semaphore class reference</h5>

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classrtos_1_1Semaphore.html)

<h4 id="signals">Signals</h4>

Each ``Thread`` can wait for signals and be notified of events:

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/rtos_signals/)](https://developer.mbed.org/teams/mbed_example/code/rtos_signals/file/476186ff82cf/main.cpp)

<h4 id="queue-memorypool">Queue and MemoryPool</h4>

<h5 id="queue">Queue</h5>

A [``Queue``](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classrtos_1_1Queue.html) allows you to queue pointers to data from producer threads to consumer threads:

<span class="images">![](Images/Thread/queue.png)</span>

>>> c
```
Queue<message_t, 32> queue;

message_t *message;

queue.put(message);

osEvent evt = queue.get();
if (evt.status == osEventMessage) {
    message_t *message = (message_t*)evt.value.p;
```
>>>

<h5 id="queue-class">Queue class reference</h5>

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classrtos_1_1Queue.html)

<h5 id="memorypool">MemoryPool</h5>

You can use the [MemoryPool](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classrtos_1_1MemoryPool.html) class to define and manage fixed-size memory pools:

>>> c
```
MemoryPool<message_t, 16> mpool;

message_t *message = mpool.alloc();

mpool.free(message);
```
>>>

<h5 id="memorypool-class">MemoryPool class reference</h5>

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classrtos_1_1MemoryPool.html)

<h5 id="queue-memorypool-example">Queue and MemoryPool example</h5>

This example shows ``Queue`` and ``MemoryPool`` (see below) managing measurements.

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/rtos_queue/)](https://developer.mbed.org/teams/mbed_example/code/rtos_queue/file/0cb43a362538/main.cpp)

<h4 id="mail">Mail</h4>

[``Mail``](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classrtos_1_1Mail.html) works like a queue, with the added benefit of providing a memory pool for allocating messages (not only pointers).

<span class="images">![](Images/Thread/mail_queue.png)</span>

<h5 id="mail-class">Mail class reference</h5>

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classrtos_1_1Mail.html)

<h5 id="mail-example">Mail example</h5>

This code uses ``mail`` to manage measurement.

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/rtos_mail/)](https://developer.mbed.org/teams/mbed_example/code/rtos_mail/file/6602f2907ac5/main.cpp)

<h4 id="rtostimer">RtosTimer</h4>

<span class="warnings">**Deprecated**: The RtosTimer has been superseded by the EventQueue. The RtosTimer and EventQueue duplicate the functionality of timing events outside of interrupt context, however the EventQueue has additional features to handle deferring other events to multiple contexts.</span>

Use the [``RtosTimer``](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classrtos_1_1RtosTimer.html) class to create and and control timer functions in the system. A timer function is called when a time period expires, so both one-shot and periodic timers are possible. A timer can be started, restarted or stopped.

Timers are handled in the thread ``osTimerThread``. Callback functions run under the control of this thread and may use CMSIS-RTOS API calls.

<span class="images">![](Images/Thread/rtos_timer.png)</span>

<h5 id="rtostimer-example">RtosTimer example</h5>

Control the timing of four LEDs.

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed/code/rtos_timer/)](https://developer.mbed.org/teams/mbed/code/rtos_timer/file/tip/main.cpp)

<h5 id="rtostimer-class">RtosTimer class reference</h5>

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classrtos_1_1RtosTimer.html)

<h4 id="isr">Interrupt Service Routines (ISR)</h4>

You can use the same RTOS API in ISR. The only two warnings are:

* You cannot use ``Mutex``.
* Wait in ISR is not allowed; all the timeouts in method parameters have to be set to 0.

<h5 id="isr-example">ISR example</h5>

This example uses a message from the queue to trigger an interrupt.

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/rtos_isr/)](https://developer.mbed.org/teams/mbed_example/code/rtos_isr/file/40078e697304/main.cpp)

<h4 id="default-timeouts">Default Timeouts</h4>

The mbed RTOS API has made the choice of defaulting to ``0`` timeout (no wait) for the producer methods, and ``osWaitForever`` (infinite wait) for the consumer methods.

A typical scenario for a producer could be a peripheral triggering an interrupt to notify an event; in the corresponding interrupt service routine you cannot wait (this would deadlock the entire system). On the other side, the consumer could be a background thread waiting for events; in this case the desired default behaviour is not using CPU cycles until this event is produced, hence the ``osWaitForever``.

<span class="warnings">**Warning**: No wait in ISR </br>When calling an RTOS object method in an ISR all the timeout parameters have to be set to 0 (no wait); waiting in ISR is not allowed. </span>

<h4 id="status-errors">Status and error codes</h4>

The CMSIS-RTOS functions will return the following statuses:

* ``osOK``: function completed; no event occurred.
* ``osEventSignal``: function completed; signal event occurred.
* ``osEventMessage``: function completed; message event occurred.
* ``osEventMail``: function completed; mail event occurred.
* ``osEventTimeout``: function completed; timeout occurred.
* ``osErrorParameter``: a mandatory parameter was missing or specified an incorrect object.
* ``osErrorResource``: a specified resource was not available.
* ``osErrorTimeoutResource``:  a specified resource was not available within the timeout period.
* ``osErrorISR``: the function cannot be called from interrupt service routines (ISR).
* ``osErrorISRRecursive``: function called multiple times from ISR with same object.
* ``osErrorPriority``: system cannot determine priority or thread has illegal priority.
* ``osErrorNoMemory``: system is out of memory; it was impossible to allocate or reserve memory for the operation.
* ``osErrorValue``: value of a parameter is out of range.
* ``osErrorOS``: unspecified RTOS error - runtime error but no other error message fits.
