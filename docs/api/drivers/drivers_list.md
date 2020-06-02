# Drivers APIs

## Serial (UART) drivers

- [BufferedSerial](../apis/serial-uart-apis.html): A class for serial data transfers so a device can interface with another device (such as sensors, printers or another board) to exchange data or to send text to be displayed on a text-based computer interface.
- [UnbufferedSerial](../apis/unbufferedserial.html): Similar to BufferedSerial, but intended for applications that are short of RAM and cannot afford buffering or that need more control of the serial port and use it from IRQ.

## SPI drivers


- [QuadSPI (QSPI)](../apis/spi-apis.html): Provides functionality to configure and access QSPI devices connected over a QuadSPI interface.
- [SPI](../apis/spi.html): Communicate with SPI slave devices, such as FLASH memory, LCD screens and other modules or integrated circuits.
- [SPISlave](../apis/spislave.html): Communicate with a SPI master device.

## Input/Output drivers


- [AnalogIn](../apis/i-o-apis.html): Read an external voltage applied to an analog input pin.
- [AnalogOut](../apis/analogout.html): Set the output voltage of an analog output pin, specified as a percentage or as an unsigned short.
- [BusIn](../apis/busin.html): Combine a number of DigitalIn pins to read them as a single interface instead of individually.
- [BusOut](../apis/busout.html): Combine a number of DigitalOut pins to write them as a single interface instead of individually.
- [BusInOut](../apis/businout.html): A bidirectional bus that supports up to 16 DigitalInOut pins that you can read and write as one value.
- [DigitalIn](../apis/digitalin.html): Read the value of a digital input pin.
- [DigitalOut](../apis/digitalout.html): Configure and control a digital output pin.
- [DigitalInOut](../apis/digitalinout.html): A bidirectional digital pin.
- [InterruptIn](../apis/interruptin.html): Trigger an event when a digital input pin changes.
- [PortIn](../apis/portin.html): Define which pins of a hardware GPIO port are set as an input and to read the value of those pins.
- [PortOut](../apis/portout.html): Define which pins of a hardware GPIO port are set as an output and to write those pins.
- [PortInOut](../apis/portinout.html): Read and write an underlying GPIO port as one value.
- [PwmOut](../apis/pwmout.html): Control the frequency and duty cycle of a PWM signal.

## USB drivers

- [USBAudio](../apis/usb-apis.html): Send and receive audio data over USB.
- [USBCDC](../apis/usbcdc.html): Emulates a basic serial port over USB so you can send or receive data.
- [USBCDC_ECM](../apis/usbcdc-ecm.html): Emulates an Ethernet interface over USB so you can send and receive Ethernet frames.
- [USBHID](../apis/usbhid.html): Turn an Mbed board into a Human Interface Device (HID) that can send and receive messages over USB.
- [USBKeyboard](../apis/usbkeyboard.html): Send key presses, check the status of control keys and send a key press sequences though a stream interface.
- [USBMIDI](../apis/usbmidi.html): Send and receive MIDI messages over USB using the standard USB-MIDI protocol.
- [USBMouse](../apis/usbmouse.html): Emulate a mouse over the USB port. You can choose relative or absolute coordinates and send clicks, button state and scroll wheel movements.
- [USBMouseKeyboard](../apis/usbmousekeyboard.html): Emulate a mouse and a keyboard at the same time so you can send both key presses and mouse movements.
- [USBMSD](../apis/usbmsd.html): Emulate a mass storage device to store or load data to and from a storage chip, such as SDcard or Flash.
- [USBSerial](../apis/usbserial.html): Emulate a serial port over USB. You can use this serial port as an extra serial port or as a debug solution.

## Other drivers

- [CAN](../apis/other-driver-apis.html): Controller-Area Network (CAN) is a bus standard that allows microcontrollers and devices to communicate with each other without going through a host computer.
- [Flash IAP](../apis/flash-iap.html): Flash In-Application Programming (IAP) interfaces with the MCU's internal flash memory.
- [I2C](../apis/i2c.html): Communicate with I2C devices such as serial memories, sensors and other modules or integrated circuits. This class is for the I2C Master.
- [I2CSlave](../apis/i2cslave.html): Communicate with I2C Master devices.
- [MbedCRC](../apis/mbedcrc.html): Provides support for Cyclic Redundancy Check (CRC) algorithms.
- [ResetReason](../apis/resetreason.html): Fetch the reason the system restarted.
- [Watchdog](../apis/watchdog.html): Set up a hardware timer that resets the system if it is not refreshed periodically.
