## Bootloader configuration

This page describes each bootloader configuration parameter in detail. For a guide on using the managed and unmanaged bootloader modes, please see [the bootloader turorial](/docs/v5.7/tutorials/bootloader.html).

There are 4 configuration parameters that affect the location of an application in ROM:

- `target.mbed_app_start`
- `target.mbed_app_size`
- `target.bootloader_img`
- `target.restrict_size`
 
All of these parameters are valid in `targets.json`, `mbed_lib.json` and `mbed_app.json` and may be defined for individual targets and the wildcard target, `*`. A parameter in `mbed_lib.json` overrides a parameter in `targets.json`, and a parameter in `mbed_app.json` overrides one in `mbed_lib.json`.

The presence of any of these parameters defines `APPLICATION_ADDR` and `APPLICATION_SIZE` for C and C++ and `MBED_APP_START` and `MBED_APP_SIZE` for the linker.
 
### `target.mbed_app_start`

This parameter defines the start address of your application. You are responsible for the alignment of this address with respect to the flash layout and vector table size of the MCU you are using. When not used in conjunction with `target.mbed_app_size`, the application being built uses the remainder of ROM.

The value of this parameter is available to C and C++ as `APPLICATION_ADDR` and to the linker as `MBED_APP_START`.

This configuration parameter conflicts with `target.bootloader_img` and `target.restrict_size`. 

### `target.mbed_app_size`

This parameter defines the size of your application. You may use `target.mbed_app_start` in conjunction with this parameter to set the start address, as well as the size. When `target.mbed_app_start` is not present, the application starts at the beginning of ROM.

The value of this parameter is available to C and C++ as `APPLICATION_SIZE` and to the linker as `MBED_APP_SIZE`.

This parameter conflicts with `target.bootloader_img` and `target.restrict_size`.

### `target.bootloader_img`

This parameter defines the bootloader image to be used during the built-in postbuild merge process. `target.bootloader_img` implicitly defines the start of the current application's code segment by taking the size of the bootloader and rounding up to the next flash erase block boundary. The built-in postbuild merge process automatically combines the current application with the image this parameter references.

The start address of the current application, as computed above, is available to C and C++ as `APPLICATION_ADDR` and to the linker as `MBED_APP_START`. The size of the current application is available as `APPLICATION_SIZE` and `MBED_APP_SIZE`. This parameter also defines `BOOTLOADER_ADDR` and `BOOTLOADER_SIZE` as the start address and size of the provided bootloader.

You may use this parameter in conjunction with `target.restrict_size`. It conflicts with `target.mbed_app_start` and `target.mbed_app_size`. When you use it with `target.restrict_size`, that parameter defines the size of the application. Otherwise, the size is the remainder of ROM.

### `target.restrict_size`

This parameter restricts the size of the application to be at most the specified size. When `target.bootloader_img` is present, the start of the current application's code segment is computed as above; otherwise, the start address is the beginning of ROM. The size of the application is computed by rounding the end address down to the nearest flash erase block boundary and subtracting the start address. The postbuild merge process pads the resulting bootloader binary to its end address.

The start address of the current application, as computed above, is available to C and C++ as `APPLICATION_ADDR` and to the linker as `MBED_APP_START`. The size of the current application is available as `APPLICATION_SIZE` and `MBED_APP_SIZE`. This parameter also defines `POST_APPLICATION_ADDR` and `POST_APPLICATION_SIZE` as the start address and size of the region after the application.

You may use this parameter in conjunction with `target.bootloader_img` and conflicts with `target.mbed_app_start` and `target.mbed_app_size`. When used with `target.bootloader_img`, that parameter defines the start of the application. Otherwise, the start is the start of ROM.

### Exporter limitations

Although the exporters can export a project using the configuration parameters above, there are some limitations. 

The exporters do not interpret Mbed OS configuration, and any changes to configuration parameters, especially bootloader parameters, require you to rerun the `mbed export` command. 

Further, the exporters do not implement the postbuild merge that managed bootloader builds use. After exporting a project with the `target.bootloader_img` setting, you are responsible for flashing the binary mentioned in the configuration parameter. 
