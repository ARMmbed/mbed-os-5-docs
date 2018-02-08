## Watchdog

Use the Watchdog interface to set up a hardware watchdog which will reset the system after a set period of time if not periodically refreshed before it expires.

### Warnings and notes

* The maximum amount of time that can be set as the Watchdog timeout varies depending on the target hardware. The maximum value can be checked by calling `Watchdog::max_timeout()`.

### Watchdog class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/v5.8/mbed-os-api-doxy/classmbed_1_1_watchdog.html)

### Watchdog example

Create a watchdog timer that expires after 5 seconds, the timer is refreshed by pushing BUTTON1 on the target board.

```c++
#include "mbed.h"

#include "InterruptIn.h"
#include "mbed_sleep.h"
#include "Watchdog.h"

mbed::InterruptIn button(BUTTON1);
mbed::Watchdog watchdog;

void trigger()
{
  printf("Refreshing watchdog timer\r\n");
  watchdog.kick();
}

int main()
{
  printf("Board started, Watchdog timer initialized to 5 seconds.\r\n");
  watchdog.start(5000);

  button.rise(&trigger);

  sleep();
}
```
