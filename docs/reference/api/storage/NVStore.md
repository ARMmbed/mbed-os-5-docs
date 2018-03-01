## NVStore

NVStore is a lightweight module that stores data by keys in the internal flash for security purposes. For each item key, the NVStore module provides the ability to set the item data or get it. Newly added values are added to the end of the existing data, superseding the previous value that was there for the same key. The NVStore module ensures that power failures don't harm existing data during any operation.

### Flash structure

NVStore uses two Flash areas, active and nonactive. Each area must consist of at least one erasable unit (sector). Data is written to the active area until it becomes full. When it does, garbage collection is invoked. This compacts items from the active area to the nonactive one and switches activity between areas. Each item is kept in an entry containing a header and data, where the header holds the item key, size and CRC.

### NVStore class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/v5.7/mbed-os-api-doxy/class_little_file_system.html)

### NVStore example

[![View code](https://www.mbed.com/embed/?url=https://github.com/armmbed/mbed-os-example-nvstore)](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-filesystem/file/8e251d9511b8/main.cpp/)
