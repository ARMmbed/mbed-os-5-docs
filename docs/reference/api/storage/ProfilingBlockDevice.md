## ProfilingBlockDevice

The ProfilingBlockDevice class provides a BlockDevice implementation to act as an interface for an existing block device object to log reads, writes and erases.

ProfilingBlockDevices take in a pointer to the block device being profiled as the only configurable parameter. If you want to count a storage operation such as programming, reading or writing to a block device, you should use the ProfilingBlockDevice object as the interface to the storage block rather than the underlying device. The below example highlights this use case.

### ProfilingBlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_profiling_block_device.html)
  
### ProfilingBlockDevice example

Create a ProfilingBlockDevice, perform storage operations and report back the read, write and erase counts.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/ProfilingBlockDevice_ex_1/)](https://os.mbed.com/compiler/#nav:/ProfilingBlockDevice_ex_1/main.cpp;)
