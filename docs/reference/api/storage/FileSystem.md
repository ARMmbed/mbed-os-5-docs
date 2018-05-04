## FileSystem

The file system API provides a common interface for implementing a file system on a [block-based storage device](/docs/development/reference/contributing-storage.html#block-devices). The file system API is a class-based interface, but implementing the file system API provides the standard POSIX file API familiar to C users.

The main purpose of a FileSystem is to be instantiated. The FileSystem's constructor can take in a BlockDevice and mount point specified as a string, as well as other implementation specific configuration options. The mount point can then act as the first directory in any paths in Mbed OS when used with the POSIX API, giving you access to files inside the file system. Note that the mount point can be `NULL` if you only need to use the FileSystem as a C++ object.

You may have noticed that the FileSystem's `file` and `dir` functions are protected. This is because the FileSystem `file` and `dir` functions should not be used directly and are only a convenience for implementors. Instead, the [`File`](File.html) and [`Dir`](Dir.html) classes provide access to file and directory operations in a C++ class that respects RAII <!-- TODO link to glossary? --> and other C++ conventions.

### File system class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_file_system.html)

### File system example

[![View code](https://www.mbed.com/embed/?url=https://github.com/armmbed/mbed-os-example-filesystem)](https://github.com/ARMmbed/mbed-os-example-filesystem/blob/master/main.cpp)

### Related content

- [Storage configuration](configuration-storage.html).
- [File](File.html).
- [Dir](Dir.html).
