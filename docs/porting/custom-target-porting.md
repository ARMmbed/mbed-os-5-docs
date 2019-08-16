# Porting Mbed OS to a custom board

If you are designing a board similar to an existing Mbed Enabled board, you can use target inheritance to configure your board to meet your needs. In previous versions of Mbed OS (before Mbed OS 5.8), adding a new target required modifying the `mbed-os` directory tree itself, but now you can extend an existing MCU port with a `custom_target.json` file and by adding source files that complete a port outside of `mbed-os`.

For detailed information about all the ways you can configure targets, go to [adding and configuring targets](../reference/adding-and-configuring-targets.html).

## Extending an existing Mbed Enabled MCU target configuration

As an example, consider a situation in which you are creating a new board based on an existing Mbed Enabled board. This tutorial considers a new board called ImaginaryBoard that is based on NRF52840.

ImaginaryBoard is the same as the standard NRF52840 development kit, but you want to remove some unused features, such as AnalogIn, and change the way some pins are connected.

1. Choose a target in Mbed OS that your board can inherit from. 

   If that existing target follows one of the recommended inheritance patterns, such as Family -> MCU -> Board, then it makes it simple to just inherit the MCU target information and add your own board information. In some cases, you may need to inherit a Family or Board and add or replace configurations accordingly.

   In this example, there is an MCU target configuration in `mbed-os/targets/targets.json` that the new board can inherit from. It is called MCU_NRF52840.
   
   Below is a short summary of the MCU target. For simplicity, areas have been omitted.
   
   From `mbed-os/targets/targets.json`:
   
   ```
       "MCU_NRF52840": {
           "inherits": ["Target"],
           "components_add": […],
           "core": "Cortex-M4F",
           "macros": […],
           "features": […],
           "device_has": […],
           "extra_labels": […],
           "config": {…},
           "overrides": {…},
           "OUTPUT_EXT": "hex",
           "supported_toolchains": ["GCC_ARM", "ARM", "IAR"],
           "public": false,
           "detect_code": ["1101"],
           "bootloader_supported": true
       }
   ```
   
   For reference, the standard NRF52840 development kit configuration is below. It inherits from the MCU target.
   
   ```
       "NRF52840_DK": {
           "supported_form_factors": ["ARDUINO"],
           "inherits": ["MCU_NRF52840"],
           "release_versions": ["5"],
           "device_name": "nRF52840_xxAA"
       },
   ```
   
   In this example, the new board is similar to the NRF52840 development kit. 
   
1. Instead of making edits within `mbed-os`, create a `custom_target.json` file, and put it in a directory alongside `mbed-os`.
   
   For example:  
   
   ```
   {
   "IMAGINARYTARGET": {
           "inherits": ["MCU_NRF52840"],
           "release_versions": ["5"],
           "device_name": "nRF52840_xxAA",
           "detect_code": ["1234"],
           "device_has_remove": ["ANALOGIN"],
           “components_remove”: ["QSPI"]
       }
   }
   ```
   
   The new board target configuration inherits the MCU target, then follows similar configurations to the development kit, including specifying it should build with Mbed OS 5. Also, it uses `device_name nRF52840_xxAA`, which matches the CMSIS pack for that device. The `detect_code` is a unique ID that identifies the board to the Mbed OS test tools.
   
   <span class="notes">**Note:** Contact the Arm Mbed team to get a unique ID, especially if you plan to have your board coexist with other Mbed Enabled boards while running automated tests.</span>

1. The new ImaginaryBoard board does not use AnalogIn, and it does not have a Quad SPI. Remove those. 

   1. AnalogIn is an Mbed OS HAL driver, which the MCU target added using `device_has`. Remove it with `device_has_remove`. 
   1. Similarly, the MCU target added QSPI using `components_add`. Remove it with `components_remove`.

1. Add `device_has_remove` to disassociate the AnalogIn driver from your target.

1. (Optional) You can also use `device_has_add` to add additional drivers.

   <span class="notes">**Note:** If you choose to add a driver, you may have to provide the driver implementation if it is not already available for your hardware.</span>

1. (Optional) Similarly, you can use `features_add`, `features_remove`, `components_add`, `components_remove`, `macros_add` and `macros_remove`.

## Configuring the code directory and folders

The target source code directory should follow a similar structure as the target configuration.

For example, in the `mbed-os/targets` folder, the directories follow this pattern:

```
mbed-os
    |_targets
           |_TARGET_NORDIC            <- MCU VENDOR
           |      |_TARGET_NRF5x            <- MCU FAMILY #1
           |             |_TARGET_NRF52            <- MCU FAMILY #2
           |                    |_TARGET_MCU_NRF52840            <- MCU
           |                           |_TARGET_NRF52840_DK            <- Board
```

This example adds your own board, inherits files from the MCU Family and MCU folders and adds your own board files.

1. Create a new directory called `TARGET_IMAGINARYBOARD`. Place this folder at the top level of your project.
   
   It should look something like this:
   
   ```
   custom_target.json
   TARGET_IMAGINARYBOARD
   mbed-os
   ```
   
1. Now, place files for the board.
   
   The following are typical files that are included for a board:
   
   `device.h`, `PeripheralNames.h`, `PeripheralPins.c` and `PinNames.h`.
   
   Some boards might also require files such as `mbed_overrides.c` or clock configuration files if they aren’t included at a higher level.

   In the case of the NRF52840, a derivative board only requires `device.h` and `PinNames.h`:
   
   -	`device.h` provides device-specific includes.
   -	`PinNames.h` sets macros for pins that define their function.
   
1. Copy these files from `TARGET_NRF52840_DK` to `TARGET_IMAGINARYBOARD` and modify. For example, in `PinNames.h`, if the ImaginaryBoard is using I2C but connected to different signals than the NRF52840_DK, change the I2C pin macro defines from:
   
   ```
       I2C_SDA0 = p26,
       I2C_SCL0 = p27,
   ```
   
   to
   
   ```
      I2C_SDA0 = p46,
      I2C_SCL0 = p47,
   ```
   
   With the target configuration set and files added, it is ready to compile.

1. Using Mbed CLI, run the command:
   
   ```
   mbed compile -m ImaginaryBoard -t <toolchain>
   ```
   
When successful, it compiles, links and generates a .bin or .hex file.

### Additional notes

- Many targets also use the `extra labels` configuration option to include directories in a build. Often this feature is used to include Family and MCU target directories instead of target inheritance.  
- Unless your board has an Mbed Enabled debug interface, you need a method of flashing the memory on your board.

### Todo:

- Need to test and confirm this is working for a few different platform types.
- What happens if you inherit a board config and provide a duplicate file such as PinNames.h?
- Need to test and make a note if macro add doesn’t work with macro remove in the same tree
