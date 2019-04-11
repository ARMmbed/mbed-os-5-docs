<h1 id="device-management-test">Validation and testing</h1>

Device Management provides built-in tests to help you define your device management configuration. Before running these tests, we recommend you refer to the [testing setup](#testing-setup) section below.

## Test suites

| **Test suite** | **Description** |
| ------------- | ------------- |
| `fs-single` | File system single-threaded tests with write buffer sizes - 1 byte, 4b, 16b, 64b, 256b, 1kb, 4kb, 16kb, 64kb. |
| `fs-multi` | File system multithreaded test with write buffer sizes - 1 byte, 4b, 16b, 64b, 256b, 1kb, 4kb, 16kb, 64kb. |
| `net-single` | Network single-threaded test with receive buffer sizes - 128 bytes, 256b, 1kb, 2kb, 4kb. |
| `net-multi` | Network multithreaded test for 1, 2 and 3 download threads with 1kb receive buffer size. |
| `stress-net-fs` | Network and file system single and multithreaded tests:<ul><li>1 thread (sequential) - 1 download (1kb buffer), 1 file thread (1kb buffer)</li><li>2 parallel threads - 1 download, 1 file thread (1kb buffer)</li><li>3 parallel threads - 1 download, 2 file (256 bytes, 1 kb buffer)</li><li>4 parallel threads - 1 download, 3 file (1 byte, 256 bytes, 1kb buffer)</li></ul> |

## Test cases - connect

| **Test case** | **Description** |
| ------------- | ------------- |
| `Connect to <Network type>` | Tests the connection to the network through the network interface. |
| `Initialize <Blockdevice>+<Filesystem>` | Initializes the block device driver and file system on top. Usually, the test will be stuck at this point if there's a problem with the storage device. |
| `Format <Filesystem>` | Tests that you can successfully format the block device for the file system type. |
| `Initialize Simple PDMC ` | Verifies you can initialize Device Management with the given network, storage and file system configuration. This is where the FCU and KCM configuration is written to storage and the Root of Trust is written to SOTP.
| `Pelion DM Bootstrap & Register` | Bootstraps the device and registers it for first time with Device Management. |
| `Pelion DM Directory` | Verifies that a registered device appears in the Device Directory in Device Management. |
| `Pelion DM Re-register` | Resets the device and reregisters with Device Management with previously bootstrapped credentials. |
| `Post-reset Identity` | Verifies that the device identity is preserved over device reset, confirming that Root of Trust is stored in SOTP correctly. |
| `ResourceLwM2M GET` | Verifies that the device can perform a GET request on an LwM2M resource. |
| `ResourceLwM2M SET Test` | Sets or changes value from the device and verifies the Device Management API client can observe the value changing. |
| `ResourceLwM2M PUT Test` | Verifies the device can perform a PUT request on an LwM2M resource by setting a new value. |
| `Resource LwM2M POST Test` | Verifies the device can execute a POST on an LwM2M resource and the callback function on the device is called. |

## Test cases - update

| **Test case** | **Description** |
| ------------- | ------------- |
| `Connect to <Network type>` | Tests the connection to the network using the network interface. |
| `Initialize <Blockdevice>+<Filesystem>` | Initializes block device driver and file system on top. Usually the test will be stuck at this point if there's problem with the storage device. |
| `Format <Filesystem>` | Tests that you can successfully format the block device for the file system type. |
| `Initialize Simple PDMC ` | Verifies you can initialize Device Management with the given network, storage and file system configuration. This is where the FCU and KCM configuration is written to storage and the Root of Trust is written to SOTP.
| `Pelion DM Bootstrap & Register` | Bootstraps the device and registers it for first time with Device Management. |
| `Pelion DM Directory` | Verifies a registered device appears in the Device Directory in Device Management. |
| `Firmware Prepare` | Prepares the firmware on the host side and calls `mbed dm` to initiate the Device Management update campaign. |
| `Firmware Download` | Downloads the firmware onto the device. |
| `Firmware Update` | Resets the device, verifies that the firmware has correct checksum, applies it and reverifies the applied firmware checksum. |
| `Pelion DM Re-register` | Reregisters the device with Device Management using the new firmware and previously bootstrapped credentials. |
| `Post-update Identity` | Verifies that the device identity is preserved over firmware update and device reset, confirming that Root of Trust is stored in SOTP correctly. |

## Requirements

Device Management tests rely on the Python SDK to test the end-to-end solution. To install the Python SDK:

```
 $ pip install mbed-cloud-sdk
```

<span class="notes">**Note:** The Python SDK requires Python 2.7.10+ or Python 3.4.3+, built with SSL support.</span>

## Testing setup

1. Import an example application for Device Management that contains the corresponding configuration for your target.

   Please refer to the following [application example](https://github.com/ARMmbed/pelion-ready-example). It demonstrates how to connect to the Device Management service, register resources and get ready to receive a firmware update.

   Also, there are board-specific applications that focus on providing more elaborate hardware features with Mbed OS and Device Management. These are available in the Pelion [quick start](https://cloud.mbed.com/quick-start).

1. Set a global `mbed config` variable `CLOUD_SDK_API_KEY` on the host machine valid for the account your device will connect to. For example:

    ```
    $ mbed config -G CLOUD_SDK_API_KEY <API_KEY>
    ```

    For instructions on how to generate an API key, please [see the documentation](https://cloud.mbed.com/docs/current/integrate-web-app/api-keys.html#generating-an-api-key).

1. Initialize your Device Management credentials (once per project):

    ```
    $ mbed dm init -d "<your company name.com>" --model-name "<product model identifier>"
    ```

    This creates your private and public key pair and also initializes various `.c` files with these credentials, so you can use Device Management Connect and (firmware) Update.

1. Remove the `main.cpp` application from the project, or ensure the content of the file is wrapped with `#ifndef MBED_TEST_MODE`.

1. Compile the tests with the `MBED_TEST_MODE` compilation flag.

    ```
    $ mbed test -t <toolchain> -m <platform> --app-config mbed_app.json -n simple-mbed-cloud-client-tests-* -DMBED_TEST_MODE --compile
    ```

1. Run the tests from the application directory:

    ```
    $ mbed test -t <toolchain> -m <platform> --app-config mbed_app.json -n simple-mbed-cloud-client-tests-* --run -v
    ```

## Troubleshooting

Below are common issues and fixes.

### Autoformatting failed with error -5005

This is due to an issue with the storage block device. If using an SD card, ensure that the SD card is seated properly.

### SYNC_FAILED during testing

Occasionally, if the test failed during a previous attempt, the SMCC Greentea tests fail to sync. If this is the case, please replug your device to the host PC. Additionally, you may need to update your DAPLink or ST-Link interface firmware.

### Device identity is inconsistent

If your device ID in Device Management is inconsistent when your device resets, it could be because it is failing to open the credentials on the storage held in the Enhanced Secure File System. Typically, this is because the device cannot access the Root of Trust stored in SOTP.

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

### Stack overflow

If you receive a stack overflow error, increase the Mbed OS main stack size to at least 6000. You can do this by modifying the following parameter in `mbed_app.json`:

```
 "MBED_CONF_APP_MAIN_STACK_SIZE=6000",
```

### Device failed to register

Check the device allocation on your Device Management account to see if you are allowed additional devices to connect. You can delete development devices. After being deleted, they will not count toward your allocation.

## Known issues

Check open issues on [GitHub](https://github.com/ARMmbed/simple-mbed-cloud-client/issues).
