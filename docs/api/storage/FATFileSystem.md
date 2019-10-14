# FATFileSystem

<span class="images">![](http://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_f_a_t_file_system.png)<span>FATFileSystem class hierarchy</span></span>

The FAT file system is an established disk-oriented file system that you can find on Mbed OS, Windows, Linux and macOS. Due to its age and popularity, the FAT file system has become the standard for portable storage, such as flash drivers and SD cards.

  - **Portable** - Due to its nearly universal support across operating systems, the FAT file system provides access to storage from both the embedded system and your PC.

  - **Embedded** - Built on the ChanFS project, the FAT file system is optimized for embedded systems.

For additional information, please see the [storage overview page](storage.html#declaring-a-file-system).

## Use cases

The main reason to use the FAT file system is its usefulness on portable storage. Because of this, most applications using FAT in conjunction with an SD card.

The first step to using the FAT file system is formatting storage with FAT. You can do this on a PC with the native format command or on Mbed OS with the `format` function.

<span class="notes">**Note:** The FAT file system requires at minimum 256 erase blocks. You can find the number of blocks on a block device by dividing the block device's size by its erase size.</span>

The FAT file system supports external flash; however, it must allocate a full erase block for internal operations, which can become large for some forms of flash. If RAM consumption becomes a problem, we suggest switching to LittleFileSystem. The Mbed OS file system APIs make switching file systems a straightforward task. One common strategy is to use the FAT file system for debugging and switch to LittleFileSystem when the application becomes stable.

The FAT file system is thread safe. Although the FAT file system is built on the ChanFS project, synchronizing in the C++ layer allows you to use the C++ RTOS APIs directly.

## Usage

Instantiate the `FATFileSystem` class with a block device and file path.

The API that this presents is the standard Mbed OS file system API. Once declared, Mbed OS provides the retargeting layer for the standard C library.

You can swap the FAT file system in place with other Mbed OS file systems, which is a good method for prototyping applications.

To configure this class, please see the [FileSystem configuration documentation](../reference/storage.html#filesystem-default-configuration).

## FATFileSystem class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_f_a_t_file_system.html)

## FATFileSystem example

[![View code](https://www.mbed.com/embed/?url=https://github.com/armmbed/mbed-os-example-filesystem/)](https://github.com/ARMmbed/mbed-os-example-filesystem/blob/mbed-os-5.14/main.cpp)

## Related content

- [Storage configuration](../reference/storage.html).
- [LittleFileSystem](littlefilesystem.html).
- [Storage overview](storage.html#declaring-a-file-system).
