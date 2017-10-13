## MBRBlockDevice

The MBRBlockDevice class provides a way to manage a Master Boot Record (MBR) on a storage device allowing for partitioning and formatting. The operating systems use the MBR to load the storage device properly into memory.

### MBRBlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_m_b_r_block_device.html)

### MBRBlockDevice example

Partition a heap backed block device into two partitions.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/MBRBlockDevice_ex_1/)](https://os.mbed.com/teams/mbed_example/code/MBRBlockDevice_ex_1/file/daa62d7aa9f9/main.cpp)

Partition an SD card, and format the new partition with a FAT filesystem. The SD card will now be recognized when plugged into a PC.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/MBRBlockDevice_ex_2/)](https://os.mbed.com/teams/mbed_example/code/MBRBlockDevice_ex_2/file/a48b7099a59c/main.cpp)
