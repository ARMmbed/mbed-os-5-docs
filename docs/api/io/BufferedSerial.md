# BufferedSerial

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_buffered_serial.png)<span>`BufferedSerial` class hierarchy</span></span>

The `BufferedSerial` class provides UART functionality, it is the recommended class for serial data transfers. It allows sending and receiving bytes of data in a sequence using separate transmit (TX) and receive pins (RX). Communication can be between two processors or for sending text to a console.

Serial channels have the following characteristics:

* TX and RX pins - can be specified as Not Connected (NC) for simplex (unidirectional) communication or as valid pins for full duplex (bi-directional) communication.

* Baud rate - pre-defined speed at which data is sent and received. Standard baud rates include 9600, 119200, 115200 or others.

Data is transmitted using packets of configurable sizes divided in different sections which include:

* Start bit: Indicates the start of UART data transmission.
* Data frame: Can be 5 to 8 (or 9 if a parity bit is not used) bits long for the actual data being transferred.
* Parity bit: Optional bit, used for data error detection.
* Stop bits: Can be 1 to 2 bits long to signal the end of a data packet.

The `BufferedSerial` calls the underlying HAL API functions. See the [porting guide](../porting/serial-port.html) for target serial support.

When the RX interrupt is trigged, the `BufferedSerial` class stores the byte(s) available to read from the hardware buffer to an internal intermediary buffer. When a read request is made, the `BufferedSerial` class uses a mutex lock and enters a critical section to read out the number of bytes requested if as many are available in the intermediary buffer.

To transmit multiple bytes, the class uses an intermediary buffer to store the bytes to send and monitors the serial interface to transfer them to the hardware buffer as soon as it is available. However, all bytes are written unbuffered if in a critical section.
Using intermediary buffers allows it to be used reliably for input from non-interrupt context whilst avoiding excess spinning waiting for transmission buffer space.

The RX and TX buffers are circular buffers with pre-allocated sizes configurable using the configuration parameters `uart-serial-rxbuf-size` and `uart-serial-txbuf-size` respectively. Both configuration parameters can be found in `drivers/mbed_lib.json`.

## Configuration

The following parameters can be configured at object instantiation:

  - _TX_
  - _RX_
  - _Baud rate_

The default baud rate value is configured in `mbed-os/platform/mbed_lib.json`.

The following parameters can be configured after an `BufferedSerial` object instantiation.

  - _Baud rate_
  - _Data frame length_
  - _Parity bit_
  - _Stop bits_

The default settings for a microcontroller are set as _9600-8-N-1_, a common notation for serial port settings. This denotes a baud rate of nine thousand six hundred (9600), eight data frame length (8), no parity bit (N) and one stop bit (1).

Additionally, hardware flow control can also be configured if necessary.

You can view more information about the configurable settings and functions in the class reference.

## Class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/classmbed_1_1_buffered_serial.html)

<span class="notes">**Note**: On a Windows machine, you need to install a USB serial driver. See [Windows serial configuration](../tutorials/serial-communication.html#windows-serial-driver).</span>

## Example

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/BufferedSerial/)](https://os.mbed.com/teams/mbed_example/code/BufferedSerial/file/112a40a5991a/main.cpp)


## Printing to the console

Mbed OS redefines target-dependent I/O functions in the C library to allow the C standard I/O library functions (`s\v\f\n\printf`, `scanf`, etc) to be used in user application for printing to the console.

The system I/O retarget code can be configured to be buffered or unbuffered depending on the configuration of the parameter `stdio-buffered-serial` in `platform/mbed_lib.json`. When it is buffered, an instance of a `BufferedSerial` class is used by the retarget code to perform the actual printing. This is where `BufferedSerial`'s `Filehandle` inheritance is used.


Alternatively, if more configuration of the serial interface is needed, an instance of the `BufferedSerial` class can be passed to the system I/O retarget code at run time to be used for printing to the console as shown below:

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/BufferedSerial/)](https://os.mbed.com/teams/mbed_example/code/BufferedSerial_printf/file/112a40a5991a/main.cpp)


Using the standard C I/O library directly is the recommended way to print to the console in Mbed OS.
