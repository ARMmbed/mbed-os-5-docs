### RTOS

The Arm Mbed RTOS is a C++ wrapper over the Keil RTX code. For more information about Keil RTX, check [the Keil CMSIS-RTOS tutorial](https://github.com/ARM-software/CMSIS/raw/master/CMSIS/Documentation/RTX/CMSIS_RTOS_Tutorial.pdf) and [the element14 introduction to Keil RTX](https://www.element14.com/community/docs/DOC-46650/l/arm-keil-rtx-real-time-operating-system-overview). You can use these resources as a general introduction to RTOS principles; it is important to be familiar with the concepts behind an RTOS in order to understand this guide.

The code of the Mbed RTOS can be found in the [`mbed-os`](https://github.com/ARMmbed/mbed-os) repository, in the [rtos subdirectory](https://github.com/ARMmbed/mbed-os/tree/master/rtos). The Doxygen is [available here](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/group__rtos.html).

##### Default Timeouts

The Mbed RTOS API has made the choice of defaulting to `0` timeout (no wait) for the producer methods, and `osWaitForever` (infinite wait) for the consumer methods.

A typical scenario for a producer could be a peripheral triggering an interrupt to notify an event; in the corresponding interrupt service routine you cannot wait (this would deadlock the entire system). On the other side, the consumer could be a background thread waiting for events; in this case the desired default behaviour is not using CPU cycles until this event is produced, hence the `osWaitForever`.

<span class="warnings">**Warning**: No wait in ISR </br>When calling an RTOS object method in an ISR all the timeout parameters have to be set to 0 (no wait); waiting in ISR is not allowed. </span>

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

##### The main() function

The function `main` is a special thread function that is started at system initialization and has the initial priority `osPriorityNormal`; it is the first thread the RTOS schedules.

A `Thread` can be in the following states:

* `Running`: The currently running thread. Only one thread at a time can be in this state.
* `Ready`: Threads that are ready to run. Once the ``running`` thread has terminated or is `waiting`, the `ready` thread with the highest priority becomes the `running` thread.
* `Waiting`: Threads that are waiting for an event to occur.
* `Inactive`: Threads that are not created or terminated. These threads typically consume no system resources.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/thread_status.png)</span>

##### The EventQueue API

One of the optional Arm Mbed OS features is an event loop mechanism that you can use to defer the execution of code to a different context. In particular, a common use of an event loop is to postpone the execution of a code sequence from an interrupt handler to a user context. This is useful because of the specific constraints of code that runs in an interrupt handler:

- The execution of certain functions (notably some functions in the C library) is not safe.
- You cannot use various RTOS objects and functions from an interrupt context.
- As a general rule, the code needs to finish as fast as possible, to allow other interrupts to be handled.

The event loop offers a solution to these issues in the form of an API that can defer execution of code from the interrupt context to the user context. More generally, the event loop can be used anywhere in a program (not necessarily in an interrupt handler) to defer code execution to a different context.

In Mbed OS, events are pointers to functions (and optionally function arguments). An event loop extracts events from a queue and executes them.

###### Creating an event loop

You must create and start the event loop manually. The simplest way to achieve that is to create a `Thread` and run the event queue's `dispatch` method in the thread:

```
#include "mbed.h"

// Create a queue that can hold a maximum of 32 events
EventQueue queue(32 * EVENTS_EVENT_SIZE);
// Create a thread that'll run the event queue's dispatch function
Thread t;

int main () {
    // Start the event queue's dispatch thread
    t.start(callback(&queue, &EventQueue::dispatch_forever));
}
```

Note that though this document assumes the presence of a single event loop in the system, there's nothing preventing the programmer from running more than one event loop, simply by following the create/start pattern above for each of them.

###### Using the event loop

Once you start the event loop, it can post events. Let's consider an example of a program that attaches two interrupt handlers for an InterruptIn object, using the InterruptIn `rise` and `fall` functions. The `rise` handler will run in interrupt context, and the `fall` handler will run in user context (more specifically, in the context of the event loop's thread). The full code for the example can be found below:

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/events_ex_1/)](https://developer.mbed.org/teams/mbed_example/code/events_ex_1/file/aea2e03f5625/main.cpp)

The above code executes two handler functions (`rise_handler` and `fall_handler`) in two different contexts:

1. In interrupt context when a rising edge is detected on `SW2` (`rise_handler`).
2. In the context of the event loop's thread function when a falling edge is detected on `SW2` (`fall_handler`). `queue.event()` is called with `fall_handler` as an argument to specify that `fall_handler` will run in user context instead of interrupt context.

This is the output of the above program on an FRDM-K64F board. We reset the board and pressed the SW2 button twice:

```
Starting in context 0x20002c50
fall_handler in context 0x20002c90
rise_handler in context 0x0
fall_handler in context 0x20002c90
rise_handler in context 0x0
```

The program starts in the context of the thread that runs the `main` function (`0x29992c5`). When the user presses SW2, `fall_handler` is automatically queued in the event queue, and  it runs later in the context of thread `t` (`0x20002c90`). When the user releases the button, `rise_handler` is executed immediately, and it displays `0x0`, indicating that the code ran in interrupt context.

The code for `rise_handler` is problematic because it calls `printf` in interrupt context, which is a potentially unsafe operation. Fortunately, this is exactly the kind of problem that event queues can solve. We can make the code safe by running `rise_handler` in user context (like we already do with `fall_handler`) by replacing this line:

```
sw.rise(rise_handler);
```

with this line:

```
sw.rise(queue.event(rise_handler));
```

The code is safe now, but we may have introduced another problem: latency. After the change above, the call to `rise_handler` will be queued, which means that it no longer runs immediately after the interrupt is raised. For this example code, this isn't a problem, but some applications might need the code to respond as fast as possible to an interrupt.

Let's assume that `rise_handler` must toggle the LED as quickly as possible in response to the user's action on SW2. To do that, it must run in interrupt context. However, `rise_handler` still needs to print a message indicating that the handler was called; that's problematic because it's not safe to call `printf` from an interrupt context.

The solution is to split `rise_handler` into two parts: the time critical part will run in interrupt context, while the non-critical part (displaying the message) will run in user context. This is easily doable using `queue.call`:

```
void rise_handler_user_context(void) {
    printf("rise_handler_user_context in context %p\r\n", Thread::gettid());
}

void rise_handler(void) {
    // Execute the time critical part first
    led1 = !led1;
    // The rest can execute later in user context (and can contain code that's not interrupt safe).
    // We use the 'queue.call' function to add an event (the call to 'rise_handler_user_context') to the queue.
    queue.call(rise_handler_user_context);
}
```

After replacing the code for `rise_handler` as above, the output of our example becomes:

```
Starting in context 0x20002c50
fall_handler in context 0x20002c90
rise_handler_user_context in context 0x20002c90
fall_handler in context 0x20002c90
rise_handler_user_context in context 0x20002c90
```

The scenario above (splitting an interrupt handler's code into time critical code and non-time critical code) is another common pattern that you can easily implement with event queues; queuing code that's not interrupt safe is not the only thing you can use event queues for. Any kind of code can be queued and deferred for later execution.

We used `InterruptIn` for the example above, but the same kind of code can be used with any `attach()`-like functions in the SDK. Examples include `Serial::attach()`, `Ticker::attach()`, `Ticker::attach_us()`, `Timeout::attach()`.

###### Prioritization

The EventQueue has no concept of event priority. If you schedule events to run at the same time, the order in which the events run relative to one another is undefined. The EventQueue only schedules events based on time. If you want to separate your events into different priorities, you must instantiate an EventQueue for each priority. You must appropriately set the priority of the thread dispatching each EventQueue instance.

###### More about events

We have discussed only a small part of how event queues work in Mbed OS. The `EventQueue` and `Event` classes in the `mbed-events` library offer a lot of features that this document does not cover, including calling functions with arguments, queueing functions to be called after a delay or queueing functions to be called periodically. The [README of the `mbed-events` library](https://github.com/ARMmbed/mbed-os/blob/master/events/README.md) shows more ways to use events and event queues. To see the implementation of the events library, review [the equeue library](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/equeue_8h_source.html)

##### Signals

Each `Thread` can wait for signals and be notified of events:

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/rtos_signals/)](https://developer.mbed.org/teams/mbed_example/code/rtos_signals/file/476186ff82cf/main.cpp)

##### RTOS APIs

The RTOS APIs handle creation and destruction of threads in Arm Mbed OS 5, as well as mechanisms for safe interthread communication. Threads are a core component of Mbed OS 5 (even your `main` function starts in a thread of its own), so understanding how to work with them is an important part of developing applications for Mbed OS 5. Pay particular attention to the [interrupt service routines](rtos.md#interrupt-service-routines) section, which contains important information about how the task management APIs can be used from an interrupt handler.

* [RTOS](#rtos-overview): The CMSIS-RTOS core.
* [Event Loop](#the-event-loop): The queue to store events, extract them and excute them later.
* [Ticker](Ticker.md): Set up a recurring interrupt.
* [Time](Time.md): The C date and time functions.
* [Timeout](TimeOut.md): Raise interrupt after certain time.
* [Timer](Timer.md): Measuring small times.
* [Wait](wait.md): NOP-type wait capabilities.

#### Task management options

[A document comparing ticker, time, timeout, wait and others.]
