# Device Management configuration

Device Management configuration has five distinct areas:

- Connectivity - the transport type for the device to connect to the Device Management service.
- Storage - the storage type and writing used for both the credentials and the firmware storage.
- Flash geometry - the device flash "sandbox" for bootloader, application header, application image and two Software One Time Programming (SOTP) regions.
- SOTP - the address and size of the SOTP regions in flash used to store the device special key that decrypts the credentials storage.
- Bootloader - the bootloader image, application and header offset.

Except for connectivity, the majority of the configuration is shared between the application and bootloader, which ensures the bootloader can correctly find, verify, authorize and apply an update to the device application.

For more information on bootloaders and firmware update, see:

- [Introduction to Mbed OS bootloaders](../porting/bootloader.html).
- [Creating and using an Mbed OS bootloader](../tutorials/bootloader.html).
- [Bootloader configuration in Mbed OS](../program-setup/bootloader-configuration.html).
- [Mbed bootloader for Device Management](https://github.com/ARMmbed/mbed-bootloader), or the short introduction [in the Device Management documentation](https://www.pelion.com/docs/device-management/current/updating-firmware/bootloaders.html).
- [Updating devices with Mbed CLI](../tools/cli-update.html).

To speed up this process, you can copy the configuration from the [application example](https://github.com/ARMmbed/pelion-ready-example/blob/master/mbed_app.json) as the basis for your application configuration.

## Application configuration

Edit the `mbed_app.json` file, and create a new entry under `target_overrides` with the target name for your device:

- **Connectivity** - Specify the default connectivity type for your target. It is essential with targets that lack default connectivity set in `targets.json` or for targets that support multiple connectivity options. For example:

   ```
            "target.network-default-interface-type" : "ETHERNET",
   ```

   The possible options are `ETHERNET`, `WIFI` and `CELLULAR`.

   Depending on connectivity type, you may have to specify more options. For an example, see the defined `CELLULAR` targets in `mbed_app.json`.

- **Storage** - Specify the storage block device type, which dynamically adds the block device driver you specified at compile time. For example:

   ```
            "target.components_add" : ["SD"],
   ```

   Valid options are `SD`, `SPIF`, `QSPIF` and `FLASHIAP` (not recommended). For more available options, see the [block device components](https://github.com/ARMmbed/mbed-os/tree/master/components/storage/blockdevice).

   You must also specify the block device pin configuration, which may vary from one block device type to another. Here's an example for `SD`:

   ```
            "sd.SPI_MOSI"                      : "PE_6",
            "sd.SPI_MISO"                      : "PE_5",
            "sd.SPI_CLK"                       : "PE_2",
            "sd.SPI_CS"                        : "PE_4",
   ```

- **Flash** - Define the basics for the microcontroller flash. For example:

   ```
            "device_management.flash-start-address"              : "0x08000000",
            "device_management.flash-size"                       : "(2048*1024)",
   ```

- **SOTP** - Define two SOTP or NVStore regions that Device Management will use to store its special keys, which encrypt the data stored. Use the last two flash sectors (if possible) to ensure that they don't get overwritten when new firmware is applied. For example:

   ```
            "device-management.sotp-section-1-address"            : "(MBED_CONF_APP_FLASH_START_ADDRESS + MBED_CONF_APP_FLASH_SIZE - 2*(128*1024))",
            "device-management.sotp-section-1-size"               : "(128*1024)",
            "device-management.sotp-section-2-address"            : "(MBED_CONF_APP_FLASH_START_ADDRESS + MBED_CONF_APP_FLASH_SIZE - 1*(128*1024))",
            "device-management.sotp-section-2-size"               : "(128*1024)",
            "device-management.sotp-num-sections" : 2
   ```

   - `*-address` defines the start of the flash sector.
   - `*-size` defines the actual sector size.
   - `sotp-num-sections` should always be set to `2`.

At this point, we recommend you run the "connect" test suite, which verifies that the device can successfully bootstrap, register and send and receive data from Device Management with the provided configuration.

If you already configured your Device Management API key and initialized your credentials as described in [Adding Device Management connectivity to your application](../mbed-os-pelion/device-management-for-mbed-os.html#adding-device-management-connectivity-to-your-application), you can compile the "connect" tests:

```
$ mbed test -t <TOOLCHAIN> -m <BOARD> -n simple*dev*connect -DMBED_TEST_MODE --compile
```

To run the tests:

```
$ mbed test -t <TOOLCHAIN> -m <BOARD> -n simple*dev*connect --run -v
```

## Bootloader configuration

When the "connect" tests have passed, enable the firmware update feature by adding a bootloader to your application.

1. Import the official [mbed-bootloader](https://github.com/ARMmbed/mbed-bootloader/) repository as a new application:

    `mbed import mbed-bootloader`

    Alternatively, you can import the [mbed-bootloader-extended](https://github.com/ARMmbed/mbed-bootloader-extended/) repository that builds on top of `mbed-bootloader` and extends the support for file systems and storage drivers:

    `mbed import mbed-bootloader-extended`.

1. In the imported bootloader application, edit the configuration, for example `mbed-bootloader-extended/mbed_app.json`. Add a new target entry, and specify:

   - **Flash** - Define the basics for the microcontroller flash (the same as in `mbed_app.json`). For example:

      ```
            "flash-start-address"              : "0x08000000",
            "flash-size"                       : "(2048*1024)",
      ```

   - **SOTP** - Specify the location of the SOTP key storage. In the bootloader, the variables are named differently. Try to use the last two flash sectors (if possible) to ensure that they don't get overwritten when new firmware is applied. For example:

    ```
            "nvstore.area_1_address"           : "(MBED_CONF_APP_FLASH_START_ADDRESS + MBED_CONF_APP_FLASH_SIZE - 2*(128*1024))",
            "nvstore.area_1_size"              : "(128*1024)",
            "nvstore.area_2_address"           : "(MBED_CONF_APP_FLASH_START_ADDRESS + MBED_CONF_APP_FLASH_SIZE - 1*(128*1024))", "nvstore.area_2_size" : "(128*1024)",
    ```

    - **Application offset** - Specify the start address for the application and the Update client meta information. As these are automatically calculated, you can copy the following:

    ```
            "update-client.application-details": "(MBED_CONF_APP_FLASH_START_ADDRESS + 64*1024)",
            "application-start-address"        : "(MBED_CONF_APP_FLASH_START_ADDRESS + 65*1024)",
            "max-application-size"             : "DEFAULT_MAX_APPLICATION_SIZE",
    ```

    - **Storage** - Specify the block device pin configuration, exactly as you defined it in the `mbed_app.json` file. For example:

    ```
            "target.components_add"            : ["SD"],
            "sd.SPI_MOSI"                      : "PE_6",
            "sd.SPI_MISO"                      : "PE_5",
            "sd.SPI_CLK"                       : "PE_2",
            "sd.SPI_CS"                        : "PE_4"
    ```

1. Compile the bootloader using the `bootloader_app.json` configuration you just edited:

   ```
   $ mbed compile -t <TOOLCHAIN> -m <TARGET> --profile=tiny.json --app-config=<path to pelion-enablement/bootloader/bootloader_app.json>
   ```

<span class="notes">**Note:** `mbed-bootloader` is primarily optimized for `GCC_ARM`, so you may want to compile it with that toolchain.
Before adding the bootloader to your application, compile and flash the bootloader and then connect over the virtual com port to ensure the bootloader is running correctly. You can ignore errors related to checksum verification or failure to jump to application - these are expected at this stage.</span>

## Adding the bootloader to your application

1. Copy the compiled bootloader from `mbed-bootloader-extended/BUILDS/<TARGET>/<TOOLCHAIN>-TINY/mbed-bootloader.bin` to `<your_application_name>/bootloader/mbed-bootloader-<TARGET>.bin`.

1. Edit `<your_application_name>/mbed_app.json`, and modify the target entry to include:

   ```
            "target.features_add"              : ["BOOTLOADER"],
            "target.bootloader_img"            : "bootloader/mbed-bootloader-<TARGET>.bin",
            "target.app_offset"                : "0x10400",
            "target.header_offset"             : "0x10000",
            "update-client.application-details": "(MBED_CONF_APP_FLASH_START_ADDRESS + 64*1024)",
   ```

      - `update-client.application-details` must be identical in `bootloader_app.json` and `mbed_app.json`.
      - `target.app_offset` is the relative offset to `flash-start-address` you specified in `mbed_app.json` and `bootloader_app.json`, and is the hex value of the offset specified by `application-start-address` in `bootloader_app.json`. For example,  `(MBED_CONF_APP_FLASH_START_ADDRESS+65*1024)` dec equals `0x10400` hex.
      - `target.header_offset` is also the relative offset to the `flash-start-address` you specified in the `bootloader_app.json`, and is the hex value of the offset specified by `update-client.application-details`. For example, `(MBED_CONF_APP_FLASH_START_ADDRESS+64*1024)` dec equals `0x10000` hex.

1. Compile and rerun all tests, including the firmware update ones:

   ```
   $ mbed test -t <TOOLCHAIN> -m <BOARD> -n simple*dev*connect -DMBED_TEST_MODE --compile

   $ mbed test -t <TOOLCHAIN> -m <BOARD> -n simple*dev*connect --run -v
   ```

See [Validation and testing](../mbed-os-pelion/device-management-test.html) for details on the tests.
