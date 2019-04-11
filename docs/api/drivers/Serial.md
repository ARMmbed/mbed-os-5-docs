# Serial

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_serial.png)<span>Serial class hierarchy</span></span>

The [Serial](../introduction/glossary.html) interface provides UART functionality. The serial link has two unidirectional channels, one for sending and one for receiving. The link is asynchronous, and so both ends of the serial link must be configured to use the same settings.

One of the serial connections uses the Arm Mbed USB port, allowing you to easily communicate with your host PC.

## Serial class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_serial.html)

<span class="notes">**Note**: On a Windows machine, you will need to install a USB serial driver. See [Windows serial configuration](../tutorials/windows-serial-driver.html).</span>

Serial channels have the following configurable parameters:

  - _TX and RX Pin_ - The physical serial transmit and receive pins. You can specify a TX or RX pin as Not Connected (NC) to get Simplex communication, or specify both to get Full Duplex communication.
  - _Baud Rate_ - Standard baud rates range from a few hundred bits per second to megabits per second. The default setting for a serial connection on the microcontroller is 9600 baud.
  - _Data length_ - Transferred data can be either 7 or 8 bits long. The default setting for a serial connection on the microcontroller is 8 bits.
  - _Parity_ - You can add an optional parity bit. The Serial object automatically sets the parity bit to make the number of 1s in the data either odd or even. Parity settings are *Odd*, *Even* or *None*. The default setting for a serial connection on the microcontroller is None.
  - _Stop Bits_ - After the transmission of data and parity bits, the Serial object inserts one or two stop bits to "frame" the data. The default setting for a serial connection on the microcontroller is one stop bit.

The default settings for the microcontroller are described as _9600-8-N-1_, a common notation for serial port settings.

## Serial hello, world

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/Serial_HelloWorld/)](https://os.mbed.com/teams/mbed_example/code/Serial_HelloWorld/file/18e08b8afd16/main.cpp)

## Serial examples

### Example one

Write a message to a device at a baud rate of 19200.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/Serial_ex_1/)](https://os.mbed.com/teams/mbed_example/code/Serial_ex_1/file/40997137fc4d/main.cpp)

### Example two

Provide a serial pass-through between the PC and an external UART.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/Serial_ex_2/)](https://os.mbed.com/teams/mbed_example/code/Serial_ex_2/file/4cf190502c9e/main.cpp)

## Related content

- [Serial](../introduction/glossary.html) glossary entry.
- [Windows serial configuration](../tutorials/windows-serial-driver.html).
