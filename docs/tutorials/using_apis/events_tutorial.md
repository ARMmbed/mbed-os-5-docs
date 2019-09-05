# The EventQueue API

One of the optional Arm Mbed OS features is an event loop mechanism that you can use to defer the execution of code to a different context. In particular, a common use of an event loop is to postpone the execution of a code sequence from an interrupt handler to a user context. This is useful because of the specific constraints of code that runs in an interrupt handler:

- The execution of certain functions (notably some functions in the C library) is not safe.
- You cannot use various RTOS objects and functions from an interrupt context.
- As a general rule, the code needs to finish as fast as possible, to allow other interrupts to be handled.

The event loop offers a solution to these issues in the form of an API that can defer execution of code from the interrupt context to the user context. More generally, the event loop can be used anywhere in a program (not necessarily in an interrupt handler) to defer code execution to a different context.

In Mbed OS, events are pointers to functions (and optionally function arguments). An event loop extracts events from a queue and executes them.

## Creating an event loop

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

## Using the event loop

Once you start the event loop, it can post events. Let's consider an example of a program that attaches two interrupt handlers for an InterruptIn object, using the InterruptIn `rise` and `fall` functions. The `rise` handler will run in interrupt context, and the `fall` handler will run in user context (more specifically, in the context of the event loop's thread). The full code for the example can be found below:

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/events_ex_1/)](https://os.mbed.com/teams/mbed_example/code/events_ex_1/file/69c11c7877b6/main.cpp)

The above code executes two handler functions (`rise_handler` and `fall_handler`) in two different contexts:

1. In interrupt context when a rising edge is detected on `SW2` (`rise_handler`).
2. In the context of the event loop's thread function when a falling edge is detected on `SW2` (`fall_handler`). `queue.event()` is called with `fall_handler` as an argument to specify that `fall_handler` will run in user context instead of interrupt context.

This is the output of the above program on an FRDM-K64F board. We reset the board and pressed the SW2 button twice:

```
Starting in context 20001fe0
fall_handler in context 20000b1c
rise_handler in context 00000000
fall_handler in context 20000b1c
rise_handler in context 00000000
```

The program starts in the context of the thread that runs the `main` function (`20001fe0`). When the user presses SW2, `fall_handler` is automatically queued in the event queue, and  it runs later in the context of thread `t` (`20000b1c`). When the user releases the button, `rise_handler` is executed immediately, and it displays `00000000`, indicating that the code ran in interrupt context.

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

## Prioritization

The EventQueue has no concept of event priority. If you schedule events to run at the same time, the order in which the events run relative to one another is undefined. The EventQueue only schedules events based on time. If you want to separate your events into different priorities, you must instantiate an EventQueue for each priority. You must appropriately set the priority of the thread dispatching each EventQueue instance.

## EventQueue memory pool

When you create an instance of the [EventQueue](../apis/event.html), you specify a fixed size for its memory. Because allocating from the general purpose heap is not IRQ safe, the EventQueue allocates this fixed size block of memory during its creation. Although the EventQueue memory size is fixed, the Eventqueue supports various sized events.

Various sized events introduce fragmentation to the memory region. This fragmentation makes it difficult to determine how many more events the EventQueue can dispatch. The EventQueue may be able to dispatch many small events, but fragmentation may prevent it from allocating one large event.

### Calculating the number of events

If your project only uses fix-sized events, you can use a counter that tracks the number of events the EventQueue has dispatched.

If your projects uses variable-sized events, you can calculate the number of available events of a specific size because successfully allocated memory is never fragmented further. However, untouched space can service any event that fits, which complicates such a calculation.

```
EventQueue queue(8*sizeof(int)); // 8 words of storage
queue.call(func, 1);       // requires 2 words of storage
queue.call(func, 1, 2, 3); // requires 4 words of storage
// after this we have 2 words of storage left

queue.dispatch(); // free all pending events

queue.call(func, 1, 2, 3); // requires 4 words of storage
queue.call(func, 1, 2, 3); // fails
// remaining storage has been fragmented into 2 events with 2 words
// of storage, no space is left for a 4 word event even though 4 bytes
// exist in the memory region
```

### Failure due to fragmentation

The following example would fail because of fragmentation:

```
EventQueue queue(4*sizeof(int)); // 4 words of storage
queue.call(func);       // requires 1 word of storage
queue.call(func);       // requires 1 word of storage
queue.call(func);       // requires 1 word of storage
queue.call(func);       // requires 1 word of storage
// 0 words of storage remain

queue.dispatch();  // free all pending events
// all memory is free again (4 words) and in one-word chunks

queue.call(func, 1, 2, 3); // requires 4 words of storage, so allocation fails
```

Four words of storage are free but only for allocations of one word or less. The solution to this failure is to increase the size of your EventQueue. Having the proper sized EventQueue prevents you from running out of space for events in the future.

### More about events

This is only a small part of how event queues work in Mbed OS. The `EventQueue`, `Event` and `UserAllocatedEvent` classes in the `mbed-events` library offer a lot of features that this document does not cover, including calling functions with arguments, queueing functions to be called after a delay or queueing functions to be called periodically. The [README of the `mbed-events` library](https://github.com/ARMmbed/mbed-os/blob/master/events/README.md) shows more ways to use events and event queues. To see the implementation of the events library, review [the equeue library](https://os.mbed.com/docs/development/mbed-os-api-doxy/_event_queue_8h_source.html).

## Static EventQueue

The EventQueue API provides a mechanism for creating a static queue, a queue that doesn't use any dynamic memory allocation and accepts only user-allocated events. After you create a static queue (by passing zero as `size` to its constructor), you can post `UserAllocatedEvent` to it. Using static EventQueue combined with UserAllocatedEvent ensures no dynamic memory allocation will take place during queue creation and events posting and dispatching. You can also declare queues and events as static objects (static in the C++ sense), and then memory for them will be reserved at compile time:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/events/static-event-queue/UserAllocatedEvent_ex_1/)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/events/static-event-queue/UserAllocatedEvent_ex_1/main.cpp)
