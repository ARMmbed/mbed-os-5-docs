## HeapBlockDevice

The HeapBlockDevice class provides a way to simulate block devices for software development or testing. The created blocks are nonvolatile; they do not persist across power cycles.

HeapBlockDevices have some notable configurable parameters:

  - _size_ - Size of the block device in bytes.
  - _read_size_ - Minimum read size required in bytes.
  - _program_size_ - Minimum program size required in bytes.
  - _erase_size_ - Minimum erase size required in bytes.

### HeapBlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_heap_block_device.html)
  
### HeapBlockDevice example

Create a HeapBlockDevice, program it, read the block back and clean up.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/HeapBlockDevice_ex_1/)](https://os.mbed.com/teams/mbed_example/code/HeapBlockDevice_ex_1/file/5991e7053465/main.cpp)

HeapBlockDevice used with MBRBlockDevice to showcase paritioning.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/MBRBlockDevice_ex_1/)](https://os.mbed.com/teams/mbed_example/code/MBRBlockDevice_ex_1/file/daa62d7aa9f9/main.cpp)
