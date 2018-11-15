# Classes implementing KVStore API
KVStore API is a common get/set API implemented by several classes. It allows flexibility in the configuration of a storage solution, that can be built by allocating several combinations of objects. For example, SecureStore can hold a TDBStore or a FileSystemStore, both implementing KVStore API, without any change in functionality.
Developers should use the static global KVStore API when possible, to get advantage of the flexibility of KVStore configuration.
It is also possible to instantiate single objects of the classes detailed below and use the KVStore class API directly. KVStore API presents additional functionality not present in the global API, like incremental set (set_start, set_add_data and set_finalize) and incremental get (parameter offset in function get). These APIs must be used with caution, because a second call  to set_start after a call to set_start and before a call to set_finalize, will be held pending on a mutex, until set_finalize is called.
## TDBStore - Tiny Database
TDBStore (Tiny Database Storage) is a lightweight module aimed for storing data on a flash storage. It is part of the KVStore class family, meaning that it supports the get/set interface. It is designed to optimize performance (speed of access), reduce wearing of the flash and to minimize storage overhead. It is also resilient to power failures.

### Requirements and assumptions
TDBStore assumes that the underlying block device is fully dedicated for it (starting offset 0). If one wishes that only a part of the device is dedicated to TDBStore, then a sliced block device should be used, typically with `SlicingBlockDevice`.   
In addition, this feature requires a flash based block device such as `FlashIAPBlockDevice` or `SpifBlockDevice`. It can work on top of block devices that don't need erasing before writes, such as `HeapBlockDevice` or `SDBlockDevice`, but requires a flash simulator layer for this purpose, like the one offered by `FlashSimBlockDevice`. 

## FileSystemStore

FileSystemStore is a lightweight implementation of the KVStore interface over file systems.

### Requirements and assumptions

FileSystemStore assumes the underlying file system qualities for resilience and file validation. This means that if the underlying file system has no protection against power failures, then neither would FileSystemStore have.  
When initializing this class, it is assumed that the underlying FileSystem is initialized and mounted. 

## SecureStore
SecureStore is a KVStore based storage solution, providing security features on the stored data, such as encryption, authentication, rollback protection and write once, over an underlying KVStore class. It references an additional KVStore class for storing the rollback protection keys. 

### Requirements and assumptions

SecureStore assumes that the underlying KVStore instances are instantiated and initialized. 