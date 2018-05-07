# StorageLite

StorageLite provides a simple API of set and get data or reduced POSIX API of Open-write-close and open-read-close. It provides very fast write and read functions, power failure resilient, strong security and built-in backup and factory reset support.

Usages: Ideally for keeping credentials and cryptographic keys, application settings, application states, small application data to be sent to servers.

Hardware: Designed for external NOR flash, can work also on internal flash and with additional block devices also on SD cards.

## Description

StorageLite is a light weight filesystem storage module for files in external memory. Files are stored and accessed by file-name. StorageLite has several main advantages, when compared to other storage modules:
+	High performance: a small RAM table is used to quickly access files and retrieve data
+ Security: Secured storage module that supports the following features, among others:
  - Integrity by using file Authentication
  - Confidentiality by using file Encryption
  - Rollback Protection
+ Wear Level: StorageLite stores files in a sequential order. This concept makes use of the entire external memory space. It is optimized for NOR flash that supports a limited number of erase per sector.
+ Backup: featuring built-in backup and factory reset support.
+	Low RAM memory footprint: 8 Bytes of RAM is used for indexing each file

[DESIGN.md](storagelite/DESIGN.md) - DESIGN.md contains the detailed design description of StorageLite

[API Prototype](storagelite/StorageLite.h) -  The full interface can be found under `StorageLite.h`.

## Flash Memory
StorageLite is optimized for NOR flash memory. It is based on dividing the allocated memory storage to areas: Active and Standby. Data is written to the active area until it becomes full. When the active area becomes full, an internal garbage collection mechanism moves only the updated relevant files to the standby area, and switches between the active and standby areas. The new standby area is then erased.
This  concept which is in the heart of StorageLite design is ideal for low wear leveling of the memory, but it comes with a price of utilizing half of the external memory size.

## APIs
StorageLite can either be used with set/get based APIs or it can be defined as StorageLiteFS and  work with a limited POSIX open-write/read-close based API (only a **single** write or read operation is allowed)

### StorageLite
- init: Bind StorageLite to a specific Block Device, construct and initialize StorageLite module elements
- deinit: Deinitialize StorageLite module
- set: Save data into persistent storage by file name
- get: Retrieve file data from storage after authenticating it
- remove: Remove an existing file from storage
- get_file_size: returns the file size after authenticating the data
- file_exist: Verifies that file exists and authenticates it.
- get_file_flags: returns files supported features (such as: RB protection, encryption, factory-reset)
- get_first/next: provides the ability to iterate through existing files, starting from the first one.
- factory_reset: Return storage to contain only files that are backed up. And return those files to their backup version.

### StorageLiteFS
- mount/unmount: Attach/Detach a block device to/from the file systems
- open/close: Establish the connection between a file and a file descriptor
- writing data to the file associated with the opened file descriptor (replacing existing data - if exists). Write can be called only once
- Read: reads data from the file associated with the open file descriptor. Read can be called only once
- Remove: deletes a file name from the file system
- Reformat: clearing a filesystem, results in an empty and mounted filesystem

## Usage

### Setup And Configuration (TBD)
Enabling StorageLite and configuring it for your board
TBD (define standby/active areas addresses and size, define max num of files, etc..)

### Using StorageLite
First define a Block Device and define the maximum number of files you want StorageLite to support. Next, create an instance of StorageLite and initialize it with the above Block device and max files setup. Then you can start saving new files and getting their data.
``` c++
    #define MAX_NUM_OF_FILES 50
    SPIFBlockDevice spif(PTE2, PTE4, PTE1, PTE5);
    StorageLite sl;
    sl.init(&spif, MAX_NUM_OF_FILES);
```

### Using StorageLiteFS
First define the Block Device you want StorageLiteFS to use, and create an instance of StorageLite. Next, create StorageLiteFS instance, giving it the name under which it will be cataloged in the filesystem tree, the StorageLite instance it will use and its feature flags. Finally, mount the selected block device onto the StorageLiteFS instance.Now you can start opening new files for write and read.
``` c++
    #define DEFAULT_FLAGS ROLLBACK_DISABLED & ENCRYPTION_ENABLED
    SPIFBlockDevice spif(PTE2, PTE4, PTE1, PTE5);
    StorageLite sl;
    StorageLiteFS slfs("/sl", &sl, DEFAULT_FLAGS);
    slfs.mount(&spif);
```

### Testing StorageLite (TBD)
Run the StorageLite functionality test with the `mbed` command as following:
```mbed test -n features-storagelite-tests-storagelite-functionality```
