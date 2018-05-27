## USBHID

The USBHID class can be used to send and receive messages over USB. For instance, you can define your own protocol and communicate between your computer and the Mbed with all capabilities of a USB communication. To use USBHID, you need a script running on the host side (computer). For instance on a 32 bits Windows 7 machine, you can use [pywinusb](https://github.com/rene-aguirre/pywinusb).

### USBHID class reference

TODO

### USBHID example

```C++
#include "mbed.h"
#include "USBHID.h"

//We declare a USBHID device. By default input and output reports are 64 bytes long.
USBHID hid(true, 8, 8);

Serial pc(USBTX, USBRX);

//This report will contain data to be sent
HID_REPORT send_report;
HID_REPORT recv_report;

DigitalOut l1(LED1);

int main(void) {
    send_report.length = 8;

    while (1) {

        //Fill the report
        for (int i = 0; i < send_report.length; i++)
            send_report.data[i] = rand() & 0xff;

        //Send the report
        hid.send(&send_report);

        //try to read a msg
        if(hid.read_nb(&recv_report)) {
            l1 = !l1;
            for(int i = 1; i < recv_report.length; i++) {
                pc.printf("%d ", recv_report.data[i]);
            }
            pc.printf("\r\n");
        }
    }
}
```

### Related content

- [USBMouse](USBMouse.md)
- [USBKeyboard](USBKeyboard.md)
- [USBMouseKeyboard](USBMouseKeyboard.md)
