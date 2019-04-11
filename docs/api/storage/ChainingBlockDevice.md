# ChainingBlockDevice

<span class="images">![](http://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_chaining_block_device.png)<span>ChainingBlockDevice class hierarchy</span></span>

The ChainingBlockDevice class provides a way to chain together multiple block devices. You can then interact with the chained block devices as if they were a single block device of size equal to the sum of each substorage unit. The ChainingBlockDevice acts as an opposite of the [SlicingBlockDevice](slicingblockdevice.html).

Note that each block device's block size must be a multiple of the other devices' block sizes (512, 1024 and so on).

The constructor takes in an array of block device pointers and provides an object from which you can access the grouped block devices as a single device.

To configure this class, please see our [BlockDevice configuration documentation](../reference/storage.html#blockdevice-default-configuration).

## ChainingBlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_chaining_block_device.html)

## ChainingBlockDevice example

This ChainingBlockDevice example creates a FAT file system across multiple [HeapBlockDevices](heapblockdevice.html).

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/ChainingBlockDevice_ex_1/)](https://os.mbed.com/teams/mbed_example/code/ChainingBlockDevice_ex_1/file/8ad9777787ba/main.cpp)

This ChainingBlockDevice example shows how to program and read back data from a chained group of [HeapBlockDevices](heapblockdevice.html).

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/ChainingBlockDevice_ex_2/)](https://os.mbed.com/teams/mbed_example/code/ChainingBlockDevice_ex_2/file/70419b9d778a/main.cpp)

## Related content

- [SlicingBlockDevice](slicingblockdevice.html) API reference.
- [HeapBlockDevice](heapblockdevice.html) API reference.
- [BlockDevice configuration documentation](../reference/storage.html#blockdevice-default-configuration).
