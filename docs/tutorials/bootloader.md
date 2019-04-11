# Creating and using a bootloader

This guide explains how to create a [bootloader](../reference/bootloader-configuration.html), how to create a main program to go with the bootloader and how to use this bootloader to perform software updates.

## Arm Mbed OS managed bootloader

The tools of Arm Mbed OS know how to manage some bootloader projects. The tools can manage bootloader projects where the bootloader comes before the application in ROM and the application starts immediately after the bootloader. If your bootloader does not meet both of these requirements, then please read the [unmanaged bootloader section](#unmanaged-bootloader). A managed bootloader project automatically merges the bootloader image with the application image as part of the application image build process.

### Creating the bootloader

Creating a bootloader is similar to creating a regular application. The only additional step you need is to specify the size of the bootloader as a target override in `mbed_app.json` in the target field `target.restrict_size`:

```
"target_overrides": {
    ...
    "<TARGET_NAME>": {
        "target.restrict_size": "0x20000"
    },
    ...
```

Adding this field:

- Restricts the bootloader code from growing larger than the specified size.
- Pads the output image to exactly the size specified.
- Defines the symbols `APPLICATION_ADDR`, `APPLICATION_SIZE`, `POST_APPLICATION_ADDR`, `POST_APPLICATION_SIZE`.

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

When the bootloader finishes its work, it needs to start the main program. To do this, the bootloader must flush or power down any external components it is using, such as filesystems or socket connections. After the bootloader powers down these components, it can start the main program by making a call to the function `mbed_start_application(uintptr_t address)` and passing on the base address of the next image to start. For Arm Mbed OS applications, the main program starts immediately after the bootloader, so you can use the symbol `POST_APPLICATION_ADDR` as its starting address.

Call the bootloader to start the main program:

```
mbed_start_application(POST_APPLICATION_ADDR);
```

For an example showing how to create a bootloader, see the [mbed-os-example-bootloader](https://github.com/armmbed/mbed-os-example-bootloader) repository.

### Creating the main program

To create an application using a bootloader, you must first have created the bootloader binary and added it to the current project. You must then specify the bootloader image in `mbed_app.json` in the `target_override` section:

```
"target_overrides": {
    ...
    "<TARGET_NAME>": {
        "target.bootloader_img": "bootloader/my_bootloader.bin"
    },
    ...
```

Adding this field has the following effects:

* When a build occurs, the application builds for the address immediately after the bootloader. The build system does this automatically by defining the symbols `MBED_APP_START` and `MBED_APP_SIZE` in the linker script (`.sct`, `.ld` or `.icf`).
* At the end of building, the build image is automatically combined with the bootloader to create the final image.

    <span class="notes">**Note:** When building offline, the original uncombined image is in the same directory `<project-name>_application.bin`.</span>

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

### Adding an application header

Take this one step further, and add a metadata header to the bootloader and application, so the bootloader can verify the integrity of the application. Create an `mbed_lib.json` that the bootloader and application share and that has the following contents.

```JSON
{
    "name": "application_header",
    "target_overrides": {
        "*": {
            "target.header_format": [
                ["magic", "const", "32be", "0x5a51b3d4"],
                ["headerVersion", "const", "32be", "2"],
                ["firmwareVersion", "timestamp", "64be", null],
                ["firmwareSize", "size", "64be", ["application"]],
                ["firmwareHash", "digest", "SHA256", "application"],
                ["headerCRC", "digest", "CRCITT32be", "header"]
            ]
        }
    }
}
```

This configuration adds a new region, named header, after the bootloader and before the application header. The ROM of your target now looks as follows:

```
|-------------------|   APPLICATION_ADDR + APPLICATION_SIZE == End of ROM
|                   |
...
|                   |
|    Application    |
|  (main program )  |
|                   |
+-------------------+   APPLICATION_ADDR == HEADER_ADDR + HEADER_SIZE
|      Header       |
+-------------------+   HEADER_ADDR == BOOTLOADER_ADDR + BOOTLOADER_SIZE
|                   |
|    Bootloader     |
|(my_bootloader.bin)|
|                   |
+-------------------+   BOOTLOADER_ADDR == Start of ROM
```


## Prebuilt bootloaders

Prebuilt bootloader mode is an option to merge prebuilt bootloaders into your application. `mbed-os\features\FEATURE_BOOTLOADER\` contains the available supported targets with the corresponding prebuilt bootloader organized in folders specific to targets. For example: `FEATURE_BOOTLOADER/targets/TARGET_STM/TARGET_STM32F4/TARGET_STM32F429xI/TARGET_NUCLEO_F429ZI/mbed-bootloader-block_device-sotp-v3_4_0.bin`.

Please note that this bootloader is not the same as the public [`mbed-bootloader`](https://github.com/ARMmbed/mbed-bootloader), which Mbed OS uses to generate the bootloader binaries in `mbed-os`.

There are two ways to test prebuilt bootloader mode.

You can add the BOOTLOADER feature into `mbed_app.json` located in the root application directory:

   ```
    "target_overrides": {
        "*": {
            "target.features_add": ["BOOTLOADER"]
        }
    }
   ```

Alternatively, you can add `-C 'target.features_add=["BOOTLOADER"]'` to your `mbed compile` command-line arguments.

Please see the [bootloader example](https://github.com/ARMmbed/mbed-os-example-feature-bootloader) for an example on how to use the bootloader feature.

There are two ways to add support for new targets:

You can place the prebuilt binary bootloader in `mbed-os/feature/FEATURE_BOOTLOADER`, and add the fields below with values corresponding to your binary:

   ```
   "target_overrides": {
           "YOUR_TARGET": {
               "target.app_offset": "0x10400",
               "target.header_offset": "0x10000",
               "target.header_format": [
                   ["magic", "const", "32be", "0x5a51b3d4"],
                   ["headerVersion", "const", "32be", "2"],
                   ["firmwareVersion", "timestamp", "64be", null],
                   ["firmwareSize", "size", "64be", ["application"]],
                   ["firmwareHash", "digest", "SHA256", "application"],
                   ["headerCRC", "digest", "CRCITT32be", "header"]
               ],
               "target.bootloader_img": "your_bootloader.bin"
           },
   ```

Alternatively, you can edit `mbed_app.json`, and override the target bootloader with the path to the bootloader and other fields:

   ```
       "target_overrides": {
           "YOUR_TARGET": {
               "target.bootloader_img": "PATH_TO_BOOTLOADER/your_bootloader.bin"
               "target.app_offset": "0x10400",
               "target.header_offset": "0x10000",
               "target.header_format": [
                   ["magic", "const", "32be", "0x5a51b3d4"],
                   ["headerVersion", "const", "32be", "2"],
                   ["firmwareVersion", "timestamp", "64be", null],
                   ["firmwareSize", "size", "64be", ["application"]],
                   ["firmwareHash", "digest", "SHA256", "application"],
                   ["headerCRC", "digest", "CRCITT32be", "header"]
               ]
          }
       }
   ```

## Unmanaged bootloader

You want to have an unmanaged bootloader when your bootloader's requirements conflict with the requirements of the managed bootloader. You need an unmanaged bootloader when your bootloader does not come before your application in ROM or your application does not start immediately after your bootloader. Unlike a managed bootloader, an unmanaged bootloader does not automatically merge the bootloader image with the application image after building the application. We expect users of an unmanaged bootloader build to construct their own set of scripts built atop the `mbed compile` primitive to perform bootloader and application merging.

An unmanaged bootloader build is a method of controlling the link location of a program within Mbed OS. There are two configuration options available for changing the link location: `target.mbed_app_start` and `target.mbed_app_size`. Please see [bootloader configuration](../reference/bootloader-configuration.html) for complete descriptions of these options.

## Exporter limitations

Although the exporters can export bootloader projects using the bootloader parameters, there are some limitations.

The exporters do not interpret Mbed OS configuration, and any changes to configuration parameters, especially bootloader parameters, require you to rerun the `mbed export` command.

Further, the exporters do not implement the postbuild merge that bootloader builds use.

For a managed bootloader:
After exporting a project with the `target.bootloader_img` setting, you are responsible for flashing the binary mentioned in the configuration parameter. Without flashing this bootloader image, the device will not boot correctly.

For an unmanaged bootloader:
After exporting a project with the `target.mbed_app_start` setting, you are responsible for ensuring that a boot loader is present, if needed. Without flashing this boot loader image, the device will not boot correctly.
