# UserAllocatedEvent

The `UserAllocatedEvent` class provides APIs to create and configure static events. `UserAllocatedEvent` advantage over `Event` is that it embeds all underlying event data and doesn't require any memory allocation while posting and dispatching on to the EventQueue. To configure event timings use `delay` and `period` APIs. You can use `call` and `try_call` API to post an event to the underlying EventQueue or `call_on` and `try_call_on` API to bind and post an event to the EventQueue passed as function argument, and you can use `cancel` to cancel the most recently posted event. As the `UserAllocatedEvent` holds event data it can't be posted more then one at the time. It means that if the event object has to be reused the previous dispatch has to finish or event has to be canceled. `try_call` API can be used to sample the event state. `try_call` call will try to post event and will return false with no action until the previous dispatching won't finish.

The UserAllocatedEvent class is thread safe. The `call`, `try_call` and `cancel` APIs are IRQ safe.

## UserAllocatedEvent class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/_event_8h_source.html)

## Static EventQueue example: posting user allocated events to the queue

The code below demonstrates how you can instantiate, configure and post events.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/mbed-os-example-events/)](https://os.mbed.com/teams/mbed_example/code/mbed-os-example-events/file/86c4bf2d90fa/main.cpp)

## Related content

- [RTOS configuration](../reference/configuration-rtos.html).
- [EventQueue tutorial](../tutorials/the-eventqueue-api.html).
