## MBRBlockDevice

The MBRBlockDevice class provides a way to manage a Master Boot Record (MBR) on a storage device allowing for partitioning. Without the MBR a storage device can still be formatted with a filesystem, but including the MBR will allow for future partition modifications.

### MBRBlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_m_b_r_block_device.html)

### MBRBlockDevice example

Partition a heap backed block device into two partitions. The HeapBlockDevice used in this example can be found [here](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_heap_block_device.html).

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/MBRBlockDevice_ex_1/)](https://os.mbed.com/teams/mbed_example/code/MBRBlockDevice_ex_1/file/daa62d7aa9f9/main.cpp)

Partition an SD card, and format the new partition with a FAT filesystem. A PC will now be able to recognize the SD card.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/MBRBlockDevice_ex_2/)](https://os.mbed.com/teams/mbed_example/code/MBRBlockDevice_ex_2/file/a48b7099a59c/main.cpp)
