<h3 id="contributing-block-device">Block Devices</h3>

Storage options in Mbed OS are all backed by block devices. Existing implementations within Mbed OS consist of:

- [HeapBlockDevice](https://os.mbed.com/docs/v5.7/reference/heapblockdevice.html)
- [MBRBlockDevice](https://os.mbed.com/docs/v5.7/reference/mbrblockdevice.html)
- [ChainingBlockDevice](https://os.mbed.com/docs/v5.7/reference/chainingblockdevice.html)
- [SlicingBlockDevice](https://os.mbed.com/docs/v5.7/reference/slicingblockdevice.html)
- [ProfilingBlockDevice](https://os.mbed.com/docs/v5.7/reference/profilingblockdevice.html)
- [SD-Driver](https://github.com/ARMmbed/sd-driver/blob/master/SDBlockDevice.h)


The block device class can be extended to implement new block device applications.

#### BlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_block_device.html)

[C++ API Reference](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/bd/BlockDevice.h)

#### Assumptions

##### Defined behavior

[Include any defined behavior in bullet format here.]

##### Undefined behavior

- Erased block devices exhibit undefined state until reprogrammed.

##### Potential bugs

[Include any potential bugs in bullet format here.]


##### Testomg

Block device tests can be found [here](https://github.com/ARMmbed/mbed-os/tree/master/features/TESTS/filesystem)

#### Implementing BlockDevice

To implement BlockDevice, each virtual function needs to be completed for the target application. The SD-Driver is a good example showing how to implement the BlockDevice class for a hardware target. By using the base BlockDevice class, any filesystem extending the Mbed OS [Filesystem class](https://os.mbed.com/docs/v5.7/mbed-os-api-doxy/classmbed_1_1_file_system.html) can utilize the new block device.

#### Testing

[Include testing information here.]
