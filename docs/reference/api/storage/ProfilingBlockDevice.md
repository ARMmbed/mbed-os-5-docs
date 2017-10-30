## ProfilingBlockDevice

The ProfilingBlockDevice class provides a BlockDevice implementation to wrap around an existing block device object to log reads, writes and erases.

ProfilingBlockDevices take in a pointer to the block device being profiled as the only configurable parameter. All block device operations that wish to be logged need to be performed through the ProfilingBlockDevice object.

### ProfilingBlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_profiling_block_device.html)
  
### ProfilingBlockDevice example

Create a ProfilingBlockDevice, perform storage operations and report back the read, write and erase counts.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/ProfilingBlockDevice_ex_1/)](https://os.mbed.com/compiler/#nav:/ProfilingBlockDevice_ex_1/main.cpp;)
