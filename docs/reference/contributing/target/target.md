<h2 id="target-port">Porting targets</h2>

This document discusses requirements for porting Mbed OS to a derivative target of any one of the Mbed OS Enabled targets. To port the MCU to Mbed OS as well, along with a custom board based on the MCU, please follow our [more detailed porting guide](docs/development/reference/porting-targets.html). 

Adding a new microcontroller to Arm Mbed OS 5 depends on CMSIS-CORE and CMSIS-Pack. The microcontroller must have these available.

[Mbed Cloud Client](https://cloud.mbed.com/docs/current) provides reference implementation for three Mbed Enabled targets: the K64F, NUCLEO_F429ZI and the UBLOX_EVK_ODIN_W2. You do not need to port Mbed OS or the Cloud Client if you are using one of these three boards.

### Summary of steps

1. Add your target to `targets.json`.
   1. Identify your target’s features.
   1. Identify any existing parent targets.
   1. Identify macros required for your target's compilation.
   1. Identify supported compilers and the Mbed OS release version.
   1. Add the target entry in `targets.json`.
   1. Verify that you can now pass your target to `mbed compile`.
1. Add your target port.
   1. Create the directory structure.
   1. Add an entry for the target in `mbed_rtx.h`.
   1. Add startup code, CMSIS headers, NVIC headers and **all** relevant drivers from the CMSIS specifications.
   1. Implement APIs, HAL, the system clock configuration and any other additional clocks.
   1. Add toolchain-specific linker descriptions.
1. Add peripherals and pin names for the target.
1. Compile with CLI on a supported compiler.

### Target properties

You can identify our sample target by the following:

- Target build name `MY_BOARD_1`.
- Vendor `MY_VENDOR`, device family `MY_FAMILY` and the device on the board `MY_DEVICE`.
- A Cortex-M4F based core.
- Porting for Mbed OS v5.x, which requires support for Arm Compiler 5, GCC Arm Embedded and IAR EWARM.
- A serial (UART) interface connected to the CMSIS-DAP implementation.
- Requirement that the macro `CPU_DEVICE_1` compiles the vendor-provided HAL for the device mounted on the board.
- Requirement that the macro `FAMILY_MY_FAMILY` compiles the vendor-provided HAL for the family of the device.

All of these requirements directly map to relevant tags in the `targets.json` entry for our target. This is shown in the following step.

### Adding a new microcontroller and board

First fork the `mbed-os` repository. This example uses the placeholder `USERNAME` to refer to your username in the following documentation, `MCU_NAME` to refer to the new microcontroller you are adding and `BOARD_NAME` to refer to the new board you are adding. Import an Mbed OS example, and add your fork of `mbed-os` using:

```
mbed import mbed-os-example-blinky
cd mbed-os-example-blinky\mbed-os
git checkout master
git pull
git checkout -b my-new-target
git remote add USERNAME https://github.com/USERNAME/mbed-os
git branch my-new-target -u USERNAME
cd ..
```

### Target description

Add the target description to `mbed-os\targets\targets.json` using keys that the [Adding and configuring targets section](/docs/development/tools/adding-and-configuring-targets.html) describes. We recommend that you run the [targets lint script](/docs/development/tools/adding-and-configuring-targets.html#style-guide) on your target hierarchy before submitting your pull request:

``` json
"MCU_NAME": {
    "inherits": ["Target"],
    "core": "Cortex-M3",
    "supported_toolchains": ["ARM", "GCC_ARM", "IAR"],
    "device_has": ["SERIAL", "STDIO_MESSAGES"]
},
"BOARD_NAME": {
    "inherits": ["MCU_NAME"],
    "macros_add": []
}
```

### Directory structure

The target’s directory structure has the following hierarchy: 

- The top level lists the manufacturer. This is the same for all targets that a vendor supports.
- The device family. This is specific to a family.
- A specific device in the family. This only applies to the single device.
- The specific board that uses the MCU in the previous level. You can use this for pin maps.

```
/mbed-os/targets/TARGET_<Manf>/TARGET_<Device_Family>/TARGET_<specific_MCU>/TARGET_<specific_board>/
```

This sample implementation uses:

```
/mbed-os/targets/TARGET_MY_VENDOR/TARGET_MY_FAMILY/TARGET_MY_DEVICE_1/TARGET_MY_BOARD_1/
```

### Entry in `mbed_rtx.h`

The `mbed_rtx` header file defines the core requirements for the RTOS, such as clock frequency, initial stack pointer, stack size, task counts and other macros. This sample target has the following specifications:

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

### Startup and HAL

Ensure that the drivers are present at the correct level in the directory structure:

1. Add startup code and CMSIS specific headers. You may obtain the startup code and other CMSIS specific headers from the device manufacturer or the CMSIS packs from KEIL&reg;.
1. Add peripherals to the `device_has_add` key in `targets.json` and include all relevant drivers for all these peripherals.
1. Implement Mbed OS HAL APIs for all hardware peripherals mentioned in `device_has`.
1. Ensure that `Objects.h` declares peripherals and is available in the `/api` directory.

### Linker files

Each supported toolchain listed in your new target's `supported_toolchains` configuration needs a linker file. Each compiler supports a different style of linker files with a different extension:

- Add a scatter file, with the extension `.sct`, for Arm Compiler 5.
- Add a linker script, with the extension `.ld`, for GCC Arm Embedded.
- Add an IAR Linker file, with the extension `.icf`, for IAR EWARM.

### Pin names

Add peripheral names and pin names, following standard naming conventions for common peripherals. Define these pins in the `PinNames.h` header file at the board level. Please refer to the [sample directory structure](sample-directory-structure) for the directory structure.

Define a default for each peripheral. Define the DAPLink serial pins as `STDIO_UART_RX` and `STDIO_UART_TX`. For example:

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

### Compiling with a supported compiler

You can verify that the new board port compiles by using an [example application](/docs/development/tutorials/mbed-os-quick-start.html), and checking out the branch containing your port in the `mbed-os` subdirectory.

### Sample directory structure

Below is an example of all of the files that you would add for a target from vendor `MY_VENDOR` with an MCU, `MY_DEVICE_1` from device family `MY_FAMILY_1` mounted on the board `MY_BOARD_1` supporting the `SERIAL` device:

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

### HAL porting

There are many more APIs to implement. You enable the following APIs by adding a `device_has` attribute to the MCU_NAME target definition in `targets.json` and providing an implementation of the API declared in the API header.

device_has       |   API header
-----------------|------------------
ANALOGIN         |   analog_in.h
ANALOGOUT        |   analog_out.h
CAN              |   can_api.h
EMAC             |   emac_api.h
INTERRUPTIN      |   gpio_irq_api.h
I2C I2CSLAVE     |   i2c_api.h
LPTICKER         |   lp_ticker_api.h
LPTICKER         |   lp_ticker_api.h
PORT_IN PORT_OUT |   port_api.h
PWMOUT           |   pwmout_api.h
RTC              |   rtc_api.h
SLEEP            |   sleep_api.h
SPI SPISLAVE     |   spi_api.h
TRNG             |   trng_api.h
FLASH            |   flash_api.h
