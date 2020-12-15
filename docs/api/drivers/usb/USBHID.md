# USBHID

<span class="images">![](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_u_s_b_h_i_d.png)<span>USBHID class hierarchy</span></span>

You can use the USBHID class to turn an Mbed board into an HID (Human Interface Device) that can send and receive messages over USB. For example, you can define your own protocol and communicate between your computer and Mbed with all capabilities of USB communication. To use USBHID, you need a script running on the host side (computer). For example, on a Windows machine, you can use [pywinusb](https://github.com/rene-aguirre/pywinusb). For convenience, there is a Python script attached below that uses pywinusb that can be run on the host computer to send and receive data from the Mbed board.

## USBHID class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_u_s_b_h_i_d.html)

## USBHID example   

### main.cpp   

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-USBHID/tree/v6.6)](https://github.com/ARMmbed/mbed-os-snippet-USBHID/blob/v6.6/main.cpp)

### USBHID.py   

To use this script, first flash the Mbed board with the code above. Connect the target's USB to the host computer. Then run this script. The script will send 8 bytes of data (1 2 3 4 5 6 7 8) to the Mbed board and will read and print the data sent to the host computer by the Mbed board.   

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-USBHID/tree/v6.6)](https://github.com/ARMmbed/mbed-os-snippet-USBHID/blob/v6.6/USBHID.py)

## Related content

- [USBMouse](../apis/usbmouse.html).
- [USBKeyboard](../apis/usbkeyboard.html).
- [USBMouseKeyboard](../apis/usbmousekeyboard.html).
