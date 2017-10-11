## RawSerial

The RawSerial class provides UART functionality without the use of [Stream's](https://github.com/ARMmbed/Handbook/blob/new_engine/docs/reference/api/platform/Stream.md)  print and scan functions as is done in the Serial class. RawSerial does not retarget the standard library print and scan functions, but re-implements them to work using each target's underlying serial communication functions. See the porting guide for [target serial support](https://os.mbed.com/docs/v5.6/reference/contributing-target.html#serial). This makes it suitable for use in interrupt handlers with the RTOS.

Serial channels have the following configurable parameters:

  - _Baud Rate_ - Standard baud rates range from a few hundred bits per second to megabits per second. The default setting for a serial connection on the Mbed microcontroller is 9600 baud.
  - _Data length_ - Transferred data can be either 7 or 8 bits long. The default setting for a serial connection on the Mbed microcontroller is 8 bits.
  - _Parity_ - You can add an optional parity bit. The object automatically sets the parity bit to make the number of 1s in the data either odd or even. Parity settings are *Odd*, *Even* or *None*. The default setting for a serial connection on the Arm Mbed microcontroller is None.
  - _Stop Bits_ - After the transmission of data and parity bits, the RawSerial object inserts one or two stop bits to "frame" the data. The default setting for a serial connection on the Mbed microcontroller is one stop bit.

_9600-8-N-1_, a  common notation for serial port settings, describes the default settings for the Mbed microcontroller.

### RawSerial class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/classmbed_1_1_raw_serial.html)

<span class="notes">**Note**: On a Windows machine, you need to install a USB serial driver. See [Windows serial configuration](/docs/v5.6/tutorials/serial-communication.html#windows-serial-driver).</span>

### RawSerial hello, world

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/RawSerial_HelloWorld/)](https://os.mbed.com/teams/mbed_example/code/RawSerial_HelloWorld/file/112a40a5991a/main.cpp)

### RawSerial examples

#### Example one

Write a message to a device at a baud rate of 19200.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/RawSerial_ex_1/)](https://os.mbed.com/teams/mbed_example/code/RawSerial_ex_1/file/6a0d9cb21969/main.cpp)

#### Mbed OS example

Common use cases for RawSerial are IRQ heavy UART operations, such as the [ATParser](https://github.com/ARMmbed/ATParser/blob/3209400df676cbf0183a5894f648c71727602d30/BufferedSerial/BufferedSerial.cpp#L29) in the ESP8266 driver. This driver uses UART on user supplied pins to communicate with the offchip ESP8266 module.
