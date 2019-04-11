# Getting a working baseline

## Create forks

Please fork or branch the following repositories:

- [DAPLink](https://github.com/armmbed/daplink).
- [pyOCD](https://github.com/mbedmicro/pyocd).
- [FlashAlgo](https://github.com/mbedmicro/flashalgo).
- [Mbed OS](https://github.com/armmbed/mbed-os). Use the format `https://github.com/ARMmbed/mbed-os-new-target`.
- [Mbed OS bootloader](https://github.com/armmbed/mbed-bootloader).
- [Blinky](https://github.com/armmbed/mbed-os-example-blinky).
- [Device Management Cloud Client example](https://github.com/armmbed/mbed-cloud-client-example).

## Get the Mbed OS source code

The following Mbed CLI commands retrieve and fork the `mbed-os-example-blinky` code, and redirect `mbed-os` to point to the newly forked `mbed-os` repository:

```
git clone mbed-os-example-blinky
cd mbed-os-example-blinky
```

Delete the file `mbed-os.lib` (`rm mbed-os.lib` on Linux/macOS, `del mbed-os.lib` on Windows).

Next, add your fork of `mbed-os` (change the URL to match your repository).

```
mbed add https://github.com/ARMmbed/mbed-os-new-target mbed-os
```

Next, set up the upstream remote, and create a branch for the new port.

```
cd mbed-os
git remote add upstream https://github.com/ARMmbed/mbed-os
git checkout -b <branch_name>
```

## Build the Blinky program for an existing target

To verify that you have a working fork, please build Blinky to a supported target:

```
cd mbed-os-example-blinky
mbed compile --target K64F --toolchain GCC_ARM
mbed compile --target K64F --toolchain ARM
mbed compile --target K64F --toolchain IAR
```

Verify the build succeeds.
Make sure the program runs correctly, if it fails, [please see the debugging page](../tutorials/debugging.html).

You now have a working baseline and are ready to add a new target.

# Adding a new target

## Add a new target to FlashAlgo

DAPlink requires FlashAlgo to program a target. You need to either write FlashAlgo source code yourself, or use the one provided with your MCU.

<span class="notes">This step requires a Windows PC.</span>

Repo: [https://github.com/mbedmicro/flashalgo](https://github.com/mbedmicro/flashalgo)

1. To add the Flash programming source code to the FlashAlgo repository:

    - Add a record to `projects.yaml`.
    - Create a `<target>.yaml` file in the `records/projects` directory.
    - Create a `FlashDev.c` file describing the attributes of the new flash device.
    - Create a `FlashPrg.c` file containing all the necessary functions, including Init, UnInit, EraseChip, EraseSector and ProgramPage.

    <span class="tips">You can use this PR as an example: [https://github.com/mbedmicro/FlashAlgo/pull/46/files](https://github.com/mbedmicro/FlashAlgo/pull/46/files).</span>

1. To generate uVision project files, follow the instructions in **Develop Setup** and **Develop** in the [FlashAlgo documentation](https://github.com/mbedmicro/flashalgo).

1. In Keil MDK, open the project file for your target in `\projectfiles\uvision<target>`, and build it. The build directory of a successful build will have the files `c_blob.c` and `c_blob_mbed.c`; save both files. You will use them in the next step (`c_blob.c` in `flash_blob.c`, and `c_blob_mbed.c` in Flash API).

## Add your new target to DAPLink

<span class="notes">This step requires a Windows PC.</span>

<span class="notes">The new target needs a unique board ID. To get one, please contact your technical account manager or email [our support team](mailto:support@mbed.com).</span>

Repo: [https://github.com/armmbed/daplink](https://github.com/armmbed/daplink).

1. [Port a target to DAPLink](https://github.com/ARMmbed/DAPLink/blob/master/docs/PORT_TARGET.md).
1. Copy the content of `c_blob.c` into `flash_blob.c`.
1. Verify your port by running [DAPLink tests](https://github.com/ARMmbed/DAPLink/blob/master/docs/AUTOMATED_TESTS.md).
1. When all DAPlink tests pass create two PRs:
    - One PR against the DAPLink repository.
    - One PR against the FlashAlgo repository.

## Add your new target to pyOCD

To be able to debug your port:

1. Set up a [development environment](https://github.com/mbedmicro/pyOCD/blob/master/docs/DEVELOPERS_GUIDE.md).
1. Add [a new target to pyOCD](https://github.com/mbedmicro/pyOCD/blob/master/docs/ADDING_NEW_TARGETS.md).
1. [Test your new target](https://github.com/mbedmicro/pyOCD/blob/master/docs/DEVELOPERS_GUIDE.md).

Wait for your target support to be merged into pyOCD's master branch and released in PyPi. You can then use `pip install pyOCD` to enable debug.

# Setting up to debug Mbed OS programs


## Update DAPLink interface firmware

You need to update the new DAPLink interface firmware, which includes the new target support, on your interface MCU.

To include the new target support:

1. Clone the latest DAPLink firmware with the new target support [completed above](#add-your-new-target-to-daplink).
1. Use the [DAPLink instructions](https://github.com/ARMmbed/DAPLink/tree/master/docs) to build the DAPLink firmware release package.
1. Locate the generated .bin or .hex firmware under `DAPLink\uvision_release\<your_board_name_if>`.
1. To update the interface firmware:
    1. Press the Reset button.
    1. Plug the USB cable to the host.
    1. Drag-n-drop the interface firmware.

## Create GDB pyOCD debug configuration

1. Install pyOCD. You need the version with the new target support. If you contributed to PyOCD and an updated version hasn't been released yet, you can invoke the local copy:

    ```
    pip install --editable <path_to_pyOCD_with_new_target_support>
    ```

    Make a note of the installation path of `pyocd-gdbserver`; you'll need it when you set up the debug configuration inside the IDE.

1. The following example is for Eclipse IDE; find similar settings for Keil and IAR.

    1. Under **Debugger**, point the **Executable path** and **Actual executable path** to the `pyocd-gdbserver` you installed earlier.

       For example: `/Library/Frameworks/Python.framework/Versions/2.7/bin/pyocd-gdbserver` on macOS.

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

# Porting HAL modules

## Recommended porting order

Based on criticality and dependency of Mbed OS software stack, we recommend the following order:

1. Create a bare metal example (based on the Blinky example).
1. Bootstrap and entry point.
1. Serial port (synchronous transfer).
1. Low power ticker.
1. Microsecond ticker.
1. GPIO and IRQ.
1. RTC.
1. SPI.
1. TRNG.
1. Connectivity.
1. Flash.
1. Bootloader.
1. Pelion Client (optional).
1. Other HAL modules (optional).

Detailed instructions for porting each module are given in the module-specific sections of this documentation.

## Create the bare metal mbed-os-example-blinky

The official `mbed-os-example-blinky` uses the RTOS, a DigitalOut object and timers. The bare metal version of the example doesn't rely on RTOS, GPIO and timers; LED toggling is done directly by accessing hardware registers. Modify the Blinky program you checked out earlier to not use the timer and DigitalOut object. You can see [an example using the CC3220SF-LAUNCHXL board](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/Baremetal-Blinky/main.cpp).

[![View code](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/Baremetal-Blinky/)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/Baremetal-Blinky/main.cpp)

## Bootstrap and entry point

[Bootstrap porting instructions](../reference/bootstrap.html).

Mbed OS uses CMSIS for bootstrap. If your target doesn't have a CMSIS implementation (which is distributed in CMSIS pack-form) yet, you'll need to create your own CMSIS files:

1. Locate CMSIS Device Template files and startup code. On Windows and if uVision is installed, you can find them in the following directories:

   ```
   C:\Keil_v5\ARM\PACK\ARM\CMSIS\5.3.0\Device\_Template_Vendor\Vendor\Device\Source
   C:\Keil_v5\ARM\PACK\ARM\CMSIS\5.3.0\Device\_Template_Vendor\Vendor\Device\Include
   ```
   
1. Create linker scripts from the templates.

1. Implement pin mapping and basic peripheral initialization code.
<!-- This is lacking in detail. Are they supposed to implement the Mbed pinmap apis? Or should they do this manually by modifying device registers? -->

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

## Serial Port (synchronous transfer)

[Serial port porting instructions](../porting/serial-port.html).

Serial port porting can be done in two stages: synchronous UART and asynchronous UART. We recommend porting synchronous UART as early as possible, because the HAL Greentea tests require it, and because `printf()` is a powerful debugging tool.

## Low power ticker

<span class="notes">**Note**: Low power ticker is mandatory for any platform that supports it.</span>

[Low power ticker porting instructions](../porting/low-power-ticker.html).

When you finish porting low power ticker:

1. Remove the `rtos` entry from the `.mbedignore` file, because the OS kernel initialization is now possible.
1. In Blinky, set a breakpoint at `osKernelInitialize` and make sure it is called.

The [Mbed OS doxygen describes LowPowerTicker tests](https://os.mbed.com/docs/latest/mbed-os-api-doxy/group__hal__lp__ticker__tests.html).


## Microsecond Ticker

[Microsecond ticker porting instructions](../porting/microsecond-ticker.html).

When you finish porting the microsecond ticker, the `wait` API should work, and the intervals should be exact. You can verify this with `printf`.

## GPIO (write and read) and IRQ

[GPIO porting instructions](../porting/gpio.html).

The vanilla Blinky program uses GPIO, which is a great tool for debugging with an oscilloscope or logic analyzer. It's a good idea to port GPIO before any other peripherals.

You can now try [using the normal Blinky application](../porting/testing-with-the-demo-applications.html).

## RTC

[RTC porting instructions](../porting/rtc-port.html).

RTC is a dependency of SPI (master) tests.

On some targets, RTC is shared with low power ticker and you can only use one of them. On these targets, you must use low power ticker instead of RTC.

## SPI (master)

SPI (master) is used to communicate with storage devices that have an SPI interface, such as SD cards. The CI test shield supports an SD card as a slave device, so you can use it to test SPI (master) implementations on evaluation boards that don't have an SPI slave.

## TRNG

[True random number generator entropy source (TRNG) porting instructions](../porting/entropy-sources.html).

If the hardware supports TRNG, you must port it before running Device Management Client, because the client uses TLS, which in turn requires an entropy source.

## Connectivity

[Porting instructions for all connectivity options](../porting/porting-connectivity.html).

You can now try running the example applications for your connectivity methods. For example:

- [https://github.com/ARMmbed/mbed-os-example-ble](https://github.com/ARMmbed/mbed-os-example-ble).
- [https://github.com/ARMmbed/mbed-os-example-wifi](https://github.com/ARMmbed/mbed-os-example-wifi).
- [https://github.com/ARMmbed/mbed-os-example-lorawan](https://github.com/ARMmbed/mbed-os-example-lorawan).
- [https://github.com/ARMmbed/mbed-os-example-cellular](https://github.com/ARMmbed/mbed-os-example-cellular).
- [https://github.com/ARMmbed/mbed-os-example-sockets](https://github.com/ARMmbed/mbed-os-example-sockets).

## Flash

[Flash porting instructions](../porting/flash.html).

Flash drivers are required by Device Management Client.

There are two ways to implement flash API: using CMSIS flash algorithms or vanilla C source code. We recommend using vanilla C source code, because it's easier to maintain and upgrade. It's also more portable across different platforms.

## Bootloader

[Bootloader porting instructions](../porting/bootloader.html).

The bootloader is a separate application, which needs to be created and integrated into Device Management Client to allow firmware updates.

## Device Management Client

You do not need to manually port Device Management Client; when the above modules are ported, you should be ready to [demo the Connect and Update functionalities of the Device Management Client](https://cloud.mbed.com/guides/connect-device-to-pelion).

## Other HAL modules (Optional)

You are now ready to port any other HAL modules that your use case and MCU require. These modules are covered in the rest of this document, with the exception of [Mbed Cordio, which has its own porting documentation](https://os.mbed.com/docs/mbed-cordio/latest/porting-pal/index.html).
