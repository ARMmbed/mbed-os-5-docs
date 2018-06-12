## BlockDevice

<span class="images">![](https://os-doc-builder.test.mbed.com/docs/v5.9/mbed-os-api-doxy/class_block_device.png)<span>BlockDevice class hierarchy</span></span>

The BlockDevice API provides an interface for access to block-based storage. You can use a block device to back a full [file system](https://os.mbed.com/docs/v5.9/reference/contributing-storage.html#contributing-filesystem) or write to it directly.

The most common types of block-based storage are different forms of flash, but the BlockDevice API can support many different forms of storage, such as SD cards, spinning disks, heap backed storage and so on.

#### Block device operations

A block device can perform three operations:

- Read a region of data from storage.
- Erase a region of data in storage.
- Program a region of data that has previously been erased.

A full write to a block device involves first erasing the region of memory you plan to program and then programming the data to the region of memory. The reason for this separation is that block devices can have different limitations for erasing and writing to regions on the device.

#### Block device blocks

Block devices are byte addressable but operate in units of "blocks". There are three types of blocks for the three types of block device operations: read blocks, erase blocks and program blocks.

<span class="notes">**Note:** For many devices, erase blocks can be large (for example, 4 KiB for SPI flash). As a result, we discourage storing an entire erase block in RAM. Instead, we suggest first erasing a block and then programming in units of the program block.</span>

![blockdevicesectors](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/blockdevice_block_size.png)

#### Erased blocks

The state of an erased block is **undefined**. The data stored on the block isn't decided until you program the block. This allows the widest range of support for different types of storage.

![blockdevicesectors](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/blockdevice_erase_block.png)

### BlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/v5.9/mbed-os-api-doxy/class_block_device.html)

### BlockDevice example

```
/* mbed Microcontroller Library
 * Copyright (c) 2006-2013 ARM Limited
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
#include "mbed.h"
#include <stdio.h>
#include <algorithm>

// Block devices
#include "SPIFBlockDevice.h"
#include "DataFlashBlockDevice.h"
#include "SDBlockDevice.h"
#include "HeapBlockDevice.h"


// Physical block device, can be any device that supports the BlockDevice API
SPIFBlockDevice bd(
        MBED_CONF_SPIF_DRIVER_SPI_MOSI,
        MBED_CONF_SPIF_DRIVER_SPI_MISO,
        MBED_CONF_SPIF_DRIVER_SPI_CLK,
        MBED_CONF_SPIF_DRIVER_SPI_CS);


// Entry point for the example
int main() {
    printf("--- Mbed OS block device example ---\n");

    // Initialize the block device
    printf("bd.init()\n");
    int err = bd.init();
    printf("bd.init -> %d\n", err);

    // Get device geometry
    bd_size_t read_size    = bd.get_read_size();
    bd_size_t program_size = bd.get_program_size();
    bd_size_t erase_size   = bd.get_erase_size();
    bd_size_t size         = bd.size();

    printf("--- Block device geometry ---\n");
    printf("read_size:    %lld B\n", read_size);
    printf("program_size: %lld B\n", program_size);
    printf("erase_size:   %lld B\n", erase_size);
    printf("size:         %lld B\n", size);
    printf("---\n");

    // Allocate a block with enough space for our data, aligned to the
    // nearest program_size. This is the minimum size necessary to write
    // data to a block.
    size_t buffer_size = sizeof("Hello Storage!") + program_size-1;
    buffer_size = buffer_size - (buffer_size % program_size);
    char *buffer = new char[buffer_size];

    // Read what is currently stored on the block device. We haven't written
    // yet so this may be garbage
    printf("bd.read(%p, %d, %d)\n", buffer, 0, buffer_size);
    err = bd.read(buffer, 0, buffer_size);
    printf("bd.read -> %d\n", err);

    printf("--- Stored data ---\n");
    for (size_t i = 0; i < buffer_size; i += 16) {
        for (size_t j = 0; j < 16; j++) {
            if (i+j < buffer_size) {
                printf("%02x ", buffer[i+j]);
            } else {
                printf("   ");
            }
        }

        printf(" %.*s\n", buffer_size - i, &buffer[i]);
    }
    printf("---\n");

    // Update buffer with our string we want to store
    strncpy(buffer, "Hello Storage!", buffer_size);

    // Write data to first block, write occurs in two parts,
    // an erase followed by a program
    printf("bd.erase(%d, %lld)\n", 0, erase_size);
    err = bd.erase(0, erase_size);
    printf("bd.erase -> %d\n", err);

    printf("bd.program(%p, %d, %d)\n", buffer, 0, buffer_size);
    err = bd.program(buffer, 0, buffer_size);
    printf("bd.program -> %d\n", err);

    // Clobber the buffer so we don't get old data
    memset(buffer, 0xcc, buffer_size);

    // Read the data from the first block, note that the program_size must be
    // a multiple of the read_size, so we don't have to check for alignment
    printf("bd.read(%p, %d, %d)\n", buffer, 0, buffer_size);
    err = bd.read(buffer, 0, buffer_size);
    printf("bd.read -> %d\n", err);

    printf("--- Stored data ---\n");
    for (size_t i = 0; i < buffer_size; i += 16) {
        for (size_t j = 0; j < 16; j++) {
            if (i+j < buffer_size) {
                printf("%02x ", buffer[i+j]);
            } else {
                printf("   ");
            }
        }

        printf(" %.*s\n", buffer_size - i, &buffer[i]);
    }
    printf("---\n");

    // Deinitialize the block device
    printf("bd.deinit()\n");
    err = bd.deinit();
    printf("bd.deinit -> %d\n", err);

    printf("--- done! ---\n");
}
```
