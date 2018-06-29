## Mbed OS porting guide

This guide will walk you through the steps required to port Mbed OS onto a derivative target of any one of the Mbed OS Enabled targets. If you need to port the MCU to Mbed OS as well, along with a custom board based on the MCU, then you can follow our [more detailed porting guide](https://os.mbed.com/docs/v5.9/reference/porting-targets.html). Mbed Cloud Client provides reference example implementation for three Mbed Enabled targets, namely the FRDM-K64F, NUCLEO_F429ZI and the UBLOX_ODIN_W2_EVK. You do not need to port either Mbed OS or the Cloud Client if you are using one of these three boards.


### Summary of steps

1. Identify the target’s features. Identify if it derives from any existing supported target, as well as the macros and features that need to be supported at a bare minimum. You should also identify supported compilers & the Mbed OS release version.
1. Create the directory structure.
1. Add the target entry in `targets.json`.
1. Add an entry for the target in `mbed_rtx.h`.
1. Add startup code and CMSIS headers, such as device specific register definitions, NVIC headers and ALL relevant drivers from CMSIS specifications, like GPIO’s, peripheral names, pin maps and others. You will also want to add APIs, HAL implementation, and other required headers for the system clocks and any other additional clocks.
<span class="notes">**Note:** Screenshots for the sample implementation are provided at the end of this section.</span>
1. Add toolchain specific linker descriptions.
1. Add peripherals and pin names for the target.
1. Compile with CLI on a supported compiler.


### 1. Identify features, compiler, Mbed OS version, core, CPU name and other features in `targets.json`

Our sample target is identified by the following:

* The name of the target for builds is `MyTarget123`.
* A Cortex-M4F based core.
* Supports Mbed OS v5.xx.
* Has SERIAL interface as a bare minimum to print standard printf messages to the console, once built successfully.
* Supports ARMCC and IAR compilers.
* Inherits some features, such as the default toolchain and the virtual disk from the standard `target` defined in `targets.json`.
* Has all the drivers, APIs, HAL and so on defined in the `/mbed-os/TARGETS` directory as
`TARGET_MY_Vendor/TARGET_VendorMCUs/TARGET_VendorDevice1/TARGET_VendorBoard_1`.
* The public flag is set to `true` to indicate that this target is visible for compilation from the toolchains.

All of these requirements are directly mapped to relevant tags in the `targets.json` entry for our target. This is shown in step 3 below.


### 2. Create the directory structure

The target’s directory structure follows the following hierarchy. The manufacturer is listed at the top level, followed by the device family, followed by a specific device in the family, with the last level being the specific board that uses this specific MCU in the immediate higher level:
```
\mbed-os\targets\TARGET_<Manf>\<Device_Family>\<specific_MCU>\<specific_board>\
```

Our sample implementation uses:
```
\mbed-os\targets\TARGET_MY_Vendor\TARGET_VendorMCUs\TARGET_VendorDevice1\TARGET_VendorBoard_1\
```


### 3. Add the target entry in `targets.json`
```
    "MyTarget123": {
                  "inherits":["Target"],
                  "core":"Cortex-M4F",
                  "public": true,
                  "extra_labels": ["MY_Vendor", "VendorMCUs", "VendorDevice1",
    "VendorBoard_1"],
                  "macros": ["CPU_<Full_Name_of_CPU>"],
                  "supported_toolchains": ["ARM", "IAR"],
                  "device_has": ["SERIAL"],
                  "release_versions": ["5"]
            },
```

<span class="notes">**Note:** The `extra_labels` must mimic the exact directory structure used to define the new target.</span>


### 4. Add an entry in `mbed_rtx.h`

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

More information on these can be found in the MCU's reference manual.


### 5. Add startup code, device specific CMSIS headers, relevant drivers, APIs, HAL implementation and others

  1. Adding startup code and CMSIS specific headers:
    Obtain the startup code and other CMSIS specific headers from the device manufacturer or the CMSIS packs from KEIL.
    You must add these at the `Device` level.
  1. Adding relevant drivers:
    Define drivers in the `device_has` key in `targets.json`. You must include all relevant drivers for all the peripherals defined as values for the `device_has` key in this step. You should add the drivers at the `Device` level.
  1. Adding APIs:
    Mbed OS defines APIs for all HW peripherals, such as GPIO, SPI, RTC and so on. APIs are standard Mbed OS defined and do not need to be modified. You should add these at the `MCU family` level. If these are already available for the MCU that you are using from the silicon vendor, then you can skip this step. Yet, ensure that the drivers are present at the correct level in the directory structure.
  1. HAL implementation:
    HAL for all the peripherals is provided as standard in Mbed OS. HAL implementations are supplied as part of the features in Mbed OS. If these are already available for the MCU that you are using from the silicon vendor, then you can skip this step. Yet, ensure that the drivers are present at the correct level in the directory structure.
  1. Others:
    Make sure `Objects.h` is available in the `/api` directory. You can also declare peripherals here. Finally, you must add any board specific features at the `Board` level.


### 6. Add toolchain specific linker descriptions

All three supported toolchains (uVision, GCC and IAR) need separate linker descriptions. These are: the scatter `*.sct` files for uVision, linker description `*.ld` files for GCC and IAR Linker file `*.icf` for IAR. You need to add these files at the `Device` level under `/device`. Also, make sure the `supported_toolchains` key in `targets.json` specifies all the supported toolchains for the new target. If these are already available for the MCU that you are using from the silicon vendor, then you can skip this step. Yet, ensure that the drivers are present at the correct level in the directory structure.


### 7. Add peripherals and pin names for the target

You must add peripherals names and pin names at the `Board` level, and you must follow standard naming conventions for common peripherals, such as BUTTONs and LEDs. These are defined in the `PinNames.h` header file at the board level. Please refer to Figure 6 below for the directory structure.

If there is more than one peripheral of the same type, then you must define a default for each peripheral. This is required for the application code to use the peripheral without having to specify the number of the peripheral brought out. It is also required to define the DAPLink pins for the new target. An example is shown below:

```
#ifndef MBED_PINNAMES_H
#define MBED_PINNAMES_H

#include "cmsis.h"
#include "PinNamesTypes.h"

#ifdef __cplusplus
extern "C" {
#endif

typedef enum {
    PA_0  = 0x00,
    PA_1  = 0x01,
<snip>
    // ADC internal channels
    ADC_VBAT = 0xF2,

    // Generic signals namings
    LED1        = PB_2,
    LED2        = PB_10,
    LED_RED     = LED1,
    LED_BLUE    = LED2,
    USER_BUTTON = PC_13,

    // Standardized button names
    BUTTON1 = USER_BUTTON,

    SERIAL_TX   = P_8,
    SERIAL_RX   = P_12,

    I2C_SCL     = P_17,
    I2C_SDA     = P_18,

    SPI_MOSI    = P_4,
    SPI_MISO    = P_7,
    SPI_SCK     = P_6,
    SPI_CS      = P_16,

    //DAPLink
    USBRX      = STDIO_UART_RX,
    USBTX      = STDIO_UART_TX,
    SWDIO      = P_26,
    SWCLK      = P_25,
    NTRST      = P_13,

    //MTB Aliases
    //Left side (top view)
    TGT_SWDIO     = SWDIO,
    TGT_SWCLK     = SWCLK,
    TGT_RESET     = NTRST,
    PC6           = SERIAL_TX,
    PC7           = SERIAL_RX,
    PB9           = I2C_SDA,
    PB8           = I2C_SCL,

    //Right side (top view)
    GND           = NC,
    PA11          = P_35,
    PA12          = P_36,

} PinName;

#ifdef __cplusplus
}
#endif

#endif
```


### 8. Compile with a supported compiler

The last step is to build the new target with any supported compiler. This requires you to use an example application, such as Blinky, to compile for the new target. You must use the new Mbed OS directory with the new target added in the example application.

Debug any missing headers for the peripherals, and your new target is ready to be built.

An introductory example of a target that supports only the SERIAL peripheral, which in turn uses the GPIO, to output debug messages by using printf statements in the `main.cpp` is included below. You can use this as a starting point and build from here.


### **Sample implementation**

**Figure 1: Target vendor level directory structure**

<span class="images">![](https://s3-us-west-2.amazonaws.com/cloud-docs-images/Picture1.png)<span>Target vendor level directory structure</span></span>



**Figure 2: Target MCU family level directory structure**

<span class="images">![](https://s3-us-west-2.amazonaws.com/cloud-docs-images/Picture2.png)<span>Target MCU family level directory structure</span></span>



**Figure 3: Target device level**

<span class="images">![](https://s3-us-west-2.amazonaws.com/cloud-docs-images/Picture3.png)<span>Target device level</span></span>



**Figure 4: Target MCU family APIs implementation**

<span class="images">![](https://s3-us-west-2.amazonaws.com/cloud-docs-images/Picture4.png)<span>Target MCU family APIs implementation</span></span>



**Figure 5: Target device level directory structure**

<span class="images">![](https://s3-us-west-2.amazonaws.com/cloud-docs-images/Picture5.png)<span>Target device level directory structure</span></span>



**Figure 6: Target board level**

<span class="images">![](https://s3-us-west-2.amazonaws.com/cloud-docs-images/Picture6.png)<span>Target board level</span></span>



**Figure 7: Target device-specific implementation**

<span class="images">![](https://s3-us-west-2.amazonaws.com/cloud-docs-images/Picture7.png)<span>Target device-specific implementation</span></span>



**Figure 8: Target device-specific toolchain support**

<span class="images">![](https://s3-us-west-2.amazonaws.com/cloud-docs-images/Picture8.png)<span>Target device-specific toolchain support</span></span>



**Figure 9: Target device-specific driver support**

<span class="images">![](https://s3-us-west-2.amazonaws.com/cloud-docs-images/Picture9.png)<span>Target device-specific driver support</span></span>
