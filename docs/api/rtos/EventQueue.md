# EventQueue

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/classevents_1_1_event_queue.png)<span>EventQueue class hierarchy</span></span>

The EventQueue class provides a flexible queue for scheduling events. You can use the EventQueue class for synchronization between multiple threads, or to move events out of interrupt context (deferred execution of time consuming or non-ISR safe operations).

The EventQueue class is thread and ISR safe.

You can use the `dispatch` and `dispatch_forever` APIs to execute pending events. `break_dispatch` is to terminate the execution of events in the specified EventQueue.

## Shared event queues

Mbed OS provides two shared queues software can use. This can avoid the need to create private event dispatch threads and reduce the total amount of RAM used.

## EventQueue class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classevents_1_1_event_queue.html)

## Shared event queue reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/mbed__shared__queues_8h_source.html)

## EventQueue example: deferring from interrupt context

The code executes two handler functions (`rise_handler` and `fall_handler`) in two different contexts:

1. In interrupt context when a rising edge is detected on `SW2` (`rise_handler`).
2. In the context of the event loop's thread function when a falling edge is detected on `SW2` (`fall_handler`). You can use the `fall_handler` function as an argument to `queue.event()` to specify that `fall_handler` runs in user context instead of interrupt context.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/events_ex_1/)](https://os.mbed.com/teams/mbed_example/code/events_ex_1/file/69c11c7877b6/main.cpp)

## Shared event example: deferring from interrupt context

Like the previous example, this defers from interrupt to an event queue thread. However, rather than creating its own thread, it uses the shared event queue – potentially sharing it with other system components and saving RAM.

As the event queue is shared, you should limit the execution time of your event functions to avoid delaying other users’ events excessively.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/Shared_Events_1/)](https://os.mbed.com/teams/mbed_example/code/Shared_Events_1/file/7c7d5b625e59/main.cpp)

## EventQueue example: posting events to the queue

The code below demonstrates queueing functions to be called after a delay and queueing functions to be called periodically.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/events_ex_2/)](https://os.mbed.com/teams/mbed_example/code/events_ex_2/file/488fe91e2e80/main.cpp)

## EventQueue example: chaining events from more than one queue

Event queues easily align with module boundaries, where event dispatch can implicitly synchronize internal state. Multiple modules can use independent event queues but still be composed through the `EventQueue::chain` function.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/events_ex_3/)](https://os.mbed.com/teams/mbed_example/code/events_ex_3/file/fca134a32b61/main.cpp)

## Shared event example: running the shared queue from main

To further save RAM, if you have no other work to do in your main function after initialization, you can dispatch the global event queue from there, avoiding the need to create a separate dispatch thread.

To do this, set the `mbed_app.json` configuration option `events.shared-dispatch-from-application` to true, and add a dispatch call to main, as in this example. (The prints now show the same context for startup and `fall_handler`).

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/Shared_Events_2/)](https://os.mbed.com/teams/mbed_example/code/Shared_Events_2/file/154179bdc39d/main.cpp)

## Static EventQueue example: posting user allocated events to the static queue

Use static EventQueue to prevent your program from failing due to queue memory exhaustion or to prevent dynamic memory allocation:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/events/static-event-queue/UserAllocatedEvent_ex_1/)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/events/static-event-queue/UserAllocatedEvent_ex_1/main.cpp)

## Related content

- [EventQueue tutorial](../tutorials/the-eventqueue-api.html).
