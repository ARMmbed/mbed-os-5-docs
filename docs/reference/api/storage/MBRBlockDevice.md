## MBRBlockDevice

<span class="images">![](https://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_m_b_r_block_device.png)<span>MBRBlockDevice class hierarchy</span></span>

The MBRBlockDevice class provides a way to manage a Master Boot Record (MBR) on a storage device, which allows you to partition the device. Without the MBR, you can still format a storage device with a file system, but including the MBR will allow for future partition modifications.

MBRBlockDevices have the following configurable parameters in the constructor:

  - _bd_ - Block device to back the MBRBlockDevice
  - _part_ - Partition to use, 1-4

You can view more information about the configurable settings and functions in the class reference.

### MBRBlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_m_b_r_block_device.html)

### MBRBlockDevice example

Partition a heap backed block device into two partitions. This example also uses the [HeapBlockDevice](/docs/development/reference/heapblockdevice.html).

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/MBRBlockDevice_ex_1/)](https://os.mbed.com/teams/mbed_example/code/MBRBlockDevice_ex_1/file/daa62d7aa9f9/main.cpp)

Partition an SD card, and format the new partition with a FAT filesystem. A PC will now be able to recognize the SD card.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/MBRBlockDevice_ex_2/)](https://os.mbed.com/teams/mbed_example/code/MBRBlockDevice_ex_2/file/a48b7099a59c/main.cpp)

### Related content

- [HeapBlockDevice](/docs/development/reference/heapblockdevice.html) API reference.
