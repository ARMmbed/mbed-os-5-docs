# SPI Flash block device

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/class_s_p_i_f_block_device.png)<span>SPIFBlockDevice class hierarchy</span></span>

This API is a block device for NOR-based SPI flash devices that support SFDP.

NOR-based SPI flash supports byte-sized read and writes, with an erase size of around 4 kbytes. An erase sets a block to all 1s, with successive writes clearing set bits.

To configure this class, please see our [BlockDevice configuration documentation](../reference/storage.html#blockdevice-default-configuration).

## SPIFBlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/class_s_p_i_f_block_device.html)

## SPIFBlockDevice example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/SPIFBlockDevice)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/blockdevices/SPIFBlockDevice/main.cpp)

## Related content

- [BlockDevice configuration documentation](../reference/storage.html#blockdevice-default-configuration).
