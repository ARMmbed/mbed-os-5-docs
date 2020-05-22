# Testing with the demo applications

You can use two applications to test your port:

1. When you've ported GPIO (and all preceeding modules), use `mbed-os-example-blinky`.
1. When you've ported all mandatory modules, use `mbed-cloud-client-example` (the Device Management Client runs on top of Mbed OS, and you don't need to manually port it). This test includes a reference bootloader for firmware update testing.

## mbed-os-example-blinky

1. Application repository: [https://github.com/ARMmbed/mbed-os-example-blinky](https://github.com/ARMmbed/mbed-os-example-blinky).
1. Import the repo, if you haven't done this already while porting:

    ```
    mbed import https://github.com/ARMmbed/mbed-os-example-blinky.git
    cd mbed-os-example-blinky
    ```
1. If your target has not been merged into `mbed-os`, replace `mbed-os` with your fork. (Change the URL to match your repository.)

    ```
    mbed remove mbed-os
    mbed add https://github.com/ARMmbed/mbed-os-new-target mbed-os
    ```

1. Build the image:

    ```
    mbed compile -m <new_target> -t gcc_arm
    ```
1. Flash the image (.bin or .hex) to the board.
1. Verify the designated LED flashes every 0.5 second. You can use an oscilloscope for accurate measurement.


## mbed-cloud-client-example

Start with building the bootloader, which you will need for the firmware update portion of this test:


1. Application repository: [https://github.com/armmbed/mbed-bootloader](https://github.com/armmbed/mbed-bootloader).
    1. If your target is not merged into `mbed-os` yet you will need to follow the same process as detailed above for adding your fork.
1. Build the image:

    ```
    mbed compile -m <new_target> -t gcc_arm --profile=tiny.json
    ```

1. Flash the image (.bin or .hex) to the board.
1. Verify the following on the terminal. Note: The value on the last line will be different.

    ```
    [BOOT] Mbed Bootloader

    [BOOT] ARM: 00000000000000000000

    [BOOT] OEM: 00000000000000000000

    [BOOT] Layout: 0 1006F44
    ```

Then, test connectivity and firmware update:

1. Application repository:[https://github.com/armmbed/mbed-cloud-client-example](https://github.com/armmbed/mbed-cloud-client-example).
    1. Again, if you have not merged your target into `mbed-os` you will need to add your fork.
1. [Set up a Pelion Device Management account](https://cloud.mbed.com/docs/latest/account-management/users.html).
1. [Generate an API key](https://cloud.mbed.com/docs/latest/integrate-web-app/api-keys.html) from the [Device Management Portal](https://portal.mbedcloud.com//login).
1. In the `mbed-cloud-client-example` clone on your machine, run the following command with the generated API key:

   ```
   $ mbed config -G CLOUD_SDK_API_KEY <API_KEY>
   $ mbed target <new_target>
   $ mbed toolchain gcc_arm
   $ mbed dm init -d "<company domain name>" --model-name <new_target>
   ```

   This creates two files: `update_default_resources.c` and `mbed_cloud_dev_credentials.c`. Add these files to your build.

1. You need to customize three files before building:
   - Add the new target to `mbed-cloud-client-example/mbed_app.json`. For example, the code block below adds `CC3220SF`:

      ```
      ...
          "target.macros_remove" : ["MBEDTLS_CONFIG_HW_SUPPORT"]
      },
      "CC3220SF": {
          "target.network-default-interface-type" : "WIFI",
          "update-client.bootloader-details" : "0x01006F44",
          "update-client.application-details" : "0x01008000",
          "client_app.auto_partition": "1"
      }
      ```

      Note that `bootloader-details` is the value displayed on your serial terminal program when you run the mbed-bootloader program.

   - If your target uses WiFi, fill in the SSID and Password fields in `mbed_app.json`.

   - Add [NVStore descriptors (previously known as SOTP)](https://cloud.mbed.com/docs/porting/porting-a-new-target-for-mbed-os.html) for storage to `mbed-cloud-client-example/mbed_lib.json`. For example:

      ```
      ...
          "sotp-section-2-size"              : "(16*1024)"
       },
       "CC3220SF": {
           "sotp-section-1-address"           : "(0x01000000+1020*1024)",
           "sotp-section-1-size"              : "(2*1024)",
           "sotp-section-2-address"           : "(0x01000000+1022*1024)",
           "sotp-section-2-size"              : "(2*1024)"
       }
      ```

1. Build the image:

   ```
   mbed compile -m <new_target> -t gcc_arm
   ```

1. Flash the image (.bin or .hex) to the board.
1. Verify your serial output is similar to:

   ```
   [BOOT] Mbed Bootloader

   [BOOT] ARM: 00000000000000000000

   [BOOT] OEM: 00000000000000000000

   [BOOT] Layout: 0 1006F44

   [BOOT] Active firmware integrity check:

   [BOOT] [++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]

   [BOOT] SHA256: ABAF3AC1F2D7B8173BC5540DA50E7093C8A479E4C0148090348BD1EA68A0958F

   [BOOT] Version: 1539890967

   [BOOT] Slot 0 is empty

   [BOOT] Active firmware up-to-date

   [BOOT] Application's start address: 0x1008400

   [BOOT] Application's jump address: 0x1046081

   [BOOT] Application's stack address: 0x20040000

   [BOOT] Forwarding to application...



   mcc_platform_storage_init() - bd->size() = 16021192704

   mcc_platform_storage_init() - BlockDevice init OK.

   Application ready. Build at: Oct 18 2018 14:29:26

   Mbed OS version 99.99.99

   Start simple mbed Cloud Client

   Using hardcoded Root of Trust, not suitable for production use.

   Starting developer flow

   mcc_platform_init_connection()

   NSAPI_STATUS_CONNECTING

   NSAPI_STATUS_GLOBAL_UP

   Network initialized, connecting...



   Client registered

   Endpoint Name: 016688bda0740000000000010010007a

   Device Id: 016688bda0740000000000010010007a
   ```

1. Verify that the device is registered by finding it in the [Device Management Portal](https://portal.mbedcloud.com//login).
1. Make a change in the application, and rebuild the firmware.
1. Perform a firmware update:

   ```
   $ mbed dm update device -D <device ID> -m <new_target>
   ```

   The following serial output is expected if firmware update is successful:

   ```
   Firmware download requested

   Authorization granted

   Downloading: [++++++++++++++++++++++++++++++++++++++++++++++++++] 100 %

   Download completed

   Firmware install requested

   Authorization granted
   ```

   Power cycle the board.

1. Verify the newer firmware is running on the device. The serial output should display the following:

   ```
   [BOOT] Mbed Bootloader

   [BOOT] ARM: 00000000000000000000

   [BOOT] OEM: 00000000000000000000

   [BOOT] Layout: 0 1006F44

   [BOOT] Active firmware integrity check:

   [BOOT] [++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]

   [BOOT] SHA256: ABAF3AC1F2D7B8173BC5540DA50E7093C8A479E4C0148090348BD1EA68A0958F

   [BOOT] Version: 1539890967

   [BOOT] Slot 0 firmware integrity check:

   [BOOT] [++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]

   [BOOT] SHA256: ABAF3AC1F2D7B8173BC5540DA50E7093C8A479E4C0148090348BD1EA68A0958F

   [BOOT] Version: 1539892842

   [BOOT] Update active firmware using slot 0:

   [BOOT] [++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]

   [BOOT] Verify new active firmware:

   [BOOT] [++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]

   [BOOT] New active firmware is valid

   [BOOT] Application's start address: 0x1008400

   [BOOT] Application's jump address: 0x1046081

   [BOOT] Application's stack address: 0x20040000

   [BOOT] Forwarding to application...



   mcc_platform_storage_init() - bd->size() = 16021192704

   mcc_platform_storage_init() - BlockDevice init OK.

   Application ready. Build at: Oct 18 2018 14:29:26

   Mbed OS version 99.99.99

   Start simple mbed Cloud Client

   Using hardcoded Root of Trust, not suitable for production use.

   Starting developer flow

   Developer credentials already exist, continuing..

   mcc_platform_init_connection()

   NSAPI_STATUS_CONNECTING

   NSAPI_STATUS_GLOBAL_UP

   Network initialized, connecting...



   Client registered

   Endpoint Name: 016688bda0740000000000010010007a

   Device Id: 016688bda0740000000000010010007a
   ```
