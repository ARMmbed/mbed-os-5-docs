## PlatformMutex

<span class="images">![](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_platform_mutex.png)<span>PlatformMutex class hierarchy</span></span>

The PlatformMutex class is used to synchronize the execution of threads.

The PlatformMutex class is used by the Mbed OS drivers instead of [Mutex](mutex.html).
This enables the use of drivers when the Mbed OS is compiled without the RTOS.
For example, please see [AnalogIn](analogin.html), [BusOut](busout.html),
[SPI](spi.html), [Serial](serial.html) and [I2C](i2c.html).

<span class="notes">**Note:**
For the standard use of RTOS mutexes, please see [Mutex](mutex.html).</span>

### PlatformMutex class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_platform_mutex.html)

### PlatformMutex example

PlatformMutex usage example for Mbed OS compiled with the RTOS.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/mbed-os-example-platform-mutex/)](https://os.mbed.com/teams/mbed_example/code/mbed-os-example-platform-mutex/file/2084d9e90526/main.cpp)

### Related content

- [Mutex](mutex.html),
- [AnalogIn](analogin.html),
- [BusOut](busout.html),
- [SPI](spi.html),
- [Serial](serial.html),
- [I2C](i2c.html).
