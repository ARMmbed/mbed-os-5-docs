## Watchdog

Use the Watchdog interface to set up a hardware watchdog that resets the system after a set period of time if you do not periodically refresh it before it expires.

<span class="notes">**Note:** The maximum amount of time that you can set as the Watchdog timeout varies depending on the target hardware. You can check the maximum value by calling `Watchdog::max_timeout()`.</span>

### Watchdog class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/v5.8/mbed-os-api-doxy/classmbed_1_1_watchdog.html)

### Watchdog example

Create a watchdog timer that expires after 5 seconds and that you refresh by pushing BUTTON1 on the target board.

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
