## PlatformMutex

The PlarformMutex class provides mutex stub functions in the absence of RTOS. This class enables you to use driver/application code when the RTOS is not present. 

### PlatformMutex class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os-doc-builder.test.mbed.com/docs/v5.7/mbed-os-api-doxy/class_platform_mutex.html)

### PlatformMutex example

The code below demonstrates usage of PlatformMutex.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/mbed-os-example-platform-mutex/)](https://os.mbed.com/teams/mbed_example/code/mbed-os-example-platform-mutex/file/2084d9e90526/main.cpp)

Mbed OS uses the PlarformMutex class instead of the RTOS mutex for all drivers. For example, please see <a href="/docs/v5.6/reference/analogin.html" target="_blank">AnalogIn</a>, <a href="/docs/v5.6/reference/busout.html" target="_blank">BusOut</a>, <a href="/docs/v5.6/reference/spi.html" target="_blank">SPI</a>, <a href="/docs/v5.6/reference/serial.html" target="_blank">Serial</a> and <a href="/docs/v5.6/reference/i2c.html" target="_blank">I2C</a>.

### Related content

- <a href="/docs/v5.6/reference/analogin.html" target="_blank">AnalogIn</a>.
- <a href="/docs/v5.6/reference/busout.html" target="_blank">BusOut</a>. 
- <a href="/docs/v5.6/reference/spi.html" target="_blank">SPI</a>. 
- <a href="/docs/v5.6/reference/serial.html" target="_blank">Serial</a>. 
- <a href="/docs/v5.6/reference/i2c.html" target="_blank">I2C</a>.
