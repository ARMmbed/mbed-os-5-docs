# Event

The Event class provides APIs to configure events `delay` and `period` timings. The timings use the std::chrono::duration class provided by the <utility> library. You can use `post` API to post an event to the underlying EventQueue, and you can use `cancel` to cancel the most recently posted event.

The Event class is thread safe. The `post` and `cancel` APIs are IRQ safe.

## Event class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/classevents_1_1_event_3_01void_07_arg_ts_8_8_8_08_4.html)

## EventQueue example: posting events to the queue

The code below demonstrates how you can instantiate, configure and post events.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Events_ex_1/tree/v6.0)](https://github.com/ARMmbed/mbed-os-snippet-Events_ex_1/blob/v6.0/main.cpp)

## Related content

- [RTOS configuration](../apis/scheduling-options-and-config.html).
- [EventQueue tutorial](../apis/scheduling-tutorials.html).
