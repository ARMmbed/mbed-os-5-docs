### Bootstrap

TODO: directory structure
TODO: mbed boot process explaination and hooks
TODO: nvic in RAM
TODO: linker script

You need CMSIS-CORE files for startup and peripheral memory addresses, and you need linker scripts for Arm, IAR and GCC toolchains. These files are usually in the `mbed-os\targets\TARGET_VENDOR\TARGET_MCU_FAMILY\TARGET_MCUNAME\device` directory.

Mbed OS requires dynamic vector relocation, which requires extensions to CMSIS-CORE. Extend CMSIS-CORE by adding an `mbed-os\targets\TARGET_VENDOR\TARGET_MCUNAME\cmsis.h` file. This header file defines the vector relocation additions and device-specific headers that include CMSIS-CORE. Next add a relocation function in `mbed-os\targets\TARGET_VENDOR\TARGET_MCUNAME\cmsis_nvic.c and .h`. This relocation function changes the contents of the Interrupt Vector Table at run time.

CMSIS-RTOS needs a few macros to initialize the SYS_TICK. These macros are usually configured in`mbed-os\targets\TARGET_VENDOR\mbed-rtx.h`.

Now verify that your target compiles by using `mbed compile -m MCU_NAME -t <toolchain>`.

The next step to port a target is to enable the test harness dependencies. To run the test suite, your target must support GPIO, microsecond ticker and serial.
