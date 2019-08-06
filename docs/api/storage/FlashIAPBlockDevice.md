# FlashIAPBlockDevice

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/class_flash_i_a_p_block_device.png)<span>FlashIAPBlockDevice class hierarchy</span></span>

The flash IAP block device is a block device driver built on top of the FlashIAP API. This is enabled using the internal flash memory as a block device. The read size, write size and erase size may differ, depending on the flash chip. Use the FlashIAPBlockDevice `get` function to discover those sizes.

Additional notes:

1. Use this driver on platforms where the FlashIAP implementation uses external flash or in conjunction with a file system with wear leveling, that can operate on a page size granularity.
1. The FlashIAP may freeze code execution for a long period of time while writing to flash. Not even high-priority IRQs are allowed to run, which may interrupt background processes.

To configure this class, please see our [BlockDevice configuration documentation](../reference/storage.html#blockdevice-default-configuration).

## FlashIAPBlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/class_flash_i_a_p_block_device.html)

## FlashIAPBlockDevice example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/blockdevices/FlashIAPBlockDevice/)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/blockdevices/FlashIAPBlockDevice/main.cpp)

## Related content

- [BlockDevice configuration documentation](../reference/storage.html#blockdevice-default-configuration).
