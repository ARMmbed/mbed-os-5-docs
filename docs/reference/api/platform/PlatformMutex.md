## PlatformMutex

The PlarformMutex class provides mutex stub functions in the absence of RTOS. This class enables you to use driver/application code when the RTOS is not present. 

### PlatformMutex class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_platform_mutex.html)

### PlatformMutex example

Mbed OS uses the PlarformMutex class instead of the RTOS mutex for all drivers. References <a href="/docs/v5.6/reference/analogin.html" target="_blank">AnalogIn</a>, <a href="/docs/v5.6/reference/busout.html" target="_blank">BusOut</a>, <a href="/docs/v5.6/reference/spi.html" target="_blank">SPI</a>, <a href="/docs/v5.6/reference/serial.html" target="_blank">Serial</a> and <a href="/docs/v5.6/reference/i2c.html" target="_blank">I2C</a>.
