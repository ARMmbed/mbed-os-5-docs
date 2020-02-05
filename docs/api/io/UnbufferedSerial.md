# UnbufferedSerial

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_unbuffered_serial.png)<span>`UnbufferedSerial` class hierarchy</span></span>

The `UnbufferedSerial` class provides UART functionality with an API similar to the [`BufferedSerial`](./BufferedSerial.md) class. The classes also share the same default configurations.

Unlike the `BufferedSerial` class, the `UnbufferedSerial` class does not use intermediary buffers to store bytes to transmit to or read from the hardware. The user application is responsible for processing each byte as they are received. The method to read data returns only one byte for every call. It is therefore suitable when more control is required and for use in interrupt handlers with the RTOS. The class can however be used to write multiple bytes at once. Since it does not acquire a mutex lock, care must be taken that only one instance is using the serial port.

For normal blocking application that require a serial channel for something other than the console, `BufferedSerial` will perform better than `UnbufferedSerial` and will cause less CPU load and latency issues. `UnbufferedSerial` should only be used by applications that are short of RAM and cannot afford buffering or need more control of the serial port and use it from IRQ.

You can view more information about the configurable settings and functions in the class reference.

## Class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/classmbed_1_1_unbuffered_serial.html)

<span class="notes">**Note**: On a Windows machine, you need to install a USB serial driver. See [Windows serial configuration](../tutorials/serial-communication.html#windows-serial-driver).</span>

## Example

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/UnbufferedSerial/)](https://os.mbed.com/teams/mbed_example/code/UnbufferedSerial/file/112a40a5991a/main.cpp)


### Mbed OS usage

Common use cases for `UnbufferedSerial` are IRQ heavy UART operations, such as the [BLE cordio in the transport driver](https://github.com/ARMmbed/mbed-os/blob/master/features/FEATURE_BLE/targets/TARGET_CORDIO/driver/H4TransportDriver.cpp#L62).
