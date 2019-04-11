# USBMSD

<span class="images">![](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_u_s_b_m_s_d.png)<span>USBMSD class hierarchy</span></span>

You can use the USBMSD interface to emulate a mass storage device over USB. You can use this class to store or load data to and from a storage chip, such as SDcard or Flash. This class implements the MSD protocol and takes in a [BlockDevice](blockdevice.html) to interact with a storage chip.

## USBMSD class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_u_s_b_m_s_d.html)

## USBMSD example

```C++ TODO
#include "mbed.h"
#include "SDBlockDevice.h"
#include "USBMSD.h"

SDBlockDevice sd(PTE3, PTE1, PTE2, PTE4);
USBMSD usb(&sd);

int main() {

    while(true) {
        usb.process();
    }

    return 0;
}
```

## Related content

- [BlockDevice](blockdevice.html).
