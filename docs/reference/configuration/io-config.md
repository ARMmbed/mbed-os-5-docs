<h1 id="configuration-drivers">Driver configuration</h1>

The driver configurations allows for customization of the OS driver layer. Options in this section pertain to hardware I/O. You can find additional serial settings for `printf` in the [platform configuration page](../apis/platform-options-and-config.html). With the exception of `default-serial-baud-rate`, these settings do not affect Serial objects.

This is the complete list of I/O configuration parameters. To view all configuration parameters, run the `--config -v` command. Please see [the configuration system documentation](../program-setup/advanced-configuration.html) for details on how you may use or override these settings.


```
Configuration parameters
------------------------
Name: drivers.crc-table-size
    Description: Number of entries in each of MbedCRC's pre-computed software tables. Higher values increase speed, but also increase image size. The value has no effect if the target performs the CRC in hardware. Permitted values are 0, 16 or 256.
    Defined by: library:drivers
    Macro name: MBED_CRC_TABLE_SIZE
    Value: 16 (set by library:drivers)
Name: drivers.qspi_csn
    Description: QSPI chip select pin
    Defined by: library:drivers
    Macro name: MBED_CONF_DRIVERS_QSPI_CSN
    Value: QSPI_FLASH1_CSN (set by library:drivers)
Name: drivers.qspi_io0
    Description: QSPI data I/O 0 pin
    Defined by: library:drivers
    Macro name: MBED_CONF_DRIVERS_QSPI_IO0
    Value: QSPI_FLASH1_IO0 (set by library:drivers)
Name: drivers.qspi_io1
    Description: QSPI data I/O 1 pin
    Defined by: library:drivers
    Macro name: MBED_CONF_DRIVERS_QSPI_IO1
    Value: QSPI_FLASH1_IO1 (set by library:drivers)
Name: drivers.qspi_io2
    Description: QSPI data I/O 2 pin
    Defined by: library:drivers
    Macro name: MBED_CONF_DRIVERS_QSPI_IO2
    Value: QSPI_FLASH1_IO2 (set by library:drivers)
Name: drivers.qspi_io3
    Description: QSPI data I/O 3 pin
    Defined by: library:drivers
    Macro name: MBED_CONF_DRIVERS_QSPI_IO3
    Value: QSPI_FLASH1_IO3 (set by library:drivers)
Name: drivers.qspi_sck
    Description: QSPI clock pin
    Defined by: library:drivers
    Macro name: MBED_CONF_DRIVERS_QSPI_SCK
    Value: QSPI_FLASH1_SCK (set by library:drivers)
Name: drivers.spi_count_max
    Description: The maximum number of SPI peripherals used at the same time. Determines RAM allocated for SPI peripheral management. If null, limit determined by hardware.
    Defined by: library:drivers
    No value set
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
