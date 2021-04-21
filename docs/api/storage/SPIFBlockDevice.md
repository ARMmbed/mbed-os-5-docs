# SPI Flash block device

<span class="images">![](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_s_p_i_f_block_device.png)<span>SPIFBlockDevice class hierarchy</span></span>

This API is a block device for NOR-based SPI flash devices that support SFDP.

<span class="notes">**Note:** Multiple protocols exist for SPI flash devices. This driver is for the SFDP SPI flash protocol. If your device uses the DataFlash protocol, you need the [DataflashBlockDevice](dataflashblockdevice.html)</span>

NOR-based SPI flash supports byte-sized read and writes, with an erase size of around 4 kbytes. An erase sets a block to all 1s, with successive writes clearing set bits.

To configure this class, please see our [BlockDevice configuration documentation](../apis/data-options-and-config.html).

## SPIFBlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_s_p_i_f_block_device.html)

## SPIFBlockDevice example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-SPIFBlockDevice/tree/v6.10)](https://github.com/ARMmbed/mbed-os-snippet-SPIFBlockDevice/blob/v6.10/main.cpp)

## Related content

- [BlockDevice configuration documentation](../apis/data-options-and-config.html).
