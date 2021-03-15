# BufferedSerial

<span class="images">![](https://os.mbed.com/docs/mbed-os/v6.9/mbed-os-api-doxy/classmbed_1_1_buffered_serial.png)<span>`BufferedSerial` class hierarchy</span></span>

The `BufferedSerial` class provides UART functionality. We recommend you use this class for serial data transfers. You can use it to send and receive bytes of data in a sequence using separate transmit (TX) and receive pins (RX). A device can interface with another device (such as sensors, printers or another board) to exchange data or to send text to be displayed on a text-based computer interface.

Serial channels have the following characteristics:

- TX and RX pins - you can specify either pin as Not Connected (NC) for simplex (unidirectional) communication or both as valid pins for full duplex (bidirectional) communication.
- Baud rate - predefined speed at which data is sent and received on the UART interface. Standard baud rates include 9600, 19200 and 115200.

Data is transmitted using packets of configurable sizes divided in different sections, which include:

- Start bit: indicates the start of UART data transmission.
- Data frame: can be 5 to 8 (or 9 if a parity bit is not used) bits for the actual data being transferred.
- Parity bit: optional bit, used for data error detection.
- Stop bits: 1-2 bits to signal the end of a data packet.

The `BufferedSerial` calls the underlying HAL API functions. Please see the [porting guide](../porting/serial-port.html) for target serial support.

When the receive interrupt is triggered when receiving data from a device, the `BufferedSerial` class stores the byte(s) available to read from the hardware buffer to an internal intermediary buffer. When a read request is made, the `BufferedSerial` class uses a mutex lock and enters a critical section to read out the number of bytes requested if as many are available in the intermediary buffer.

To transmit multiple bytes, the class uses an intermediary buffer to store the bytes to send and monitors the serial interface to transfer them to the hardware buffer as soon as it is available. However, all bytes are written unbuffered if in a critical section.
Using intermediary buffers allows the UART interface to be used reliably for input from noninterrupt context while avoiding excess spinning waiting for transmission buffer space.

The RX and TX buffers are circular buffers with preallocated sizes configurable using the configuration parameters `uart-serial-rxbuf-size` and `uart-serial-txbuf-size`. You can find both configuration parameters in `drivers/mbed_lib.json`.

## Configuration

The following parameters can be configured at object instantiation:

  - _TX_.
  - _RX_.
  - _Baud rate_.

The default baud rate value is configured in `mbed-os/platform/mbed_lib.json`.

The following parameters can be configured after an `BufferedSerial` object instantiation.

  - _Baud rate_.
  - _Data frame length_.
  - _Parity bit_.
  - _Stop bits_.

The default settings for a microcontroller are set as _9600-8-N-1_, a common notation for serial port settings. This denotes a baud rate of 9,600 (9600), eight data frame length (8), no parity bit (N) and one stop bit (1).

You can also configure hardware flow control if necessary.

You can view more information about the configurable settings and functions in the class reference.

## BufferedSerial class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.9/mbed-os-api-doxy/classmbed_1_1_buffered_serial.html)

## BufferedSerial examples

This example toggles an LED and echoes input to a terminal:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-BufferedSerial_echo/tree/v6.9)](https://github.com/ARMmbed/mbed-os-snippet-BufferedSerial_echo/blob/v6.9/main.cpp)

### Printing to the console

Mbed OS redefines target-dependent I/O functions in the C library to allow you to use the C standard I/O library functions (`s\v\f\n\printf`, `scanf` and so on) in your application for printing to the console.

You can configure the system I/O retarget code to be buffered or unbuffered, depending on the configuration of the parameter `stdio-buffered-serial` in `platform/mbed_lib.json`. When it is buffered, the retarget code uses an instance of a `BufferedSerial` class to perform the actual printing. This is where `BufferedSerial`'s `Filehandle` inheritance is used.

Alternatively, if you need more configuration of the serial interface, you can pass an instance of the `BufferedSerial` class to the system I/O retarget code at run time for printing to the console:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-BufferedSerial_printf/tree/v6.9)](https://github.com/ARMmbed/mbed-os-snippet-BufferedSerial_printf/blob/v6.9/main.cpp)

We recommend you use the standard C I/O library directly to print to the console in Mbed OS.
