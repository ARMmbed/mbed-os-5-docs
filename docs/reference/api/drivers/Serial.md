## Serial

The [Serial](/docs/v5.6/introduction/glossary.html) interface provides UART functionality. The serial link has two unidirection channels, one for sending and one for receiving. The link is asynchronous, and so both ends of the serial link must be configured to use the same settings.

One of the serial connections uses the Arm Mbed USB port, allowing you to easily communicate with your host PC.

### Serial class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/classmbed_1_1_serial.html)

<span class="notes">**Note**: On a Windows machine, you will need to install a USB serial driver. See [Windows serial configuration](/docs/v5.6/tutorials/serial-communication.html#windows-serial-driver).</span>

Serial channels have a number of configurable parameters:

  - _Baud Rate_ - There are a number of standard baud rates ranging from a few hundred bits per second, to megabits per second. The default setting for a serial connection on the Mbed microcontroller is 9600 baud.
  - _Data length_ - Data transferred can be either 7 or 8 bits long. The default setting for a serial connection on the Mbed microcontroller is 8 bits.
  - _Parity_ - You can add an optional parity bit. The parity bit will be automatically set to make the number of 1s in the data either odd or even. Parity settings are *Odd*, *Even* or *None*. The default setting for a serial connection on the Arm Mbed microcontroller is None.
  - _Stop Bits_ - After data and parity bits have been transmitted, one or two stop bits are inserted to "frame" the data. The default setting for a serial connection on the Mbed microcontroller is one stop bit.

The default settings for the Mbed microcontroller are described as _9600-8-N-1_, a  common notation for serial port settings.

### Serial Hello World!

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/Serial_HelloWorld/)](https://os.mbed.com/teams/mbed_example/code/Serial_HelloWorld/file/e540d7769e69/main.cpp)

### Serial examples

#### Example one

Write a message to a device at a baud rate of 19200.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/Serial_ex_1/)](https://os.mbed.com/teams/mbed_example/code/Serial_ex_1/file/7376f17bb36e/main.cpp)

#### Example two

Provide a serial pass-through between the PC and an external UART.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/Serial_ex_2/)](https://os.mbed.com/teams/mbed_example/code/Serial_ex_2/file/8d318218bac1/main.cpp)

#### Example three

Attach a function to call during the generation of serial interrupts. This function defaults to interrupt on an RX pin.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/Serial_ex_3/)](https://os.mbed.com/teams/mbed_example/code/Serial_ex_3/file/3b040f367dd8/main.cpp)
