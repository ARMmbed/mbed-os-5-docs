## EventFlags

The EventFlags class is a C++ wrapper over the Keil RTX EventFlags functionality. The EventFlags class provides a mechanism for setting and waiting for flags. It provides a generic way of notifying other threads about conditions or events. You can think of each instance of the EventFlags class as an event channel. There are 31 different flags available for each event. For more information and implementation details, see [the Keil CMSIS-RTOS documentation](http://arm-software.github.io/CMSIS_5/RTOS2/html/group__CMSIS__RTOS__EventFlags.html).

### EventFlag class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/v5.7/mbed-os-api-doxy/classrtos_1_1_event_flags.html)

### EventFlags example

Below is an example of EventFlags usage, where one thread is generating events every 1s, and the second thread is waiting for the events and executing some action.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images//eventflags_usage.png)</span>

```
#include "mbed.h"

EventFlags event;

void worker_f()
{
    while (true) {
        event.wait_all(0x1);

        printf("Got signal!\r\n");
    }
}

int main()
{
    Thread worker;

    worker.start(callback(worker_f));

    while (true) {
        wait(1);
        event.set(0x1);
    }
}
```

### Related content

- [The Keil CMSIS-RTOS](http://arm-software.github.io/CMSIS_5/RTOS2/html/group__CMSIS__RTOS__EventFlags.html) documentation.
