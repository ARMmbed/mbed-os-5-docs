## USB Device

The Universal Serial Bus (USB) is the most widely used bus in today's computer. USB has particularly been designed to standardize connections between the computer and peripherals. For instance, keyboards, mice, USB audio devices, printers, scanners, disk drives or cameras can use the same bus to exchange data with a computer.

A USB device stack has been developed in order to provide all the great capabilities of USB to mbed.   

# Boards supporting USB Device

LPC1768 | LPC11U24 | FRDM-KL25Z   
---|---|---  
![](../../Images/lpc1768_usb.png) | ![](../../Images/LPC11U24_usb.png) | ![](../../Images/FRDM_KL25Z.png)  |

<span class="images">![](../../Images/mbed_usb_drawing.png)</span>

# mbed as a USB device

<span class="images">![](../../Images/capa2.png)</span>

## Mouse

The USBMouse class allows to emulate a mouse with your mbed. You can either chose a relative or absolute mouse. This class allows you to:

* Move the cursor on the screen
* Click 
* Scroll

For more information, please visit [USBMouse](USBMouse.md).

## Keyboard

The USBKeyboard class allows to use mbed as a keyboard. You can:

* Send basic keys
* Send "modified keys" such as: CTRL + 'c'
* Send media keys (Mute, Volume Up, Volume Down, next track, ...)

For more information, please visit [USBKeyboard](USBKeyboard.md).

## Mouse and Keyboard

If you want to have all capabilities from a mouse and a keyboard at the same time, you can use the USBMouseKeyboard class. 

For more information, please visit [USBMouseKeyboard](USBMouseKeyboard.md).

## Human Interface Device (HID)

The USBHID class is a great opportunity to send and receive raw data to a custom program. This allows you to design your own USB device without any specific drivers on the host side as all operating systems have a built-in HID driver.

For more information, please visit [USBHID](USBHID.md).

## USBSerial

The USBSerial class uses the USB interface to emulate a serial port. The mbed is recognized by the computer as a serial port. This is a great solution to communicate easily between the microcontroller and a computer.

For more information, please visit [USBSerial](USBSerial.md).

## USBMIDI

Using this library, you can do things like send MIDI messages to a computer (such as to record in a sequencer, or trigger a software synthesiser) and receive messages from a computer (such as actuate things based on MIDI events).

For more information, please visit [USBMIDI](USBMIDI.md).

## USBAudio

The USBAudio class enables the mbed to be recognized as an audio device. With this interface, you can receive audio packet from the computer (play music) and receive them over USB. For instance you connect a speaker or an I2S/I2C chip to the mbed and play the stream received from the computer.

## USBMSD

The USBMSD interface is used to emulate a mass storage device over USB. You can use this class to store or load data to and from a storage chip (SDcard, flash,...). This class implements the MSD protocol and calls pure virtual functions such as **disk_initialize**, **disk_write** or **disk_read** to interact with a storage chip. 

For more information, please visit [USBMSD](USBMSD.md).

## USB HID Bindings

[USBHID bindings](http://mbed.org/cookbook/USBHID-bindings-) - Design your own USB device on top of USBHID class by developing programs in different languages and running on different platforms.

# More information

If you want information concerning the stack architecture, visit the [USBDevice stack architecture](http://mbed.org/users/samux/notebook/usbdevice-stack-architecture/).
