## NVStore
NVStore is a lightweight module providing the functionality of storing data by keys in the internal flash, for security purpose.
For each item key, NVStore module provides the ability to set the item data or get it.
Newly set values are added to the flash (as in journal), with the effect of overriding the previous value for this key.
NVStore module ensures that existing data isn't harmed by power failures, during any operation.

### Flash structure
NVStore uses two Flash areas, active and non-active. Data is written to the active area, until it gets full.
When it does, garbage collection is invoked, compacting items from the active area to the non-active one,
and switching activity between areas.
Each item is kept in an entry, containing header and data, where the header holds the item key, size and CRC.
Each area must consist of one or more erasable units (sectors). 

### NVStore class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/v5.7/mbed-os-api-doxy/class_little_file_system.html)

### NVStore example

[![View code](https://www.mbed.com/embed/?url=https://github.com/armmbed/mbed-os-example-filesystem)](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-filesystem/file/8e251d9511b8/main.cpp/)
