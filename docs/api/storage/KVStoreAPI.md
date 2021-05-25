# KVStore

<span class="tips">**Tip:** This API replaces the deprecated NVStore API.</span>

<span class="images">![](http://os.mbed.com/docs/v6.11/mbed-os-api-doxy/classmbed_1_1_k_v_store.png)<span>KVStore class hierarchy</span></span>

The KVStore API is a common get/set API implemented by several classes. It allows flexibility in the configuration of a storage solution that you can build by allocating several combinations of objects. For example, SecureStore can hold a TDBStore or a FileSystemStore, both implementing the KVStore API, without any change in functionality.

Developers should use the static global KVStore API when possible, to use the flexibility of KVStore configuration.

It is also possible to instantiate single objects of the classes detailed below and use the KVStore class API directly. The KVStore API presents additional functionality not present in the global API, such as incremental set (`set_start`, `set_add_data` and `set_finalize`) and incremental get (parameter offset in function `get`). You must use these APIs with caution because two calls to `set_start` result in the second call to `set_start` being held pending on a mutex until `set_finalize` is called.

Classes implementing KVStore API:

- Tiny Database Storage (TDBStore): A lightweight module that stores data on a block device. It is part of the KVStore class family, so it supports the get/set interface. It is designed to optimize performance (speed of access), reduce wearing of the storage and minimize storage overhead. It is also resilient to power failures.

   - Requirements and assumptions: TDBStore assumes that the underlying block device is fully dedicated for it (starting offset 0). If you want to dedicate only a part of the device to TDBStore, then use a sliced block device, typically with `SlicingBlockDevice`.

- FileSystemStore: A lightweight implementation of the KVStore interface over file systems.

   - Requirements and assumptions: FileSystemStore assumes the underlying file system qualities for resilience and file validation. If the underlying file system has no protection against power failures, then neither does FileSystemStore. When initializing this class, it is assumed that the underlying FileSystem is initialized and mounted.

- SecureStore: A KVStore-based storage solution that provides security features on the stored data, such as encryption, authentication, rollback protection and write once, over an underlying KVStore class. It references an additional KVStore class for storing the rollback protection keys.

   - Requirements and assumptions: SecureStore assumes that the underlying KVStore instances are instantiated and initialized.

## KVStore class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.11/mbed-os-api-doxy/classmbed_1_1_k_v_store.html)

## KVStore example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-kvstore)](https://github.com/ARMmbed/mbed-os-example-kvstore/blob/mbed-os-6.11.0/main.cpp)

## Related content

- [KVStore Global Static API](static-global-api.html).
- [Storage configuration](../apis/data-storage.html).
