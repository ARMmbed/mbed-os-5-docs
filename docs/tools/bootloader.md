## Boot loader Configuration

This page describes each boot loader configuration parameter in detail.
For an guide on using the managed and unmanaged boot loader modes, see [the boot loader turorial](../tutorials/bootloder.md).

There are 4 configuration parameters that affect the location of an application in ROM:
 * `target.mbed_app_start`
 * `target.mbed_app_size`
 * `target.bootloader_img`
 * `target.restrict_size`
 
All of these parameters are valid in `targets.json`, `mbed_lib.json` and `mbed_app.json` and may be defined for individual targets and the wildcard target, `*`. A parameter in `mbed_lib.json` overrides a parameter in `targets.json`, and a parameter in `mbed_app.json` overrides one in `mbed_lib.json`.

The presence of any of these parameters defines `APPLICATION_ADDR` and `APPLICATION_SIZE` for C and C++ and `MBED_APP_START` and `MBED_APP_SIZE` for the linker.
 
### `target.mbed_app_start`

This parameter defines the start address of your application. You are responsible for the alignment of this address with respect to the flash layout and vector table size of the MCU you are using. When not used in conjunction with `target.mbed_app_size`, the application currently being build will user the remainder of ROM.

The value of this parameter is available to C and C++ as `APPLICATION_ADDR` and to the linker as `MBED_APP_START`.

This configuration parameter conflicts with `target.bootloader_img` and `target.restrict_size`. 


### `target.mbed_app_size`

This parameter defines the size of your application. `target.mbed_app_start` may be used in conjunction with this parameter to set the start address as well as the size. When `target.mbed_app_start` is not present, the application starts at the beginning of ROM.

The value of this parameter is available to C and C++ as `APPLICATION_SIZE` and to the linker as `MBED_APP_SIZE`.

This parameter conflicts with `target.bootloader_img` and `target.restrict_size`.


### `target.bootloader_img`

This parameter defines the boot loader image to be used during the builtin post-build merge process. `target.bootloader_img` implicitly defines the start of the current application's code segment by taking the size of the boot loader and rounding up to the next flash erase block boundary. The builtin post-build merge process automatically combines the current application with the image referenced in this parameter.

The start address of the current application, as computed above, is available to C and C++ as `APPLICATION_ADDR` and to the linker as `MBED_APP_START` ; The size of the current application is available as `APPLICATION_SIZE` and `MBED_APP_SIZE`. This parameter also defines `BOOTLOADER_ADDR` and `BOOTLOADER_SIZE` as the start address and size of the provided boot loader.

This parameter may be used in conjunction with `target.restrict_size` and conflicts with `target.mbed_app_start` and `target.mbed_app_size`. When used with `target.restrict_size`, the size off the application is defined by that parameter; Otherwise, the size is the remainder of ROM.

### `target.restrict_size`

This parameter restricts the size of the application to be at most the specified size. When `target.bootloader_img` is present, the start of the current application's code segment is computed as above; Otherwise, the start address is the beginning of ROM. The size of the application computed by rounding the end address down to the nearest flash erase block boundary and subtracting the start address. The post-build merge process will pad the resulting boot loader binary to it's end address.

The start address of the current application, as computed above, is available to C and C++ as `APPLICATION_ADDR` and to the linker as `MBED_APP_START` ; The size of the current application is available as `APPLICATION_SIZE` and `MBED_APP_SIZE`. This parameter also defines `POST_APPLICATION_ADDR` and `POST_APPLICATION_SIZE` as the start address and size of the region after the application.

This parameter may be used in conjunction with `target.bootloader_img` and conflicts with `target.mbed_app_start` and `target.mbed_app_size`. When used with `target.bootloader_img`, the start off the application is defined by that parameter; Otherwise, the start is the start of ROM.
