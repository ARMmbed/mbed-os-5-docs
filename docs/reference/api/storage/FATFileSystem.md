## FATFileSystem

<span class="images">![](https://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_f_a_t_file_system.png)<span>FATFileSystem class hierarchy</span></span>

The FAT file system is a well-known and established disk oriented file system that you can find on Mbed OS and some lesser known operating systems such as Windows, Linux, and OSX. Due to its age and popularity, the FAT file system has become the de facto standard for forms of portable storage, such as flash drivers and SD cards.

  - **Portable** - Due to its nearly universal support across OSs, the FAT file system provides and easy way to access storage from both the embedded system and a user's PC.

  - **Embedded** - Built on the well-known ChanFS project, the FAT file system has been heavily optimized for embedded systems.

For additional information, please see the [storage overview page](/docs/development/reference/storage.html#declaring-a-file-system).

### Use cases

The main reason to use the FAT file system is for its usefulness on portable storage. Because of this, most applications using FAT will likely use it in conjunction with an SD card.

The first step to using the FAT file system will be formatting storage with FAT. This can be performed on a PC with the native format command, or it can be performed on Mbed OS with the `format` function.

**Note:** The FAT file system requires at minimum 256 erase blocks. You can find the number of blocks on a block device by dividing the block device's size by its erase size.

The FAT file system does support external flash, however it must allocate a full erase block for internal operations, which can get quite large for some forms of flash. If RAM consumption becomes a problem, we suggest switching to LittleFS. Fortunately, the Mbed OS file system APIs make switching file systems an easy task. One common strategy is to use the FAT file system for debugging, and switch to LittleFS when the application becomes stable.

### Usage

Instantiate the `FATFileSystem` class with a block device and file path.

The API that this presents is the standard Mbed OS file system API. Once declared, Mbed OS provides the retargeting layer for the standard C library.

The FAT file system can be easily swapped in place with other Mbed OS file systems and is a great method for prototyping applications.

### FATFileSystem class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_f_a_t_file_system.html)

### FATFileSystem example

[![View code](https://www.mbed.com/embed/?url=https://github.com/armmbed/mbed-os-example-
filesystem)](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-filesystem/file/
8e251d9511b8/main.cpp)

### Related content

- [Storage configuration](configuration-storage.html).
