## USBMSD

The USBMSD interface is used to emulate a mass storage device over USB. You can use this class to store or load data to and from a storage chip (SDcard, flash,...). This class implements the MSD protocol and takes in a [BlockDevice](../storage/BlockDevice.md) to interact with a storage chip.

### USBMSD class reference

TODO

### USBMSD example

```C++
#include "mbed.h"
#include "SDBlockDevice.h"
#include "USBMSD.h"

SDBlockDevice sd(PTE3, PTE1, PTE2, PTE4);
USBMSD usb(&sd);

int main_msd() {
    usb.connect();

    while(true) {
        usb.process();
    }

    return 0;
}
```

### Related content

- [BlockDevice](../storage/BlockDevice.md)
