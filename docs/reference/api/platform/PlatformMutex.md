## PlatformMutex

<span class="images">![](https://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_platform_mutex.png)<span>PlatformMutex class hierarchy</span></span>

The PlarformMutex class provides mutex stub functions in the absence of RTOS. This class enables you to use driver/application code when the RTOS is not present.

### PlatformMutex class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_platform_mutex.html)

### PlatformMutex example

The code below demonstrates usage of PlatformMutex.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/mbed-os-example-platform-mutex/)](https://os.mbed.com/teams/mbed_example/code/mbed-os-example-platform-mutex/file/2084d9e90526/main.cpp)

Mbed OS uses the PlatformMutex class instead of the RTOS mutex for all drivers. For example, please see [AnalogIn](analogin.html), [BusOut](busout.html), [SPI](spi.html), [Serial](serial.html) and [I2C](i2c.html).

### Related content

- [AnalogIn](analogin.html).
- [BusOut](busout.html).
- [SPI](spi.html).
- [Serial](serial.html).
- [I2C](i2c.html).
