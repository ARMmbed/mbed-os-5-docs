## Storage overview

The storage APIs present in Arm Mbed OS are:

- <a href="/docs/v5.6/reference/contributing-storage.html#contributing-filesystem" target="_blank">File system</a>: a common interface for using file systems on block devices.
- <a href="/docs/v5.6/reference/contributing-storage.html#block-devices" target="_blank">Block device</a>: a common interface for block-based storage devices.

#### Declaring a file system

The <a href="https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/FileSystem.h" target="_blank">FileSystem</a> class provides the core API for file system operations. You must provide a block device to back the file system. When you declare a file system with a name, you can open files on the file system through standard POSIX functions (see <a href="http://pubs.opengroup.org/onlinepubs/009695399/functions/open.html" target="_blank">open</a> or <a href="http://pubs.opengroup.org/onlinepubs/9699919799/functions/fopen.html" target="_blank">fopen</a>).

Existing file systems:

1. [LittleFileSystem](TODO LINK ME, TO DOCS PAGE?)

   The littlefs is a little fail-safe filesystem designed for embedded systems.

   **Bounded RAM/ROM** - The littlefs is designed to work with a limited amount
   of memory. Recursion is avoided, and dynamic memory is limited to configurable
   buffers that can be provided statically.
   
   **Power-loss resilient** - The littlefs is designed for systems that may have
   random power failures. The littlefs has strong copy-on-write guarantees, and
   storage on disk is always kept in a valid state.
   
   **Wear leveling** - Because the most common form of embedded storage is erodible
   flash memories, littlefs provides a form of dynamic wear leveling for systems
   that cannot fit a full flash translation layer.

   You can find more info about the littlefs [here](TODO LINK ME, TO DOCS PAGE?).

1. [FATFileSystem](TODO LINK ME, TO DOCS PAGE?)

   The FAT filesystem is a well known filesystem that you can find on almost every
   system, including PCs. Mbed OS's implementation of the FAT filesystem is based
   on [ChanFS](TODO LINK ME?), and is optimized for small embedded systems.

   **Portable** - The FAT filesystem is supported on almost every system, and is
   the most common filesystem found on portable storage such as SD cards and flash
   drives. The FAT filesystem is the easiest way to support access from a PC.

   You can find more info about the FAT filesystem [here](TODO LINK ME, TO DOCS PAGE?).

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

Here is the full API that a filesystem may implement:

[![View code](https://www.mbed.com/embed/?type=library)](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/FileSystem.h#L205)

#### Block device operations

A block device can perform three operations on a block in a device:

- Read a block from storage.
- Erase a block in storage.
- Program a block that has previously been erased.

<span class="notes">**Note:** The state of an erased block is undefined. NOR flash devices typically set an erased block to all 0xff, but for some block devices such as the SD card, erase is a NOOP. If a deterministic value is required after an erase, the consumer of the block device must verify this.</span>

#### Block sizes

Some storage technologies have different sized blocks for different operations. For example, NAND flash can be read and programmed in 256-byte pages, but must be erased in 4-kilobyte sectors.

Block devices indicate their block sizes through the `get_read_size`, `get_program_size` and `get_erase_size` functions. The erase size must be a multiple of the program size, and the program size must be a multiple of the read size. Some devices may even have a read/program size of a single byte.

As a rule of thumb, you can use the erase size for applications that use a single block size (for example, the FAT file system).

#### Block devices

Mbed OS has four options for the block device:

1. [SPIFBlockDevice](TODO LINK ME)

   Block device driver for NOR based SPI flash devices that support SFDP.

   NOR based SPI flash supports byte-sized read and writes, with an erase size
   of around 4kbytes. An erase sets a block to all 1s, with successive writes
   clearing set bits.

   More info on NOR flash can be found on wikipedia:
   https://en.wikipedia.org/wiki/Flash_memory#NOR_memories

   You can find more info about the SPI flash driver [here](TODO LINK ME, TO DOCS PAGE? MAYBE JUST GIT REPO).

1. [DataFlashBlockDevice](TODO LINK ME)

   Block device driver for NOR based SPI flash devices that support the DataFlash
   protocol, such as the Adesto AT45DB series of devices.

   DataFlash is a memory protocol that combines flash with SRAM buffers for a
   simple programming interface. DataFlash supports byte-sized read and writes,
   with an erase size of around 528 bytes or sometimes 1056 bytes. DataFlash
   provides erase sizes with and extra 16 bytes for error correction codes (ECC)
   so that a flash translation layer (FTL) may still present 512 byte erase sizes.

   More info on DataFlash can be found on wikipedia:
   https://en.wikipedia.org/wiki/DataFlash

   You can find more info about the DataFlash driver [here](TODO LINK ME, TO DOCS PAGE? MAYBE JUST GIT REPO).

1. [SDBlockDevice](TODO LINK ME)

   Block device driver for SD cards and eMMC memory chips.

   SD cards or eMMC chips offer a full FTL layer on top of NAND flash. This
   makes the storage well suited for systems that require a very large amount of
   memory (>1GB).

   Additionally, SD cards are a popular form of portable storage, and useful
   if you want to store data that can be accessed from a PC.

   More info on SD cards can be found on wikipedia:
   https://en.wikipedia.org/wiki/Secure_Digital

   You can find more info about the SD driver [here](TODO LINK ME, TO DOCS PAGE? MAYBE JUST GIT REPO).

1. [HeapBlockDevice](TODO LINK ME)

   Block device that simulates storage in RAM using the heap.

   The heap block device is useless for storing data persistently, given that a
   power loss will cause complete loss of data. However, it is useful for testing
   applications when a storage device is not available.

   You can find more info about the heap block device [here](TODO LINK ME, TO DOCS PAGE?).

#### Utility block devices

Additionally, Mbed OS contains several utility block devices to give you better control over the allocation of storage.

- [SlicingBlockDevice](TODO LINK ME)

  With the slicing block device, you can partition storage into smaller
  block devices that you can use independently.

- [ChainingBlockDevice](TODO LINK ME)

  With the chaining block device, you can chain multiple block devices
  together and extend the usable amount of storage.

- [MBRBlockDevice](TODO LINK ME)

  Mbed OS comes with support for storing partitions on disk with a Master Boot
  Record (MBR). The MBRBlockDevice provides this functionality and supports
  creating partitions at runtime or using pre-formatted partitions configured
  separately from outside the application.

- [ReadOnlyBlockDevice](TODO LINK ME)

  With the read-only block device, you can wrap a block device in a read-only
  layer. Insuring that the storage is not modified by the user of the block device.

- [ProfilingBlockDevice](TODO LINK ME)

  With the profiling block device, you can profile the quantity of erase, program,
  and read operations that are incured on a block device.

- [ObservingBlockDevice](TODO LINK ME)

  The observing block device grants the user the ability to register a callback
  on block device operations. This can be used to inspect the state of the block
  device, log different metrics, or perform some other operation.

- [ExhaustibleBlockDevice](TODO LINK ME)

  Useful for evaluating how filesystems respond to wear, the exhaustible block
  device simulates wear on another form of storage, and can be configured to
  expire blocks as necessary.

