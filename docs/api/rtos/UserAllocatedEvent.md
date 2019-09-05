# UserAllocatedEvent

The `UserAllocatedEvent` class provides APIs to create and configure static events. The advantage in using `UserAllocatedEvent` instead of `Event` is `UserAllocatedEvent` embeds all underlying event data and doesn't require any memory allocation while posting and dispatching to the EventQueue.

This class includes the following APIs:

- `delay` and `period` to configure event timings.
- `call` and `try_call` to post an event to the underlying EventQueue.
- `call_on` and `try_call_on` to bind and post an event to the EventQueue as a function argument.
- `cancel` to cancel the most recently posted event.

Because the `UserAllocatedEvent` holds event data, you can post only one event object to it at a time. This means that if the event object has to be reused, the previous dispatch has to finish or the event has to be canceled. You can use the `try_call` API to sample the event state. This call tries to post an event and returns false with no action until the previous dispatching finishes.

The UserAllocatedEvent class is thread safe. The `call`, `try_call` and `cancel` APIs are IRQ safe.

## UserAllocatedEvent class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/classevents_1_1_user_allocated_event.html)

## Static EventQueue example: posting user allocated events to the queue

This example demonstrates how you can instantiate, configure and post events:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/events/static-event-queue/UserAllocatedEvent_ex_1/)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/events/static-event-queue/UserAllocatedEvent_ex_1/main.cpp)


## Related content

- [RTOS configuration](../reference/configuration-rtos.html).
- [EventQueue tutorial](../tutorials/the-eventqueue-api.html).
