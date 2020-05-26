<h1 id="configuration-drivers">Driver configuration</h1>

The driver configurations allows for customization of the OS driver layer. Options in this section pertain to hardware I/O. You can find additional serial settings for `printf` in the [platform configuration page](../apis/platform-options-and-config.html). With the exception of `default-serial-baud-rate`, these settings do not affect Serial objects.

This is the complete list of I/O configuration parameters. To view all configuration parameters, run the `--config -v` command. Please see [the configuration system documentation](../program-setup/advanced-configuration.html) for details on how you may use or override these settings.


```
Configuration parameters
------------------------
Name: drivers.uart-serial-rxbuf-size
    Description: Default RX buffer size for a BufferedSerial instance (unit Bytes))
    Defined by: library:drivers
    Macro name: MBED_CONF_DRIVERS_UART_SERIAL_RXBUF_SIZE
    Value: 256 (set by library:drivers)
Name: drivers.uart-serial-txbuf-size
    Description: Default TX buffer size for a BufferedSerial instance (unit Bytes))
    Defined by: library:drivers
    Macro name: MBED_CONF_DRIVERS_UART_SERIAL_TXBUF_SIZE
    Value: 256 (set by library:drivers)
```
