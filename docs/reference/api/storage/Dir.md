## Dir

<span class="images">![](https://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_dir.png)<span>Dir class hierarchy</span></span>

With a file system, the Dir class allows a user to iterate over directories on the underlying storage. Directories, also called folders, are a way to group files. Each directory has a name which forms a part of the path to any files stored in that directory. Additionally, `rename` operations at the file system level can be used to change a directory's name, and efficiently change the path to any files in that directory. To make a new directory, use the `mkdir` function found in the [FileSystem](FileSystem.html) class.

The Dir class operates as an iterator or stream similarly to the File class, except operating on file names instead of bytes or other type. Each `read` call returns the next file name in the directory and increments the Dir position. Similarly to a file, a Dir object can be `seek`ed to a specific position, however this is limited to a position previously returned a call to the Dir's `tell` function.

**Note:** Iterating through a directory may return the file names '.' and '..', which are special file names for "this directory" and the "parent directory" respectively. When performing operations recursively, it is acceptable to treat any file starting with the character '.' as a special or "hidden" file.

### Dir class API

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_dir.html)

### File system example

[![View code](https://www.mbed.com/embed/?url=https://github.com/armmbed/mbed-os-example-filesystem)](https://github.com/ARMmbed/mbed-os-example-filesystem/blob/master/main.cpp)

### Related content

- [FileSystem](FileSystem.html).
- [File](File.html).
