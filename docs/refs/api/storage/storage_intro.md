### Storage

The storage APIs present in Arm Mbed OS are:

* [File system](filesystem.md): a common interface for using file systems on block devices.
* [Block device](block_device.md): a common interface for block-based storage devices.

##### Declaring a file system

The [FileSystem](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/FileSystem.h) class provides the core API for file system operations. You must provide a block device to back the file system. When you declare a file system with a name, you can open files on the file system through standard POSIX functions (see [open](http://pubs.opengroup.org/onlinepubs/009695399/functions/open.html) or [fopen](http://pubs.opengroup.org/onlinepubs/9699919799/functions/fopen.html).

Existing file systems:

The [FAT file system](https://github.com/ARMmbed/mbed-os/tree/master/features/filesystem/fat) is a standard file system.

The [BlockDevice](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/bd/BlockDevice.h) class provides the underlying API for representing block-based storage that can be used to back a file system. Mbed OS provides standard interfaces for the more common storage media, and you can extend the BlockDevice class to provide support for unsupported storage.

Additionally, two utility block devices give you better control over how storage is allocated. The [slicing block device](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/bd/SlicingBlockDevice.h) allows you to partition storage into smaller block devices that you can use independently, and the [chaining block device](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/bd/ChainingBlockDevice.h) allows you to chain multiple block devices together and extend the usable amount of storage.

Note: Some file systems may provide a format function for cleanly initializing a file system on an underlying block device or require external tools to set up the file system before the first use.

##### Partitioning

Partitioning allows you to split a block device among multiple storage users such that the split is portable across multiple systems. Partitioning also allows you to have multiple file systems that you can mount on one disk from both Mbed OS devices and host computers. The primary partitioning scheme that Mbed OS supports is the Master Boot Record (MBR).

Note: File system partitioning is not required if there is only one file system present.

##### C++ classes

The [FileSystem](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/FileSystem.h) class provides the core user interface with general functions that map to their global POSIX counterparts. Mbed OS provides [File](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/File.h) and [Dir](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/Dir.h) classes that represent files and directories in a C++ API that uses object-oriented features in C++.

To implement a new file system in Mbed OS, an implementor just needs to provide the abstract functions in the file system interface. The [FAT file system](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/fat/FATFileSystem.cpp) provides an excellent example, you can find tests of the POSIX API [here](https://github.com/ARMmbed/sd-driver/tree/master/features/TESTS/filesystem).

A minimal file system needs to provide the following functions:

- file open
- file close
- file read
- file write
- file seek

Here is the full API that a filesystem may implement:

[![View code](https://www.mbed.com/embed/?type=library)](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/FileSystem.h#L205)

##### Block device operations

A block device can perform three operations on a block in a device:

- Read a block from storage.
- Erase a block in storage.
- Program a block that has previously been erased.

<span class="notes">**Note:** The state of an erased block is undefined. NOR flash devices typically set an erased block to all 0xff, but for some block devices such as the SD card, erase is a NOOP. If a deterministic value is required after an erase, the consumer of the block device must verify this.</span>

##### Block sizes

Some storage technologies have different sized blocks for different operations. For example, NAND flash can be read and programmed in 256-byte pages, but must be erased in 4-kilobyte sectors.

Block devices indicate their block sizes through the `get_read_size`, `get_program_size` and `get_erase_size` functions. The erase size must be a multiple of the program size, and the program size must be a multiple of the read size. Some devices may even have a read/program size of a single byte.

As a rule of thumb, you can use the erase size for applications that use a single block size (for example, the FAT file system).

##### Utility block devices

Arm Mbed OS contains several utility block devices to give you better control over the allocation of storage.

- With the [slicing block device](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/bd/SlicingBlockDevice.h), you can partition storage into smaller block devices that you can use independently.
- With the [chaining block device](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/bd/ChainingBlockDevice.h), you can chain multiple block devices together and extend the usable amount of storage.
- Mbed OS comes with support for storing partitions on disk with a [Master Boot Record (MBR)](https://en.wikipedia.org/wiki/Master_boot_record). The [MBR block device](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/bd/MBRBlockDevice.h) provides this functionality and supports creating partitions at runtime or using pre-formatted partitions configured separately from outside the application.
