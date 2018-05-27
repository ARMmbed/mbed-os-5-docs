## USBSerial

The USBSerial interface is used to emulate a serial port over USB. You can use this serial port as an extra serial port or as a debug solution. It's also a great solution to easily communicate between your mbed and a computer.

### USBSerial class reference


[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.8/feature-hal-spec-usb-device-doxy/class_u_s_b_serial.html)

### USBSerial example

```C++
#include "mbed.h"
#include "USBSerial.h"

//Virtual serial port over USB
USBSerial serial;

int main(void) {

    while(1)
    {
        serial.printf("I am a virtual serial port\r\n");
        wait(1);
    }
}
```

### Related content

- [USBCDC](usbcdc.md)
