# Dir

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_dir.png)<span>Dir class hierarchy</span></span>

With a file system, the Dir class allows you to iterate over directories on the underlying storage. Directories, also called folders, are a way to group files. Each directory has a name that forms a part of the path to any files stored in that directory. Additionally, you can use `rename` operations at the file system level to change a directory's name and efficiently change the path to any files in that directory. To make a new directory, use the `mkdir` function in the [FileSystem](filesystem.html) class.

The Dir class operates as an iterator or stream similarly to the File class, except operating on file names instead of bytes or other type. Each `read` call returns the next file name in the directory and increments the Dir position. Similarly to a file, you can `seek` a Dir object to a specific position; however, this is limited to a position previously returned by a call to the Dir's `tell` function.

<span class="notes">**Note:** Iterating through a directory may return the file names '.' and '..', which are special file names for the current directory and the parent directory. When performing operations recursively, it is acceptable to treat any file starting with the character '.' as a special or "hidden" file.</span>

## Dir class API

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_dir.html)

## File system example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-filesystem/)](https://github.com/ARMmbed/mbed-os-example-filesystem/blob/mbed-os-5.14/main.cpp)

## Related content

- [FileSystem](filesystem.html).
- [File](file.html).
