#### Block Devices

TODO: section on testing
TODO: api embed, not header files

The block device API provides an interface for access to block-based storage. You can use a block device to back a full [file system](filesystem.md) or write to it directly.

##### Block Device class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/vignesh/en/latest/api/classBlockDevice.html)

[C++ API Reference](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/bd/BlockDevice.h)

##### SD card block device example

Block device for SD cards.

[![View code](https://www.mbed.com/embed/?url=https://github.com/armmbed/sd-driver)](https://github.com/armmbed/sd-driver)

##### Heap block device example

Block device the heap backs for quick testing.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/bd/HeapBlockDevice.h)](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/bd/HeapBlockDevice.h)

##### Block Device NOR-based SPI example

Block device for NOR-based SPI flash devices.

[![View code](https://www.mbed.com/embed/?url=https://github.com/armmbed/spiflash-driver)](https://github.com/armmbed/spiflash-driver)

##### EEPROM-based I2C block device example

Block device for EEPROM-based I2C devices.

[![View code](https://www.mbed.com/embed/?url=https://github.com/armmbed/i2ceeprom-driver)](https://github.com/armmbed/i2ceeprom-driver)
