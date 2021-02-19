# ChainingBlockDevice

<span class="images">![](http://os.mbed.com/docs/v6.8/mbed-os-api-doxy/classmbed_1_1_chaining_block_device.png)<span>ChainingBlockDevice class hierarchy</span></span>

The ChainingBlockDevice class provides a way to chain together multiple block devices. You can then interact with the chained block devices as if they were a single block device of size equal to the sum of each substorage unit. The ChainingBlockDevice acts as an opposite of the [SlicingBlockDevice](slicingblockdevice.html).

Note that each block device's block size must be a multiple of the other devices' block sizes (512, 1024 and so on).

The constructor takes in an array of block device pointers and provides an object from which you can access the grouped block devices as a single device.

To configure this class, please see our [BlockDevice configuration documentation](../apis/data-options-and-config.html).

## ChainingBlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/v6.8/mbed-os-api-doxy/classmbed_1_1_chaining_block_device.html)

## ChainingBlockDevice example

This ChainingBlockDevice example creates a FAT file system across multiple [HeapBlockDevices](heapblockdevice.html).

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-ChainingBlockDevice_ex_1/tree/v6.8)](https://github.com/ARMmbed/mbed-os-snippet-ChainingBlockDevice_ex_1/blob/v6.8/main.cpp)

This ChainingBlockDevice example shows how to program and read back data from a chained group of [HeapBlockDevices](heapblockdevice.html).

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-ChainingBlockDevice_ex_2/tree/v6.8)](https://github.com/ARMmbed/mbed-os-snippet-ChainingBlockDevice_ex_2/blob/v6.8/main.cpp)

## Related content

- [SlicingBlockDevice](slicingblockdevice.html) API reference.
- [HeapBlockDevice](heapblockdevice.html) API reference.
- [BlockDevice configuration documentation](../apis/data-options-and-config.html).
