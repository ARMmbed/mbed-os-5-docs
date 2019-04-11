<h1 id="contributing-storage">Storage</h1>

Mbed OS provides various storage solutions, all built on top of the [BlockDevice interface](../apis/blockdevice.html). 

When you add a new platform, you must add the supported block devices to the list of components in the `targets.json` file. The block devices are located in the [components folder]( https://github.com/ARMmbed/mbed-os/tree/master/components/storage/blockdevice). To enable a block device in the `COMPONENT_<component name>` folder, add the `<component name>` string to the component list for the target in the `targets.json` file. For example, for the internal memory block device, `COMPONENT_FLASHIAP`, add `"components_add": ["FLASHIAP"]` to your target section in the `targets.json` file. 

For more information about existing storage solutions in Mbed OS, see the [Storage API page](../apis/storage.html).

### Block Device

You might have to add a block device implementation if you have new storage hardware that is not supported by the existing block devices. You can extend the [BlockDevice](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_block_device.html) class to provide support for unsupported storage.

If you want to port a new file system to Mbed OS on existing storage options you can skip to the following section.

### File systems

To implement a new file system in Mbed OS, an implementor needs to provide the abstract functions in the file system interface. The [FAT file system](https://os.mbed.com/docs/development/mbed-os-api-doxy/_f_a_t_file_system_8h_source.html) provides an excellent example.

A minimal file system needs to provide the following functions:

- `file_open`.
- `file_close`.
- `file_read`.
- `file_write`.
- `file_seek`.

Here is the full API that a file system may implement:

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_file_system.html)

File systems must be backed by a block device in Mbed OS. If you are using supported hardware, then you can use the Mbed OS block device classes. Otherwise, view the [block device porting section](#block-device) earlier in this guide.

### Related content

- [BlockDevice](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_block_device.html).
- [FAT file system](https://os.mbed.com/docs/development/mbed-os-api-doxy/_f_a_t_file_system_8h_source.html).
