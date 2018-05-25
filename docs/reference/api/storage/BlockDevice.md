## BlockDevice

The BlockDevice API provides an interface for access to block-based storage. You can use a block device to back a full [file system](https://os.mbed.com/docs/development/reference/contributing-storage.html#contributing-filesystem) or write to it directly.

The most common type of block-based storage are different forms of flash, but the BlockDevice API can support many different forms of storage, such as SD cards, spinny disks, heap backed storage, and so on.

### Block device operations

A block device can perform three operations:
- Read a region of data from storage
- Erase a region of data in storage
- Program a region of data that has previously been erased

A full write to a block device involves first erasing the region of memory you plan to program, and then programming the data to the region of memory. The reason for this seperation is because block devices can have different limitations for erasing and writing to regions on the device.

### Block devices blocks

Block devices are byte addressable, but operate in units of "blocks". There are three types of blocks for the three types of block device operations: read blocks, erase blocks, program blocks.

**Note:** For many devices, erase blocks can be very large (for example, 4 KiB for SPI flash). As a result, it is discouraged to store an entire erase block in RAM. Instead, it is suggested to first erase a block and then program in units of the program block.

!!! Block block diagram (ask Kevin) !!!

### What does a block look like when it is erased

The state of an erased block is **undefined**. The data is stored on the block isn't decided until the block is programmed. This can be surprising, but allows the widest range of support for different types of storage.

!!! Erased block diagram (ask Kevin) !!!

### BlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_block_device.html)

[C++ API Reference](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/bd/BlockDevice.h)

### BlockDevice example

[![View example](https://www.mbed.com/embed/?type=example)](https://github.com/ARMmbed/mbed-os-example-blockdevice)
