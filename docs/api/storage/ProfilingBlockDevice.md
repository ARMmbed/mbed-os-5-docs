# ProfilingBlockDevice

<span class="images">![](http://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_profiling_block_device.png)<span>ProfilingBlockDevice class hierarchy</span></span>

The ProfilingBlockDevice class provides a decorator for an existing block device object to log reads, writes and erases.

ProfilingBlockDevices take in a pointer to the block device being profiled as the only configurable parameter. If you want to count a storage operation such as programming, reading or writing to a block device, you should use the ProfilingBlockDevice object as the interface to the storage block rather than the underlying device. The below example highlights this use case.

To configure this class, please see our [BlockDevice configuration documentation](../reference/storage.html#blockdevice-default-configuration).

## ProfilingBlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_profiling_block_device.html)

## ProfilingBlockDevice example

Create a ProfilingBlockDevice, perform storage operations and report back the read, write and erase counts.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/blockdevices/ProfilingBlockDevice/)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/blockdevices/ProfilingBlockDevice/main.cpp)

## Related content

- [BlockDevice configuration documentation](../reference/storage.html#blockdevice-default-configuration).
