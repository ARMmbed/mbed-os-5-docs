## PlatformMutex

The PlarformMutex class provides mutex stub functions in the absence of RTOS. This class enables you to use driver/application code when the RTOS is not present.

### PlatformMutex class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/v5.8/mbed-os-api-doxy/class_platform_mutex.html)

### PlatformMutex example

The code below demonstrates usage of PlatformMutex.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/mbed-os-example-platform-mutex/)](https://os.mbed.com/teams/mbed_example/code/mbed-os-example-platform-mutex/file/2084d9e90526/main.cpp)

Mbed OS uses the PlatformMutex class instead of the RTOS mutex for all drivers. For example, please see [AnalogIn](/docs/v5.8/reference/analogin.html), [BusOut](/docs/v5.8/reference/busout.html), [SPI](/docs/v5.8/reference/spi.html), [Serial](/docs/v5.8/reference/serial.html) and [I2C](/docs/v5.8/reference/i2c.html).

### Related content

- [AnalogIn](/docs/v5.8/reference/analogin.html).
- [BusOut](/docs/v5.8/reference/busout.html).
- [SPI](/docs/v5.8/reference/spi.html).
- [Serial](/docs/v5.8/reference/serial.html).
- [I2C](/docs/v5.8/reference/i2c.html).
