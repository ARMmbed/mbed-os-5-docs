Assumptions

- Internal and external flash storage needs to be wear-leveled.
- Firmware, both active and incoming update, cannot be wear-leveled.
- Internal flash is considered secure against the level of attack threat we are targeting.
- Security only needs to be applied to external storage.

Design

Storage in Mbed OS is composed of multiple layers that stack to achieve the desired properties. The way this works is that the user chooses a storage system that is most appropriate for their needs. If only smaller, fixed size data items are going to be stored, then TDBStore makes sense. If the user needs a POSIX-like API for random access of larger files such as logs or databases, then LittleFS is a good choice. 

If a filesystem with a POSIX-like API is chosen, then a KVStore API can still be made available via the FileSystemStore adapter class. Then, if security features are required, the SecureStore can be added on top of the layer stack. The SecureStore can only sit on top of a KVStore and cannot work on top of a POSIX-like API due to this requiring a vastly more complex design.

Multiple filesystems may be created in a single flash media, if desired. For instance, in a system with multiple privilege levels, the secure software partition may require its own KVStore. The application may also have a KVStore and/or a LittleFS instance.

The SecureStore requires storage at a higher privilege level than the data for holding the CMAC of each of the data items it manages. Here, the SecureStore will manage its own KVStore which is intended to be resident in internal flash, in addition to the KVStore used for data storage which can be on external flash. This simplifies the SecureStore's implementation by reusing existing code that achieves the required wear-leveling properties.

Here's a detailed diagram of the complete layer stack using the C++ class names (Blue indicates implementation and yellow indicates interfaces):

Interfaces from low-level to high-level:

- BlockDevice: Access to raw block-based storage device such as (Q)SPI flash, SD card, EEPROM or internal flash
- FileSystem: POSIX-style filesystem
- FileHandle: POSIX-style files
- KVStore: Key-value database

An example of implementations of the interfaces are:

- BlockDevice
   - SPIFBlockDevice - Block device driver for NOR based SPI flash devices that support SFDP. NOR based SPI flash supports byte-sized read and writes, with an erase size of around 4kbytes. An erase sets a block to all 1s, with successive writes clearing set bits. More info on NOR flash can be found on wikipedia: https://en.wikipedia.org/wiki/Flash_memory#NOR_memories
   - SDBlockDevice - The purpose of this document is to describe how to use the mbed OS SDCard driver (sd-driver) so applications can read/write data to flash storage cards using the standard POSIX File API programming interface. The sd-driver uses the SDCard SPI-mode of operation which is a subset of possible SDCard functionality.
   - FlashIAPBlockDevice - Block device driver bound to the FlashIAP driver in Mbed OS for reading and writing to internal flash. This driver should only be used on platforms where the FlashIAP implementation is using external flash or in conjunction with a filesystem with wear leveling, that can operate on a page size granularity.
   - MBRBlockDevice - The MBRBlockDevice class provides a way to manage a Master Boot Record (MBR) on a storage device, which allows you to partition the device. Without the MBR, you can still format a storage device with a file system, but including the MBR will allow for future partition modifications.
   - SlicingBlockDevice - The SlicingBlockDevice class provides a way to break up a block device into partitions not managed by or registered with a MBR without the need to manually track offsets.
   - ChainingBlockDevice - The ChainingBlockDevice class provides a way to chain together multiple block devices. You can then interact with the chained block devices as if they were a single block device of size equal to the sum of each substorage unit. 
- FileSystem
   - LittleFS - The little file system is a fail-safe file system designed for embedded systems, specifically for microcontrollers that use external flash storage
   - FATFS - The FAT file system is an established disk-oriented file system that you can find on Mbed OS, Windows, Linux and Mac OS X. Due to its age and popularity, the FAT file system has become the standard for portable storage, such as flash drivers and SD cards.
- FileHandle
   - File - The File class provides read/write access to files on a file system.
   - BlockDeviceFile - The BlockDeviceFile class provides read/write access to raw block device storage in the form of a FileHandle.
   - UARTSerial - The UARTSerial class provides read/write access to a device's serial hardware. It is an example of a non-storage device which can be accessed as a file.
- KVStore
   - TDBStore - The TDBStore is the go-to implementation of the KVStore API. It provides static wear-leveling and quick access for when you have a small number of KV pairs.
   - FileSystemStore - The FileSystemStore class provides a key-value store API on top of a POSIX-like filesystem API.
   - SecureStore - The SecureStore class provides encryption, authentication, and rollback protection on top of the KVStore API. It requires two KVStore implementations, the first provides the storage for the KV pairs, while the second provides storage for the CMACs used to protect KV pairs stored in the KVStore. The second should be stored in a secure location, but may be much smaller than the first.

Class hierarchy

Here's a complete summary of the storage class hierarchy after the addition of the KV classes. Blue indicates implementation classes, and yellow indicates interfaces:

KVStore

The newest addition to the storage design is the KVStore API. The KVStore API provides a simple interface for storing fixed-size key-value pairs on a underlying block device. In this API a "key" is defined as a null terminated C string, and a "value" is a fixed size opaque binary blob.

Note that KVStore refers only to the API, not the implementation. Like the BlockDevice API, there are multiple implementations of the KVStore API that provide various features and functionality.

For storage, the go-to KVStore implementation is the TDBStore. The TDBStore provides a small storage solution for providing KV access on block devices. It provides static wear-leveling and quick access for when you have a small number of KV pairs.

Other KVStore implementations include the SecureStore, a KVStore implementation that builds on top of other KVStores to provide security in the form of encryption, authentication, and roll-back protection, and the FileSystemStore, a KVStore implementation that provides KV access on top of the FileSystem API, which is suitible for storing larger sets of KV pairs.

The KVStore interface provides the following interface. Note for KVStore::iterator_open(), the pattern is simply a prefix, or starts-with, match.

Global Key Value API

A parallel key-value API will be provided as global C-style functions. This API will perform a limited type of mapping of partition or mount point names present in the keys. For each of the APIs defined in KVStore, the global version will extract a partition prefix from the key name. The prefix must be in the form "/partition/key-name". Then a lookup will be performed to map the partition name to a concrete KVStore instance, and the API call routed to that instance. The routed key name will have the partition prefix stripped, leaving only "key-name".

A default KVStore instance can be set. If the key name does not begin with a slash, then the entire key will be passed to the default KVStore. Note that only the first 2 slashes are relevant in the key name.

Here is the definition of the key-value C API. Note that these functions are global and rely on the above partition prefixes to identify specific KVStore interfaces:

File and partition instantiation

To keep middleware code such as MCC simple, we need a way to cleanly reference storage that exists in any of the supported filesystem, or even raw flash pages. This can be handled through the existing FileSystem and File interfaces. External media already supports a partition table (MBR). We need a partition table for internal flash, as well. However, it could be defined in the configuration system for a board support package and implemented through SlicingBlockDevices rather than residing on the media. The configuration should be defined by a target but able to be overridden by an application or custom target that matches a derivative design that may have started from a target (development board). 
