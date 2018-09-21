## USBHID

<span class="images">![](https://os.mbed.com/docs/v5.10/feature-hal-spec-usb-device-doxy/class_u_s_b_h_i_d.png)<span>USBHID class hierarchy</span></span>

You can use the USBHID class to send and receive messages over USB. For example, you can define your own protocol and communicate between your computer and Mbed with all capabilities of USB communication. To use USBHID, you need a script running on the host side (computer). For example, on a 32-bit Windows 7 machine, you can use [pywinusb](https://github.com/rene-aguirre/pywinusb).

### USBHID class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.10/feature-hal-spec-usb-device-doxy/class_u_s_b_h_i_d.html)

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

- [USBMouse](USBMouse.html).
- [USBKeyboard](USBKeyboard.html).
- [USBMouseKeyboard](USBMouseKeyboard.html).
