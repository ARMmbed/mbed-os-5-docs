### Block Devices

The block device API provides an interface for access to block-based storage. You can use a block device to back a full <a href="https://os.mbed.com/docs/v5.6/reference/contributing-storage.html#contributing-filesystem" target="_blank">file system</a> or write to it directly.

#### BlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_block_device.html)

<a href="https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/bd/BlockDevice.h" target="_blank">C++ API Reference</a>

#### SD card block device example

Block device for SD cards.

[![View code](https://www.mbed.com/embed/?url=https://github.com/armmbed/sd-driver)](https://github.com/ARMmbed/sd-driver/blob/master/SDBlockDevice.cpp)

#### Heap block device example

Block device the heap backs for quick testing.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/bd/HeapBlockDevice.h)](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/bd/HeapBlockDevice.h)

#### Block Device NOR-based SPI example

Block device for NOR-based SPI flash devices.

[![View code](https://www.mbed.com/embed/?url=https://github.com/armmbed/spiflash-driver)](https://github.com/ARMmbed/spif-driver/blob/master/SPIFBlockDevice.cpp)

#### EEPROM-based I2C block device example

Block device for EEPROM-based I2C devices.

[![View code](https://www.mbed.com/embed/?url=https://github.com/armmbed/i2ceeprom-driver)](https://github.com/ARMmbed/i2cee-driver/blob/master/I2CEEBlockDevice.cpp)
