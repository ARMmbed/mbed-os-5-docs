# PlatformMutex

<span class="images">![](https://os.mbed.com/docs/mbed-os/v6.7/mbed-os-api-doxy/class_platform_mutex.png)<span>PlatformMutex class hierarchy</span></span>

You can use the PlatformMutex class to synchronize the execution of threads.

The Mbed OS drivers use the PlatformMutex class instead of [Mutex](../apis/mutex.html). This enables the use of drivers when the Mbed OS is compiled without the RTOS. For examples, please see [AnalogIn](../apis/analogin.html), [BusOut](../apis/busout.html), [SPI](../apis/spi.html) and [I2C](../apis/i2c.html).

<span class="notes">**Note:** For the standard use of RTOS mutexes, please see [Mutex](../apis/mutex.html).</span>

## PlatformMutex class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.7/mbed-os-api-doxy/class_platform_mutex.html)

## PlatformMutex example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-PlatformMutex_ex_1/tree/v6.7)](https://github.com/ARMmbed/mbed-os-snippet-PlatformMutex_ex_1/blob/v6.7/main.cpp)

## Related content

- [Mutex](../apis/mutex.html).
- [AnalogIn](../apis/analogin.html).
- [BusOut](../apis/busout.html).
- [BufferedSerial](../apis/serial-uart-apis.html).
- [UnbufferedSerial](../apis/unbufferedserial.html).
- [SPI](../apis/spi.html).
- [I2C](../apis/i2c.html).
