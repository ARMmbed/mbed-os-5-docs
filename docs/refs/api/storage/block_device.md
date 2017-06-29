### Block Devices

The block device API provides an interface for access to block-based storage. You can use a block device to back a full [file system](filesystem.md) or write to it directly.

You can find the full C++ API [here](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/bd/BlockDevice.h).

#### Example

Here is an example that uses a block device:

[SD block device example](https://github.com/ARMmbed/sd-driver/blob/master/README.md)

#### Block device operations

A block device can perform three operations on a block in a device:

- Read a block from storage.
- Erase a block in storage.
- Program a block that has previously been erased.

Note: The state of an erased block is undefined. NOR flash devices typically set an erased block to all 0xff, but for some block devices such as the SD card, erase is a NOOP. If a deterministic value is required after an erase, the consumer of the block device must verify this.

#### Block sizes

Some storage technologies have different sized blocks for different operations. For example, NAND flash can be read and programmed in 256-byte pages, but must be erased in 4-kilobyte sectors.

Block devices indicate their block sizes through the `get_read_size`, `get_program_size` and `get_erase_size` functions. The erase size must be a multiple of the program size, and the program size must be a multiple of the read size. Some devices may even have a read/program size of a single byte.

As a rule of thumb, you can use the erase size for applications that use a single block size (for example, the FAT file system).

#### Utility block devices

mbed OS contains several utility block devices to give you better control over the allocation of storage.

- With the [slicing block device](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/bd/SlicingBlockDevice.h), you can partition storage into smaller block devices that you can use independentally.
- With the [chaining block device](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/bd/ChainingBlockDevice.h), you can chain multiple block devices together and extend the usable amount of storage.
- mbed OS comes with support for storing partitions on disk with a [Master Boot Record (MBR)](https://en.wikipedia.org/wiki/Master_boot_record). The [MBR block device](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/bd/MBRBlockDevice.h) provides this functionality and supports creating partitions at runtime or using preformatted partitions configured separately from outside the application.

#### Example block devices

- [SDBlockDevice](https://github.com/armmbed/sd-driver) - Block device for SD cards.
- [SPIFBlockDevice](https://github.com/armmbed/spiflash-driver) - Block device for NOR-based SPI flash devices.
- [I2CEEBlockDevice](https://github.com/armmbed/i2ceeprom-driver) - Block device for EEPROM-based I2C devices.
- [HeapBlockDevice](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/bd/HeapBlockDevice.h) - Block device the heap backs for quick testing.
