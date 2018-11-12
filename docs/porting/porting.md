## Porting guide

This document provides guidelines for adding a new MCU target to Mbed OS and Pelion.

### Scope and milestones
<!--I'm not sure I see how these milestones follow what's below, at least in numbering-->
The following milestones usually need to happen to port Mbed OS to a board or target:

1. Set up a development environment. Please choose:
   - Your primary development PC (Windows, Mac OS or Linux).

       You can port targets, connectivity and storage on Windows, macOS or Linux. Due to limitations in some development tools that Mbed OS uses, you need a Windows PC for DAPLink/FlashAlgo development.

  - An evaluation board with a target MCU, debug probe or an integrated interface chip.<!--I'm guessing the "or" is only for the last two things - debug probe or interface chip. In which case, this sentence requires rewriting.--> The hardware [is reviewed in greater details later in this document]().
  - A storage device (SD or external flash).

1. Locate reusable code to port to Mbed OS.
<!--Are the reusable code and SDK related? Are they the same thing?-->
    If there is an SDK available to speed up the porting process, we recommend reusing it (assuming copyright of the existing code is preserved).

1. Choose an IDE and debugger. The three commonly used IDEs are [Eclipse](https://www.eclipse.org/ide/), [IAR Embedded Workbench](https://www.iar.com/iar-embedded-workbench/) and [Keil MDK](http://www.keil.com/).

    Limitations:

    - Eclipse is license free, whereas both IAR and Keil IDE require licenses.
    - Currently, DAPLink development works only Keil MDK.

1. Arm and the Mbed OS community actively maintain pyOCD.<!--Do we need the info about who maintains pyOCD?--> The [Mbed Enabled](https://www.mbed.com/en/about-mbed/mbed-enabled/introduction/) program requires pyOCD, <!--I don't see that requierment https://www.mbed.com/en/about-mbed/mbed-enabled/requirements/ -->so ultimately pyOCD needs to support the new target. To allow parallel development in porting targets, connectivity and storage while pyOCD is still under development, you can use other IDEs supported on the evaluation board in the beginning phase.<!--Is this actually part of the previous point?-->

1. Implement and test CMSIS pack, bootstrap, linker script and startup code.

A basic framework is ready after this step. You can do the rest of the porting work in parallel:

1. Implement and test porting APIs. This includes all components described in the rest of this porting guide.

1. Test Mbed OS and Pelion example applications (as listed [in the final steps in this porting guide]()). This steps verifies that your new port is fully functional.

## Setting up

### Hardware setup

Porting Mbed OS requires the following hardware:

- An evaluation board with the targeted MCU.

    The new target needs a unique board ID. [Contact Arm]() to get one.

- A micro USB cables. One Micro USB cable connects the evaluation board to your development PC.

You may also need:

- If the interface MCU is not on the evaluation board, choose a debug probe, such as [SDWAP-LPC11U35](https://os.mbed.com/platforms/SWDAP-LPC11U35/). You will then need a micro USB cable (in addition to the micro USB cable listed above).
- An FTDI TTL232R-3V3 USB cable, for the Tx and Rx pins of debug probes that do not have a serial connection.
<!--I reversed the order because it seemed that the second will only be relevant if the first one is true. -->

The following items might help you test SPI, I2C and Pins:

- A CI test shield v2.0.0. For details, refer to [https://github.com/ARMmbed/ci-test-shield](https://github.com/ARMmbed/ci-test-shield).
- A micro SD card for the CI test shield.

<span class="tips">Check the user guide of the evaluation board to see if anything needs to be done prior to using a debug probe and running Mbed OS programs.</span>

### Software setup

Please install the following:

- [Python 2.7](https://www.python.org/downloads/release/python-2715/).
- [Git](https://git-scm.com/downloads).
- [Mbed CLI](/docs/development/tools/installation-and-setup.html).
- (Optional) [FTDI serial driver](http://www.ftdichip.com/Drivers/VCP.htm).
- Toolchains:
   - [GNU Arm Embedded Toolchain (GCC)](https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads).
   - [IAR](https://www.iar.com/iar-embedded-workbench/).
   - [Arm Compiler 5 or 6](https://developer.arm.com/products/software-development-tools/compilers/arm-compiler/downloads/version-5).

<span class="notes">The [tools documentation](https://os.mbed.com/docs/latest/tools/index.html) contains the exact tool versions supported in a specific Mbed OS release.</span><!--well... no, that's the support for the latest version of Mbed OS, not each version-->

Please fork or branch the following repositories:

- [DAPLink](https://github.com/armmbed/daplink).
- [pyOCD](https://github.com/mbedmicro/pyocd).
- [FlashAlgo](https://github.com/mbedmicro/flashalgo).
- [Mbed OS](https://github.com/armmbed/mbed-os).
- [Mbed OS bootloader](https://github.com/armmbed/mbed-bootloader).
- [Blinky](https://github.com/armmbed/mbed-os-example-blinky).
- [Device Management Cloud Client example](https://github.com/armmbed/mbed-cloud-client-example).

## Getting a working baseline

### Get the Mbed OS source code

The following Mbed CLI commands retrieve and fork the `mbed-os-example-blinky` code, and redirect `mbed-os` to point to the newly forked `mbed-os` repository:

<!--Why would I want to do that? Why are we starting with an application rather than a "clean" Mbed OS?-->

```
mbed import mbed-os-example-blinky
cd mbed-os-example-blinky
```

Add the URL of your forked repo (such as https://github.com/ARMmbed/mbed-os-new-target) to `mbed-os.lib`.<!--why isn't this at the end? At this point, I haven't created a new repo on GitHub yet--> Then:


```
mbed deploy
mkdir mbed-os
cd mbed-os
git init
git remote add origin https://github.com/<your_username>/mbed-os-new-target
git remote add upstream https://github.com/ARMmbed/mbed-os-new-target
git pull origin master
git checkout -b <branch_name>
```

### Build the Blinky program for an existing target

<!--what does that accomplish?-->

```
cd mbed-os-example-blinky
mbed compile --target K64F --toolchain GCC_ARM
mbed compile --target K64F --toolchain ARM
mbed compile --target K64F --toolchain IAR
```

Verify the build succeeds.<!--what if it fails?-->

You now have a working baseline and are ready to add a new target.

## Adding a new target

### Add a new target to FlashAlgo

<!--why do I need this step? what is FlashAlgo and why does Mbed OS porting rely on it?-->

<span class="notes">This step requires a Windows PC.</span>

Repo: [https://github.com/mbedmicro/flashalgo](https://github.com/mbedmicro/flashalgo)

To add the source code to support the new target:<!--this doesn't quite parse. is it two steps?-->

- Add a record to `projects.yaml`. <!--where is that?-->
- Create a `<target>.yaml` file in the `records/projects` directory.<!--where is that?-->
- Create a `FlashDev.c` file describing the attributes of the new flash device.<!--where do I put it?-->
- Create a `FlashPrg.c` file containing all the necessary functions, including Init, UnInit, EraseChip, EraseSector and ProgramPage.

<span class="tips">You can use this PR as an example: [https://github.com/mbedmicro/FlashAlgo/pull/46/files](https://github.com/mbedmicro/FlashAlgo/pull/46/files).</span>

<!--to do what?-->Follow the steps under **Develop Setup** and **Develop** in the [FlashAlgo documentation](https://github.com/mbedmicro/flashalgo).<!--why send them to another repo for five lines of code? @amanda that readme needs editing if we're going to point to it.-->

<!--when did I open Keil? at the end of the other file?-->
In Keil MDK, open the project file for your target in `\projectfiles\uvision<target>` and build it. The build directory of a successful build will have the files `c_blob.c` and `c_blob_mbed.c`; save both files. You will use them in the next step (`c_blob.c` in `flash_blob.c`, and `c_blob_mbed.c` in Flash API).

### Add your new target to DAPLink

<span class="notes">This step requires a Windows PC.</span>

<span class="notes">The new target needs a unique board ID. [Contact Arm]() to get one.</span>

Repo: [https://github.com/armmbed/daplink](https://github.com/armmbed/daplink).

1. [Port a target to DAPLink](https://github.com/ARMmbed/DAPLink/blob/master/docs/PORT_TARGET.md).
1. Copy the content of `c_blob.c` into `flash_blob.c`.
1. Verify your port by running [DAPLink tests](https://github.com/ARMmbed/DAPLink/blob/master/docs/AUTOMATED_TESTS.md).
1. When all DAPlink tests pass, create a PR <!--against which repo?-->.

### Add your new target to pyOCD

1. Set up a [development environment](https://github.com/mbedmicro/pyOCD/blob/master/docs/DEVELOPERS_GUIDE.md).
1. Add [a new target to pyOCD](https://github.com/mbedmicro/pyOCD/blob/master/docs/ADDING_NEW_TARGETS.md).
1. [Test your new target](https://github.com/mbedmicro/pyOCD/blob/master/docs/DEVELOPERS_GUIDE.md).
<!--not only do we keep sending them outside the docs, we send them back and forth between the same docs-->

Wait for your target support to be merged into pyOCD's master branch and released in PyPi. You can then use `pip install pyOCD` to enable debug.

<!--how? when? how long does it take? does Arm do it? do I have to wait for this to continue with my work?-->

## Debugging Mbed OS programs

<!--what on earth am I debugging? or am I setting up for later?-->

### Update DAPLink interface firmware

<!--why?-->

1. Clone the latest DAPLink firmware with the new target support completed in Step 8<!--by the time this got to me, there was no step 8 or 9-->.
1. Use the [DAPLink instructions](https://github.com/ARMmbed/DAPLink/tree/master/docs) to build the DAPLink firmware release package.
1. Locate the generated .bin or .hex firmware under `DAPLink\uvision_release\<your_board_name_if>`.
1. To update the interface firmware:
    1. Press the Reset button.
    1. Plug the USB cable to the host.
    1. Drag-n-drop the interface firmware.

### Creating GDB pyOCD debug configuration

1. Install pyOCD. You need the version with the new target support. If that hasn't been released yet, you can invoke the local copy:

    ```
    pip install --editable <path_to_pyOCD_with_new_target_support>
    ```

    Make a note of the installation path of `pyocd-gdbserver`; you'll need it when you set up the debug configuration inside the IDE.

1. The following example is for Eclipse IDE; find similar settings for Keil and IAR.

    1. Under **Debugger**, point the **Executable path** and **Actual executable path** to the `pyocd-gdbserver` you installed earlier.

       For example: `/Library/Frameworks/Python.framework/Versions/2.7/bin/pyocd-gdbserver`.

    1. In **GDB Client Setup**, change the executable to `arm-none-eabi-gdb`, which was part of the GNU Arm Embedded Toolchain you installed earlier.

       For example, on Windows, it looks like:

       ```
       C:\Program Files (x86)\GNU Tools ARM Embedded\7 2017-q4-major\bin\arm-none-eabi-gdb.exe
       ```

       On macOS, it may be:

       ```
       /usr/local/mbed-tools/gcc-arm-none-eabi-7-2017-q4-major/bin/arm-none-eabi-gdb
       ```

1. You can use the default values for all other settings.

## Porting modules

### Recommended porting order

Based on criticality and dependency of Mbed OS software stack, we recommend the following order:

1. Bare metal (based on the Blinky example).
1. Bootstrap and entry point.
1. Low power ticker.
1. Serial port (synchronous).
1. Microsecond ticker.
1. GPIO and IRQ.
1. RTC.
1. SPI.
1. TRNG.
1. Connectivity.
1. Flash.
1. Bootloader.
1. Pelion Client (optional).
1. Other HAL components (optional).

Detailed instructions for porting each module are given in the module-specific sections of this documentation.

### Bare metal mbed-os-example-blinky

The official mbed-os-example-blinky uses a DigitalOut object and timers. It doesn't rely on RTOS, GPIO and timers<!--timers shows up once in the "used" list and once in the "unused list"-->. LED toggling is done directly by accessing hardware registers.

Modify the Blinky program you checked out earlier. <!--to do what?-->You can see [an example using the CC3220SF-LAUNCHXL board](https://github.com/linlingao/mbed-os-example-blinky).<!--we're sending official documentation to one of our user accounts?-->

<span class="notes">Blinky is a stop-gap measure; please don't commit it to master.</span>

### Bootstrap and entry point

[Bootstrap porting instructions](https://os.mbed.com/docs/latest/reference/bootstrap.html).

Mbed OS uses CMSIS Pack. If your target doesn't have CMSIS pack yet, you'll need to create your own CMSIS files:<!--how is this related to the topic? And do I do it before or after bootstrap?-->

1. Locate CMSIS Device Template files and startup code. On Windows, they can be found in the following directories:<!--what's the context I'm looking through? my project? what if I'm not using Keil?-->

   ```
   C:\Keil_v5\ARM\PACK\ARM\CMSIS\5.3.0\Device\_Template_Vendor\Vendor\Device\Source
   C:\Keil_v5\ARM\PACK\ARM\CMSIS\5.3.0\Device\_Template_Vendor\Vendor\Device\Include
   ```
1. Create linker scripts from the template.<!--template or templates?-->

1. Implement pin mapping and basic peripheral initialization code.

    At this point, none of the peripherals for the new target has been implemented. To build for this new target with just the bootstrap, create a file called `.mbedignore` in your mbed-os directory (if one doesn't exist), and add the following entry:

    ```
    features/
    events/
    rtos/
    ```

    This removes dependencies on timers and peripherals that are yet to be ported.

When both the bootstrap and entry point are ready, you should be able to build and run the bare metal Blinky program:

```
cd mbed-os-example-blinky
mbed compile --target <target_name> --toolchain GCC_ARM
mbed compile --target <target_name> --toolchain ARM
mbed compile --target <target_name> --toolchain IAR
```

<!--what do I do if my build fails?-->

### Low power ticker

[Low power ticker porting instructions](https://os.mbed.com/docs/latest/porting/low-power-ticker.html).

<!--so is porting this module mandatory, or is it conditional - depending on what my hardware has?-->

When you finish porting low power ticker:

1. Remove the `rtos` entry from the `.mbedignore` file, because the OS kernel initialization is now possible.
1. In Blinky, set a breakpoint at `osKernelInitialize` and make sure it is called.

The [Mbed OS doxygen describes LowPowerTicker tests](https://os.mbed.com/docs/latest/mbed-os-api-doxy/group__hal__lp__ticker__tests.html). They rely on UART, so it's a good time to port UART.<!--if testing LPT requires UART, why don't I port UART first?-->

### Serial Port (synchronous)

[Serial port porting instructions](https://os.mbed.com/docs/latest/porting/serial-port.html).

Serial port porting can be done in two stages: synchronous UART and asynchronous UART. We recommend porting synchronous UART as early as possible, because the HAL Greentea tests require it, and because `printf()` is a powerful debugging tool.

### Microsecond Ticker

[Microsecond ticker porting instructions](https://os.mbed.com/docs/latest/porting/microsecond-ticker.html).

When you finish porting the microsecond ticker, the `wait` API should work, and the intervals should be exact. You can verify this with Blinky, which invokes both millisecond and microsecond tickers in its `wait (n second)` blinking behaviour.

### GPIO (write and read) and IRQ

[GPIO porting instructions](https://os.mbed.com/docs/latest/porting/gpio.html).

The vanilla Blinky program uses GPIO, which is a great tool for debuging with an oscilloscope or logic analyzer. It's a good idea to port GPIO before any other peripherals.

### RTC

[RTC porting instructions](https://os.mbed.com/docs/latest/porting/rtc-port.html).

RTC is a dependent of SPI (master) tests.<!--did you mean "dependency"?-->

On some targets, RTC is shared with low power ticker. On these targets, enable low power ticker instead of RTC.<!--does that mean "don't bother porting RTC"? What does "enable" mean in this context?-->

### SPI (master)

SPI (master) is used to communicate with storage devices that have an SPI interface, such as SD cards. The CI test shield supports an SD card as a slave device, so you can use it to test SPI (master) implementations on evaluation boards that don't have an SPI slave.

### TRNG

[True random number generator entropy source (TRNG) porting instructions](https://os.mbed.com/docs/latest/porting/entropy-sources.html).

If the hardware supports TRNG, you must port it before running Device Management Client, because the client uses TLS, which in turn uses entropy.

### Connectivity

[Porting instructions for all connectivity options](https://os.mbed.com/docs/latest/porting/porting-connectivity.html).

When you finish porting WiFi, run [https://github.com/ARMmbed/mbed-os-example-wifi](https://github.com/ARMmbed/mbed-os-example-wifi).
<!--Do we have any other examples, for the other connectivity methods?-->

### Flash

[Flash porting instructions](https://os.mbed.com/docs/latest/porting/flash.html).

Flash is required by Device Management Client.

There are two ways to implement flash API: using CMSIS flash algorithms or C source code. We recommend using C source code, because it's easier to maintain and upgrade. It's also more portable across different platforms.

### Bootloader

[Bootloader porting instructions](https://os.mbed.com/docs/latest/porting/bootloader.html).

The bootloader is a separate application, which needs to be created and integrated into Device Management Client.<!--this is a stub - it's only understandable if you already know everything about bootloader. Needs more info here.-->

### Device Management Client

<!--But I haven't ported the client yet, have I?-->
Once the above components are ported, you should be ready to demo the Connect and Update functionalities of the Device Management Client. See https://cloud.mbed.com/docs/current for details.<!--details of what? shouldn't we just send them to the quick starts, if all we want is for them to try connecting and updating?-->

### Other HAL Components (Optional)

You are now ready to port any other HAL components that your use case and MCU require. These components are covered in the rest of this document.

<!--Amanda, should we organise the modules so that they fit the porting order?-->

## Testing ported code

<!--wasn't I supposed to test as I go? this makes me think I test all at once, at the end-->
### Testing with the Greentea framework

<!--does Greentea only work with eclipse?--><!--what if I'm not using eclipse?-->

Read the following page to understand how tests are structured and exported into Eclipse:

<!--I can only find eclipse content in debugging, not in testing, and not in the page covering Greentea-->
<!--https://os.mbed.com/docs/v5.10/tutorials/eclipse.html-->
<!--[https://os.mbed.com/docs/latest/tools/greentea-testing-applications.html](https://os.mbed.com/docs/v5.10/tools/greentea-testing-applications.html)-->

<!--This 404s [https://os.mbed.com/docs/latest/tools/testing-applications.html]-->


#### 7.1 Test prerequisites

To run `mbed-os` tests, at the minimum, the following components must have been ported and verified:

- DAPLink.
- Serial port (synchronous transfer).
- Microsecond ticker.
- LowPowerTicker.

#### 7.2 Verify Serial port connection

Load a test binary with printf. Verify the text can be seen on your serial terminal program.

#### 7.3 Automated tests

If DAPLink is working, initiate the test using mbedgt from the terminal.

If DAPLink is still under development, follow Step 12.5 to run manual tests.

##### 7.3.1 Setup

The board under test needs to be supported in mbedls for automated tests to work. If official mbedls pip package hasn't been released, you need to direct pip to use your local directory that includes the change to support the new board.

Clone your repo from mbed-ls at https://github.com/ARMmbed/mbed-ls. Then run `pip install --editable <your_local_root_to_mbed-ls>`.

Create an `mbedls.json` file. This file allows you to override and specify the FTDI USB port. You can use mbedls command to find your board ID. The serial port path varies in different operation systems. On Mac OS and Linux, you can use ls /dev/tty.usb* to find the FTDI usbserial device. For Windows, you can find it using device manager, which usually would be something like COM#.

For example, on macOS:

```
{
    "33000000e062afa300000000000000000000000097969902": {
        "serial_port": "/dev/tty.usbserial-FTGDJJOC"
    }
}
```

##### 7.3.2 Compile

- To compile all tests, run mbed test -compile.
- To see the list of compiled tests, run mbed test --compile-list.
- To compile a specific test, run  mbed test -compile -n <test_name> (E.g.: mbed test --compile -n tests-concurrent-gpio).

##### 7.3.3 Run

        To run test, type command mbedgt.

On success, you should get something like this:

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

#### 7.4 Manual tests

Export a test and import it to Eclipse by following the instructions below.

```
# Find the directory of a test
mbed test --compile-list -n mbed-os-tests-mbed_hal-common_ticker
# Copy the source code to the project root directory
cd <root_dir>
cp -R mbed-os-example-blinky/mbed-os/TESTS/mbed_hal/common_tickers .
cd common_tickers
mbed new .
rm -rf mbed-os
# Copy mbed-os directory
cp -R ../mbed-os-example-blinky/mbed-os .
# Export to a makefile project
mbed export -i gcc_arm -m <new_target>
```

Load the program with pyOCD, configure Debug Configuration per instructions at Step 10.3.

Run the program. On the host, type the following command:

```
# mbedhtrun --skip-flashing --skip-reset -p <serial port>:9600 -e mbed-os/TESTS/host_tests
```

Customize the serial port path and baudrate as needed.

### Testing with demo applications

The `mbed-os-example-blinky` application should run after 11.6 is ported.

The `mbed-cloud-client-example` application should run after 11.10 is ported.

### 9 Detailed test procedure
<!--for what, Greentea again?-->
#### 9.1 Mbed OS Built-in Tests

##### 9.1.1 Build tests

All tests can be built under the `mbed-os-example-blinky` directory.

```
cd mbed-os-example-blinky
# Rename main.cpp to main.txt
mv main.cpp main.txt

#Build tests
mbed test --compile -m <new_target> -t gcc_arm -c
# You'll see some build errors. These errors should reduce or eventually disappear as more HAL components are ported.

# Go to mbed-os directory, all built-in tests will be run from there.
cd mbed-os

# The following command returns the list of tests built:
mbed test --compile-list
```

##### 9.1.2 Execute tests

###### 9.1.2.1 Locate image

Test images are located under the following directory:

```
mbed-os-example-blinky/BUILD/tests/<new_target>/gcc_arm/mbed-os/
```

For example,

```
$ mbed test --compile-list | grep common_tickers

    Test Case:

Name: tests-mbed_hal-common_tickers

Path: ./TESTS/mbed_hal/common_tickers

  Test Case:

      Name: tests-mbed_hal-common_tickers_freq

      Path: ./TESTS/mbed_hal/common_tickers_freq
```

- common_tickers test image is at mbed-os-example-blinky/BUILD/tests/<new_target>/gcc_arm/mbed-os/TESTS/mbed_hal/common_tickers.
- common_tickers_freq test image is at mbed-os-example-blinky/BUILD/tests/<new_target>/gcc_arm/mbed-os/TESTS/mbed_hal/common_tickers_freq.

###### 9.1.2.2 Program image

The following procedure requires the image to be flashed to the board. You may use DAPLink, Eclipse IDE to flash the image. If the new target is already supported by IAR or Keil programming tool, programming can be done using those tools as well. They easiest method is to use the command line tool pyocd-flashtool:

Note: We recommended:
pyocd-flashtool BUILD/mbed-os-example-blinky.bin or
pyocd-flashtool BUILD/mbed-os-example-blinky.hex

###### 9.1.2.3 Execute tests

Prior to running tests, make sure the serial port is not already opened by programs like screen, Teraterm etc. Close the program if it's open. In addition, verify mbedls lists the new target device. Read https://github.com/armmbed/greentea to troubleshoot issues if test doesn't start.

#### 9.2 Demo applications

##### 9.2.1 mbed-os-example-blinky

###### 9.2.1.1 Application repository

https://github.com/ARMmbed/mbed-os-example-blinky

###### 9.2.1.2 Test procedure

(1) Build image:

```
git clone https://github.com/ARMmbed/mbed-os-example-blinky.git
cd mbed-os-example-blinky
# Open a text editor and change the link in mbed-os.lib to https://github.com/ARMmbed/mbed-os-new-target
# This step is skipped if mbed-os-new-target has been merged to mbed-os
vi mbed-os.lib
mbed deploy
mbed compile --target <new_target> --toolchain GCC_ARM
```

(2) Flash Image:

Program the .bin or .hex image to the board.

(3) Verify the designated LED flashes every 0.5 second. Verify the interval on oscilloscope if desired.

##### 9.2.2 mbed-bootloader
###### 9.2.2.1 Application repository

https://github.com/armmbed/mbed-bootloader

###### 9.2.2.2 Test procedure

(1) Build image:

Build bootloader

```
cd mbed-os-bootloader
mbed deploy
mbed compile --target <new_target> --toolchain GCC_ARM --profile=tiny.json
```

(2) Flash Image:

Program the generated .bin or .hex.

(3) Verify the following on the terminal. The value on the last line will be different.

```
[BOOT] Mbed Bootloader

[BOOT] ARM: 00000000000000000000

[BOOT] OEM: 00000000000000000000

[BOOT] Layout: 0 1006F44
```

##### 9.2.3 mbed-cloud-client-example

Use the following test procedure on the `mbed-cloud-client-example` [application repository](https://github.com/armmbed/mbed-cloud-client-example)

1. Set up Pelion Account per instructions on https://cloud.mbed.com/product-overview.
1. Generate API key on Pelion Portal.
1. Run the following command with the generated API key in mbed-cloud-client-example directory

   ```
   $ mbed config -G CLOUD_SDK_API_KEY <API_KEY>
   $ mbed target <new_target>
   $ mbed toolchain GCC_ARM
   $ mbed dm init -d "<company domain name>" --model-name <new_target>
   ```

   Two files update_default_resources.c and mbed_cloud_dev_credentials.c should be created and used in the build.

1. Customize json files.

   The following customization is needed prior to build:

   - Modify mbed-os.lib by changing the URL to https://github.com/ARMmbed/mbed-os-new-target
   - Add the new target to mbed-cloud-client-example/mbed_app.json. For example, the code block below adds CC3220SF:

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

   In addition, fill in the SSID and Password in mbed_app.json if connectivity method for the new target is WiFi.

   Note that bootloader-details is the value displayed on the serial program while running mbed-bootloader program.

   - Add SOTP descriptors to mbed-cloud-client-example/mbed_lib.json, e.g.

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

1. Build image.

   ```
   cd mbed-cloud-client-example
   mbed deploy
   mbed compile --target <new_target> --toolchain GCC_ARM
   ```

1. Program the generated .bin or .hex to the board.
1. Verify serial output similar to:

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

1. Verify device is registered on Pelion portal
1. Make change in the MCC client and rebuild the firmware.
1. Perform firmware update

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

1. Verify the newer firmware is running on the device. Serial output should display the following:

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
