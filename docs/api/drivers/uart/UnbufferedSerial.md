# UnbufferedSerial

<span class="images">![](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/classmbed_1_1_unbuffered_serial.png)<span>`UnbufferedSerial` class hierarchy</span></span>

The UnbufferedSerial class provides UART functionality with an API similar to the [BufferedSerial](../apis/serial-uart-apis.html) class. The classes also share the same default configurations.

Unlike the BufferedSerial class, the UnbufferedSerial class does not use intermediary buffers to store bytes to transmit to or read from the hardware. The user application is responsible for processing each byte as it is received. The method to read data returns only one byte for every call. Therefore, we recommend you use this class when you need more control and for use in interrupt handlers with the RTOS. You can also use this class to write multiple bytes at once. Because it does not acquire a mutex lock, you must ensure only one instance uses the serial port.

For normal blocking applications that require a serial channel for something other than the console, BufferedSerial performs better than `UnbufferedSerial` and causes less CPU load and fewer latency issues. Only applications that are short of RAM and cannot afford buffering or that need more control of the serial port and use it from IRQ should use UnbufferedSerial.

You can view more information about the configurable settings and functions in the class reference.

## Class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/classmbed_1_1_unbuffered_serial.html)

## UnbufferedSerial Example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-UnbufferedSerial/tree/v6.11)](https://github.com/ARMmbed/mbed-os-snippet-UnbufferedSerial/blob/v6.11/main.cpp)

## Mbed OS use

Common use cases for `UnbufferedSerial` are IRQ heavy UART operations, such as [BLE Cordio in the transport driver](https://github.com/ARMmbed/mbed-os/blob/master/features/FEATURE_BLE/targets/TARGET_CORDIO/driver/H4TransportDriver.cpp#L62).
