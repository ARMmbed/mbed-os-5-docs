# Using Mbed OS on a custom board

When designing a custom microcontroller board to run Mbed OS, you may need to
make software customizations for the unique design choices you have made for
your new board, such as clocking, pin connections and peripheral use. You can
accomplish this by adding configuration and source files to an Mbed OS-based
application project without the need to modify files within Mbed OS, itself.
You can add a file named `custom_targets.json` to your project, which can store
your custom target configurations. If your board is based on an existing Mbed
Enabled microcontroller, you can simply extend that board configuration without
the need to implement all the files yourself.

This tutorial covers the most common methods used to create a custom port of
Mbed OS when starting from an existing Mbed Enabled board. For detailed
information on how to create a port from scratch, go to the [Mbed Porting
guide](../porting/index.html). Additionally, not all possible aspects of target
configuration are covered. For detailed information on all the ways you can
configure targets, go to [adding and configuring
targets](../program-setup/adding-and-configuring-targets.html).

## Extending an existing MCU target configuration

Consider a situation in which you are creating a new board based on an existing
Mbed Enabled board. This tutorial lists the steps to create the software for a
new board we will call `ImaginaryBoard`. This board is based on
[DISCO-L475VG-IOT01A](https://os.mbed.com/platforms/ST-Discovery-L475E-IOT01A/).
It shares most of the features of DISCO-L475VG-IOT01A, but it does not use
`AnalogOut`, `AnalogIn`, `CAN` or `USB`. Some pins are connected differently on
the new board.

Follow these steps to create a custom port for Mbed OS:

### Preparing

1. [Install Mbed CLI](../build-tools/install-and-set-up.html) if you don't
   already have it.

1. (Optional) Create a new Mbed program (for example,
   `mbed-os-imaginary-port`).

   If you don't already have an Mbed program on your computer, run this Mbed
   CLI command in a command terminal:

   ```
   mbed new --program mbed-os-imaginary-port
   ```

   This command creates a new program folder called `mbed-os-imaginary-port`
   and then imports `mbed-os` from the [official Mbed OS source
   repository](https://github.com/armmbed/mbed-os) into it.

1. Change directories into your new project:

   ```
   cd mbed-os-imaginary-port
   ```

1. Create a new file named `custom_targets.json` at the same level as the
   `mbed-os` directory.

1. Inspect the contents of `mbed-os/targets/targets.json`. For this example,
   search for `DISCO_L475VG_IOT01A`.

1. Copy the contents from the `DISCO_L475VG_IOT01A` section into your
   `custom_targets.json` file. Be sure to include brackets `{ }` surrounding
   the content.

### Customizing

1. Make changes to `custom_targets.json` for your board.

   In this example:

   1. The board name changes from `DISCO_L475VG_IOT01A` to `IMAGINARYBOARD`, so
      the board can be uniquely identified.
   1. The `detect_code` changes from `0764` to `1234`. The `detect_code` is a
      unique four-digit hexadecimal value, also called a `Platform ID`, that
      identifies the board to the Mbed OS test tools. For Mbed Enabled boards,
      this number is exposed through the debug interface with Mbed CLI by
      typing `mbedls`.
   1. The `macros_add` section changes to remove `USBHOST_OTHER` because the
      new board does not use USB.
   1. The `device_has_add` section changes to remove the `ANALOGOUT`, `CAN`,
      and `USBDEVICE` drivers because the new board doesn't use those features.

   After making changes, the full contents look like this:

   ```
   {
       "IMAGINARYBOARD": {
           "inherits": [
               "MCU_STM32L475xG"
           ],
           "components_add": [
               "BlueNRG_MS",
               "QSPIF"
           ],
           "extra_labels_add": [
               "CORDIO",
               "MX25R6435F"
           ],
           "supported_form_factors": [
               "ARDUINO"
           ],
           "detect_code": [
               "1234"
           ],
           "device_has_add": [
               "QSPI"
           ],
           "device_has_remove": [
               "ANALOGOUT",
               "ANALOGIN",
               "CAN",
               "I2CSLAVE",
               "I2C_ASYNC"
           ],
           "features": [
               "BLE"
           ],
           "device_name": "STM32L475VG"
       }
   }
   ```

#### Other possible additions

Other changes you may need include:

   - `features_add`, `features_remove`, `components_add`, `components_remove`,
     `macros_add` and `macros_remove` to add or remove configurations.
   - `device_has_add` to add additional drivers.

   <span class="notes">**Note:** If you choose to add a driver that is not
   already available for your hardware, you will have to provide the driver
   implementation.</span>

#### Where other configurations live

All the other configurations for the board are inherited from the MCU Family
configuration called `MCU_STM32L475xG`.

## Configuring the target code directories

In some cases, the target source code directories follow a similar structure to
the target configuration, but they could have a few more levels.

For example, in the `mbed-os/targets` folder, the target directories for
`DISCO_L475VG_IOT01A` follow this pattern:

   ```
   mbed-os
       |_targets
             |_TARGET_STM            <- MCU VENDOR
             |      |_TARGET_STM32L4             <- MCU FAMILY
             |             |_TARGET_STM32L475xG               <- MCU
             |                    |_TARGET_DISCO_L475VG_IOT01A     <- Board
   ```

Boards typically inherit files that support the MCU, MCU family and MCU vendor.
When adding a new board, you need to add a new set of files for the board.

There are more directory levels than target configuration levels because many
targets use the `extra_labels_add` feature in the target configuration. The
keywords `STM32L4`, `STM32L475xG` and `STM32L475VG` resolve to
`TARGET_STM32L4`, `TARGET_STM32L475xG` and `TARGET_STM32L475VG`, respectively.
With those labels applied, the build includes these directory names for this
target.

### Preparing

1. Create a new directory called `TARGET_IMAGINARYBOARD` at the top level of
   your project to store the source files for your board.

1. Inspect the files at
   `mbed-os/targets/TARGET_STM/TARGET_STM32L4/TARGET_STM32L475xG/TARGET_DISCO_L475VG_IOT01A`.
   You should find the following files or similar:

   `PeripheralPinMaps.h`, `PeripheralPins.c`, `PinNames.h`

1. Copy the files into your new `TARGET_IMAGINARYBOARD` directory.

   The files provide these capabilities:

   - `PeripheralPinMaps.h` and `PeripheralPins.c` describe the available pins
     and their association with peripherals.
   - `PinNames.h` sets macros for pins that define their function.

### Customizing

1. Modify the files.

   `PinNames.h` is the most common file to be edited. For this tutorial, the
   ImaginaryBoard uses I2C but connected to different supported signals. Change
   the I2C pin macro definitions from:

   ```
   I2C_SCL     = D15,
   I2C_SDA     = D14,
   ```

   to

   ```
   I2C_SCL     = PC_0,
   I2C_SDA     = PC_1,
   ```

   You may also choose to add or remove peripherals, add or remove pins or
   change the clock frequency by editing `PeripheralNames.h`,
   `PeripheralPins.c`, or `system_clock.c`. For simplicity, this tutorial
   doesn't edit these files.

1. (Optional) Add additional source files for drivers or middleware you have
   implemented for the new board. This tutorial doesn't have any files to add.

1. (Optional) Add a simple application source file for testing.

   To confirm the software builds for the new target, add a file named
   `main.cpp` with the following contents:

   ```
   #include "mbed.h"

   DigitalOut led1(LED1);

   int main()
   {
       while (true) {
           led1 = !led1;
           ThisThread::sleep_for(500ms);
       }
   }
   ```

   This blinks an LED. If `LED1` is not defined, inspect `PinNames.h` for a
   valid pin definition for an available LED.

   Your directory now looks something like this:

   ```
   custom_targets.json
   main.cpp
   mbed_app.json
   mbed-os/
   mbed-os.lib
   TARGET_IMAGINARYBOARD/
   ```

## Testing your code

1. Compile the application:

   ```
   mbed compile -m IMAGINARYBOARD -t <toolchain>
   ```

   When successful, it compiles, links and generates a `.bin` file (or `.hex`
   file for some other boards).

   For example, it prints to the screen:

   ```
   Image: .\BUILD\IMAGINARYBOARD\GCC_ARM\mbed-os-imaginary-port.bin
   ```

1. Program the board.

   You can test this using a `DISCO-L475VG-IOT01A`. If you actually created an
   `ImaginaryBoard` board, you could use that, too.

   <span class="notes">**Note:** Unless your board has an Mbed Enabled debug
   interface, you need a method of flashing the memory on your board.</span>

   Because the `DISCO-L475VG-IOT01A` has an Mbed Enabled debug interface
   (STLink in this case), you can use drag-and-drop programming to flash the
   board.

1. Locate the binary file, and drag it onto the disk drive name for the board
   (for example, `DIS_L4IOT`).

1. Wait for the file transfer to complete.

1. Run the application

   Press the reset button on the board. You should see the LED blinking.

1. (Optional) Run automated tests.

   With an Mbed Enabled debug interface, you can also run the Mbed OS automated
   tests on your port. Because a new board has a new name unknown to the Mbed
   tools, you need to tell the tools which `Platform ID` (aka `detect_code`) to
   associate it to.

   To do this, you can use the `mbedls` `mock` command option. This tutorial
   tests with a `DISCO-L475VG-IOT01A`, which has a debug interface that exposes
   `0764` as its `Platform ID`. If you have a new board that uses a different
   `Platform ID`, such as `1234`, then use that.

   For the `ImaginaryBoard` based on `DISCO-L475VG-IOT01A`, run this command.

   ```
   mbedls --mock 0764:IMAGINARYBOARD
   ```

1. Run the tests, with the following command:

   ```
   mbed test -m IMAGINARYBOARD -t <toolchain>
   ```

   The tests start running.

   For more information on testing a new board, go to the [Testing your
   port](../porting/testing.html) section of the porting guide.

Now you have successfully ported Mbed OS to a new board.
