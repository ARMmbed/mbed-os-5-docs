## Storage overview

The storage APIs present in Arm Mbed OS are:

- File system: a common interface for using file systems on block devices.
- Block device: a common interface for block-based storage devices.

### Declaring a file system

The <a href="https://os.mbed.com/docs/v5.7/mbed-os-api-doxy/classmbed_1_1_file_system.html" target="_blank">FileSystem</a> class provides the core API for file system operations. You must provide a block device to back the file system. When you declare a file system with a name, you can open files on the file system through the `open` and `fopen` functions.

#### Open

The `open` function creates a connection between a file and a file descriptor. Using a string path argument, you can open a file with a set of option flags. Other functions in Mbed OS can use the file descriptor to track the current position in a file, read and write content and so on.

#### Fopen

The `fopen` function is similar to the open function above but associates a stream with the opened file. This can be helpful when performing mainly sequential read and write operations. However, it is important to flush and close the stream to update the file. This option is weaker when trying to seek through a file often.

#### Types of file systems

- <a href="https://os.mbed.com/docs/v5.7/reference/littlefilesystem.html" target="_blank">**LittleFileSystem**</a> - The little file system (LittleFS) is a fail-safe file system we designed for embedded systems, specifically for microcontrollers that use flash storage.

  - **Bounded RAM/ROM** - This file system works with a limited amount of memory. It avoids recursion and limits dynamic memory to configurable buffers.

  - **Power-loss resilient** - We designed this for operating systems that may have random power failures. It has strong copy-on-write guarantees and keeps storage on disk in a valid state.

  - **Wear leveling** - Because the most common form of embedded storage is erodible flash memories, this file system provides a form of dynamic wear leveling for systems that cannot fit a full flash translation layer.

- **FATFileSystem** - The FAT file system is a well-known file system that you can find on almost every system, including PCs. The Mbed OS implementation of the FAT file system is based on ChanFS and is optimized for small embedded systems.

  - **Portable** - Almost every operating system supports the FAT file system, which is the most common file system found on portable storage, such as SD cards and flash drives. The FAT file system is the easiest way to support access from a PC.

The <a href="https://os.mbed.com/docs/v5.7/mbed-os-api-doxy/class_block_device.html" target="_blank">BlockDevice</a> class provides the underlying API for representing block-based storage that you can use to back a file system. Mbed OS provides standard interfaces for the more common storage media, and you can extend the BlockDevice class to provide support for unsupported storage.

Additionally, two utility block devices give you better control over storage allocation. The <a href="https://os.mbed.com/docs/v5.7/mbed-os-api-doxy/class_slicing_block_device.html" target="_blank">slicing block device</a> allows you to partition storage into smaller block devices that you can use independently, and the <a href="https://os.mbed.com/docs/v5.7/mbed-os-api-doxy/class_chaining_block_device.html" target="_blank">chaining block device</a> allows you to chain multiple block devices together and extend the usable amount of storage.

<span class="notes">**Note:** Some file systems may provide a format function for cleanly initializing a file system on an underlying block device or require external tools to set up the file system before the first use.</span>

#### The LittleFileSystem

Microcontrollers and flash storage present three challenges for embedded storage: [power loss](#power-loss-resilience), [wear](#wear-leveling) and [limited RAM and ROM](#bounded-ram-and-rom). This file system provides a solution to all three of these problems.

##### Power loss resilience

Microcontroller-scale embedded systems are usually without a shutdown routine, rely on power loss to shut down and notably lack a user interface for recovery. With a file system that is not resilient to power loss, you rely on luck to not end up with a corrupted file system. The combination of persistent storage and unpredictable power loss creates bugs that are difficult to notice and ruin the experience of unlucky users.

We built this file system with a structure that is resilient to power loss. It uses checksums to limit the assumptions of how the physical storage reacts to power loss. It provides copy-on-write guarantees and keeps the storage on disk in a valid state.

##### Wear leveling

Flash storage presents its own challenge: wear. Flash is a destructive form of storage, and continuously rewriting data to a block causes that block to wear out and become unwritable. File systems that don't account for wear can quickly burn through the blocks that store frequently updated metadata and result in the premature death of the system.

We accounted for wear when we built this file system, and the underlying structure of the file system reactively mutates as the underlying storage develops errors throughout its lifetime. This results in a form of dynamic wear-leveling that extends the lifetime of the physical storage proportionally to the size of storage. With this file system, you can extend the lifetime of storage by increasing the size of storage, which is cheaper than upgrading the storage's erase cycles.

##### Bounded RAM and ROM

File systems normally target operating systems where the scale of resources available is foreign to a microcontroller. A common trend of embedded Linux file systems is RAM usage that scales linearly with the size of storage, which makes rationalizing RAM usage in a system difficult.

We optimized this file system to work with a limited amount of RAM and ROM. It avoids recursion and limits dynamic memory to configurable buffers. At no point during operation does it store an entire storage block in RAM. The result is small RAM usage that is independent of the geometry of the underlying storage.

##### Scope

The "little" in the little file system comes from the focus on both keeping resource usage low and keeping the scope self-contained. Aside from the three targeted issues above, there is a heavy restriction against bloat in this software module. Instead, we push additional features to separate layers in the BlockDevice API that drives the Mbed OS storage stack. This gives Mbed OS a tool for remaining flexible as technology used by IoT devices develops.

### Partitioning

Partitioning allows you to split a block device among multiple storage users such that the split is portable across multiple systems. Partitioning also allows you to have multiple file systems that you can mount on one disk from both Mbed OS devices and host computers. The primary partitioning scheme that Mbed OS supports is the Master Boot Record (MBR).

<span class="notes">**Note:** File system partitioning is not required if only one file system is present.</span>

### C++ classes

The FileSystem class provides the core user C++ API. Mbed OS provides <a href="https://os.mbed.com/docs/v5.7/mbed-os-api-doxy/classmbed_1_1_file.html" target="_blank">File</a> and <a href="https://os.mbed.com/docs/v5.7/mbed-os-api-doxy/classmbed_1_1_dir.html" target="_blank">Dir</a> classes that represent files and directories in a C++ API.

### Block device operations

A block device can perform three operations on a block in a device:

- Read a block from storage.
- Erase a block in storage.
- Program a block that has previously been erased.

<span class="notes">**Note:** The state of an erased block is undefined. NOR flash devices typically set an erased block to all 0xff, but for some block devices, such as the SD card, erase is a NOOP. If a deterministic value is required after an erase, the consumer of the block device must verify this.</span>

### Block sizes

Some storage technologies have different sized blocks for different operations. For example, you can read and program NAND flash in 256-byte pages, but you must erase it in 4-kilobyte sectors.

Block devices indicate their block sizes through the `get_read_size`, `get_program_size` and `get_erase_size` functions. The erase size must be a multiple of the program size, and the program size must be a multiple of the read size. Some devices may even have a read/program size of a single byte.

As a rule of thumb, you can use the erase size for applications that use a single block size (for example, the FAT file system).

### Block devices

Mbed OS has several options for the block device:

- **SPIFBlockDevice** - Block device driver for NOR-based SPI flash devices that support SFDP. NOR-based SPI flash supports byte-sized read and writes, with an erase size of about 4kbytes. An erase sets a block to all 1s, with successive writes clearing set bits.

- **DataFlashBlockDevice** - Block device driver for NOR-based SPI flash devices that support the DataFlash protocol, such as the Adesto AT45DB series of devices. DataFlash is a memory protocol that combines flash with SRAM buffers for a programming interface. DataFlash supports byte-sized read and writes, with an erase size of around 528 bytes or sometimes 1056 bytes. DataFlash provides erase sizes with and extra 16 bytes for error correction codes (ECC), so a flash translation layer (FTL) may still present 512 byte erase sizes.

- **SDBlockDevice** - Block device driver for SD cards and eMMC memory chips. SD cards or eMMC chips offer a full FTL layer on top of NAND flash. This makes the storage well-suited for systems that require a about 1GB of memory. Additionally, SD cards are a popular form of portable storage. They are useful if you want to store data that you can access from a PC.

- <a href="https://os.mbed.com/docs/v5.7/reference/heapblockdevice.html" target="_blank">**HeapBlockDevice**</a> - Block device that simulates storage in RAM using the heap. Do not use the heap block device for storing data persistently because a power loss causes complete loss of data. Instead, use it fortesting applications when a storage device is not available.

### Utility block devices

Additionally, Mbed OS contains several utility block devices to give you better control over the allocation of storage.

- <a href="https://os.mbed.com/docs/v5.7/reference/slicingblockdevice.html" target="_blank">**SlicingBlockDevice**</a> - With the slicing block device, you can partition storage into smaller block devices that you can use independently.

- <a href="https://os.mbed.com/docs/v5.7/reference/chainingblockdevice.html" target="_blank">**ChainingBlockDevice**</a> - With the chaining block device, you can chain multiple block devices together and extend the usable amount of storage.

- <a href="https://os.mbed.com/docs/v5.7/reference/mbrblockdevice.html" target="_blank">**MBRBlockDevice**</a> - Mbed OS comes with support for storing partitions on disk with a Master Boot Record (MBR). The MBRBlockDevice provides this functionality and supports creating partitions at runtime or using preformatted partitions configured separately from outside the application.

- **ReadOnlyBlockDevice** - With the read-only block device, you can wrap a block device in a read-only layer, ensuring that user of the block device does not modify the storage.

- **ProfilingBlockDevice** - With the profiling block device, you can profile the quantity of erase, program and read operations that are incurred on a block device.

- **ObservingBlockDevice** - The observing block device grants the user the ability to register a callback on block device operations. You can use this to inspect the state of the block device, log different metrics or perform some other operation.

- **ExhaustibleBlockDevice** - Useful for evaluating how file systems respond to wear, the exhaustible block device simulates wear on another form of storage. You can configure it to expire blocks as necessary.
