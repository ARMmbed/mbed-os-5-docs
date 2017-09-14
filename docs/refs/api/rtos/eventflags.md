#### EventFlags

The EventFlags class is a C++ wrapper over the Keil RTX EventFlags functionality. The EventFlags class provides a mechanism for setting and waiting for flags. It provides a generic way of notifying other threads about conditions or events. You can think of each instance of the EventFlags class as an event channel. There are 31 different flags available for each event. For more information and implementation details, see [the Keil CMSIS-RTOS documentation](http://arm-software.github.io/CMSIS_5/RTOS2/html/group__CMSIS__RTOS__EventFlags.html).

You can find the Arm Mbed OS EventFlags wrapper source code in the [Mbed OS repository](https://github.com/ARMmbed/mbed-os/blob/master/rtos/EventFlags.h).

##### EventFlags class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.6/api/classrtos_1_1EventFlags.html)

##### EventFlags example

Below is an example of EventFlags usage, where one thread is generating events every 1s, and the second thread is waiting for the events and executing some action.

<span class="images">![](Images/eventflags_usage.png)</span>


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
