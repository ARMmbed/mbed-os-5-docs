# MBRBlockDevice

<span class="images">![](http://os.mbed.com/docs/v6.13/mbed-os-api-doxy/classmbed_1_1_m_b_r_block_device.png)<span>MBRBlockDevice class hierarchy</span></span>

The MBRBlockDevice class provides a way to manage a Master Boot Record (MBR) on a storage device, which allows you to partition the device. Without the MBR, you can still format a storage device with a file system, but including the MBR will allow for future partition modifications.

MBRBlockDevices have the following configurable parameters in the constructor:

  - _bd_ - Block device to back the MBRBlockDevice
  - _part_ - Partition to use, 1-4

You can view more information about the configurable settings and functions in the class reference. To configure this class, please see our [BlockDevice configuration documentation](../apis/data-options-and-config.html).

## MBRBlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/v6.13/mbed-os-api-doxy/classmbed_1_1_m_b_r_block_device.html)

## MBRBlockDevice example

Partition a heap backed block device into two partitions. This example also uses the [HeapBlockDevice](heapblockdevice.html).

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-MBRBlockDevice_ex_1/tree/v6.13)](https://github.com/ARMmbed/mbed-os-snippet-MBRBlockDevice_ex_1/blobl/v6.13/main.cpp)

Partition an SD card, and format the new partition with a FAT filesystem. A PC will now be able to recognize the SD card.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-MBRBlockDevice_ex_2/tree/v6.13)](https://github.com/ARMmbed/mbed-os-snippet-MBRBlockDevice_ex_2/blobl/v6.13/main.cpp)

## Related content

- [HeapBlockDevice](heapblockdevice.html) API reference.
- [BlockDevice configuration documentation](../apis/data-options-and-config.html).
