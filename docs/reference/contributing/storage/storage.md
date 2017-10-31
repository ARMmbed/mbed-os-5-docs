<h2 id="contributing-storage">Storage</h2>

Storage support is split between filesystems and their underlying block device support. The [storage API page](/docs/v5.6/reference/storage-overview.html) has more information on existing APIs in Mbed OS for both interfaces.

#### Block Device

Adding a block device implementation is required for backing filesystems on new hardware. You can extend the [BlockDevice](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/bd/HeapBlockDevice.h) class to provide support for unsupported storage. 

If you want to port a new filesystem to Mbed OS on existing storage options you can skip to the following section.

#### Filesystems

To implement a new file system in Mbed OS, an implementor just needs to provide the abstract functions in the file system interface. The [FAT file system](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/fat/FATFileSystem.cpp) provides an excellent example, you can find tests of the POSIX API here.

A minimal file system needs to provide the following functions:

- `file_open`.
- `file_close`.
- `file_read`.
- `file_write`.
- `file_seek`.

Here is the full API that a filesystem may implement:

[![View code](https://www.mbed.com/embed/?type=library)](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/FileSystem.h#L205)

Filesystems must be backed by a block device in Mbed OS. If you are using supported hardware then you can continue, otherwise view the block device porting section above.
