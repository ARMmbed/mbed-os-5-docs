<h1 id="storage-api">Storage overview</h1>

The storage APIs present in Arm Mbed OS are:

- [KVStore:](#kvstore) a common interface for components presenting set/get API.
- [File system:](#declaring-a-file-system) a common interface for using file systems on block devices.
- [Block device:](#declaring-a-block-device) a common interface for block-based storage devices.

Additionally, the following PSA-compliant APIs are present in Mbed OS:

- [PSA protected storage:](../apis/psa-protected-storage.html) PSA-compliant API for a Non-Secure Processing Environment (NSPE).
- [PSA internal storage:](../apis/psa-internal-storage.html) PSA-compliant API for a Secure Processing Environment (SPE).

## KVStore

The [KVStore API](../apis/kvstore.html) is a common get/set API implemented by several classes. It gives you the flexibility to build a storage solution by allocating several combinations of objects.

Classes that implementing the KVStore API are:

- Tiny Database Storage (TDBStore).
- FileSystemStore.
- SecureStore.

The [KVStore static global API](static-global-api.html) is the only API applications should use to access the instances of KVStore components allocated by the selected configuration.

## Declaring a file system

The [FileSystem](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_file_system.html) class provides the core API for file system operations. You must provide a block device to back the file system, which provides the raw storage for the file system. When you declare a file system with a name, you can open files on the file system through the `open` and `fopen` functions or through the File class's `open` function.

### File systems

File systems are the strongest persistent storage solutions in Mbed OS, providing an extensive POSIX API. We highly recommend using the little file system for embedded applications because of to its resilience to power failures.

- [**LittleFileSystem**](littlefilesystem.html) - The little file system (LittleFS) is a fail-safe file system we designed for embedded systems, specifically for microcontrollers that use flash storage.

  - **Bounded RAM/ROM** - This file system works with a limited amount of memory. It avoids recursion and limits dynamic memory to configurable buffers.

  - **Power-loss resilient** - We designed this for operating systems that may have random power failures. It has strong copy-on-write guarantees and keeps storage on disk in a valid state.

  - **Wear leveling** - Because the most common form of embedded storage is erodible flash memories, this file system provides a form of dynamic wear leveling for systems that cannot fit a full flash translation layer.

- [**FATFileSystem**](fatfilesystem.html) - The FAT file system is an established disk-oriented file system that you can find on most operating systems, including Windows, Linux, macOS and Mbed OS.

  - **Portable** - Due to its support across operating systems, the FAT file system provides access to storage from both the embedded system and your PC.

  - **Embedded** - Built on the ChanFS project, the FAT file system is optimized for embedded systems.

- **LocalFileSystem** - The LocalFileSystem is a symbiotic file system that connects to the Mbed board's interface chip if the interface chip has built-in storage. The features available on the LocalFileSystem is dependent on the board's interface chip. **Note:** The LocalFileSystem is only available on the LPC1768 and LPC11U24.

<span class="notes">**Note:** Some file systems may provide a format function for cleanly initializing a file system on an underlying block device or require external tools to set up the file system before the first use.</span>

### The LittleFileSystem

Microcontrollers and flash storage present three challenges for embedded storage: [power loss](#power-loss-resilience), [wear](#wear-leveling) and [limited RAM and ROM](#bounded-ram-and-rom). This file system provides a solution to all three of these problems.

#### Power loss resilience

Microcontroller-scale embedded systems are usually without a shutdown routine, rely on power loss to shut down and notably lack a user interface for recovery. With a file system that is not resilient to power loss, you rely on luck to not end up with a corrupted file system. The combination of persistent storage and unpredictable power loss creates bugs that are difficult to notice and ruin the experience of unlucky users.

We built this file system with a structure that is resilient to power loss. It uses checksums to limit the assumptions of how the physical storage reacts to power loss. It provides copy-on-write guarantees and keeps the storage on disk in a valid state.

#### Wear leveling

Flash storage presents its own challenge: wear. Flash is a destructive form of storage, and continuously rewriting data to a block causes that block to wear out and become unwritable. File systems that don't account for wear can quickly burn through the blocks that store frequently updated metadata and result in the premature death of the system.

We accounted for wear when we built this file system, and the underlying structure of the file system reactively mutates as the underlying storage develops errors throughout its lifetime. This results in a form of dynamic wear-leveling that extends the lifetime of the physical storage proportionally to the size of storage. With this file system, you can extend the lifetime of storage by increasing the size of storage, which is cheaper than upgrading the storage's erase cycles.

#### Bounded RAM and ROM

File systems normally target operating systems where the scale of resources available is foreign to a microcontroller. A common trend of embedded Linux file systems is RAM usage that scales linearly with the size of storage, which makes rationalizing RAM usage in a system difficult.

We optimized this file system to work with a limited amount of RAM and ROM. It avoids recursion and limits dynamic memory to configurable buffers. At no point during operation does it store an entire storage block in RAM. The result is small RAM usage that is independent of the geometry of the underlying storage.

#### Scope

The "little" in the little file system comes from the focus on both keeping resource usage low and keeping the scope self-contained. Aside from the three targeted issues above, there is a heavy restriction against bloat in this software module. Instead, we push additional features to separate layers in the BlockDevice API that drives the Mbed OS storage stack. This gives Mbed OS a tool for remaining flexible as technology used by IoT devices develops.

### The FATFileSystem

The FAT file system is an established disk-oriented file system that you can find on Mbed OS, Windows, Linux and macOS. Due to its age and popularity, the FAT file system has become the standard for portable storage, such as flash drives and SD cards.

#### Portable

The primary feature of the FAT file system is its portability. With support across PC operating systems, the FAT file system lets you access storage from both the embedded system your PC. This gives users a way to get information onto and off of the device.

#### Embedded

The Mbed OS FAT file system is built on the ChanFS project. It is optimized for embedded systems and is one of the smallest FAT file system implementations.

### C++ classes

The FileSystem class provides the core user C++ API. Mbed OS provides [File](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_file.html) and [Dir](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_dir.html) classes that represent files and directories in a C++ API.

## Declaring a block device

The [BlockDevice](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_block_device.html) class provides the underlying API for raw storage that you can use to back a file system. The BlockDevice API is a standard block-oriented interface built around three modes of operation: read, erase, and program. However, the rules behind this API is flexible enough to allow support for a large range of different storage types.

Mbed OS provides standard implementations for the more common storage media, and you can extend the BlockDevice class to provide support for unsupported storage. Additionally, Mbed OS contains a handful of utility block devices, such as the [SlicingBlockDevice](https://os.mbed.com/docs/development/mbed-os-api-doxy/_slicing_block_device_8h_source.html) and [ChainingBlockDevice](https://os.mbed.com/docs/development/mbed-os-api-doxy/_chaining_block_device_8h_source.html), to give you better control over storage allocation. These utility block devices can be stacked to provide relatively complex storage architectures through relatively simple components.

### Block devices

Mbed OS has several block device implementations for common forms of storage:

- **SPIFBlockDevice** - Block device driver for NOR-based SPI flash devices that support SFDP. NOR-based SPI flash supports byte-sized read and writes, with an erase size of about 4kbytes. An erase sets a block to all 1s, with successive writes clearing set bits.

- **DataFlashBlockDevice** - Block device driver for NOR-based SPI flash devices that support the DataFlash protocol, such as the Adesto AT45DB series of devices. DataFlash is a memory protocol that combines flash with SRAM buffers for a programming interface. DataFlash supports byte-sized read and writes, with an erase size of around 528 bytes or sometimes 1056 bytes. DataFlash provides erase sizes with and extra 16 bytes for error correction codes (ECC), so a flash translation layer (FTL) may still present 512 byte erase sizes.

- **SDBlockDevice** - Block device driver for SD cards and eMMC memory chips. SD cards or eMMC chips offer a full FTL layer on top of NAND flash. This makes the storage well-suited for systems that require a about 1GB of memory. Additionally, SD cards are a popular form of portable storage. They are useful if you want to store data that you can access from a PC.

- [**HeapBlockDevice**](heapblockdevice.html) - Block device that simulates storage in RAM using the heap. Do not use the heap block device for storing data persistently because a power loss causes complete loss of data. Instead, use it for testing applications when a storage device is not available.

- **FlashIAPBlockDevice** - Block device adapter for the [FlashIAP driver](flash-iap.html), which provides an in application programming (IAP) interface for the MCU's internal flash memory.

### Utility block devices

Additionally, Mbed OS contains several utility block devices to give you better control over the allocation of storage.

- [**SlicingBlockDevice**](slicingblockdevice.html) - With the slicing block device, you can partition storage into smaller block devices that you can use independently.

- [**ChainingBlockDevice**](chainingblockdevice.html) - With the chaining block device, you can chain multiple block devices together and extend the usable amount of storage.

- [**MBRBlockDevice**](mbrblockdevice.html) - Mbed OS comes with support for storing partitions on disk with a Master Boot Record (MBR). The MBRBlockDevice provides this functionality and supports creating partitions at runtime or using preformatted partitions configured separately from outside the application.

- **ReadOnlyBlockDevice** - With the read-only block device, you can wrap a block device in a read-only layer, ensuring that user of the block device does not modify the storage.

- **ProfilingBlockDevice** - With the profiling block device, you can profile the quantity of erase, program and read operations that are incurred on a block device.

- **ObservingBlockDevice** - The observing block device grants the user the ability to register a callback on block device operations. You can use this to inspect the state of the block device, log different metrics or perform some other operation.

- **ExhaustibleBlockDevice** - Useful for evaluating how file systems respond to wear, the exhaustible block device simulates wear on another form of storage. You can configure it to expire blocks as necessary.

- [**FlashSimBlockDevice**](../apis/flashsimblockdevice.html) - Simulate the behavior of a flash component if the underlying block device doesn't support such behavior.

- [**BufferedBlockDevice**](../apis/bufferedblockdevice.html) - Provides a buffer for the read and program blocks on a block device which reduces the read and program sizes of the underlying block device to 1 B.
