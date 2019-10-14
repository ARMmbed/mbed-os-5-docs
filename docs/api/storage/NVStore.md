# NVStore

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/class_n_v_store.png)<span>NVStore class hierarchy</span></span>

NVStore is a lightweight module that stores data by keys in the internal flash for security purposes. For each item key, the NVStore module provides the ability to set the item data or get it. Newly added values are added to the end of the existing data, superseding the previous value that was there for the same key. The NVStore module ensures that power failures don't harm existing data during any operation.

## Flash structure

NVStore uses two Flash areas, active and nonactive. Each area must consist of at least one erasable unit (sector). Data is written to the active area until it becomes full. When it does, garbage collection is invoked. This compacts items from the active area to the nonactive one and switches activity between areas. Each item is kept in an entry containing a header and data, where the header holds the item key, size and CRC.

Unless specifically configured by the user, NVStore selects the last two flash sectors as its areas, with the minimum size of 4KBs. This means that if the sectors are smaller, NVStore uses a few continuous ones for each area. If the automatically selected sectors do not fit your flash configuration, you can override this by setting the addresses and sizes of both areas in `mbed_app.json` for each board.

## NVStore class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/class_n_v_store.html)

## NVStore example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-nvstore)](https://github.com/ARMmbed/mbed-os-example-nvstore/blob/mbed-os-5.14/main.cpp)

## Related content

- [Storage configuration](../reference/storage.html).
