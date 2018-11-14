### Declaring a file system

The [FileSystem](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_file_system.html) class provides the core API for file system operations. You must provide a block device to back the file system, which provides the raw storage for the file system. When you declare a file system with a name, you can open files on the file system through the `open` and `fopen` functions or through the File class's `open` function.

#### File systems

- [**LittleFileSystem**](littlefilesystem.html) - The little file system (LittleFS) is a fail-safe file system we designed for embedded systems, specifically for microcontrollers that use flash storage.

  - **Bounded RAM/ROM** - This file system works with a limited amount of memory. It avoids recursion and limits dynamic memory to configurable buffers.

  - **Power-loss resilient** - We designed this for operating systems that may have random power failures. It has strong copy-on-write guarantees and keeps storage on disk in a valid state.

  - **Wear leveling** - Because the most common form of embedded storage is erodible flash memories, this file system provides a form of dynamic wear leveling for systems that cannot fit a full flash translation layer.

- [**FATFileSystem**](fatfilesystem.html) - The FAT file system is an established disk-oriented file system that you can find on most operating systems, including Windows, Linux, macOS and Mbed OS.

  - **Portable** - Due to its support across operating systems, the FAT file system provides access to storage from both the embedded system and your PC.

  - **Embedded** - Built on the ChanFS project, the FAT file system is optimized for embedded systems.

- **LocalFileSystem** - The LocalFileSystem is a symbiotic file system that connects to the Mbed board's interface chip if the interface chip has built-in storage. The features available on the LocalFileSystem is dependent on the board's interface chip. **Note:** The LocalFileSystem is only available on the LPC1768 and LPC11U24.

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

#### The FATFileSystem

The FAT file system is an established disk-oriented file system that you can find on Mbed OS, Windows, Linux and macOS. Due to its age and popularity, the FAT file system has become the standard for portable storage, such as flash drives and SD cards.

##### Portable

The primary feature of the FAT file system is its portability. With support across PC operating systems, the FAT file system lets you access storage from both the embedded system your PC. This gives users a way to get information onto and off of the device.

##### Embedded

The Mbed OS FAT file system is built on the ChanFS project. It is optimized for embedded systems and is one of the smallest FAT file system implementations.

#### C++ classes

The FileSystem class provides the core user C++ API. Mbed OS provides [File](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_file.html) and [Dir](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_dir.html) classes that represent files and directories in a C++ API.
