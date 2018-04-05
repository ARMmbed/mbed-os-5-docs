<h2 id="contributing-storage">Storage</h2>

Storage support is split between file systems and their underlying block device support. The [storage API page](/docs/v5.8/reference/storage.html) has more information on existing APIs in Mbed OS for both interfaces.

### Block Device

Adding a block device implementation is required for backing filesystems on new hardware. You can extend the [BlockDevice](https://os.mbed.com/docs/v5.8/mbed-os-api-doxy/class_block_device.html) class to provide support for unsupported storage. 

If you want to port a new file system to Mbed OS on existing storage options you can skip to the following section.

### File systems

To implement a new file system in Mbed OS, an implementor needs to provide the abstract functions in the file system interface. The [FAT file system](https://os.mbed.com/docs/v5.8/mbed-os-api-doxy/class_f_a_t_file_system.html) provides an excellent example.

A minimal file system needs to provide the following functions:

- `file_open`.
- `file_close`.
- `file_read`.
- `file_write`.
- `file_seek`.

Here is the full API that a file system may implement:

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.8/mbed-os-api-doxy/classmbed_1_1_file_system.html)

File systems must be backed by a block device in Mbed OS. If you are using supported hardware, then you can use the Mbed OS block device classes. Otherwise, view the [block device porting section](#block-device) earlier in this guide.

### Related content

- [BlockDevice](https://os.mbed.com/docs/v5.8/mbed-os-api-doxy/class_block_device.html).
- [FAT file system](https://os.mbed.com/docs/v5.8/mbed-os-api-doxy/class_f_a_t_file_system.html).
