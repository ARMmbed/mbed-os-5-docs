# Storage APIs

## File system APIs

- [Dir](../apis/file-system-apis.html): Manage and navigate directories.
- [FATFileSystem](../apis/fatfilesystem.html): Normally used for application working on boards with an SD card.
- [File](../apis/file.html): Access the underlying storage of a file system in a generic manner.
- [FileSystem](../apis/filesystem.html): A common interface for implementing a file system on a block-based storage device.
- [KVStore](../apis/kvstore.html): A common get/set API implemented by several classes. It allows flexibility in when configuring a storage solution.
- [kvstore_global_api (Static Global API)](../apis/static-global-api.html): Access the instances of KVStore components that the selected configuration allocates.
- [LittleFileSystem](../apis/littlefilesystem.html): A fail-safe file system designed for embedded systems, specifically for microcontrollers that use external flash storage.

## BlockDevice (block-based storage) APIs

- [BlockDevice](../apis/blockdevice-apis.html): An interface for access to block-based storage such as SD cards, spinning disks and heap backed storage.
- [BufferedBlockDevice](../apis/bufferedblockdevice.html): A block device adpator that reduces the read and program sizes of the underlying block device to 1.
- [ChainingBlockDevice](../apis/chainingblockdevice.html): Chain together multiple block devices and interact with the chained block devices as if they were a single block device of size equal to the sum of each substorage unit.
- [DataFlashBlockDevice](../apis/dataflashblockdevice.html): A driver for serial flash devices that supports the Atmel DataFlash protocol, such as the Adesto AT45DB series of devices.
- [FlashIAPBlockDevice](../apis/flashiapblockdevice.html): A block device driver built on top of the FlashIAP API for use where the FlashIAP implementation uses external flash or in conjunction with a file system with wear leveling, that can operate on a page size granularity.
- [FlashSimBlockDevice](../apis/flashsimblockdevice.html): A block device adapator that simulates the behavior of a flash component if the underlying block device doesn't support such a behavior.
- [HeapBlockDevice](../apis/heapblockdevice.html): Simulate block devices for software development or testing.
- [MBRBlockDevice](../apis/mbrblockdevice.html): Manage a Master Boot Record (MBR) on a storage device, which allows you to partition the device.
- [ProfilingBlockDevice](../apis/profilingblockdevice.html): A decorator for an existing block device object to log reads, writes and erases.
- [QSPIFBlockDevice](../apis/qspifblockdevice.html): A block device driver for NOR-based QSPI Flash devices that support the SFDP standard.
- [SDBlockDevice](../apis/sdblockdevice.html): Read and write data to flash storage cards using the standard POSIX File API programming interface.
- [SlicingBlockDevice](../apis/slicingblockdevice.html): Break up a block device into subunits without the need to manually track offsets. The SlicingBlockDevice acts as an opposite of the ChainingBlockDevice class.
- [SPI Flash block device](../apis/spi-flash-block-device.html): A block device for NOR-based SPI flash devices that support SFDP.

## PSA compliant

- [PSA internal storage](../apis/psa-compliant-apis.html): Save and retrieve data from a Platform Security Architecture (PSA) internal flash.
- [PSA protected storage](../apis/psa-protected-storage.html): Save and retrieve data from a Platform Security Architecture (PSA) protected storage.
