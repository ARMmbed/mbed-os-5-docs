# PlatformMutex

<span class="images">![](https://os.mbed.com/docs/mbed-os/v6.0-preview/mbed-os-api-doxy/class_platform_mutex.png)<span>PlatformMutex class hierarchy</span></span>

You can use the PlatformMutex class to synchronize the execution of threads.

The Mbed OS drivers use the PlatformMutex class instead of [Mutex](mutex.html). This enables the use of drivers when the Mbed OS is compiled without the RTOS. For examples, please see [AnalogIn](analogin.html), [BusOut](busout.html), [Serial](serial.html), [SPI](spi.html) and [I2C](i2c.html).

<span class="notes">**Note:** For the standard use of RTOS mutexes, please see [Mutex](mutex.html).</span>

## PlatformMutex class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.0-preview/mbed-os-api-doxy/class_platform_mutex.html)

## PlatformMutex example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_Platform/PlatformMutex_ex_1/)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_Platform/PlatformMutex_ex_1/main.cpp)

## Related content

- [Mutex](mutex.html).
- [AnalogIn](analogin.html).
- [BusOut](busout.html).
- [Serial](serial.html).
- [SPI](spi.html).
- [I2C](i2c.html).
