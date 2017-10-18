## ChainingBlockDevice

The ChainingBlockDevice class provides a way to chain together multiple block devices. The chained block devices can then be interacted with as if they were a single block device of size equal to the sum of each sub storage unit. 

Note that each block device's block size must be a multiple of the other devices' block sizes (512, 1024, etc).

The constructor takes in an array of block device pointers and provides an object from which the grouped block devices can be accessed from as a single device.

### ChainingBlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_chaining_block_device.html)

### ChainingBlockDevice example

ChainingBlockDevice example to create a FAT filesystem across multiple [HeapBlockDevices](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_heap_block_device.html).

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/ChainingBlockDevice_ex_1/)](https://os.mbed.com/teams/mbed_example/code/ChainingBlockDevice_ex_1/file/8ad9777787ba/main.cpp)

ChainingBlockDevice example showing how to program and readback data off of a chained group of [HeapBlockDevices](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_heap_block_device.html).

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/ChainingBlockDevice_ex_2/)](https://os.mbed.com/teams/mbed_example/code/ChainingBlockDevice_ex_2/file/70419b9d778a/main.cpp)
