# Testing your port

It's important to test your port at the end of each module porting, rather than only once when you've imported all modules. There are two testing methods:

1. Running the Mbed OS built-in tests with [*Greentea*](../tools/greentea-testing-applications.html).
1. Manually running the Mbed OS built-in tests.

# Testing with the Greentea framework

Read the following page to understand how tests are structured:

## Prerequisites

### Minimum HAL module support

To run the Mbed OS built-in tests, you need to have ported and verified at least these HAL modules:

- Low power ticker.
- Serial port (synchronous transfer). To verify that it works, load a test binary with `printf()`. Verify debug messages can be seen on your serial terminal program.
- Microsecond ticker.


You'll also need to have ported DAPLink or compatible interface firmware to your interface chip.
    <span class="notes">If DAPLink is still under development, you can still [run tests manually](../porting/manual-testing.html).</span>

### mbedls

The platform under test needs to be supported in mbedls for automated tests to work.

If an updated mbedls pip package including support for your platform hasn't been released yet, you need to direct pip to use your local directory (which includes the code changes to support the new platform):

1. Clone [https://github.com/ARMmbed/mbed-os-tools](https://github.com/ARMmbed/mbed-os-tools).
1. [Add your target to the platform database](https://github.com/ARMmbed/mbed-os-tools/tree/master/packages/mbed-ls#adding-platform-support)
1. Run `pip install --editable <your_local_root_to_mbed-os-tools>`.
1. Run `pip install --editable <your_local_root_to_mbed-os-tools>/packages/mbed-ls`.
1. If you're using an external serial probe (like an FTDI USB cable), create an `mbedls.json` file and specify the serial port.

    The serial port path varies in different operation systems. On **Windows**, you can find it through Device Manager; it will usually be something like `COM#`. On **Mac OS** you can use `ls /dev/tty.usb*`. On Linux you can use `ls /dev/ttyACM*`. The format of `mbedls.json` is as follows:

    ```
    {
        "33000000e062afa300000000000000000000000097969902": {
            "serial_port": "/dev/tty.usbserial-FTGDJJOC"
        }
    }
    ```

    Where `"33000000e062afa300000000000000000000000097969902"` is the correct target id.

## Compiling and running tests

1. Compile the tests:
    - To compile all tests, run `mbed test --compile`.
    - To see the list of compiled tests, run `mbed test --compile-list`.
    - To compile a specific test, run  `mbed test --compile -n <test_name>`. For example: `mbed test --compile -n mbed-os-tests-concurrent-gpio)`.
1. To run your tests, run `mbed test --run`.


Here is an example of a successful run:

<!-- Needs to be updated with output from mbed-cli (mbed test) -->
```
mbed test --run -n tests-concurrent-gpio
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

# Manual testing

You may want to run tests manually, for example if DAPLink is still under development. You will need to export your tests from Greentea and import them to your IDE. For example:

1. Find the test directory:

    ```
    mbed test -m <new_target> -t gcc_arm --compile-list -n mbed-os-tests-mbed_hal-common_ticker
    ```

1. Copy the source code to the project root directory:

    ```
    cd <separate folder from existing porting project>
    cp -R mbed-os-example-blinky/mbed-os/TESTS/mbed_hal/common_tickers .
    cd common_tickers
    mbed new --create-only .
    ```

1. Copy the `mbed-os` directory:

    ```
    cp -R ../mbed-os-example-blinky/mbed-os .
    ```

1. Export to a makefile project:

    ```
    mbed export -i <exporter> -m <new_target>
    ```

1. Flash the program with pyOCD (using the same configuration you used [when you initially set up pyOCD](#creating-GDB-pyOCD-debug-configuration).

1. Run the program:

    ```
    # mbedhtrun --skip-flashing --skip-reset -p <serial port>:9600 -e mbed-os/TESTS/host_tests
    ```

    Customize the serial port path and baudrate as needed.


# Mbed OS built-in tests - detailed procedure

Whether you're using Greentea or performing manual tests, the procedure for using the built-in Mbed OS tests is the same.

To build and run the Mbed OS tests:

1. Build the tests:

   ```
   mbed test -m <new_target> -t gcc_arm --compile
   ```

   If you see some build errors, it means that some HAL modules required to run the tests are missing and need porting.

1. You can see the full list of built tests:

    ```
    mbed test -m <new_target> -t gcc_arm --compile-list
    ```

1. Test images are located under the following directory:

    ```
    mbed-os-example-blinky/BUILD/tests/<new_target>/gcc_arm/mbed-os/
    ```

    For example:

    ```
    $ mbed test -m <new_target> -t gcc_arm --compile-list -n *tickers*

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

1. You need to flash the test image to the board. You can use pyOCD (from the command line or IDE), or you could use IAR and Keil (if they already support the new target).

    The easiest method is using the pyOCD flash tool:

    ```
    pyocd-flashtool BUILD/mbed-os-example-blinky.bin    # Use the .hex file if appropriate
    ```

1. Before you begin the test run, please make sure the serial port is not already opened by programs like Screen or Teraterm (close them if they're open). In addition, verify `mbedls` lists the new target device.

    If your test run doesn't start, please read about [troubleshooting Greentea](https://github.com/ARMmbed/mbed-os-tools/tree/master/packages/mbed-greentea#common-issues).
