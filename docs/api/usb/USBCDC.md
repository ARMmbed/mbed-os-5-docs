# USBCDC

<span class="images">![](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_u_s_b_c_d_c.png)<span>USBCDC class hierarchy</span></span>

The USBCDC class emulates a basic serial port over USB. You can use this serial port to send or receive data. If you want printf functionality, please see the [USBSerial](../apis/usbserial.html) class.

## USBCDC class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_u_s_b_c_d_c.html)

## USBCDC example

```C++ TODO
#include "mbed.h"
#include "USBCDC.h"

USBCDC cdc;

int main(void) {

    while(1)
    {
        char msg[] = "Hello world\r\n";
        cdc.send((uint8_t*)msg, strlen(msg));
        wait(1.0);
    }
}
```

## Related content

- [USBSerial](../apis/usbserial.html).
