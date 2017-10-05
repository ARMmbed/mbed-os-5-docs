## HeapBlockDevice

The HeapBlockDevice class provides a way to simulate block devices for software development or testing. The created blocks are nonvolatile, they will not persist across power cycles.

### HeapBlockDevice Class Reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_heap_block_device.html)

HeapBlockDevices have some notable configurable parameters:

  - _size_ - Size of the Block Device in bytes
  - _read_size_ - Minimum read size required in bytes
  - _program_size_ - Minimum program size required in bytes
  - _erase_size_ - Minimum erase size required in bytes
  
### HeapBlockDevice Example

Create a HeapBlockDevice, program it, read the block back, and cleanup.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/HeapBlockDevice_ex_1/)](https://os.mbed.com/teams/mbed_example/code/HeapBlockDevice_ex_1/file/5991e7053465/main.cpp)
