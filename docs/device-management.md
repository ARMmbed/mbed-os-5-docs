<h2 id="device-management">Device Management for Mbed OS</h2>

(This was previously called Simple Mbed Cloud Client.)

This provides a way to add device management capabilities to Mbed OS devices using the Arm Pelion Device Management IoT platform.

It:

- Enables applications to connect and perform firmware updates in a few lines of code.
- Runs separately from your main application; it does not take over your main loop.
- Provides LWM2M resources, variables that sync automatically through Pelion Device Management.
- Helps users avoid doing blocking network operations in interrupt contexts, by automatically defering actions to a separate thread.
- Provides end-to-end Greentea tests for Pelion Device Management.

This library makes it trivial to expose sensors, actuators and other variables to a cloud service. For a complete Pelion Device Management Client API, please see our [documentation](https://cloud.mbed.com/docs/current/mbed-cloud-client/index.html).

### Device management for your Mbed OS application

Not every device (microcontroller, module or board) is capable of running device management features. Although you can add or extend some hardware capabilities, such as connectivity, storage and TRNG, others are impossible or inconvenient to extend (for example, RAM or flash).

The minimum requirements to add device management feature to your application are:

- RAM: 128K or more.
- Flash: 512K or more.
- Real Time Clock (RTC).
- (Optional but recommended) True Random Number Generator (TRNG).
- A storage device: SD card, SPI flash, QSPI flash or data flash.
- IP connectivity: Ethernet, Wi-Fi, cellular, 6LoWPAN or Thread.

Additionally, we recommend the latest version of Mbed OS support the device and any additional complementary hardware components, or that they have support for the APIs provided in the latest releases of Mbed OS.

Useful references:

- Check which Mbed OS platforms are supported in the [Pelion Device Management quick start guide](https://cloud.mbed.com/quick-start).
- Check the [storage options available](../reference/storage.html).
- Check the [network options available]../reference/network-socket.html).

#### Adding a device management feature to your application

1. Add this library to your Mbed OS project:
   
   ```
   $ mbed add https://github.com/ARMmbed/simple-mbed-cloud-client
   ```
   
   If you do not have an Mbed OS project to add, you can create one with `mbed new <your_application_name>` and then the `mbed add` step above.

1. Reference the library from the `main.cpp` file, and add network and storage drivers. Finally, initialize the SimpleMbedCloudClient library. This is the architecture of a device management application with Mbed OS:

    ```cpp
    #include "simple-mbed-cloud-client.h"
    #include <Block device>
    #include <Filesystem>
    #include <Network>

    int main() {

        /* Initialize connectivity */
        NetworkInterface *net = NetworkInterface::get_default_instance();
        net->connect();

        /* Initialize storage */
        BlockDevice *bd = BlockDevice::get_default_instance();
        <Filesystem> fs("fs", &bd);

        /* Initialize SimpleMbedCloudClient */
        SimpleMbedCloudClient client(net, &bd, &fs);
        client.init();

        /* Create resource */
        MbedCloudClientResource *variable;
        variable = client.create_resource("3201/0/5853", "variable");
        variable->set_value("assign new value");
        variable->methods(M2MMethod::GET | M2MMethod::PUT);

    }
    ```

1. Configure the API key for your Pelion Portal account.

   If you don't have an API key available, then log in to the [Pelion IoT Platform portal](https://portal.mbedcloud.com/), navigate to `Access Management` and `API keys`, and create a new one. Then specify the API key as the global `mbed` configuration:

    ```
    $ mbed config -G CLOUD_SDK_API_KEY <your-api-key>
    ```

1. Install the device management certificate:

    ```
    $ mbed dm init -d "<your company name.com>" --model-name "<product model identifier>"
    ```

This creates your private and public key pair and also initialize various `.c` files with these credentials, so you can use Connect and (firmware) Update device management features.

#### Example applications

To help you start quickly, please refer to the following [application example](https://github.com/ARMmbed/pelion-ready-example). It demonstrates how to connect to the Pelion IoT Platform service, register resources and get ready to receive a firmware update.

Also, there are a number of board-specific applications that focus on providing more elaborate hardware features with Mbed OS and the Pelion IoT Platform. These are available in the Pelion [quick start](https://cloud.mbed.com/quick-start). Please see the reference table below, organized by vendor name, for details:

Platform                        |  Connectivity      | Storage   | Example URL
--------------------------------| -------------------| --------- | --------------------
Nuvoton NUMAKER-IOT-M487        | Wi-Fi              | SD Card   | https://os.mbed.com/teams/Nuvoton/code/pelion-example-common/
Nuvoton NUMAKER-PFM-M487        | Ethernet           | SD Card   | https://os.mbed.com/teams/Nuvoton/code/pelion-example-common/
Nuvoton NUMAKER-PFM-NUC472      | Ethernet           | SD Card   |https://os.mbed.com/teams/Nuvoton/code/pelion-example-common/
NXP FRDM-K64F                   | Ethernet           | SD Card   | https://os.mbed.com/teams/NXP/code/mbed-cloud-connect-example-ethernet
NXP FRDM-K66F                   | Ethernet           | SD Card   | https://os.mbed.com/teams/NXP/code/mbed-cloud-connect-example-ethernet
Renesas GR-LCYHEE               | Wi-Fi              | SD Card   | https://os.mbed.com/teams/Renesas/code/pelion-example-common/
Sigma Delta Technologies SDT64B | Ethernet           | SD Card   | https://os.mbed.com/teams/Sigma-Delta-Technologies/code/pelion-example-common
ST DISCO_L475E_IOT01A           | Wi-Fi              | QSPI      | https://os.mbed.com/teams/ST/code/pelion-example-disco-iot01/
ST DISCO_F413H                  | Wi-Fi              | QSPI      | https://os.mbed.com/teams/ST/code/pelion-example-common/
ST DISCO_F746NG                 | Ethernet           | QSPI      | https://os.mbed.com/teams/ST/code/pelion-example-common/
ST NUCLEO_F429ZI                | Ethernet           | SD Card   | https://os.mbed.com/teams/ST/code/pelion-example-common/
ST NUCLEO_F767ZI                | Ethernet           | SD Card   | https://os.mbed.com/teams/ST/code/pelion-example-common/
ST NUCLEO_F746ZG                | Ethernet           | SD Card   | https://os.mbed.com/teams/ST/code/pelion-example-common/
ST NUCLEO_F207ZG                | Ethernet           | SD Card   | https://os.mbed.com/teams/ST/code/pelion-example-common/
UBlox EVK ODIN W2               | Wi-Fi              | SD Card   | https://os.mbed.com/teams/ublox/code/pelion-example-common/
UBlox C030 U201                 | Cellular           | SD Card   | https://os.mbed.com/teams/ublox/code/pelion-example-common/

### Device management configuration

The device management configuration has five distinct areas:

- Connectivity - the transport type for the device to connect to the device management service.
- Storage - the storage type and writing used for both the credentials and the firmware storage.
- Flash geometry - the device flash "sandbox" for bootloader, application header, application image and two SOTP regions.
- SOTP - the address and size of the SOTP regions in flash used to store the device special key that decrypts the credentials storage.
- Bootloader - the bootloader image, application and header offset.

Except for connectivity, the majority of the configuration is shared between the application and bootloader, which ensures the bootloader can correctly find, verify, authorize and apply an update to the device application.

For full documentation about bootloaders and firmware update, please read the following documents:

- [Introduction to Mbed OS bootloaders](../porting/bootloader.html).
- [Creating and using an Mbed OS bootloader](../tutorials/bootloader.html).
- [Bootloader configuration in Mbed OS](../tools/configuring-tools.html).
- [Mbed Bootloader for Pelion Device Management](https://github.com/ARMmbed/mbed-bootloader).
- [Updating devices with Mbed CLI](../tools/cli-update.html).

To hasten this process, you can copy the configuration from the [application example](https://github.com/ARMmbed/pelion-ready-example/blob/master/mbed_app.json) as the basis for your application configuration.

#### 1. Application configuration

Edit the `mbed_app.json` file, and create a new entry under `target_overrides` with the target name for your device:

- **Connectivity** - Specify the default connectivity type for your target. It's essential with targets that lack default connectivity set in `targets.json` or for targets that support multiple connectivity options. For example:
   
   ```
            "target.network-default-interface-type" : "ETHERNET",
   ```
      
   The possible options are `ETHERNET`, `WIFI` and `CELLULAR`.
   
   Depending on connectivity type, you might have to specify more config options. For an example, please see the defined `CELLULAR` targets in `mbed_app.json`.

- **Storage** - Specify the storage block device type, which dynamically adds the block device driver you specified at compile time. For example:

   ```
            "target.components_add" : ["SD"],
   ```

   Valid options are `SD`, `SPIF`, `QSPIF` and `FLASHIAP` (not recommended). For more available options, please see the [block device components](https://github.com/ARMmbed/mbed-os/tree/master/components/storage/blockdevice).

   You also have to specify block device pin configuration, which may vary from one block device type to another. Here's an example for `SD`:
      
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
   
- **SOTP** - Define two SOTP or NVStore regions that Mbed OS Device Management will use to store its special keys, which encrypt the data stored. Use the last two Flash sectors (if possible) to ensure that they don't get overwritten when new firmware is applied. For example:

   ```
            "device_management.sotp-section-1-address"            : "(MBED_CONF_APP_FLASH_START_ADDRESS + MBED_CONF_APP_FLASH_SIZE - 2*(128*1024))",
            "device_management.sotp-section-1-size"               : "(128*1024)",
            "device_management.sotp-section-2-address"            : "(MBED_CONF_APP_FLASH_START_ADDRESS + MBED_CONF_APP_FLASH_SIZE - 1*(128*1024))",
            "device_management.sotp-section-2-size"               : "(128*1024)",
            "device_management.sotp-num-sections" : 2
   ```

`*-address` defines the start of the Flash sector, and `*-size` defines the actual sector size. `sotp-num-sections` should always be set to `2`.

At this point, we recommend you run the "connect" test suite, which verifies that the device can successfully bootstrap, register and send and receive data from Pelion Device Management service with the provided configuration.

If you already configured your Pelion API key and initialized your credentials as described in the [previous section](#adding-device-management-feature-to-your-application), you can compile the "Connect" tests using:

```
$ mbed test -t <TOOLCHAIN> -m <BOARD> -n simple*dev*connect -DMBED_TEST_MODE --compile
```

To run the tests:

```
$ mbed test -t <TOOLCHAIN> -m <BOARD> -n simple*dev*connect --run -v
```

#### 2. Bootloader configuration

After you've successfully passed the "Connect" tests as described above, you can enable firmware update feature by adding a bootloader to your application.

1. Import as a new application the official [mbed-bootloader](https://github.com/ARMmbed/mbed-bootloader/) repository or the [mbed-bootloader-extended](https://github.com/ARMmbed/mbed-bootloader-extended/) repository that builds on top of `mbed-bootloader` and extends the support for file systems and storage drivers. You can do this with `mbed import mbed-bootloader-extended`.

1. Inside the imported bootloader application, and edit the application configuration, for example `mbed-bootloader-extended/mbed_app.json`. Add a new target entry similar to the step above, and specify:

   - **Flash** - Define the basics for the microcontroller flash (the same as in `mbed_app.json`). For example:
   
      ```
            "flash-start-address"              : "0x08000000",
            "flash-size"                       : "(2048*1024)",
      ```

   - **SOTP** - Similar to the **SOTP** step above, specify the location of the SOTP key storage. In the bootloader, the variables are named differently. Try to use the last two Flash sectors (if possible) to ensure that they don't get overwritten when new firmware is applied. For example:
   
    ```
            "nvstore.area_1_address"           : "(MBED_CONF_APP_FLASH_START_ADDRESS + MBED_CONF_APP_FLASH_SIZE - 2*(128*1024))",
            "nvstore.area_1_size"              : "(128*1024)",
            "nvstore.area_2_address"           : "(MBED_CONF_APP_FLASH_START_ADDRESS + MBED_CONF_APP_FLASH_SIZE - 1*(128*1024))", "nvstore.area_2_size" : "(128*1024)",
    ```

    - **Application offset** - Specify start address for the application, and also the update-client meta information. As these are automatically calculated, you can copy the ones below:
    
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
Before jumping to the next step, you should compile and flash the bootloader and then connect over the virtual comport to ensure the bootloader is running correctly. You can ignore errors related to checksum verification or falure to jump to application - these are expected at this stage.</span>

#### 3. Add the bootloader to your application

1. Copy the compiled bootloader from `mbed-bootloader-extended/BUILDS/<TARGET>/<TOOLCHAIN>-TINY/mbed-bootloader.bin` to `<your_application_name>/bootloader/mbed-bootloader-<TARGET>.bin`.

1. Edit `<your_application_name>/mbed_app.json`, and modify the target entry to include:

   ```
            "target.features_add"              : ["BOOTLOADER"],
            "target.bootloader_img"            : "bootloader/mbed-bootloader-<TARGET>.bin",
            "target.app_offset"                : "0x10400",
            "target.header_offset"             : "0x10000",
            "update-client.application-details": "(MBED_CONF_APP_FLASH_START_ADDRESS + 64*1024)",
   ```
 
   <span class="notes">**Note:**    
      - `update-client.application-details` should be identical in both `bootloader_app.json` and `mbed_app.json`.
      - `target.app_offset` is relative offset to `flash-start-address` you specified in `mbed_app.json` and `bootloader_app.json`, and is the hex value of the offset specified by `application-start-address` in `bootloader_app.json`. For example,  `(MBED_CONF_APP_FLASH_START_ADDRESS+65*1024)` dec equals `0x10400` hex.
      - `target.header_offset` is also relative offset to the `flash-start-address` you specified in the `bootloader_app.json`, and is the hex value of the offset specified by `update-client.application-details`. For example, `(MBED_CONF_APP_FLASH_START_ADDRESS+64*1024)` dec equals `0x10000` hex.</span>

1. Finally, compile and rerun all tests, including the firmware update ones with:

   ```
   $ mbed test -t <TOOLCHAIN> -m <BOARD> -n simple*dev*connect -DMBED_TEST_MODE --compile
   
   $ mbed test -t <TOOLCHAIN> -m <BOARD> -n simple*dev*connect --run -v
   ```

Refer to the next section about what tests are being executed.

### Validation and testing

Mbed Device Management provides built-in tests to help you when define your device management configuration. Before running these tests, we recommend you refer to the [testing setup](#testing-setup) section below. 

#### Test suites

| **Test suite** | **Description** |
| ------------- | ------------- |
| `fs-single` | File system single-threaded tests with write buffer sizes - 1 byte, 4b, 16b, 64b, 256b, 1kb, 4kb, 16kb, 64kb. |
| `fs-multi` | File system multithreaded test with write buffer sizes - 1 byte, 4b, 16b, 64b, 256b, 1kb, 4kb, 16kb, 64kb. |
| `net-single` | Network single-threaded test with receive buffer sizes - 128 bytes, 256b, 1kb, 2kb, 4kb. |
| `net-multi` | Network multithreaded test for 1, 2 and 3 download threads with 1kb receive buffer size. |
| `stress-net-fs` | Network and file system single and multithreaded tests:<ul><li>1 thread (sequential) - 1 download (1kb buffer), 1 file thread (1kb buffer)</li><li>2 parallel threads - 1 download, 1 file thread (1kb buffer)</li><li>3 parallel threads - 1 download, 2 file (256 bytes, 1 kb buffer)</li><li>4 parallel threads - 1 download, 3 file (1 byte, 256 bytes, 1kb buffer)</li></ul> |

#### Test cases - connect

| **Test case** | **Description** |
| ------------- | ------------- |
| `Connect to <Network type>` | Tests the connection to the network through the network interface. |
| `Initialize <Blockdevice>+<Filesystem>` | Initializes the block device driver and file system on top. Usually, the test will be stuck at this point if there's a problem with the storage device. |
| `Format <Filesystem>` | Tests that you can successfully format the block device for the file system type. |
| `Initialize Simple PDMC ` | Verifies you can initialize Pelion Device Management with the given network, storage and file system configuration. This is where the FCU and KCM configuration is written to storage and the Root of Trust is written to SOTP.
| `Pelion DM Bootstrap & Register` | Bootstraps the device and registers it for first time with Pelion Device Management. |
| `Pelion DM Directory` | Verifies that a registered device appears in the Device Directory in Pelion Device Management. |
| `Pelion DM Re-register` | Resets the device and reregisters with Pelion Device Management with previously bootstrapped credentials. |
| `Post-reset Identity` | Verifies that the device identity is preserved over device reset, confirming that Root of Trust is stored in SOTP correctly. |
| `ResourceLwM2M GET` | Verifies that the device can perform a GET request on an LwM2M resource. |
| `ResourceLwM2M SET Test` | Sets or changes value from the device and verifies the Pelion Device Management API client can observe the value changing. |
| `ResourceLwM2M PUT Test` | Verifies the device can perform a PUT request on an LwM2M resource by setting a new value. |
| `Resource LwM2M POST Test` | Verifies the device can execute a POST on an LwM2M resource and the callback function on the device is called. |

#### Test cases - update

| **Test case** | **Description** |
| ------------- | ------------- |
| `Connect to <Network type>` | Tests the connection to the network using the network interface. |
| `Initialize <Blockdevice>+<Filesystem>` | Initializes block device driver and file system on top. Usually the test will be stuck at this point if there's problem with the storage device. |
| `Format <Filesystem>` | Tests that you can successfully format the block device for the file system type. |
| `Initialize Simple PDMC ` | Verifies you can initialize Pelion Device Management with the given network, storage and file system configuration. This is where the FCU and KCM configuration is written to storage and the Root of Trust is written to SOTP.
| `Pelion DM Bootstrap & Register` | Bootstraps the device and registers it for first time with Pelion Device Management. |
| `Pelion DM Directory` | Verifies a registered device appears in the Device Directory in Pelion Device Management. |
| `Firmware Prepare` | Prepares the firmware on the host side and calls `mbed dm` to initiate the Pelion Device Management update campaign. |
| `Firmware Download` | Downloads the firmware onto the device. |
| `Firmware Update` | Resets the device, verifies that the firmware has correct checksum, applies it and reverifies the applied firmware checksum. |
| `Pelion DM Re-register` | Reregisters the device with Pelion Device Management using the new firmware and previously bootstrapped credentials. |
| `Post-update Identity` | Verifies that the device identity is preserved over firmware update and device reset, confirming that Root of Trust is stored in SOTP correctly. |

#### Requirements

Mbed Device Management tests rely on the Python SDK to test the end-to-end solution. To install the Python SDK:

```
 $ pip install mbed-cloud-sdk
```

<span class="notes">**Note:** The Python SDK requires Python 2.7.10+ or Python 3.4.3+, built with SSL support.</span>

#### Testing setup

1. Import an example application for Pelion Device Management that contains the corresponding configuration for your target. 

   Please refer to the following [application example](https://github.com/ARMmbed/pelion-ready-example). It demonstrates how to connect to the Pelion IoT Platform service, register resources and get ready to receive a firmware update.

   Also, there are board-specific applications that focus on providing more elaborate hardware features with Mbed OS and the Pelion IoT Platform. These are available in the Pelion [quick start](https://cloud.mbed.com/quick-start).

1. Set a global `mbed config` variable `CLOUD_SDK_API_KEY` on the host machine valid for the account your device will connect to. For example:

    ```
    $ mbed config -G CLOUD_SDK_API_KEY <API_KEY>
    ```

    For instructions on how to generate an API key, please [see the documentation](https://cloud.mbed.com/docs/current/integrate-web-app/api-keys.html#generating-an-api-key).

1. Initialize your Pelion DM credentials (once per project):

    ```
    $ mbed dm init -d "<your company name.com>" --model-name "<product model identifier>"
    ```

    This creates your private and public key pair and also initializes various `.c` files with these credentials, so you can use Connect and (firmware) Update device management features.

1. Remove the `main.cpp` application from the project, or ensure the content of the file is wrapped with `#ifndef MBED_TEST_MODE`.
 
1. Compile the tests with the `MBED_TEST_MODE` compilation flag.

    ```
    $ mbed test -t <toolchain> -m <platform> --app-config mbed_app.json -n simple-mbed-cloud-client-tests-* -DMBED_TEST_MODE --compile
    ```

1. Run the tests from the application directory:

    ```
    $ mbed test -t <toolchain> -m <platform> --app-config mbed_app.json -n simple-mbed-cloud-client-tests-* --run -v
    ```

#### Troubleshooting

Below are common issues and fixes.

##### Autoformatting failed with error -5005

This is due to an issue with the storage block device. If using an SD card, ensure that the SD card is seated properly.

##### SYNC_FAILED during testing

Occasionally, if the test failed during a previous attempt, the SMCC Greentea tests fail to sync. If this is the case, please replug your device to the host PC. Additionally, you may need to update your DAPLink or ST-Link interface firmware.

##### Device identity is inconsistent

If your device ID in Pelion Device Management is inconsistent over a device reset, it could be because it is failing to open the credentials on the storage held in the Enhanced Secure File System. Typically, this is because the device cannot access the Root of Trust stored in SOTP.

One way to verify this is to see if the storage is reformatted after a device reset when `format-storage-layer-on-error` is set to `1` in `mbed_app.json`.  It would appear on the serial terminal output from the device as:

```
[SMCC] Initializing storage.
[SMCC] Autoformatting the storage.
[SMCC] Reset storage to an empty state.
[SMCC] Starting developer flow
```

When this occurs, look at the SOTP sectors defined in `mbed_app.json`:

```
"sotp-section-1-address"           : "0xFE000",
"sotp-section-1-size"              : "0x1000",
"sotp-section-2-address"           : "0xFF000",
"sotp-section-2-size"              : "0x1000",
```

Ensure that the sectors are correct according to the flash layout of your device, and they are not being overwritten during the programming of the device. ST-Link devices overwrite these sectors when you use drag-and-drop of `.bin` files. Thus, moving the SOTP sectors to the end sectors of flash ensures they are not overwritten.

##### Stack overflow

If you receive a stack overflow error, increase the Mbed OS main stack size to at least 6000. You can do this by modifying the following parameter in `mbed_app.json`:

```
 "MBED_CONF_APP_MAIN_STACK_SIZE=6000",
```

##### Device failed to register

Check the device allocation on your Pelion account to see if you are allowed additional devices to connect. You can delete development devices. After being deleted, they will not count toward your allocation.

#### Known issues

Check open issues on [GitHub](https://github.com/ARMmbed/simple-mbed-cloud-client/issues).
