## SlicingBlockDevice

The SlicingBlockDevice class provides a way to break up a block device into subunits without the need to manually track offsets. The SlicingBlockDevice acts as an opposite of the [ChainingBlockDevice](/docs/v5.7/reference/chainingblockdevice.html) class.

The constructor takes in the master block device pointer and the start and end addresses of where you would like to partition the sub-block. By not specifying the end address, you create a block device that spans from the provided start address to the end of the underlying block device.

  - _bd_ -  Block device to back the SlicingBlockDevice.
  - _start_ - Start block address to map to block 0. Negative addresses are calculated from the end of the underlying block device.
  - _end_ - End block address to mark the end of the block device. This block is not mapped; negative addresses are calculated from the end of the underlying block device.

### SlicingBlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.7/mbed-os-api-doxy/class_slicing_block_device.html)

### SlicingBlockDevice example

This SlicingBlockDevice example partitions a [HeapBlockDevice](/docs/v5.7/reference/heapblockdevice.html) into three subunits and showcases programming and reading back data segments through both the underlying master block device and the sliced subunits.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/SlicingBlockDevice_ex_1/)](https://os.mbed.com/teams/mbed_example/code/SlicingBlockDevice_ex_1/file/62c01cd06ff7/main.cpp)

### Related content

- [ChainingBlockDevice](/docs/v5.7/reference/chainingblockdevice.html) API reference.
- [HeapBlockDevice](/docs/v5.7/reference/heapblockdevice.html) API reference.
