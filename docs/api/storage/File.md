# File

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_file.png)<span>File class hierarchy</span></span>

The File class provides access to the underlying storage of a file system in a generic manner. This acts as a buffer between the file system and any technical limitations of the physical storage medium. On the storage, each file is a blob of data referenced by a file name represented as a string. By providing a file name to the `open` function in the File class, you can access the blob of data stored on disk.

The File API allows operations on stored data without ever needing to buffer the data in RAM. Because flash is several orders of magnitude cheaper than RAM, this can significantly increase the amount of data a device can store without significantly increasing the device's cost.

<span class="notes">**Note:** To get and set a buffer to a file, jump to the `read` and `write` functions. In the File class, the `read` and `write` functions always read or write the entire file at a time.</span>

A File operates like an infinitely long reel of tape. Each File object keeps track of its current position in the data, and this position updates as you read from or write to the file. As data is written to the File, the File grows unless the underlying storage runs out of memory. If supported by the underlying file system, you can explicitly move the File position with the `seek` and `rewind` functions.

Combining `read`, `write`, and `seek` on a File allows both streaming and random access to data stored on external memory without necessarily buffering the file contents on the device's RAM.

## File class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_file.html)

## File system example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-filesystem/)](https://github.com/ARMmbed/mbed-os-example-filesystem/blob/mbed-os-5.14/main.cpp)

## Related content

- [FileSystem](filesystem.html).
- [Dir](dir.html).
