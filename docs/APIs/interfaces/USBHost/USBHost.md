# USBHost

The Universal Serial Bus (USB) is the most widely used bus in today's computer. USB has particularly been designed to standardize connections between the computer and peripherals. For instance, keyboards, mice, USB audio devices, printers, scanners, disk drives or cameras can use the same bus to exchange data with a computer.

A USB host stack has been developed in order to be communicate with USB devices.

<span class="warnings">**Warning:** Library in Beta! </br>This library is in Beta. If you have any problems using the USBHost library, please send a bug report at [support@mbed.org](support@mbed.org) </span> 

[![View code](https://www.mbed.com/embed/?type=library)](https://developer.mbed.org/users/mbed_official/code/USBHost/) 

# Boards supporting USB Host

**LPC1768** 
 
<span class="images">![](../../Images/LPC1768_pic.png)</span>

<span class="images">![](../../Images/LPC1768_drawing.png)</span>

# Mbed as USB Host

## USBHostMouse

The USBHostMouse class allows to communicate with a USB mouse:

* read mouse position
* read buttons state
* read scroll state

For more information, please visit [USBHostMouse](USBHostMouse.md).

## USBHostKeyboard

The USBHostKeyboard class allows to communicate with a USB keyboard:

* read keycode pressed
* read modifier pressed

For more information, please visit [USBHostKeyboard](USBHostKeyboard.md).

## USBHostMSD

The USBHostMSD interface is used to read/write a USB flash drive.

For more information, please visit [USBHostMSD](USBHostMSD.md).

## USBHostSerial

The USBHostSerial class uses the USB interface to communicate with a virtual serial port usb device.

For more information, please visit [USBHostSerial](USBHostSerial.md).

## USBHostHub

You can connect several devices to your mbed using a USB hub. Hubs are automatically detected by the USBHost stack so no need to change your programs if you are using a hub!

For more information, please visit [USBHostHub](USBHostHub.md).

# Library in development

This library is currently in development. 

* Currently the stack supports:
    * Mouse class
    * Keyboard class
    * MSD class
    * Serial class
    * Hub auto detection
* What can be developed:
    * Support of isochronous endpoints
    * Bluetooth class
    * Webcam class
    * And so on

# Contribution

It would be great if the USBHost stack development involves several developers. There is plenty of work to be done such as:

* Core modification by adding isochronous endpoint support
* Develop drivers on top of the USBHost stack

Any contribution from the mbed community would be greatly appreciated!
