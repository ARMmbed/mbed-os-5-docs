# DataFlashBlockDevice

<span class="images">![](http://os.mbed.com/docs/mbed-os/v6.0-preview/mbed-os-api-doxy/class_data_flash_block_device.png)<span>DataFlashBlockDevice class hierarchy</span></span>

DataFlashBlockDevice is a block device driver for serial flash devices that support the Atmel DataFlash protocol, such as the Adesto AT45DB series of devices.

<span class="notes">**Note:** Multiple protocols exist for SPI flash devices. This driver is for the DataFlash protocol. If your device uses the SFDP flash protocol, you need the [SPIFlashBlockDevice](../apis/spi-flash-block-device.html).</span>

DataFlash is a memory protocol that combines flash with SRAM buffers for a programming interface. DataFlash supports byte-sized read and writes, with an erase size of around 528 bytes or sometimes 1056 bytes. DataFlash provides erase sizes with an extra 16 bytes for error correction codes (ECC), so a flash translation layer (FTL) may still present 512 byte erase sizes.

You can configure the DataFlashBlockDevice to force the underlying device to use either the binary size (in other words, 512 bytes) or the raw DataFlash size (in other words, 528 bytes).

To configure this class, please see our [BlockDevice configuration documentation](../reference/storage.html#blockdevice-default-configuration).

## DataFlashBlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.0-preview/mbed-os-api-doxy/class_data_flash_block_device.html)

## DataFlashBlockDevice example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_Storage/DataFlashBlockDevice)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_Storage/DataFlashBlockDevice/main.cpp)

## Related content

- [BlockDevice configuration documentation](../reference/storage.html#blockdevice-default-configuration).
