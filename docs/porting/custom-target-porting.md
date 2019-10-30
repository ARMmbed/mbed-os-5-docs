# Porting Mbed OS to a custom board

When designing a custom board based on an existing Mbed Enabled board, you may need to make configuration and software changes to adapt Mbed OS to run on your new board. This is called a software port. The necessary changes may include adaptations for the unique design choices you have made for your new board, such as clocking, pin connections and peripheral usage. This can often be accomplished by adding configuration and source files to an Mbed OS-based application project without the need to modify files within `mbed-os`, itself. If you don't plan to push your changes to the upstream `mbed-os` repository, this simplifies your software configuration management by allowing you to keep your new files separate.

Mbed OS supports target inheritance, which allows you to extend an existing microcontroller (MCU) target and just add software and configurations required for your board. You have the ability to add a file named `custom_target.json` to your project, which can store your custom target configurations without the need to modify `targets.json`.

This tutorial covers the most common methods used to create a custom port with `custom_target.json`. For detailed information covering all the ways you can configure targets, go to [adding and configuring targets](../reference/adding-and-configuring-targets.html).

## Extending an existing MCU target configuration

As an example, consider a situation in which you are creating a new board based on an existing Mbed Enabled board. For this tutorial, consider a new board called `ImaginaryBoard` that is based on [DISCO-L475VG-IOT01A](https://os.mbed.com/platforms/ST-Discovery-L475E-IOT01A/).

`ImaginaryBoard` shares most of the features of DISCO-L475VG-IOT01A, but it does not use `AnalogOut`, `AnalogIn`, `CAN` or `USB`. Some pins are also connected differently on the new board.

Assuming you have Mbed CLI installed, follow these steps to make the port.

1. (Optional) Create a new Mbed program (for example, `mbed-os-imaginary-port`).

   If you don't already have an Mbed program on your computer, at a command terminal, run this Mbed CLI command:

   ```
   mbed new --program mbed-os-imaginary-port
   ```
  
   This command imports `mbed-os` from the [official Mbed OS source repository](https://github.com/armmbed/mbed-os) into a new directory called `mbed-os-imaginary-port`.

   Now, change directories into your new project:  

  ```
  cd mbed-os-imaginary-port
  ```

1. Create a new file named `custom_targets.json` at the same level as the `mbed-os` directory:

   Inspect the contents of `mbed-os/targets/targets.json`. For this example, search for `DISCO_L475VG_IOT01A`.

   Copy the contents from the `DISCO_L475VG_IOT01A` section into your `custom_targets.json` file. Be sure to include brackets `{ }` surrounding the content.

   Then make changes for your board. For example, after making changes, the full contents look like this:
   
   ```
   {
     "IMAGINARYBOARD": {
         "components_add": ["QSPIF", "FLASHIAP"],
         "inherits": ["FAMILY_STM32"],
         "core": "Cortex-M4F",
         "extra_labels_add": ["STM32L4", "STM32L475xG", "STM32L475VG"],
         "config": {
             "clock_source": {
                 "help": "Mask value : USE_PLL_HSE_EXTC (need HW patch) | USE_PLL_HSE_XTAL (need HW patch) | USE_PLL_HSI | USE_PLL_MSI",
                 "value": "USE_PLL_MSI",
                 "macro_name": "CLOCK_SOURCE"
             },
             "lpticker_lptim": {
                 "help": "This target supports LPTIM. Set value 1 to use LPTIM for LPTICKER, or 0 to use RTC wakeup timer",
                 "value": 1
             }
         },
         "overrides": { "lpticker_delay_ticks": 4 },
         "detect_code": ["1234"],
         "macros_add": [
             "MBED_TICKLESS",
             "MBED_SPLIT_HEAP"
         ],
         "device_has_add": [
             "CRC",
             "TRNG",
             "FLASH",
             "QSPI",
             "MPU"
         ],
         "device_has_remove": [         
             "ANALOGIN",
             "I2CSLAVE",
             "I2C_ASYNCH"
         ],                     
         "release_versions": ["2", "5"],
         "device_name": "STM32L475VG",
         "bootloader_supported": true
     }
   }
   ```

   Let's review the changes one by one.

   - The board name was changed from `DISCO_L475VG_IOT01A` to `IMAGINARYBOARD` so the board can be uniquely identified.

   - The `detect_code` was changed from `0764` to `1234`. The `detect_code` is a unique number that identifies the board to the Mbed OS test tools. This number is typically built into the debug interface.

   - The `macros_add` section was changed to remove `USBHOST_OTHER` because USB is not used on the new board.

   - The `device_has_add` section was changed to not add the `ANALOGOUT`, `CAN`, and `USBDEVICE` drivers because those features are not used on the new board.

   - A new section, `device_has_remove`, was added. This removes `ANALOGIN`, `I2CSLAVE`, and `I2C_ASYNCH` drivers because these features are also not used.  The reason why `device_has_remove` is used in this case is because the board is inheriting from the MCU Family configuration `FAMILY_STM32`, which has those drivers added by default.

   All the other configurations for the board are inherited from the MCU Family configuration called `FAMILY_STM32`.  

   Here are some other typical changes that might be needed.
   
   - (Optional) You can also use `device_has_add` to add additional drivers.

   <span class="notes">**Note:** If you choose to add a driver, you may have to provide the driver implementation if it is not already available for your hardware.</span>

   - (Optional) Similarly, you can use `features_add`, `features_remove`, `components_add`, `components_remove`, `macros_add` and `macros_remove` to add/remove configurations.

## Configuring the target code directories

In some cases, the target source code directories follow a similar structure as the target configuration, but they could have a few more levels.

For example, in the `mbed-os/targets` folder, the target directories for DISCO_L475VG_IOT01A follow this pattern:

   ```
   mbed-os
       |_targets
             |_TARGET_STM            <- MCU VENDOR
             |      |_TARGET_STM32L4             <- MCU FAMILY
             |             |_TARGET_STM32L475xG               <- MCU
             |                    |_TARGET_DISCO_L475VG_IOT01A     <- Board
   ```

Boards typically inherit files that support the MCU, MCU family and MCU vendor. When adding a new board, you need to add a new set of files for the board.

You may be wondering why there are more directory levels than target configuration levels. This is because many targets use the `extra_labels_add` feature in the target configuration. The following keywords `STM32L4`, `STM32L475xG`, `STM32L475VG` resolve to `TARGET_STM32L4`, `TARGET_STM32L475xG`, `TARGET_STM32L475VG` respectively. With those labels applied, these directory names get included in the build for this target.

1. Create a new directory called `TARGET_IMAGINARYBOARD` at the top level of your project.
   
   Your directory should look something like this:
   
   ```
   custom_target.json
   TARGET_IMAGINARYBOARD
   mbed-os
   .mbed
   mbed_settings.py
   mbed-os.lib
   ```
   
1. Now place source files for the board.
   
   Inspect the files at `mbed-os\targets\TARGET_STM\TARGET_STM32L4\TARGET_STM32L475xG\TARGET_DISCO_L475VG_IOT01A`. You should find the following files or similar:
   
   `PeripheralNames.h`, `PeripheralPins.c`, `PinNames.h`, `system_clock.c`
   
   Copy the files into your new `TARGET_IMAGINARYBOARD` directory.
   
   The files provide these capabilities.
      
   - `PeripheralNames.h` describes the available peripherals and their base addresses.
   - `PeripheralPins.c` describes the available pins and their association with peripherals.
   - `PinNames.h` sets macros for pins that define their function.
   - `system_clock.c` vendor specific file that initializes the system and sets up the clocks.
      
1. Modify the files.

   `PinNames.h` is the most common file to be edited. For our example, the ImaginaryBoard is using I2C but connected to different supported signals. Change the I2C pin macro definitions from:
   
   ```
   I2C_SCL     = D15,
   I2C_SDA     = D14,
   ```
   
   to
   
   ```
   I2C_SCL     = PC_0,
   I2C_SDA     = PC_1,
   ```
   
   This edit is mainly for convenience if your application code uses standard I2C pin names `I2C_SDA` and `I2C_SCL`.
   
   You may also choose to add or remove peripherals, add or remove pins or change the clock frequency by editing `PeripheralNames.h`, `PeripheralPins.c` or `system_clock.c`. In our example, for simplicity, we will not edit these files.
   
1. (Optional) Add additional files.

   If necessary, add additional source files for drivers or middleware you have implemented for the new board. In our example, we do not have any files to add.

1. (Optional) Add a simple application source file for testing.

    To confirm the software builds for the new target, add a file named `main.cpp` with the following contents:

    ```  
    #include "mbed.h"
    
    DigitalOut led1(LED1);

    int main()
    {
        while (true) {
            led1 = !led1;
            wait_ms(500);
        }
    }
    ``` 

    This blinks an LED. Just make sure LED1 is defined for the board.
    
    Your directory now looks something like this:
    
    ```
    main.cpp
    custom_target.json
    TARGET_IMAGINARYBOARD
    mbed-os
    .mbed
    mbed_settings.py
    mbed-os.lib
    ```
    
1. Compile the project.
   
  With the target configuration set and files added, it is ready to compile. Run the command:

   ```
   mbed compile -m IMAGINARYBOARD -t <toolchain>
   ```
   
   When successful, it compiles, links and generates a `.bin` file (or `.hex` file for some other boards).

   For example, it prints to the screen:
   
   ```
   Image: .\BUILD\IMAGINARYBOARD\GCC_ARM\mbed-os-imaginary-port.bin
   ```

1. Program the board.  

  You can test this simple example using a `DISCO-L475VG-IOT01A`. If you actually created a `ImaginaryBoard` board, you could use that too.  
  
  <span class="notes">**Note:** Unless your board has an Mbed Enabled debug interface, you need a method of flashing the memory on your board. </span>
  
  Since the `DISCO-L475VG-IOT01A` has a Mbed Enabled debug interface (STLink in this case), we can use drag-and-drop programming to flash the board.
  
  Locate the binary file and drag it onto the disk drive name for the board (for example, `DIS_L4IOT`).
  
  After the file transfer is complete, press the reset button on the board. You should see the LED blinking.
 
1. (Optional) Run automated tests.

  With an Mbed Enabled debug interface, you can also run the Mbed OS automated tests on your port. Since a new board has a new name that is unknown to the Mbed tools, you will need to tell the tools which `detect_code` to associate it to.
  
  To do this, you can use the `mbedls` `mock` command option. In our case, we are testing with a `DISCO-L475VG-IOT01A`, which has a debug interface that exposes `0764` as its detect code. If you have a new board that is using a different detect_code, such as `1234`, then use that.
  
  For the `ImaginaryBoard` based on `DISCO-L475VG-IOT01A`, run this command.

  ```
  mbedls --mock 0764:IMAGINARYBOARD
  ```
   
   <span class="notes">**Note:** Contact the Arm Mbed team to get a unique ID if you plan to have your board coexist with other Mbed Enabled boards while running automated tests.</span>

  Now run the tests, with the following command.
  
  ```
  mbed test -m IMAGINARYBOARD -t <toolchain>
  ```
  
  The tests should start running.
  
Now you have successfully ported Mbed OS to a new board.
