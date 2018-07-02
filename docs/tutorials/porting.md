## Mbed OS porting guide

This guide will walk you through the steps required to port Mbed OS onto a derivative target of any one of the Mbed OS Enabled targets. If you need to port the MCU to Mbed OS as well, along with a custom board based on the MCU, then you can follow our [more detailed porting guide](https://os.mbed.com/docs/v5.9/reference/porting-targets.html). 

Mbed Cloud Client provides reference implementation for three Mbed Enabled targets, namely the K64F, NUCLEO_F429ZI and the UBLOX_EVK_ODIN_W2. You do not need to port either Mbed OS or the Cloud Client if you are using one of these three boards.


### Summary of steps

1. Add your target to `targets.json`
    1. Identify the your target’s features.
    1. Identify any existing parent targets.
    1. Identify macros required for you target's compilation
    1. Identify supported compilers and the Mbed OS release version.
    1. Add the target entry in `targets.json`.
    1. Verify that you can now pass your target to `mbed compile`.
1. Add your target port
    1. Create the directory structure.
    1. Add an entry for the target in `mbed_rtx.h`.
    1. Add startup code and CMSIS headers, NVIC headers and **all** relevant drivers from CMSIS specifications
    1. Implement APIs, HAL, the system clock configuration and any other additional clocks.
    1. Add toolchain-specific linker descriptions.
1. Add peripherals and pin names for the target.
1. Compile with CLI on a supported compiler.


### Identify Target properties

Our sample target is identified by the following:

* The name of the target for builds is `MY_BOARD_1`.
* The vendor is "MY_VENDOR", the device family is "MY_FAMILY" and the device on the board is "MY_DEVICE"
* A Cortex-M4F based core.
* Porting for Mbed OS v5.x, which requires support for Arm Compiler 5, GCC Arm Embedded, and IAR EWARM.
* Has a serial (UART) interface connected to the CMSIS-DAP implementation.
* Requires the macro `CPU_DEVICE_1` to compile the vendor-provided HAL for the device mounted on the board.
* Requires the macro `FAMILY_MY_FAMILY` to compile the vendor-provided HAL for the family of the device.

All of these requirements are directly mapped to relevant tags in the `targets.json` entry for our target. This is shown in step 3 below.


### Add the target entry in `targets.json`
```json
"MY_FAMILY": {
    "inherits": ["Target"],
    "macros_add": ["FAMILY_MY_FAMILY"],
    "extra_labels_add": ["MY_VENDOR"],
    "public": false
},
"MY_DEVICE_1": {
    "inherits": ["MY_FAMILY"],
    "macros_add": ["CPU_DEVICE_1"],
    "supported_toolchains": ["GCC_ARM", "ARM", "IAR"],
    "device_has_add": ["SERIAL"],
    "core": "Cortex-M4F",
    "release_versions": [5]
},
"MY_BOARD_1": {
    "inherits":["MY_DEVICE_1"]
},
```

<span class="notes">**Note:** The `extra_labels_add` of `MY_VENDOR` is a stand in for the vendor, as it would not configure anything by itself.</span>


### Create the directory structure

The target’s directory structure has the following hierarchy: 
- The manufacturer is listed at the top level. This is used for implantation that is general to all targets supported by a vendor.
- The device family. This is used for implementation that is specific to a family.
- A specific device in the family. This is used for implementation that applies to only the single device.
- The specific board that uses the MCU in the previous level. This is used for pin maps.

```
/mbed-os/targets/TARGET_<Manf>/TARGET_<Device_Family>/TARGET_<specific_MCU>/TARGET_<specific_board>/
```

Our sample implementation uses:
```
/mbed-os/targets/TARGET_MY_VENDOR/TARGET_MY_FAMILY/TARGET_MY_DEVICE_1/TARGET_MY_BOARD_1/
```


### Add an entry in `mbed_rtx.h`

The `mbed_rtx` header file defines the core requirements for the RTOS, such as clock frequency, initial stack pointer, stack size, task counts and other macros. The sample target implemented here has the following specs:
```

    #elif defined(TARGET_MyTarget123)

    #ifndef INITIAL_SP
    #define INITIAL_SP              (0x20030000UL)
    #endif

    #if defined(__CC_ARM) || defined(__GNUC__)
    #define ISR_STACK_SIZE          (0x1000)
    #endif

    #ifndef OS_TASKCNT
    #define OS_TASKCNT              14
    #endif
    #ifndef OS_MAINSTKSIZE
    #define OS_MAINSTKSIZE          256
    #endif
    #ifndef OS_CLOCK
    #define OS_CLOCK                120000000
    #endif   
```

Please refer to your chosen MCU's reference manual for these values.


### Implement startup and HAL

Ensure that the drivers are present at the correct level in the directory structure.

1. Add startup code and CMSIS specific headers. You may obtain the startup code and other CMSIS specific headers from the device manufacturer or the CMSIS packs from KEIL.
1. Add peripherals to the `device_has_add` key in `targets.json` and include all relevant drivers for all these peripherals.
1. Implement Mbed OS HAL APIs for all hardware peripherals mentioned in `device_has`.
1. Ensure that `Objects.h` declares peripherals and is available in the `/api` directory.


### Add linker files

For each supported toolchain listed in your new target's `supported_toolchains` configuration, add a linker file. Each compiler supports a different style of linker files with a different extension.
- Add a scatter file, with the extension `.sct`, for Arm Compiler 5.
- Add a linker script, with the extension `.ld`, for GCC Arm Embedded.
- Add an IAR Linker file, with the extension `.icf`, for IAR EWARM. 


### Add pin names

Add peripheral names and pin names, following standard naming conventions for common peripherals. Define these pins in the `PinNames.h` header file at the board level. Please refer to Figure 6 below for the directory structure.

Define a default for each peripheral. Define the DAPLink serial pins as `STDIO_UART_RX` and `STDIO_UART_TX`.  For example:

```C
#ifndef MBED_PINNAMES_H
#define MBED_PINNAMES_H

#ifdef __cplusplus
extern "C" {
#endif

typedef enum {
    PA_0  = 0x00,
    PA_1  = 0x01,
    PA_1  = 0x01,
<snip>

    // Generic signals namings
    LED1        = PB_2,
    LED2        = PB_10,
    LED_RED     = LED1,
    LED_BLUE    = LED2,
    USER_BUTTON = PC_13,

    // Standardized button names
    BUTTON1 = USER_BUTTON,

    SERIAL_TX   = PA_8,
    SERIAL_RX   = PA_12,

    I2C_SCL     = PA_17,
    I2C_SDA     = PA_18,

    SPI_MOSI    = PA_4,
    SPI_MISO    = PA_7,
    SPI_SCK     = PA_6,
    SPI_CS      = PA_16,

    //DAPLink
    STDIO_UART_RX = SERIAL_RX
    STDIO_UART_TX = SERIAL_TX
    USBRX      = STDIO_UART_RX,
    USBTX      = STDIO_UART_TX,
    SWDIO      = PA_26,
    SWCLK      = PA_25,
    NTRST      = PA_13,
} PinName;

#ifdef __cplusplus
}
#endif

#endif
```


### Compile with a supported compiler

Finally, verify that the new board port compiles. Use an example application, such as [Blinky](https://github.com/ARMmbed/mbed-os-example-blinky), and checkout the branch containing your port in the `mbed-os` sub-directory. Correct any compiler errors and then submit a pull request to [the master branch of the upstream repo](https://github.com/ARMmbed/mbed-os/pull/new/master)


### Sample directory structure

Below is an example of all of the files that would be added for a target from vendor `MY_VENDOR` with an MCU, `MY_DEVICE_1` from device family `MY_FAMILY_1` mounted on the board `MY_BOARD_1` supporting the `SERIAL` device.

```
mbed-os
└── targets
   └── TARGET_MY_VENDOR
      ├── TARGET_MY_FAMILY
      │  ├── TARGET_MY_DEVICE_1
      │  │  ├── TARGET_MY_BOARD_1
      │  │  │  ├── PeripheralNames.h
      │  │  │  ├── PeripheralPins.c
      │  │  │  ├── PeripheralPins.h
      │  │  │  ├── clock_config.c
      │  │  │  ├── clock_config.h
      │  │  │  └── device.h
      │  │  ├── TOOLCHAIN_ARM
      │  │  │  ├── device.sct
      │  │  │  └── startup.S
      │  │  ├── TOOLCHAIN_GCC
      │  │  │  ├── device.ld
      │  │  │  └── startup.S
      │  │  ├── TOOLCHAIN_IAR
      │  │  │  ├── device.icf
      │  │  │  └── startup.S
      │  │  ├── clock.c
      │  │  ├── clock.h
      │  │  ├── uart.c
      │  │  ├── uart.h
      │  │  └── us_ticker.c
      │  └── api
      │     ├── Objects.h
      │     └── PortNames.h
      └── mbed_rtx.h
```
