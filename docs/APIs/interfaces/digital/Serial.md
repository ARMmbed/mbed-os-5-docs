# Serial

Serial is a generic protocol used by computers and electronic modules to send and receive control information and data. The Serial link has two unidirection channels, one for sending and one for receiving. The link is asynchronous, and so both ends of the serial link must be configured to use the same settings.

One of the Serial connections goes via the mbed USB port, allowing you to easily communicate with your host PC.

## Hello World!

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/users/mbed_official/code/Serial_HelloWorld_Mbed/)](https://developer.mbed.org/users/mbed_official/code/Serial_HelloWorld_Mbed/file/879aa9d0247b/main.cpp) 

## API

API summary

[![View code](https://www.mbed.com/embed/?type=library)](https://developer.mbed.org/users/mbed_official/code/mbed/docs/tip/classmbed_1_1Serial.html) 

## Interface

The Serial Interface can be used on supported pins and USBTX/USBRX

<span class="images">![](../Images/pin_out.png)</span>
  
Note that USBTX/USBRX are not DIP pins; they represent the pins that route to the interface USB Serial port so you can communicate with a host PC.

<span class="tips">**Tip:** If you want to send data to a host PC, take a look at [SerialPC](Serial.md) </span>

<span class="notes">**Note**: on a windows machine, you will need to install a USB Serial driver. See [Windows serial configuration](Windows serial configuration) **MISSING LINK** </span>

Serial channels have a number of configurable parameters:

  * _Baud Rate_ - There are a number of standard baud rates ranging from a few hundred bits per seconds, to megabits per second. The default setting for a Serial connection on the mbed Microcontroller is 9600 baud.
  * _Data length_ - Data transferred can be either 7 or 8 bits long. The default setting for a Serial connection on the mbed Microcontroller is 8 bits.
  * _Parity_ - An optional parity bit can be added. The parity bit will be automatically set to make the number of 1's in the data either odd or even. Parity settings are Odd, Even or None. The default setting for a Serial connection on the mbed microcontroller is for the parity to be set to None.
  * _Stop Bits_ - After data and parity bits have been transmitted, 1 or 2 stop bit is inserted to "frame" the data. The default setting for a Serial connection on the mbed microcontroller is for one stop bit to be added.

The default settings for the mbed microcontroller are described as _9600 8N1_, and this is common notation for Serial port settings.

## See Also

  * [Communication with a PC](Serial.md)

## Reference

  * [Serial Port on Wikipedia](http://en.wikipedia.org/wiki/Serial_port)

## Examples

### Example one

```
#include "mbed.h"

Serial device(p9, p10);  // tx, rx

int main() {
    device.baud(19200);
    device.printf("Hello World\n");
}
```
### Example two

```
#include "mbed.h"

Serial pc(USBTX, USBRX); // tx, rx
Serial device(p9, p10);  // tx, rx

int main() {
    while(1) {
        if(pc.readable()) {
            device.putc(pc.getc());
        }
        if(device.readable()) {
            pc.putc(device.getc());
        }
    }
}
```

### Example three

```
#include "mbed.h"

DigitalOut led1(LED1);
DigitalOut led2(LED2);

Serial pc(USBTX, USBRX);

void callback() {
    // Note: you need to actually read from the serial to clear the RX interrupt
    printf("%c\n", pc.getc());
    led2 = !led2;
}

int main() {
    pc.attach(&callback;);
    
    while (1) {
        led1 = !led1;
        wait(0.5);
    }
}
```

See [the full attach API](http://mbed.org/projects/libraries/api/mbed/trunk/Serial#Serial.attach)
