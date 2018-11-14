
### Declaring a block device

The [BlockDevice](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_block_device.html) class provides the underlying API for raw storage that you can use to back a file system. The BlockDevice API is a standard block-oriented interface built around three modes of operation: read, erase, and program. However, the rules behind this API is flexible enough to allow support for a large range of different storage types.

Mbed OS provides standard implementations for the more common storage media, and you can extend the BlockDevice class to provide support for unsupported storage. Additionally, Mbed OS contains a handful of utility block devices, such as the [SlicingBlockDevice](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_slicing_block_device.html) and [ChainingBlockDevice](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_chaining_block_device.html), to give you better control over storage allocation. These utility block devices can be stacked to provide relatively complex storage architectures through relatively simple components.

#### Block devices

Mbed OS has several block device implementations for common forms of storage:

- **SPIFBlockDevice** - Block device driver for NOR-based SPI flash devices that support SFDP. NOR-based SPI flash supports byte-sized read and writes, with an erase size of about 4kbytes. An erase sets a block to all 1s, with successive writes clearing set bits.

- **DataFlashBlockDevice** - Block device driver for NOR-based SPI flash devices that support the DataFlash protocol, such as the Adesto AT45DB series of devices. DataFlash is a memory protocol that combines flash with SRAM buffers for a programming interface. DataFlash supports byte-sized read and writes, with an erase size of around 528 bytes or sometimes 1056 bytes. DataFlash provides erase sizes with and extra 16 bytes for error correction codes (ECC), so a flash translation layer (FTL) may still present 512 byte erase sizes.

- **SDBlockDevice** - Block device driver for SD cards and eMMC memory chips. SD cards or eMMC chips offer a full FTL layer on top of NAND flash. This makes the storage well-suited for systems that require a about 1GB of memory. Additionally, SD cards are a popular form of portable storage. They are useful if you want to store data that you can access from a PC.

- [**HeapBlockDevice**](heapblockdevice.html) - Block device that simulates storage in RAM using the heap. Do not use the heap block device for storing data persistently because a power loss causes complete loss of data. Instead, use it for testing applications when a storage device is not available.

- **FlashIAPBlockDevice** - Block device adapter for the [FlashIAP driver](flash-iap.html), which provides an in application programming (IAP) interface for the MCU's internal flash memory.

#### Utility block devices

Additionally, Mbed OS contains several utility block devices to give you better control over the allocation of storage.

- [**SlicingBlockDevice**](slicingblockdevice.html) - With the slicing block device, you can partition storage into smaller block devices that you can use independently.

- [**ChainingBlockDevice**](chainingblockdevice.html) - With the chaining block device, you can chain multiple block devices together and extend the usable amount of storage.

- [**MBRBlockDevice**](mbrblockdevice.html) - Mbed OS comes with support for storing partitions on disk with a Master Boot Record (MBR). The MBRBlockDevice provides this functionality and supports creating partitions at runtime or using preformatted partitions configured separately from outside the application.

- **ReadOnlyBlockDevice** - With the read-only block device, you can wrap a block device in a read-only layer, ensuring that user of the block device does not modify the storage.

- **ProfilingBlockDevice** - With the profiling block device, you can profile the quantity of erase, program and read operations that are incurred on a block device.

- **ObservingBlockDevice** - The observing block device grants the user the ability to register a callback on block device operations. You can use this to inspect the state of the block device, log different metrics or perform some other operation.

- **ExhaustibleBlockDevice** - Useful for evaluating how file systems respond to wear, the exhaustible block device simulates wear on another form of storage. You can configure it to expire blocks as necessary.

- [**FlashSimBlockDevice**](https://github.com/ARMmbed/mbed-os-5-docs/blob/new_engine/docs/reference/api/storage/FlashSimBlockDevice.md) - Simulate the behavior of a flash component if the underlying block device doesn't support such behavior.

- [**BufferedBlockDevice**](https://github.com/ARMmbed/mbed-os-5-docs/blob/new_engine/docs/reference/api/storage/BufferedBlockDevice.md) - Provides a buffer for the read and program blocks on a block device which reduces the read and program sizes of the underlying block device to 1 B.
