## Testing your port

It's important to test your port at the end of each module porting, rather than only once when you've imported all modules. There are three testing methods:

1. Using the Mbed OS built-in tests with *Greentea*.
1. Using the Mbed OS built-in tests with *manual testing*.
1. Testing with the example applications.


## Testing with the Greentea framework

<!--does Greentea only work with eclipse?--><!--what if I'm not using eclipse?-->
<!--did we actually ask people to install Greentea? I don't see it in the lists, unless it's bundled into Mbed CLI-->
<!--We don't currently link to user docs for Greentea, but we really should - I'm just not sure which link to use-->

<!--I can only find eclipse content in debugging, not in testing, and not in the page covering Greentea-->
<!--../tutorials/eclipse.html-->
<!--[https://os.mbed.com/docs/latest/tools/greentea-testing-applications.html](../tools/greentea-testing-applications.html)-->

Read the following page to understand how tests are structured and exported into Eclipse:

### Prerequisites

#### Minimum component support

To run the Mbed OS built-in tests, you need to have ported and verified at least these components:
<!--modules - make sure we don't use components-->

- DAPLink.

    <span class="notes">If DAPLink is still under development, please [use manual tests](#manual-testing).</span>
- Low power ticker.
- Serial port (synchronous transfer). To verify that it works, load a test binary with `printf()`. Verify debug messages can be seen on your serial terminal program.
- Microsecond ticker.

#### mbedls

<!--did we ask them to install that? I don't think we've mentioned it. We need a section that discusses the testing tools
Get Brian to confirm whether it's part of the Mbed OS installation or whether we need a new bit in the installation list to cover Greentea and mbedls-->

The board under test needs to be supported in mbedls for automated tests to work.

If the official mbedls pip package hasn't been released yet, you need to direct pip to use your local directory (which includes the  code changes to support the new board):

1. Clone [https://github.com/ARMmbed/mbed-ls](https://github.com/ARMmbed/mbed-ls).
1. Run `pip install --editable <your_local_root_to_mbed-ls>`.
1. Create an `mbedls.json` file. This file allows you to override and specify the FTDI USB port.

    The serial port path varies in different operation systems. On **Windows**, you can find it through Device Manager; it will usually be something like `COM#`. On **Mac OS** and Linux, you can use `ls /dev/tty.usb*`:

    ```
    {
        "33000000e062afa300000000000000000000000097969902": {
            "serial_port": "/dev/tty.usbserial-FTGDJJOC"
        }
    }
    ```

### Compiling and running tests

1. Compile your tests:
    - To compile all tests, run `mbed test -compile`.
    - To see the list of compiled tests, run `mbed test --compile-list`.
    - To compile a specific test, run  `mbed test -compile -n <test_name>`. For example: `mbed test --compile -n tests-concurrent-gpio)`.
1. To run your tests, run `mbedgt`.


Here is an example of a successful run:

```
mbedgt: greentea test automation tool ver. 1.4.0
mbedgt: using multiple test specifications from current directory!
    using 'BUILD/tests/CC3220SF/GCC_ARM/test_spec.json'
mbedgt: detecting connected mbed-enabled devices...
mbedgt: detected 1 device
mbedgt: processing target 'CC3220SF' toolchain 'GCC_ARM' compatible platforms... (note: switch set to --parallel 1)
mbedgt: running 1 test for platform 'CC3220SF' and toolchain 'GCC_ARM'
mbedgt: mbed-host-test-runner: started
mbedgt: checking for GCOV data...
mbedgt: test on hardware with target id: 33000000e062afa300000000000000000000000097969902
mbedgt: test suite 'tests-concurrent-gpio' ........................................................... OK in 19.25 sec
    test case: 'Concurrent testing of DIO(D0,D1), and InterruptIn(D2,D3)' ........................ OK in 0.09 sec
    test case: 'Concurrent testing of DIO(D1,D0), and InterruptIn(D3,D2)' ........................ OK in 0.07 sec
    test case: 'Concurrent testing of DIO(D2,D3), and InterruptIn(D4,D5)' ........................ OK in 0.08 sec
    test case: 'Concurrent testing of DIO(D3,D2), and InterruptIn(D5,D4)' ........................ OK in 0.10 sec
    test case: 'Concurrent testing of DIO(D4,D5), and InterruptIn(D0,D1)' ........................ OK in 0.09 sec
    test case: 'Concurrent testing of DIO(D4,D5), and InterruptIn(D2,D3)' ........................ OK in 0.10 sec
    test case: 'Concurrent testing of DIO(D5,D4), and InterruptIn(D1,D0)' ........................ OK in 0.09 sec
    test case: 'Concurrent testing of DIO(D5,D4), and InterruptIn(D3,D2)' ........................ OK in 0.09 sec
    test case: 'Concurrent testing of DIO(D6,D7), and InterruptIn(D8,D9)' ........................ OK in 0.09 sec
    test case: 'Concurrent testing of DIO(D7,D6), and InterruptIn(D9,D8)' ........................ OK in 0.10 sec
    test case: 'Concurrent testing of DIO(D8,D9), and InterruptIn(D2,D3)' ........................ OK in 0.08 sec
    test case: 'Concurrent testing of DIO(D9,D8), and InterruptIn(D3,D2)' ........................ OK in 0.10 sec
mbedgt: test case summary: 12 passes, 0 failures
mbedgt: all tests finished!
mbedgt: shuffle seed: 0.3988791596
mbedgt: test suite report:
+------------------+---------------+-----------------------+--------+--------------------+-------------+
| target           | platform_name | test suite            | result | elapsed_time (sec) | copy_method |
+------------------+---------------+-----------------------+--------+--------------------+-------------+
| CC3220SF-GCC_ARM | CC3220SF      | tests-concurrent-gpio | OK     | 19.25              | default     |
+------------------+---------------+-----------------------+--------+--------------------+-------------+
mbedgt: test suite results: 1 OK
mbedgt: test case report:
+------------------+---------------+-----------------------+----------------------------------------------------------+--------+--------+--------+--------------------+
| target           | platform_name | test suite            | test case                                                | passed | failed | result | elapsed_time (sec) |
+------------------+---------------+-----------------------+----------------------------------------------------------+--------+--------+--------+--------------------+
| CC3220SF-GCC_ARM | CC3220SF      | tests-concurrent-gpio | Concurrent testing of DIO(D0,D1), and InterruptIn(D2,D3) | 1      | 0      | OK     | 0.09               |
| CC3220SF-GCC_ARM | CC3220SF      | tests-concurrent-gpio | Concurrent testing of DIO(D1,D0), and InterruptIn(D3,D2) | 1      | 0      | OK     | 0.07               |
| CC3220SF-GCC_ARM | CC3220SF      | tests-concurrent-gpio | Concurrent testing of DIO(D2,D3), and InterruptIn(D4,D5) | 1      | 0      | OK     | 0.08               |
| CC3220SF-GCC_ARM | CC3220SF      | tests-concurrent-gpio | Concurrent testing of DIO(D3,D2), and InterruptIn(D5,D4) | 1      | 0      | OK     | 0.1                |
| CC3220SF-GCC_ARM | CC3220SF      | tests-concurrent-gpio | Concurrent testing of DIO(D4,D5), and InterruptIn(D0,D1) | 1      | 0      | OK     | 0.09               |
| CC3220SF-GCC_ARM | CC3220SF      | tests-concurrent-gpio | Concurrent testing of DIO(D4,D5), and InterruptIn(D2,D3) | 1      | 0      | OK     | 0.1                |
| CC3220SF-GCC_ARM | CC3220SF      | tests-concurrent-gpio | Concurrent testing of DIO(D5,D4), and InterruptIn(D1,D0) | 1      | 0      | OK     | 0.09               |
| CC3220SF-GCC_ARM | CC3220SF      | tests-concurrent-gpio | Concurrent testing of DIO(D5,D4), and InterruptIn(D3,D2) | 1      | 0      | OK     | 0.09               |
| CC3220SF-GCC_ARM | CC3220SF      | tests-concurrent-gpio | Concurrent testing of DIO(D6,D7), and InterruptIn(D8,D9) | 1      | 0      | OK     | 0.09               |
| CC3220SF-GCC_ARM | CC3220SF      | tests-concurrent-gpio | Concurrent testing of DIO(D7,D6), and InterruptIn(D9,D8) | 1      | 0      | OK     | 0.1                |
| CC3220SF-GCC_ARM | CC3220SF      | tests-concurrent-gpio | Concurrent testing of DIO(D8,D9), and InterruptIn(D2,D3) | 1      | 0      | OK     | 0.08               |
| CC3220SF-GCC_ARM | CC3220SF      | tests-concurrent-gpio | Concurrent testing of DIO(D9,D8), and InterruptIn(D3,D2) | 1      | 0      | OK     | 0.1                |
+------------------+---------------+-----------------------+----------------------------------------------------------+--------+--------+--------+--------------------+
mbedgt: test case results: 12 OK
mbedgt: completed in 20.24 sec
```

## Manual testing

You may want to run manual tests, for example if DAPLink is still under development. You will need to export your tests from Greentea and import them to your IDE. For example, to work with Eclipse:

1. Find the test directory:

    ```
    mbed test --compile-list -n mbed-os-tests-mbed_hal-common_ticker
    ```

1. Copy the source code to the project root directory:

    ```
    cd <root_dir>
    cp -R mbed-os-example-blinky/mbed-os/TESTS/mbed_hal/common_tickers .
    cd common_tickers
    mbed new .
    rm -rf mbed-os
    ```

1. Copy the `mbed-os` directory:

    ```
    cp -R ../mbed-os-example-blinky/mbed-os .
    ```

1. Export to a makefile project:

    ```
    mbed export -i gcc_arm -m <new_target>
    ```

1. Open the project with pyOCD (using the same configuration you used [when you initially set up pyOCD]( Creating GDB pyOCD debug configuration).

1. Run the program:

    ```
    # mbedhtrun --skip-flashing --skip-reset -p <serial port>:9600 -e mbed-os/TESTS/host_tests
    ```

    Customize the serial port path and baudrate as needed.


## Mbed OS built-in tests - detailed procedure

Whether you're using Greentea or performing manual tests, the procedure for using the built-in Mbed OS tests is the same.

To build and run the Mbed OS tests:

1. In your `mbed-os-example-blinky` clone, rename `main.cpp` to `main.txt`:

   ```
   mv main.cpp main.txt
   ```

1. Build the tests:

   ```
   mbed test --compile -m <new_target> -t gcc_arm -c
   ```

   You'll see some build errors. These errors should reduce and eventually disappear as more HAL components are ported.

1. To run the tests, go to the `mbed-os` directory.

   ```
   cd mbed-os
   ```

   You can see the full list of built tests:


    ```
    mbed test --compile-list
    ```

1. Test images are located under the following directory:

    ```
    mbed-os-example-blinky/BUILD/tests/<new_target>/gcc_arm/mbed-os/
    ```

    For example:

    ```
    $ mbed test --compile-list | grep common_tickers

        Test Case:

    Name: tests-mbed_hal-common_tickers

    Path: ./TESTS/mbed_hal/common_tickers

      Test Case:

          Name: tests-mbed_hal-common_tickers_freq

          Path: ./TESTS/mbed_hal/common_tickers_freq
    ```

    In this example:

    - The `common_tickers` test image is at `mbed-os-example-blinky/BUILD/tests/<new_target>/gcc_arm/mbed-os/TESTS/mbed_hal/common_tickers`.
    - The `common_tickers_freq` test image is at `mbed-os-example-blinky/BUILD/tests/<new_target>/gcc_arm/mbed-os/TESTS/mbed_hal/common_tickers_freq.`

1. You need to flash the test image to the board. You can use either DAPLink or Eclipe IDE. You may also be able to use IAR and Keil (if they already support the new target).

    The easiest method is using the pyOCD flash tool:

    ```
    pyocd-flashtool BUILD/mbed-os-example-blinky.bin or
    pyocd-flashtool BUILD/mbed-os-example-blinky.hex
    ```

1. Before you begin the test run, please make sure the serial port is not already opened by programs like Screen or Teraterm (close them if they're open). In addition, verify `mbedls` lists the new target device.

    If your test run doesn't start, read [the Greentea documentation for troubleshooting](https://github.com/armmbed/greentea).
    <!--do we have this within the docs, rather than on GitHub?-->

## Demo applications

The `mbed-os-example-blinky` application should run after GPIO is ported.

The `mbed-cloud-client-example` application should run after the Device Management Client is ported. It includes a reference bootloader.

### mbed-os-example-blinky

1. Application repository: [https://github.com/ARMmbed/mbed-os-example-blinky](https://github.com/ARMmbed/mbed-os-example-blinky).
1. Clone the repo, if you haven't done this already while porting:

    ```
    git clone https://github.com/ARMmbed/mbed-os-example-blinky.git
    cd mbed-os-example-blinky
    ```

1. Open a text editor and change the link in `mbed-os.lib` to `https://github.com/ARMmbed/mbed-os-new-target`, if you haven't done this already while porting.

    Skip this step if `mbed-os-new-target` has been merged into `mbed-os`.

1. Build the image:

    ```
    vi mbed-os.lib
    mbed deploy
    mbed compile --target <new_target> --toolchain GCC_ARM
    ```
1. Flash the image (.bin or.hex) to the board.
1. Verify the designated LED flashes every 0.5 second. You can use an oscilloscope.


### mbed-cloud-client-example

Start with building the bootloader, which you will need for the firmware update portion of this test:


1. Application repository: [https://github.com/armmbed/mbed-bootloader](https://github.com/armmbed/mbed-bootloader).
1. Build the image:

    ```
    cd mbed-os-bootloader
    mbed deploy
    mbed compile --target <new_target> --toolchain GCC_ARM --profile=tiny.json
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
1. [Set up a Pelion account](https://cloud.mbed.com/docs/current/account-management/users.html).
1. [Generate an API key](https://cloud.mbed.com/docs/current/integrate-web-app/api-keys.html) from the [Device Management Portal](https://portal.mbedcloud.com//login).
1. In the `mbed-cloud-client-example` clone on your machine, run the following command with the generated API key:

   ```
   $ mbed config -G CLOUD_SDK_API_KEY <API_KEY>
   $ mbed target <new_target>
   $ mbed toolchain GCC_ARM
   $ mbed dm init -d "<company domain name>" --model-name <new_target>
   ```

   This creates two files: `update_default_resources.c` and `mbed_cloud_dev_credentials.c`. Add these files to your build.

1. You need to customize four files before building:

   - Modify `mbed-os.lib` by changing the URL to `https://github.com/ARMmbed/mbed-os-new-target`.
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

   - Add SOTP descriptors to `mbed-cloud-client-example/mbed_lib.json`. For example:

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
   cd mbed-cloud-client-example
   mbed deploy
   mbed compile --target <new_target> --toolchain GCC_ARM
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
1. Make change in the Device Management Client and rebuild the firmware.
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
