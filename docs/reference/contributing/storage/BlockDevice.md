<h2 id="contributing-block-device">Block Devices</h2>

Block devices are the basic building block of storage solutions in Mbed OS. 

![MbedOSStorage](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/MbedOS-storage-overview.png)
  
Filesystems are backed by blockdevice implementations. <--TODO: Link to said implementations? --> The BlockDevice API performs the low level interactions with the hardware storage. To add your own block device implementation it is recommended to inherit from the BlockDevice class. For details on how to extend the BlockDevice interface, please refer to the [class reference](#blockdevice-class-reference) and [Implementing BlockDevice](#implementing-blockdevice) sections below.

### BlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_block_device.html)

[C++ API Reference](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/bd/BlockDevice.h)

### Assumptions

#### Defined behavior

* Erase leaves memory as undefined, it does not set memory to a predetermined value.

#### Undefined behavior

* Programming without erase is undefined behaviour don't do it silly billy.

#### Notes

![blockdevicesectors](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/blockdevice_block_size.png)

Erase, Program, and Read block sizes my not be the same; however, they must be multiples of each other.

### Implementing BlockDevice

You can find the BlockDevice class on the master branch under the features/filesystem/bd path in Mbed OS.

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_block_device.html)

The primary functions to implement are:
* `int read(void *buffer, bd_addr_t addr, bd_size_t size);`
* `int program(void *buffer, bd_addr_t addr, bd_size_t size);`
* `int erase(bd_addr_t addr, bd_size_t size);`

### Testing

You can run blockdevice tests for heap, mbr, and util block devices with the following command.

```
mbed test -t <toolchain> -m <target> -n features-tests-filesystem-*_block_device
```

The simpliest way to add tests for new block devices is to copy an existing implementation such as HeapBlocKDevice <-- TODO: Linky linky? --> and changing the block device class to your own.