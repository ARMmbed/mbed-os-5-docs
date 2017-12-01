## Storage overview

The storage APIs present in Arm Mbed OS are:

- <a href="/docs/v5.6/reference/contributing-storage.html#contributing-filesystem" target="_blank">File system</a>: a common interface for using file systems on block devices.
- <a href="/docs/v5.6/reference/contributing-storage.html#block-devices" target="_blank">Block device</a>: a common interface for block-based storage devices.

#### Declaring a file system

The <a href="https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/classmbed_1_1_file_system.html" target="_blank">FileSystem</a> class provides the core API for file system operations. You must provide a block device to back the file system. When you declare a file system with a name, you can open files on the file system through the `open` and `fopen` functions.

##### Open

The `open` function creates a connection between a file and a file descriptor. Using a string path argument, you can open a file with a set of option flags. Other functions in Mbed OS can use the file descriptor to track the current position in a file, read and write content and so on.

##### Fopen

The `fopen` function is similar to the open function above but associates a stream with the opened file. This can be helpful when performing mainly sequential read and write operations. However, it is important to flush and close the stream to update the file. This option is weaker when trying to seek through a file often.

The IEEE C standard specifications for both `open` and `fopen` can provide additional information.

Existing file systems:

The <a href="https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_f_a_t_file_system.html" target="_blank">FAT file system</a> is a standard file system.

The <a href="https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_block_device.html" target="_blank">BlockDevice</a> class provides the underlying API for representing block-based storage that you can use to back a file system. Mbed OS provides standard interfaces for the more common storage media, and you can extend the BlockDevice class to provide support for unsupported storage.

Additionally, two utility block devices give you better control over how storage is allocated. The <a href="https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_slicing_block_device.html" target="_blank">slicing block device</a> allows you to partition storage into smaller block devices that you can use independently, and the <a href="https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_chaining_block_device.html" target="_blank">chaining block device</a> allows you to chain multiple block devices together and extend the usable amount of storage.

<span class="notes">**Note:** Some file systems may provide a format function for cleanly initializing a file system on an underlying block device or require external tools to set up the file system before the first use.</span>

#### Partitioning

Partitioning allows you to split a block device among multiple storage users such that the split is portable across multiple systems. Partitioning also allows you to have multiple file systems that you can mount on one disk from both Mbed OS devices and host computers. The primary partitioning scheme that Mbed OS supports is the Master Boot Record (MBR).

<span class="notes">**Note:** File system partitioning is not required if only one file system is present.</span>

#### C++ classes

The FileSystem class provides the core user C++ API. Mbed OS provides <a href="https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/classmbed_1_1_file.html" target="_blank">File</a> and <a href="https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/classmbed_1_1_dir.html" target="_blank">Dir</a> classes that represent files and directories in a C++ API.

#### Block device operations

A block device can perform three operations on a block in a device:

- Read a block from storage.
- Erase a block in storage.
- Program a block that has previously been erased.

<span class="notes">**Note:** The state of an erased block is undefined. NOR flash devices typically set an erased block to all 0xff, but for some block devices such as the SD card, erase is a NOOP. If a deterministic value is required after an erase, the consumer of the block device must verify this.</span>

#### Block sizes

Some storage technologies have different sized blocks for different operations. For example, NAND flash can be read and programmed in 256-byte pages, but must be erased in 4-kilobyte sectors.

Block devices indicate their block sizes through the `get_read_size`, `get_program_size` and `get_erase_size` functions. The erase size must be a multiple of the program size, and the program size must be a multiple of the read size. Some devices may even have a read/program size of a single byte.

As a rule of thumb, you can use the erase size for applications that use a single block size (for example, the FAT file system).

#### Utility block devices

Arm Mbed OS contains several utility block devices to give you better control over the allocation of storage.

- With the <a href="https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_slicing_block_device.html" target="_blank">slicing block device</a>, you can partition storage into smaller block devices that you can use independently.
- With the <a href="https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_chaining_block_device.html" target="_blank">chaining block device</a>, you can chain multiple block devices together and extend the usable amount of storage.
- Mbed OS comes with support for storing partitions on disk with a Master Boot Record (MBR). The <a href="https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_m_b_r_block_device.html" target="_blank">MBRBlockDevice</a> provides this functionality and supports creating partitions at runtime or using preformatted partitions configured separately from outside the application.
