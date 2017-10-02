## RawSerial

The RawSerial interface provides UART functionality without the use of streams like the Serial class. This makes it suitable for use in interrupt handlers with the RTOS.

### RawSerial class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/classmbed_1_1_raw_serial.html)

<span class="notes">**Note**: On a Windows machine, you will need to install a USB serial driver. See [Windows serial configuration](/docs/v5.6/tutorials/serial-communication.html#windows-serial-driver).</span>

Serial channels have a number of configurable parameters:

  - _Baud Rate_ - There are a number of standard baud rates ranging from a few hundred bits per second, to megabits per second. The default setting for a serial connection on the Mbed microcontroller is 9600 baud.
  - _Data length_ - Data transferred can be either 7 or 8 bits long. The default setting for a serial connection on the Mbed microcontroller is 8 bits.
  - _Parity_ - You can add an optional parity bit. The parity bit will be automatically set to make the number of 1s in the data either odd or even. Parity settings are *Odd*, *Even* or *None*. The default setting for a serial connection on the Arm Mbed microcontroller is None.
  - _Stop Bits_ - After data and parity bits have been transmitted, one or two stop bits are inserted to "frame" the data. The default setting for a serial connection on the Mbed microcontroller is one stop bit.

The default settings for the Mbed microcontroller are described as _9600-8-N-1_, a  common notation for serial port settings.

### RawSerial hello, world

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/RawSerial_HelloWorld/)](https://os.mbed.com/teams/mbed_example/code/RawSerial_HelloWorld/file/112a40a5991a/main.cpp)

### RawSerial examples

#### Example one

Write a message to a device at a baud rate of 19200.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/RawSerial_ex_1/)](https://os.mbed.com/teams/mbed_example/code/RawSerial_ex_1/file/6a0d9cb21969/main.cpp)

#### Mbed OS Example

RawSerial is commonly used in IRQ heavy UART operations such as the [ATParser](https://github.com/ARMmbed/ATParser/blob/3209400df676cbf0183a5894f648c71727602d30/BufferedSerial/BufferedSerial.cpp#L29) used in the ESP8266 driver. This driver uses UART on user supplied pins to communicate with the offchip ESP8266 module.
