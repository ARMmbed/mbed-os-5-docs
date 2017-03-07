# Bootloader

This guide explains how to create a bootloader, how to create a main program to go with the bootloader and how to use this bootloader to perform software updates.

## Creating the bootloader

Creating a bootloader is similar to creating a regular application. The only additional step you need is to specify the size of the bootloader as a target override in mbed_app.json in the target field "target.restrict_size":

```
    "target_overrides": {
        ...
        "NUCLEO_F429ZI": {
            "target.restrict_size": "0x20000"
        },
        ...
```

Adding this field:

* Restricts the bootloader code from growing larger than this size.
* Pads the output image to exactly the size specified.
* Defines the symbols APPLICATION_ADDR, APPLICATION_SIZE, POST_APPLICATION_ADDR, POST_APPLICATION_SIZE.

It produces the following ROM layout:

```
|-------------------|   POST_APPLICATION_ADDR + POST_APPLICATION_SIZE == End of ROM
|                   |
...
|                   |
|                   |
|     Reserved      |
|                   |
+-------------------+   POST_APPLICATION_ADDR == APPLICATION_ADDR + APPLICATION_SIZE
|                   |
|    Application    |
| (is a bootloader) |
|                   |
+-------------------+   APPLICATION_ADDR == Start of ROM
```

When the bootloader finishes its work, it needs to start the main program. To do this, the bootloader must flush or power down any external components it is using, such as filesystems or socket connections. After the bootloader powers down these components, it can start the main program by making a call to the function `mbed_start_application(uintptr_t address)` and passing in the base address of the next image to start. For mbed OS applications, the main program starts immediately after the bootloader, so you can use the symbol POST_APPLICATION_ADDR as its starting address.

Call the bootloader to start the main program:

```
mbed_start_application(POST_APPLICATION_ADDR);
```

For an example showing how to create a bootloader, see the [mbed-os-example-bootloader](https://github.com/armmbed/mbed-os-example-bootloader) repository.

## Creating the main program

To create an application using a bootloader, you must first have created the bootloader binary and added it to the current project. You must then specify the bootloader image in mbed_app.json in the target_override section similar to this:

```
    "target_overrides": {
        ...
        "NUCLEO_F429ZI": {
            "target.bootloader_img": "bootloader/my_bootloader.bin"
        },
        ...
```

Adding this field has following effects:

* When a build occurs, the application builds for the address immediately after the bootloader. The build system does this automatically by defining the symbols `MBED_APP_START` and `MBED_APP_SIZE` in the linker script (.sct, .ld or .icf).
* At the end of building, the build image is automatically combined with the bootloader to create the final image. 

Note: When building offline, the original uncombined image is in the same directory `<project-name>_application.bin`.

* It defines the symbols `APPLICATION_ADDR`, `APPLICATION_SIZE`, `BOOTLOADER_ADDR` and `BOOTLOADER_SIZE`.

It produces the following ROM layout:

```
|-------------------|   APPLICATION_ADDR + APPLICATION_SIZE == End of ROM
|                   |
...
|                   |
|    Application    |
|  (main program )  |
|                   |
+-------------------+   APPLICATION_ADDR == BOOTLOADER_ADDR + BOOTLOADER_SIZE
|                   |
|    Bootloader     |
|(my_bootloader.bin)|
|                   |
+-------------------+   BOOTLOADER_ADDR == Start of ROM
``` 

For an example showing how to create an application that uses a bootloader, see the [mbed OS bootloader example](https://github.com/armmbed/mbed-os-example-bootloader-blinky) repository.
