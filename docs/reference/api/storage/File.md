## File

<span class="images">![](https://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_file.png)<span>File class hierarchy</span></span>

With a file system, the File class provides access to the underlying storage in a generic manner that is abstracted by the file system from any technical limitations of the underlying storage. On the storage, each file is a blob of data referenced by a file name represented as a string. By providing a file name to the `open` function in the File class, you can access the blob of data stored on disk.

The API used to access the data stored on disk may come across as intimidating, but the API is not without reason. The File API allows operations on stored data without ever needing to buffer the data in RAM. Since flash is several orders of magnitude cheaper than RAM, this can significantly increase the amount of data a device can store without significantly increasing the device's cost.

**Note:** If you just need to get and set a buffer to a file, jump to the `read` and `write` functions. In the File class the `read` and `write` functions will always read or write the entire file at a time.

At its heart, a File operates like a reel of tape. An infinitely long reel of tape. Each File object keeps track of its current position in the data, and this position updates as the file is read from or written to. As data is written to the File, the File will grow unless the underlying storage runs out of memory. And if supported by the underlying file system, the File position can be explicitly moved with the `seek` and `rewind` functions.

Combining `read`, `write`, and `seek` on a File allows both streaming and random access to data stored on external memory without necessarily buffering the file contents on the device's RAM.

### File class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_file.html)

### File system example

[![View code](https://www.mbed.com/embed/?url=https://github.com/armmbed/mbed-os-example-filesystem)](https://github.com/ARMmbed/mbed-os-example-filesystem/blob/master/main.cpp)

### Related content

- [FileSystem](FileSystem.html).
- [Dir](Dir.html).
