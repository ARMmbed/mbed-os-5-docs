## FlashIAPBlockDevice

<span class="images">![](https://os.mbed.com/docs/v5.10/mbed-os-api-doxy/class_flash_i_a_p_block_device.png)<span>FlashIAPBlockDevice class hierarchy</span></span>

The flash IAP block device is a block device driver built on top of the FlashIAP API. This is enabled using the internal flash memory as a block device. The read size, write size and erase size may differ, depending on the flash chip. Use the FlashIAPBlockDevice `get` function to discover those sizes.

Additional notes:

1. Use this driver on platforms where the FlashIAP implementation uses external flash or in conjunction with a file system with wear leveling, that can operate on a page size granularity.
1. The FlashIAP may freeze code execution for a long period of time while writing to flash. Not even high-priority IRQs are allowed to run, which may interrupt background processes.

### FlashIAPBlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.10/mbed-os-api-doxy/class_flash_i_a_p_block_device.html)

### FlashIAPBlockDevicesBlockDevice example:

``` cpp
#include "mbed.h"
#include "FlashIAPBlockDevice.h"

// Create flash block device.
FlashIAPBlockDevice bd;

int main() {
    printf("FlashIAPBlockDevice test\n");

    // Initialize the FLASHIAP device and print the memory layout
    bd.init();
    printf("Flash block device size: %llu\n",         bd.size());
    printf("Flash block device read size: %llu\n",    bd.get_read_size());
    printf("Flash block device program size: %llu\n", bd.get_program_size());
    printf("Flash block device erase size: %llu\n",   bd.get_erase_size());

    // Write "Hello World!" to the first block
    char *buffer = (char*)malloc(bd.get_erase_size());
    sprintf(buffer, "Hello World!\n");
    bd.erase(0, bd.get_erase_size());
    bd.program(buffer, 0, bd.get_erase_size());

    // Read back what was stored
    bd.read(buffer, 0, bd.get_erase_size());
    printf("%s", buffer);

    // Deinitialize the device
    bd.deinit();
}
```
