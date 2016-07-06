# LocalFileSystem

A filesystem for accessing the local mbed Microcontroller USB disk drive.

This allows programs to read and write files on the same disk drive that is used to program the mbed Microcontroller. Once created, the standard C file access functions are used to open, read and write files.

<span class="note"> As the FRDM-KL25Z does not have external flash to store files, the LocalFileSystem is not available for this board </span>

## Hello World!

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/users/mbed_official/code/LocalFileSystem_HelloWorld/)](https://developer.mbed.org/users/mbed_official/code/LocalFileSystem_HelloWorld/file/cc465aef98cf/main.cpp) 

## Notes

If the microcontroller program opens a file on the local drive, it will be marked as removed on the Host computer. This means the PC will often display a message such as "insert a disk into drive" if you try to access it at this time; this is normal, and stops both the mbed and the PC trying to access the disk at the same time. 

<span class="warnings">**Warning:** The USB drive will only re-appear when all file handles are closed in your program, or the microcontroller program exits.</br>
If a running program on the mbed does not exit or does not release it's open file handles, you will _no longer be able to see the USB drive_ when you plug the mbed into your PC. To allow you to see the drive again (and load a new program), use the following procedure:</br>
1. Unplug the microcontroller
2. Hold the reset button down
3. While still holding the button, plug in the microcontroller. The mbed USB drive should appear.
4. Keep holding the button until the new program is saved onto the USB drive. </span>

## Implementation Details

The LocalFileSystem actually accesses the mbed USB disk by making "semihosting" calls to the mbed Interface, which does the actual accesses on behalf of your program. This means the "filesystem" in this case is running on the interface. The underlying mechanism is the interface acting like a debugger, and the "semihost" calls are effectively breakpoints that the interface spots and does the requested operation.

<span class="warnings">**Warning:** The LocalFilesystem has a few restrictions:</br>
- Only 8.3 filenames are supported 
- Sub-directories are not supported
- fseek is not supported for files opened for writing ("w")
- File access calls (fread, fwrite) will block, including interrupts, as semihosting is effectively a debug breakpoint </span>

Other filesystems (such as ones to talk to an SD card, or a USB FLASH drive) run on the target itself, so don't talk to the mbed Interface at all and these restrictions don't necessarily apply.
