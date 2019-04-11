# USBSerial

<span class="images">![](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_u_s_b_serial.png)<span>USBSerial class hierarchy</span></span>

You can use the USBSerial interface to emulate a serial port over USB. You can use this serial port as an extra serial port or as a debug solution. It also communicates between Mbed and a computer.

## USBSerial class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_u_s_b_serial.html)

## USBSerial example

```C++ TODO
#include "mbed.h"
#include "USBSerial.h"

//Virtual serial port over USB
USBSerial serial;

int main(void) {

    while(1)
    {
        serial.printf("I am a virtual serial port\r\n");
        wait(1.0);
    }
}
```

## Related content

- [USBCDC](usbcdc.html).
