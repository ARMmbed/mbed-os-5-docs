# USBSerial

The USBSerial interface is used to emulate a serial port over USB. You can use this serial port as an extra serial port or as a debug solution. It's also a great solution to easily communicate between your mbed and a computer.

The USB connector should be attached to 

* **p31 (D+), p32 (D-) and GND** for the **LPC1768 and the LPC11U24**
* The on-board USB connector of the **FRDM-KL25Z**

<span class="notes">**Note:** On Windows, you need a configuration file. You can download this [archive](https://developer.mbed.org/media/uploads/samux/serial.zip) containing a .inf file. Extract it.   
When you plug your USBSerial serial device, Windows will try to find an existing driver for it without success. After this step, go into the device manager to find the unknown device:</br>
- Right click on the device
- Update driver software
- Click on "Browse my computer for driver software"
- Indicate the path of serial.inf extracted previously and click next.
- Accept the warning and you should have a virtual port (called Mbed Virtual Serial Port in device manager) over USB!</br>
As _product_id_ and _vendor_id_ are hardcoded in the .inf file, if you don't want to use default values, you will have to change them in your program _AND_ in the .inf file.
</span>

## Hello World

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/users/samux/code/USBSerial_HelloWorld/)](https://developer.mbed.org/users/samux/code/USBSerial_HelloWorld/file/tip/main.cpp) 

## API

[![View code](https://www.mbed.com/embed/?url=<http://mbed.org/users/mbed_official/code/USBDevice/)](http://mbed.org/users/mbed_official/code/USBDevice/file/6d85e04fb59f/main.cpp) 

## More example

In this example, the program waits a line on the virtual serial port. When it receives a line, it sends it to the usual mbed serial port (the one used to flash a new program) and to the virtual one.

```
#include "mbed.h"
#include "USBSerial.h"

//Virtual serial port over USB
USBSerial serial;
Serial pc(USBTX, USBRX);

int main(void) {
    uint8_t buf[128];
    while(1)
    {
        serial.scanf("%s", buf);
        serial.printf("recv: %s", buf);
        pc.printf("recv: %s\r\n", buf);
    }
}
```
