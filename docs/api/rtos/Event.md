# Event

The Event class provides APIs to configure events `delay` and `period` timings. You can use `post` API to post an event to the underlying EventQueue, and you can use `cancel` to cancel the most recently posted event.

The Event class is thread safe. The `post` and `cancel` APIs are IRQ safe.

## Event class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.0-preview/mbed-os-api-doxy/_event_8h_source.html)

## EventQueue example: posting events to the queue

The code below demonstrates how you can instantiate, configure and post events.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_RTOS/Events_ex_1/)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_RTOS/Events_ex_1/main.cpp)

## Related content

- [RTOS configuration](../reference/configuration-rtos.html).
- [EventQueue tutorial](../tutorials/the-eventqueue-api.html).
