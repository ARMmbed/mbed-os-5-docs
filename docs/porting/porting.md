## Porting guide

This document provides guidelines to the Mbed community for adding a new MCU target to Mbed OS and Pelion.

### Scope and milestones

The following milestones usually need to happen in order to enable a board/target in the Mbed OS ecosystem:

- Setup development environment
   This involves choosing your primary development PC(Windows, Mac OS or Linux), evaluation board with target MCU, debug probe or an integrated interface chip on the eval board, storage device (SD or external flash).
   Due to limitations in some development tools used by Mbed OS, a Windows PC must be available for Daplink/Flashalgo development. Mbed OS porting target, connectivity and storage can all be done on Windows, Mac OS or Linux.
- Locate reusable code to port to Mbed OS
   If there's SDK available to speed up the porting process, it's recommended to reuse it assuming copyright of the existing code is preserved.
- Choose IDE and debugger
   Eclipse https://www.eclipse.org/ide/, IAR Embedded Workbench https://www.iar.com/iar-embedded-workbench/ and Keil MDK http://www.keil.com/ are the three common IDEs. Eclipse is license free, both IAR and Keil IDE require license. Currently Keil MDK is the only tool supported in Daplink development.
- pyOCD is actively maintained by ARM and the Mbed OS community. It's required by the Mbed Enable program, hence ultimately it needs to support the new target. To allow parallel development in porting target, connectivity and storage while pyOCD is still under development, other IDEs supported on the eval board can be used in the beginning phase.
- Implement and test CMSIS pack, bootstrap, linker script and startup code
   A basic framework is ready after this step. The rest of the porting work can be done in parallel.
- Implement and test porting APIs
   This includes all components described in https://os.mbed.com/docs/latest/porting/index.html.
- Test Mbed OS and Pelion demo applications
   Arm provides a number of demos and examples to help showcase Mbed OS and Pelion.

### Hardware setup

Porting Mbed OS requires the following hardware:

- Eval board with the targeted MCU.
- (Optional) FTDI TTL232R-3V3 USB cable.
   Some debug probes do not have serial connection such as SWDAP https://os.mbed.com/teams/mbed/wiki/SWDAP. If you have to use such boards, an FTDI cable connecting the TX and RX pin can be used.
- (Optional) Debug probe.
   If the Interface MCU is not on the eval board, choose an debug probe such as https://os.mbed.com/platforms/SWDAP-LPC11U35/.
- 1-2 Micro USB cables.
   One Micro USB cable is used to connect the eval board to your development PC. Optionally you may need another cable to connect the debug probe to the PC.

The following items might be helpful in testing SPI, I2C and Pins:

- 1 CI Test Shield v2.0.0. For details, refer to https://github.com/ARMmbed/ci-test-shield.
- 1 Micro SD card for the CI Test Shield.

Check the user guide of the eval board to see if anything needs to be done prior to using debug probe and running Mbed OS programs.

### Software installations

Install the following packages:

- Python 2.7: https://www.python.org/downloads/release/python-2715/.
- Git: https://git-scm.com/downloads.
- Mbed CLI https://os.mbed.com/docs/v5.10/tools/installation-and-setup.html.
- (Optional) FTDI serial driver http://www.ftdichip.com/Drivers/VCP.htm.
- Toolchains f4ef4rfrr44.
   - GNU Arm Embedded Toolchain (GCC): https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads.
   - IAR: https://www.iar.com/iar-embedded-workbench/.
   - Arm Compiler 5 or 6: https://developer.arm.com/products/software-development-tools/compilers/arm-compiler/downloads/version-5.

Check https://os.mbed.com/docs/latest/tools/index.html for exact tool versions supported in a specific Mbed OS release.

#### Fork Github repositories

At the minimum, the following repositories need to be forked or branched for the porting project:

- https://github.com/armmbed/daplink
- https://github.com/mbedmicro/pyocd
- https://github.com/mbedmicro/flashalgo
- https://github.com/armmbed/mbed-os
- https://github.com/armmbed/mbed-bootloader
- https://github.com/armmbed/mbed-os-example-blinky
- https://github.com/armmbed/mbed-cloud-client-example

### 1. Get Mbed OS Source Code
#### 1.1 Clone code to your local directory

The following commands retrieve mbed-os-example-blinky code and redirect mbed-os to point to the newly forked mbed-os repository:

```
mbed import mbed-os-example-blinky
cd mbed-os-example-blinky
# Edit mbed-os.lib with the URL of your forked repo, e.g., https://github.com/ARMmbed/mbed-os-new-target
mbed deploy
mkdir mbed-os
cd mbed-os
git init
git remote add origin https://github.com/<your_username>/mbed-os-new-target
git remote add upstream https://github.com/ARMmbed/mbed-os-new-target
git pull origin master
git checkout -b <branch_name>
```

#### 1.2 Build the Blinky program for an existing target

```
cd mbed-os-example-blinky
mbed compile --target K64F --toolchain GCC_ARM
mbed compile --target K64F --toolchain ARM
mbed compile --target K64F --toolchain IAR
```

Verify build succeeds. At this point, you have a working baseline and are ready to add a new target.

### 2. Add new target to FlashAlgo

Repo: https://github.com/mbedmicro/flashalgo

Windows PC is required for this step.

Follow the procedure below to add the source code to support the new target:

- Add a record to projects.yaml
- Create <target>.yaml file in the records/projects directory
- Create FlashDev.c file describing the attributes of the new flash device
- Create FlashPrg.c to include all necessary functions including Init, UnInit, EraseChip, EraseSector and ProgramPage

This PR can be used as an example: https://github.com/mbedmicro/FlashAlgo/pull/46/files.

Follow the steps under Develop Setup and Develop section in https://github.com/mbedmicro/flashalgo.

Once Keil MDK starts, open the project file for the desired target in \projectfiles\uvision<target> and build it. Upon a successful build, you'll find the following files in the build directory:

c_blob.c and c_blob_mbed.c. Save these files. c_blob.c will be used in flash_blob.c, c_blob_mbed.c can be used in Flash API.

### 3. Add new target to DapLink

Repo: https://github.com/armmbed/daplink.

Windows PC is required for Daplink environment.

The new target will need to have a unique board ID. Contact Arm to get one.

Follow the instructions below to port a new target:

https://github.com/ARMmbed/DAPLink/blob/master/docs/PORT_TARGET.md

Copy the content of c_blob.c into flash_blob.c.

Refer to https://github.com/ARMmbed/DAPLink/blob/master/docs/AUTOMATED_TESTS.md to run existing Daplink tests to verify the port.

Once DapLink tests pass, create a PR to request merge.

### 4. Add new target to pyOCD

Follow https://github.com/mbedmicro/pyOCD/blob/master/docs/DEVELOPERS_GUIDE.md to setup development environment.

This guide describes how to add a new target to pyOCD:

https://github.com/mbedmicro/pyOCD/blob/master/docs/ADDING_NEW_TARGETS.md

Test instructions can be found in https://github.com/mbedmicro/pyOCD/blob/master/docs/DEVELOPERS_GUIDE.md.

Once the changes to support the new target are merged into pyOCD master branch, and subsequently released in PyPi, one can use 'pip install pyOCD" to enable debug.

### 5. Debug Mbed OS programs
#### 5.1 Update DAPLink interface firmware

- Clone the latest DAPLink firmware with the new target support completed at Step 8.
- Build DAPLink firmware release package and locate the generated .bin or .hex firmware under DAPLink\uvision_release\<your_board_name_if> directory per instructions at https://github.com/ARMmbed/DAPLink/tree/master/docs.
- Update the Interface firmware by pressing the reset prior to plugging the USB cable to the host, then drag-n-dropping the interface firmware.

10.2 Install pyOCD
You'll need the pyOCD version completed at step 9. If the pyOCD version with the new target support hasn't been released, use the following command to invoke the local copy:

```
pip install --editable <path_to_pyOCD_with_new_target_support>
```

Make a note of the installation path of pyocd-gdbserver, you'll need it in the next step when you set up Debug Configuration inside the IDE.

#### 5.3 Create GDB pyOCD debug configuration

The following procedure is for Eclipse IDE, find similar settings for Keil and IAR.

- Under Debugger, point Executable path and Actual executable path to the pyocd-gdbserver you installed at Step 10.2.
   
   For example,  /Library/Frameworks/Python.framework/Versions/2.7/bin/pyocd-gdbserver

- In GDB Client Setup, change the executable to arm-none-eabi-gdb which was part of the GNU Arm Embedded Toolchain installed at Step 4.

   For example, on Windows, it'll look like
   
   ```
   C:\Program Files (x86)\GNU Tools ARM Embedded\7 2017-q4-major\bin\arm-none-eabi-gdb.exe
   ```
   
   On Mac, it may be:
   
   ```
   /usr/local/mbed-tools/gcc-arm-none-eabi-7-2017-q4-major/bin/arm-none-eabi-gdb
   ```
   
- The rest of the settings can be kept default.

### 6. Recommended Porting Order

Detailed instructions on how to port targets/connectivity/storage are given in https://os.mbed.com/docs/latest/porting/index.html.

Based on criticality and dependency of Mbed OS software stack, the following order is recommended:

#### 6.1 Baremetal mbed-os-example-blinky

The official mbed-os-example-blinky requires DigitalOut object and timers. Since these modules are yet to be ported, a baremetal Blinky program is recommended.

Modify the Blinky programmed checked out at Step 6.1.

Baremetal program doesn't rely on rtos,GPIO object or timers. LED toggling is done directly by accessing hardware registers. See an example using CC3220SF LAUNCHXL board at https://github.com/linlingao/mbed-os-example-blinky.

This Blinky program is a stop-gap measure, obviously you don't want to commit it to master.

#### 6.2 Bootstrap and entry point

Bootstrap instructions can be found at https://os.mbed.com/docs/v5.9/reference/bootstrap.html.

Mbed OS uses CMSIS Pack. It's possible that this new target does not have CMSIS pack yet. In this case, you'll need to create your own CMSIS files.

- Locate CMSIS Device Template files and startup code. On Windows, they can be found in the following directories:

   ```
   C:\Keil_v5\ARM\PACK\ARM\CMSIS\5.3.0\Device\_Template_Vendor\Vendor\Device\Source
   C:\Keil_v5\ARM\PACK\ARM\CMSIS\5.3.0\Device\_Template_Vendor\Vendor\Device\Include
   ```
- Create linker scripts from the template.

Implement pin mapping and basic peripheral initialization code.

At this point, none of the peripherals for the new target has been implemented. To build for this new target with just the bootstrap, create a file called .mbedignore in mbed-os directory if it doesn't exist, add the following entry:

```
features/
events/
rtos/
```

This will remove dependencies on timers and peripherals that are yet to be ported.

Upon completion of bootstrap and entry point, you should be able to build and run the baremetal Blinky program.

```
cd mbed-os-example-blinky
mbed compile --target <target_name> --toolchain GCC_ARM
mbed compile --target <target_name> --toolchain ARM
mbed compile --target <target_name> --toolchain IAR
```

#### 6.3 LowPowerTicker

Low Power Ticker porting instructions can be found at https://os.mbed.com/docs/latest/porting/low-power-ticker.html.

If this new target provides a low power ticker, porting this will allow OS kernel initialization to succeed. Therefore, upon completion of this task, rtos can be added back in to the build by removing the "rtos" entry from the .mbedignore file.

The Blinky program should be able to run to main with rtos after low power ticker is successfully ported. Set a breakpoint at osKernelInitialize and make sure it is called.

There're some low power ticker tests described at https://os.mbed.com/docs/latest/mbed-os-api-doxy/group__hal__lp__ticker__tests.html. These tests rely on UART to work so it's a good time to proceed to UART next.

### 6.4 Serial Port (Synchronous)

Serial port porting instructions can be found here: https://os.mbed.com/docs/latest/porting/serial-port.html.

Serial porting can be done in two stages: synchronous UART and asynchronous UART. It's recommended to get synchronous UART ported as early as possible, because the HAL greentea tests require UART, and printf is a powerful debugging tool.

#### 6.5 Microsecond Ticker

Microsecond ticker porting instructions can be found here: https://os.mbed.com/docs/latest/porting/microsecond-ticker.html.

The vanilla Blinky code uses "wait (n second)" API that invokes both the millisecond ticker and the microsecond ticker. At the conclusion of this step, "wait" API is expected to work and interval should be exact.

#### 6.6 GPIO (Write and Read) and IRQ

GPIO porting instructions can be found here: https://os.mbed.com/docs/latest/porting/gpio.html.

The vanilla Blinky program uses GPIO. GPIO can be a great tool to help debug using oscilloscope or logic analyzer. It's a good idea to port GPIO prior to other peripherals.

#### 6.7 RTC

RTC pointing instructions can be found here: https://os.mbed.com/docs/latest/porting/rtc-port.html.

RTC is a dependent of SPI master tests.

On some target, RTC is shared with Low Power Ticker. Enable Low Power Ticker instead of RTC on these targets.

#### 6.8 SPI (Master)

SPI (Master) is used to communicate with storage devices such as SD card with SPI interface. CI test shield supports SD card as a slave device, therefore it can be used to test SPI master implementation if the eval board in use doesn't have a SPI slave.

#### 6.9 TRNG

Entropy source (TRNG) porting instructions can be found here: https://os.mbed.com/docs/latest/porting/entropy-sources.html.

If the hardware supports TRNG, this must be ported before running Pelion client, since entropy is used by TLS.

#### 6.10 Connectivity

Depending on the connectivity type, refer to the corresponding section in https://os.mbed.com/docs/latest/porting/porting-connectivity.html for porting instructions.

Upon completion of porting connectivity, if using WiFi, mbed-os-example-wifi demo shall run successfully at the completion of this step.

#### 6.11 Flash

Flash porting instructions can be found here: https://os.mbed.com/docs/latest/porting/flash.html.

Flash is required by Pelion client. Although there're are two ways to implement flash API, using CMSIS flash algorithms or C source code, it's recommended to use C source code since it's easier to maintain and upgrade. It's also more portable across different platforms.

#### 6.12 Bootloader

Bootloader porting instructions can be found here: https://os.mbed.com/docs/latest/porting/bootloader.html.

Bootloader is a separate application. It needs to be created and integrated into Pelion client.

#### 6.13 Pelion Client

Once the above components are ported, you should be ready to demo Connect and Update functionality of Pelion client. See https://cloud.mbed.com/docs/current for details.

#### 6.14 Other HAL Components (Optional)

Depending on the use case and MCU capability, other HAL components may need to be ported at this stage. Follow the instructions here: https://os.mbed.com/docs/latest/porting/index.html.

### 7 Test Ported Code Using Greentea Framework

#### 7.1 Greentea Overview

Read the following page to understand how tests are structured and exported into Eclipse:

https://os.mbed.com/docs/latest/tools/testing-applications.html

#### 7.2 Test Prerequisites

To run mbed-os tests, at the minimum, the following components must have been ported and verified:

Daplink, serial port (synchronous transfer), microsecond ticker and low power ticker

#### 7.3 Verify Serial Port Connection

Load a test binary with printf, verify the text can be seen on your serial terminal program.

#### 7.4 Automated Tests

If DAPLink is working, initiate the test using mbedgt from the terminal.

If DAPLink is still under development, follow Step 12.5 to run manual tests.

##### 7.4.1 Setup

The board under test needs to be supported in mbedls for automated tests to work. If official mbedls pip package hasn't been released, you'll need to direct pip to use your local directory that includes the change to support the new board.

Clone your repo from mbed-ls at https://github.com/ARMmbed/mbed-ls. Then run "pip install --editable <your_local_root_to_mbed-ls>".

Create a mbedls.json file. This file allows you to override and specify the FTDI usb port. You can use mbedls command to find your board ID. The serial port path varies in different operation systems. On Mac OS and Linux, you can use ls /dev/tty.usb* to find the FTDI usbserial device. For Windows, you can find it using device manager, which usually would be something like COM#.

For example, on macOS:

```
{
    "33000000e062afa300000000000000000000000097969902": {
        "serial_port": "/dev/tty.usbserial-FTGDJJOC"
    }
}
```

##### 7.4.2 Compile

- To compile all tests, run mbed test -compile.
- To see the list of compiled tests, run mbed test --compile-list.
- To compile a specific test, run  mbed test -compile -n <test_name> (E.g.: mbed test --compile -n tests-concurrent-gpio).

##### 7.4.3 Run

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

#### 7.5 Manual Tests

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

### 8 Test Ported Code Using Demo Applications

#### 8.1 mbed-os-example-blinky

This application should run after 11.6 is ported.

#### 8.2 mbed-cloud-client-example

This application should run after 11.10 is ported.

### 9 Detailed Test Procedure

#### 9.1 Mbed OS Built-in Tests

##### 9.1.1 Build Tests

All tests can be built under the mbed-os-example-blinky directory.

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

##### 9.1.2 Execute Tests
###### 9.1.2.1 Locate Image

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

###### 9.1.2.2 Program Image

The following procedure requires the image to be flashed to the board. You may use Daplink, Eclipse IDE to flash the image. If the new target is already supported by IAR or Keil programming tool, programming can be done using those tools as well. They easiest method is to use the command line tool pyocd-flashtool:

Note: We recommended: 
pyocd-flashtool BUILD/mbed-os-example-blinky.bin or
pyocd-flashtool BUILD/mbed-os-example-blinky.hex

###### 9.1.2.3 Execute Tests

Prior to running tests, make sure the serial port is not already opened by programs like screen, Teraterm etc. Close the program if it's open. In addition, verify mbedls lists the new target device. Read https://github.com/armmbed/greentea to troubleshoot issues if test doesn't start.

#### 9.2 Demo Applications

##### 9.2.1 mbed-os-example-blinky

###### 9.2.1.1 Application Repository

https://github.com/ARMmbed/mbed-os-example-blinky

###### 9.2.1.2 Test Procedure

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
###### 9.2.2.1 Application Repository

https://github.com/armmbed/mbed-bootloader

###### 9.2.2.2 Test Procedure

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

###### 9.2.3.1 Application Repository

https://github.com/armmbed/mbed-cloud-client-example

###### 9.2.3.2 Test Procedure

(1) Setup Pelion Account per instructions on https://cloud.mbed.com/product-overview.

(2) Generate API key on Pelion Portal.

(3) Run the following command with the generated API key in mbed-cloud-client-example directory

```
$ mbed config -G CLOUD_SDK_API_KEY <API_KEY>
$ mbed target <new_target>
$ mbed toolchain GCC_ARM
$ mbed dm init -d "<company domain name>" --model-name <new_target>
```

Two files update_default_resources.c and mbed_cloud_dev_credentials.c should be created and used in the build.

(4) Customize json files.

The following customization is needed prior to build:

- Modify mbed-os.lib by changing the URL to https://github.com/ARMmbed/mbed-os-new-target
- Add the new target to mbed-cloud-client-example/mbed_app.json. For example, the code block below adds CC3220SF:

   mbed_app.json example
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
   
   mbed_app.json example
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

(5) Build image.

Build MMC
```
cd mbed-cloud-client-example
mbed deploy
mbed compile --target <new_target> --toolchain GCC_ARM
```

(6) Program the generated .bin or .hex to the board.

(7) Verify serial output similar to: 

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

(8) Verify device is registered on Pelion portal

(9) Make change in the MCC client and rebuild the firmware.

(10) Perform firmware update

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

(11) Verify the newer firmware is running on the device. Serial output should display the following:

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
