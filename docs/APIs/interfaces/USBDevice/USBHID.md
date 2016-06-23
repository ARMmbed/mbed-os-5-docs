# USBHID

The USBHID class can be used to send and receive messages over USB. For instance, you can define your own protocol and communicate between your computer and the Mbed with all capabilities of a USB communication. To use USBHID, you need a script running on the host side (computer). For instance on a 32 bits Windows 7 machine, you can use [pywinusb](http://code.google.com/p/pywinusb/).

The USB connector should be attached to 

* **p31 (D+), p32 (D-) and GND** for the **LPC1768 and the LPC11U24**
* The on-board USB connector of the **FRDM-KL25Z**

## Hello World

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/users/samux/code/USBHID_HelloWorld/)](https://developer.mbed.org/users/samux/code/USBHID_HelloWorld/file/tip/main.cpp) 

## API

[![View code](https://www.mbed.com/embed/?url=<http://mbed.org/users/mbed_official/code/USBDevice/)](http://mbed.org/users/mbed_official/code/USBDevice/file/tip/main.cpp>) 

## Details

You can choose the length of exchanged packets. In this example, mbed leds are controlled by four switches. When you press a button, there is a message sent containing buttons state. According to this message, the mbed will receive back a new message to light on leds.   
We need one byte to control leds and one byte to send buttons state.

```
#include "mbed.h"
#include "USBHID.h"

//We declare a USBHID device: it can send 1 byte and receive 1 byte
USBHID hid(1, 1);

//Two reports where will be stored values to send and received
HID_REPORT recv_report;
HID_REPORT send_report;

//Bus of leds
BusOut leds(LED1,LED2,LED3,LED4);

//Bus of buttons
BusInOut buttons(p21, p22, p23, p24);

int main(void) {
    uint8_t p_bus = 0;
    send_report.length = 1;

    while (1) {
        //If a data is received, update led bus
        if (hid.readNB(&recv;_report)) {
            leds = recv_report.data[0];
        }

        //if the bus of buttons has changed, send a report
        if (buttons.read() != p_bus) {
            p_bus = buttons.read();
            send_report.data[0] = p_bus;
            hid.send(&send;_report);
        }
        wait(0.01);
    }
}
```

## Contribute to the USBHID bindings webpage!

A great thing would be to develop in several languages running on different platforms, programs able to communicate with the mbed over USB. Visit the [USBHID bindings webpage](http://mbed.org/cookbook/USBHID-bindings-) and develop your own USBHID device!
