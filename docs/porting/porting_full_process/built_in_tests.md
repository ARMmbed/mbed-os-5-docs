## Testing your port

It's important to test your port at the end of each module porting, rather than only once when you've imported all modules. There are three testing methods:

1. Using the Mbed OS built-in tests with *Greentea*.
1. Using the Mbed OS built-in tests with *manual testing*.
1. Testing with the example applications.


## Testing with the Greentea framework

<!--does Greentea only work with eclipse?--><!--what if I'm not using eclipse?-->
<!--From Jimmy: Greentea isn't designed to be used with Eclipse. Eclipse can do something, but it's designed to be run from the command-line.-->
<!--did we actually ask people to install Greentea? I don't see it in the lists, unless it's bundled into Mbed CLI-->
<!--From Jimmy: Mbed CLI will install Greentea for you, but that may change in the future.-->
<!--We don't currently link to user docs for Greentea, but we really should - I'm just not sure which link to use-->

<!--I can only find eclipse content in debugging, not in testing, and not in the page covering Greentea-->
<!--From Jimmy: Becuse Eclipse is unrelated-->
<!--../tutorials/eclipse.html-->
<!--[https://os.mbed.com/docs/latest/tools/greentea-testing-applications.html](../tools/greentea-testing-applications.html)-->

Read the following page to understand how tests are structured and exported into Eclipse:
<!--From Jimmy: Don't export tests to Eclipse or at all. It's not supported, AKA not in CI-->

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
<!--From Jimmy: Mbed CLI automatically installs mbed ls, yes, but that may change in the future-->

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
    <!--do we have this within the docs, rather than on GitHub? Answer: We think it's this: https://github.com/armmbed/greentea#common-issues We can add this to our docs.-->
