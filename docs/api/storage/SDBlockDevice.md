# SDBlockDevice

<span class="images">![](https://os.mbed.com/docs/v5.10/mbed-os-api-doxy/class_s_d_block_device.png)<span>SDBlockDevice class hierarchy</span></span>

You can use the Mbed OS SD card block device, so applications can read and write data to flash storage cards using the standard POSIX File API programming interface. Applications use the FAT filesystem and SD block device components to persistently store data on SDCards. The SD block device uses the SD card SPI-mode of operation, which is a subset of possible SD card functionality.

To configure this class, please see our [BlockDevice configuration documentation](/docs/v5.10/reference/configuration-storage.html#blockdevice-default-configuration).

## Mbed OS file system software component stack


    ------------------------
    |                      |
    |    Application       |        // This application uses the POSIX File API
    |                      |        // to read/write data to persistent storage backends.
    ------------------------

    ------------------------        // POSIX File API (ISO).

    ------------------------
    |                      |
    |     libc             |        // The standard c library implementation
    |                      |        // for example, newlib.
    ------------------------

    ------------------------        // sys_xxx equivalent API.

    ------------------------
    |                      |
    |  mbed_retarget.cpp   |        // Target specific mapping layer.
    |                      |
    ------------------------

    ------------------------        // File system Upper Edge API.

    ------------------------
    |                      |
    |     File System      |        // File system wrappers and implementation.
    |                      |
    ------------------------

    ------------------------        // FS Lower Edge API (Block Store Interface).

    ------------------------
    |    Block API         |
    |  Device Block device |        // The SD card block device, for example.
    |  e.g. SDBlockDevice  |
    ------------------------

    ------------------------        // SPI.h interface.

    ------------------------
    |                      |
    |       SPI            |        // SPI subsystem (C++ classes and C-HAL implementation).
    |                      |
    ------------------------

    Figure 1. Mbed OS generic architecture of filesystem software stack.

The figure above shows the Mbed OS software component stack used for data storage on the SD card:

- At the top level is the application component, which uses the standard POSIX File API to read and write application data to persistent storage.
- The newlib standard library (libc) `stdio.h` interface (POSIX File API) implementation is optimized for resource-limited embedded systems.
- `mbed_retarget.cpp` implements the libc backend file OS handlers and maps them to the file system.
- The file system code (hosted in `mbed-os`) is composed of 2 parts: the FAT file system implementation code and the file system classes that present a consistent API to the retarget module for different (third-party) file system implementations.
- The Block API. The SDCard block device is a persistent storage block device.
- The SPI module provides the Mbed OS SPI API.

## SDBlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.10/mbed-os-api-doxy/class_s_d_block_device.html)

## SDBlockDevice example application

The following sample code illustrates how to use the SD block device API:

``` cpp
#include "mbed.h"
#include "SDBlockDevice.h"

// Instantiate the SDBlockDevice by specifying the SPI pins connected to the SDCard
// socket. The PINS are:
//     MOSI (Master Out Slave In)
//     MISO (Master In Slave Out)
//     SCLK (Serial Clock)
//     CS (Chip Select)
SDBlockDevice sd(MBED_CONF_SD_SPI_MOSI, MBED_CONF_SD_SPI_MISO, MBED_CONF_SD_SPI_CLK, MBED_CONF_SD_SPI_CS);
uint8_t block[512] = "Hello World!\n";

int main()
{
    // call the SDBlockDevice instance initialisation method.
    if ( 0 != sd.init()) {
        printf("Init failed \n");
        return -1;
    }
    printf("sd size: %llu\n",         sd.size());
    printf("sd read size: %llu\n",    sd.get_read_size());
    printf("sd program size: %llu\n", sd.get_program_size());
    printf("sd erase size: %llu\n",   sd.get_erase_size());

    // set the frequency
    if ( 0 != sd.frequency(5000000)) {
        printf("Error setting frequency \n");
    }

    if ( 0 != sd.erase(0, sd.get_erase_size())) {
        printf("Error Erasing block \n");
    }

    // Write some the data block to the device
    if ( 0 == sd.program(block, 0, 512)) {
        // read the data block from the device
        if ( 0 == sd.read(block, 0, 512)) {
            // print the contents of the block
            printf("%s", block);
        }
    }

    // call the SDBlockDevice instance de-initialisation method.
    sd.deinit();
}
```

## Related content

- [BlockDevice configuration](/docs/v5.10/reference/configuration-storage.html#blockdevice-default-configuration).
