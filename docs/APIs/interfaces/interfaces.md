# Interface options

These APIs allow your board to interface with a computer or external devices.

## Digital interfaces

* [Serial](digital/Serial.md): generic asynchronous protocol. 
* SPI: serial peripheral interface:
	* [SPI](digital/SPI.md): master.
	* [SPISlave](digital/SPISlave.md): slave.
* I2C: inter-integrated circuit:
	* [I2C](digital/I2C.md): master.
	* [I2CSlave](digital/I2CSlave.md): slave.
* [CAN](digital/CAN.md): connect two devices without using a computer.

## USB

mbed boards can be either a USB device or a USB host.

### USB device

Use your mbed board as a a source of input to your PC's USB port:

* [General introduction](USBDevice/USBDevice.md).
* [USBMouse](USBDevice/USBMouse.md): emulate a USB mouse with absolute or relative positioning.
* [USBKeyboard](USBDevice/USBKeyboard.md): emulate a USB keyboard, sending normal and media control keys.
* [USBMouseKeyboard](USBDevice/USBMouseKeyboard.md): emulate a USB keyboard and a USB mouse with absolute or relative positioning.
* [USBHID](USBDevice/USBHID.md): communicate over a raw USBHID interface; great for driverless communication with a custom PC program.
* [USBMIDI](USBDevice/USBMIDI.md): send and receive MIDI messages to control and be controlled by PC music sequencers.
* [USBSerial](USBDevice/USBSerial.md): create a virtual serial port over the USB port; great for easy communication with a computer.
* [USBAudio](USBDevice/USBAudio.md): receive audio stream from a computer over USB.
* [USBMSD](USBDevice/USBMSD.md): Generic class implementing the Mass Storage Device protocol; access block storage chips.

### USB host

Use USB devices as sources of input to your mbed board:

* [General introduction](USBHost/USBHost.md).
* [USBHostMouse](USBHost/USBHostMouse.md): receive events from a USB mouse.
* [USBHostKeyboard](USBHost/USBHostKeyboard.md): read key code modifier from a USB keyboard.
* [USBHostMSD](USBHost/USBHostMSD.md): read and write to a USB flash disk.
* [USBHostSerial](USBHost/USBHostSerial.md): communicate with a virtual serial port.
* [USBHostHub](USBHost/USBHostHub.md): plug several USB devices to an mbed board using a USB hub.
