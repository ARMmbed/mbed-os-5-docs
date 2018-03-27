## ChainingBlockDevice

The ChainingBlockDevice class provides a way to chain together multiple block devices. You can then interact with the chained block devices as if they were a single block device of size equal to the sum of each substorage unit. The ChainingBlockDevice acts as an opposite of the [SlicingBlockDevice](/docs/v5.7/reference/slicingblockdevice.html).

Note that each block device's block size must be a multiple of the other devices' block sizes (512, 1024 and so on).

The constructor takes in an array of block device pointers and provides an object from which you can access the grouped block devices as a single device.

### ChainingBlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.7/mbed-os-api-doxy/class_chaining_block_device.html)

### ChainingBlockDevice example

This ChainingBlockDevice example creates a FAT file system across multiple [HeapBlockDevices](/docs/v5.7/reference/heapblockdevice.html).

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/ChainingBlockDevice_ex_1/)](https://os.mbed.com/teams/mbed_example/code/ChainingBlockDevice_ex_1/file/8ad9777787ba/main.cpp)

This ChainingBlockDevice example shows how to program and read back data from a chained group of [HeapBlockDevices](/docs/v5.7/reference/heapblockdevice.html).

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/ChainingBlockDevice_ex_2/)](https://os.mbed.com/teams/mbed_example/code/ChainingBlockDevice_ex_2/file/70419b9d778a/main.cpp)

### Related content

- [SlicingBlockDevice](/docs/v5.7/reference/slicingblockdevice.html) API reference.
- [HeapBlockDevice](/docs/v5.7/reference/heapblockdevice.html) API reference.
