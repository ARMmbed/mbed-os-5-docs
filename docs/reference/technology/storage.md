<h1 id="storage-tech">Storage</h1>

We designed the architecture of the Mbed OS storage solution with the following properties:

- Wear-leveling of internal and external flash storage.
- No wear-leveling for firmware, both active and future updates.
- Security applied to external storage.

## Architectural design

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/storagearch.png)<span>Mbed OS storage C++ class names (Blue indicates implementation and yellow indicates interfaces)</span></span>

Storage in Mbed OS is composed of multiple layers that stack. With these stackable layers, you can configure the storage system that is most appropriate for your needs. For example, if you only need to store small, fixed-size data, you can use TDBStore. If you need a POSIX-like API for random access of larger files, such as logs or databases, then LittleFS is a good choice. 

## Class hierarchy

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/storageclasshierarchy.png)<span>Storage class hierarchy (Blue indicates implementation classes, and yellow indicates interfaces)</span></span>

Interfaces from low-level to high-level:

- BlockDevice: Access to raw block-based storage device, such as (Q)SPI flash, SD card, EEPROM or internal flash.
- FileSystem: POSIX-style file system.
- FileHandle: POSIX-style files.
- KVStore: Key-value database.

An example of implementations of the interfaces are:

- BlockDevice.
   - QSPIBlockDevice - Block device driver for NOR-based QSPI Flash devices that support the SFDP standard. 
   - SPIFBlockDevice - Block device driver for NOR-based SPI flash devices that support SFDP. NOR-based SPI flash supports byte-sized read and writes, with an erase size of around 4 kbytes. An erase sets a block to all 1s, with successive writes clearing set bits.
   - SDBlockDevice - The SD driver uses the SDCard SPI mode of operation, which is a subset of possible SDCard functionality.
   - FlashIAPBlockDevice - Block device driver bound to the FlashIAP driver in Mbed OS for reading and writing to internal flash. Only use this driver on platforms where the FlashIAP implementation is using external flash or in conjunction with a file system with wear leveling, that can operate on a page size granularity.
   - MBRBlockDevice - Class that provides a way to manage a Master Boot Record (MBR) on a storage device, which allows you to partition the device. Without the MBR, you can still format a storage device with a file system, but including the MBR allows for future partition modifications.
   - SlicingBlockDevice - Class that provides a way to break a block device into partitions not managed by or registered with an MBR without the need to manually track offsets.
   - ChainingBlockDevice - Class that provides a way to chain multiple block devices together. You can then interact with the chained block devices as if they were a single block device of size equal to the sum of each substorage unit.
- FileSystem.
   - LittleFS - File system designed for embedded systems, specifically for microcontrollers that use external flash storage.
   - FATFS - Established disk-oriented file system that you can find on Mbed OS, Windows, Linux and macOS. Due to its age and popularity, this file system has become the standard for portable storage, such as flash drivers and SD cards.
- FileHandle.
   - File - Class that provides read and write access to files on a file system.
   - BlockDeviceFile - Class that provides read and write access to raw block device storage in the form of a FileHandle.
   - UARTSerial - The UARTSerial class provides read and write access to a device's serial hardware. It is an example of a nonstorage device that you can access as a file.
- KVStore.
   - TDBStore - Default implementation of the KVStore API. It provides static wear-leveling and quick access for when you have a small number of KV pairs.
   - FileSystemStore - Class that provides a key-value store API on top of a POSIX-like file system API.
   - SecureStore - Class that provides encryption, authentication and rollback protection on top of the KVStore API. It requires two KVStore implementations, one that provides the storage for the KV pairs and one that provides storage for the CMACs that protect KV pairs stored in the KVStore.

### Security

If you choose a file system with a POSIX-like API, then a KVStore API can still be made available through the FileSystemStore adapter class. Then, if you require security features, the SecureStore can be added on top of the layer stack. The SecureStore can only sit on top of a KVStore and cannot work on top of a POSIX-like API due to this requiring a vastly more complex design.

You can create multiple file systems in a single flash media. For instance, in a system with multiple privilege levels, the secure software partition may require its own KVStore. The application may also have a KVStore and a LittleFS instance.

SecureStore requires storage at a higher privilege level than the data for holding the CMAC of each of the data items it manages. SecureStore manages its own KVStore, which is intended to be resident in internal flash, in addition to the KVStore used for data storage, which can be on external flash. This simplifies the SecureStore's implementation by reusing existing code that achieves the required wear-leveling properties.
