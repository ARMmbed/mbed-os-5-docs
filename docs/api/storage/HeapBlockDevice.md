# HeapBlockDevice

<span class="images">![](http://os.mbed.com/docs/v6.16/mbed-os-api-doxy/classmbed_1_1_heap_block_device.png)<span>BlockDevice class hierarchy</span></span>

The HeapBlockDevice class provides a way to simulate block devices for software development or testing. The created blocks are volatile; they do not persist across power cycles.

HeapBlockDevices have the following configurable parameters in either one of two constructors:

## Verbose constructor

  - _size_ - Size of the block device in bytes.
  - _read_size_ - Minimum read size required in bytes.
  - _program_size_ - Minimum program size required in bytes.
  - _erase_size_ - Minimum erase size required in bytes.

Optionally, you can create a HeapBlockDevice that will set the read, program and erase sizes to the same size rather than requiring each parameter be repeated if all of the values are constrained by a common block size.

## Shortened constructor

  - _size_ - Size of the block device in bytes.
  - _block_ - Block size in bytes. You can use this to configure the minimum read, program and erase sizes to this value. Default value is 512 bytes.

You can view more information about the configurable settings and functions in the class reference. To configure this class, please see our [BlockDevice configuration documentation](../apis/data-options-and-config.html).

## HeapBlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/v6.16/mbed-os-api-doxy/classmbed_1_1_heap_block_device.html)

## HeapBlockDevice example

Create a HeapBlockDevice, program it, read the block back and clean up.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-HeapBlockDevice_ex_1/tree/v6.7)](https://github.com/ARMmbed/mbed-os-snippet-HeapBlockDevice_ex_1/blob/v6.7/main.cpp)

The HeapBlockDevice used with MBRBlockDevice showcases partitioning.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-MBRBlockDevice_ex_1/tree/v6.7)](https://github.com/ARMmbed/mbed-os-snippet-MBRBlockDevice_ex_1/blob/v6.7/main.cpp)

## Related content

- [BlockDevice configuration documentation](../apis/data-options-and-config.html).
