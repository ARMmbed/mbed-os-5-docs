## Storage overview

The storage APIs present in Arm Mbed OS are:

- <a href="/docs/v5.6/reference/contributing-storage.html#contributing-filesystem" target="_blank">File system</a>: a common interface for using file systems on block devices.
- <a href="/docs/v5.6/reference/contributing-storage.html#block-devices" target="_blank">Block device</a>: a common interface for block-based storage devices.

#### Declaring a file system

The <a href="https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/FileSystem.h" target="_blank">FileSystem</a> class provides the core API for file system operations. You must provide a block device to back the file system. When you declare a file system with a name, you can open files on the file system through standard POSIX functions (see <a href="http://pubs.opengroup.org/onlinepubs/009695399/functions/open.html" target="_blank">open</a> or <a href="http://pubs.opengroup.org/onlinepubs/9699919799/functions/fopen.html" target="_blank">fopen</a>).

Existing file systems:

1. <a href="https://os.mbed.com/docs/v5.6/reference/littlefilesystem.html" target="_blank">LittleFileSystem</a>

   The little filesystem (LittleFS) is a fail-safe filesystem designed for embedded systems, specifically for microcontrollers that use flash storage.

   **Bounded RAM/ROM** - The LittleFS works with a limited amount of memory. The LittleFS avoids recursion and limits dynamic memory to configurable buffers that can be provided statically.
   
   **Power-loss resilient** - The LittleFS is designed for operating systems that may have random power failures. The LittleFS has strong copy-on-write guarantees and keeps storage on disk in a valid state.
   
   **Wear leveling** - Because the most common form of embedded storage is erodible flash memories, the LittleFS provides a form of dynamic wear leveling for systems that cannot fit a full flash translation layer.

1. FATFileSystem

   The FAT file system is a well known file system that you can find on almost every system, including PCs. Mbed OS's implementation of the FAT file system is based on <a href="http://elm-chan.org/fsw/ff/00index_e.html" target="_blank">ChanFS</a> and is optimized for small embedded systems.

   **Portable** - Almost every operating system supports the FAT file system, which is the most common file system found on portable storage, such as SD cards and flash drives. The FAT file system is the easiest way to support access from a PC.

The <a href="https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/bd/BlockDevice.h" target="_blank">BlockDevice</a> class provides the underlying API for representing block-based storage that can be used to back a file system. Mbed OS provides standard interfaces for the more common storage media, and you can extend the BlockDevice class to provide support for unsupported storage.

Additionally, two utility block devices give you better control over how storage is allocated. The <a href="https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/bd/SlicingBlockDevice.h" target="_blank">slicing block device</a> allows you to partition storage into smaller block devices that you can use independently, and the <a href="https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/bd/ChainingBlockDevice.h" target="_blank">chaining block device</a> allows you to chain multiple block devices together and extend the usable amount of storage.

<span class="notes">**Note:** Some file systems may provide a format function for cleanly initializing a file system on an underlying block device or require external tools to set up the file system before the first use.</span>

#### Partitioning

Partitioning allows you to split a block device among multiple storage users such that the split is portable across multiple systems. Partitioning also allows you to have multiple file systems that you can mount on one disk from both Mbed OS devices and host computers. The primary partitioning scheme that Mbed OS supports is the Master Boot Record (MBR).

<span class="notes">**Note:** File system partitioning is not required if only one file system is present.</span>

#### C++ classes

The <a href="https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/FileSystem.h" target="_blank">FileSystem</a> class provides the core user interface with general functions that map to their global POSIX counterparts. Mbed OS provides <a href="https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/File.h" target="_blank">File</a> and <a href="https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/Dir.h" target="_blank">Dir</a> classes that represent files and directories in a C++ API that uses object-oriented features in C++.

To implement a new file system in Mbed OS, an implementor just needs to provide the abstract functions in the file system interface. The <a href="https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/fat/FATFileSystem.cpp" target="_blank">FAT file system</a> provides an excellent example. You can see <a href="https://github.com/ARMmbed/sd-driver/tree/master/features/TESTS/filesystem" target="_blank">tests of the POSIX API</a>.

A minimal file system needs to provide the following functions:

- `file_open`.
- `file_close`.
- `file_read`.
- `file_write`.
- `file_seek`.

Here is the full API that a file system may implement:

[![View code](https://www.mbed.com/embed/?type=library)](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/FileSystem.h#L205)

#### Block device operations

A block device can perform three operations on a block in a device:

- Read a block from storage.
- Erase a block in storage.
- Program a block that has previously been erased.

<span class="notes">**Note:** The state of an erased block is undefined. NOR flash devices typically set an erased block to all 0xff, but for some block devices such as the SD card, erase is a NOOP. If a deterministic value is required after an erase, the consumer of the block device must verify this.</span>

#### Block sizes

Some storage technologies have different sized blocks for different operations. For example, you can read and program NAND flash in 256-byte pages, but you must erase it in 4-kilobyte sectors.

Block devices indicate their block sizes through the `get_read_size`, `get_program_size` and `get_erase_size` functions. The erase size must be a multiple of the program size, and the program size must be a multiple of the read size. Some devices may even have a read/program size of a single byte.

As a rule of thumb, you can use the erase size for applications that use a single block size (for example, the FAT file system).

#### Block devices

Mbed OS has four options for the block device:

1. SPIFBlockDevice

   Block device driver for NOR-based SPI flash devices that support SFDP.

   NOR-based SPI flash supports byte-sized read and writes, with an erase size of about 4kbytes. An erase sets a block to all 1s, with successive writes clearing set bits.

1. DataFlashBlockDevice

   Block device driver for NOR-based SPI flash devices that support the DataFlash protocol, such as the Adesto AT45DB series of devices.

   DataFlash is a memory protocol that combines flash with SRAM buffers for a programming interface. DataFlash supports byte-sized read and writes, with an erase size of around 528 bytes or sometimes 1056 bytes. DataFlash provides erase sizes with and extra 16 bytes for error correction codes (ECC), so a flash translation layer (FTL) may still present 512 byte erase sizes.

1. SDBlockDevice

   Block device driver for SD cards and eMMC memory chips.

   SD cards or eMMC chips offer a full FTL layer on top of NAND flash. This makes the storage well-suited for systems that require a about 1GB of memory.

   Additionally, SD cards are a popular form of portable storage. They are useful if you want to store data that you can be access from a PC.

1. <a href="https://os.mbed.com/docs/v5.6/reference/heapblockdevice.html" target="_blank">HeapBlockDevice</a>

   Block device that simulates storage in RAM using the heap.

   Do not use the heap block device for storing data persistently because a power loss causes complete loss of data. Instead, use it fortesting applications when a storage device is not available.

#### Utility block devices

Additionally, Mbed OS contains several utility block devices to give you better control over the allocation of storage.

- <a href="https://os.mbed.com/docs/v5.6/reference/slicingblockdevice.html" target="_blank">SlicingBlockDevice</a>

  With the slicing block device, you can partition storage into smaller block devices that you can use independently.

- <a href="https://os.mbed.com/docs/v5.6/reference/chainingblockdevice.html" target="_blank">ChainingBlockDevice</a>

  With the chaining block device, you can chain multiple block devices together and extend the usable amount of storage.

- <a href="https://os.mbed.com/docs/v5.6/reference/mbrblockdevice.html" target="_blank">MBRBlockDevice</a>

  Mbed OS comes with support for storing partitions on disk with a Master Boot Record (MBR). The MBRBlockDevice provides this functionality and supports creating partitions at runtime or using preformatted partitions configured separately from outside the application.

- ReadOnlyBlockDevice

  With the read-only block device, you can wrap a block device in a read-only layer, ensuring that user of the block device does not modify the storage.

- ProfilingBlockDevice

  With the profiling block device, you can profile the quantity of erase, program and read operations that are incurred on a block device.

- ObservingBlockDevice

  The observing block device grants the user the ability to register a callback on block device operations. You can use this to inspect the state of the block device, log different metrics or perform some other operation.

- ExhaustibleBlockDevice

  Useful for evaluating how file systems respond to wear, the exhaustible block device simulates wear on another form of storage. You can configure it to expire blocks as necessary.
