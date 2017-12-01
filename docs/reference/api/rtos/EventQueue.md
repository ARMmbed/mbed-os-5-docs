## EventQueue

The EventQueue class provides a flexible queue for scheduling events. You can use the EventQueue class for synchronization between multiple threads, or to move events out of interrupt context (deferred execution of time consuming or non-ISR safe operations).

The EventQueue class is thread and ISR safe.

You can use the `dispatch` and `dispatch_forever` APIs to execute pending events. `break_dispatch` is to terminate the execution of events in the specified EventQueue. 

### EventQueue class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/classevents_1_1_event_queue.html)

### EventQueue example: deferring from interrupt context

The code executes two handler functions (`rise_handler` and `fall_handler`) in two different contexts:

1. In interrupt context when a rising edge is detected on `SW2` (`rise_handler`).
2. In the context of the event loop's thread function when a falling edge is detected on `SW2` (`fall_handler`). You can use the `fall_handler` function as an argument to `queue.event()` to specify that `fall_handler` runs in user context instead of interrupt context.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/events_ex_1/)](https://os.mbed.com/teams/mbed_example/code/events_ex_1/file/6ae734681f16/main.cpp)

### EventQueue example: posting events to the queue

The code below demonstrates queueing functions to be called after a delay and queueing functions to be called periodically.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/events_ex_2/)](https://os.mbed.com/teams/mbed_example/code/events_ex_2/file/488fe91e2e80/main.cpp)

### EventQueue example: chaining events from more than one queue

Event queues easily align with module boundaries, where event dispatch can implicitly synchronize internal state. Multiple modules can use independent event queues but still be composed through the `EventQueue::chain` function.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/events_ex_3/)](https://os.mbed.com/teams/mbed_example/code/events_ex_3/file/fca134a32b61/main.cpp)
