### Bootstrap

#### Bring in CMSIS-Core files

You need CMSIS-CORE files for startup and peripheral memory addresses, and you need linker scripts for Arm, IAR and GCC toolchains. These files are usually in the `mbed-os\targets\TARGET_VENDOR\TARGET_MCU_FAMILY\TARGET_MCUNAME\device` directory.

#### Modify Linker scripts

After adding the core files, the next step is to update the linker scripts for `mbed-os`. To do this, follow the steps below.

- Reserve space for the RAM vector table. For the example below, this is:

    ```
    RW_IRAM1 (0x20000000 + (VECTORS*4)) (0x30000 - (VECTORS*4))  {  ; RW data
    ```

- Define the start of the heap:
    - Arm - The heap starts immediately after the region `RW_IRAM1`.
    - GCC_ARM - The heap starts at the symbol `__end__`.
    - IAR - The heap is the `HEAP` region.
    - Add defines for a relocatable application - `MBED_APP_START` and `MBED_APP_SIZE`.
    - Add preprocessing directive `#! armcc -E` (ARM compiler only).

Example linker script for the Arm compiler:

```
#! armcc -E

#if !defined(MBED_APP_START)
  #define MBED_APP_START 0x08000000
#endif

#if !defined(MBED_APP_SIZE)
  #define MBED_APP_SIZE 0x200000
#endif

;This value must match NVIC_NUM_VECTORS
#define VECTORS 107

LR_IROM1 MBED_APP_START MBED_APP_SIZE  {

  ER_IROM1 MBED_APP_START MBED_APP_SIZE  {
     *.o (RESET, +First)
     *(InRoot$$Sections)
     .ANY (+RO)
   }

   RW_IRAM1 (0x20000000 + (VECTORS*4)) (0x30000 - (VECTORS*4))  {  ; RW data
    .ANY (+RW +ZI)
   }
 }
```

#### Create and update files

- Extend CMSIS-CORE by adding the file `mbed-os\targets\TARGET_VENDOR\TARGET_MCUNAME\cmsis.h`. This header file includes device-specific headers that include CMSIS-CORE.
- Add a relocation function in `mbed-os\targets\TARGET_VENDOR\TARGET_MCUNAME\cmsis_nvic.h`. This contains the define `NVIC_NUM_VECTORS`, which is the number of vectors the devices has, and `NVIC_RAM_VECTOR_ADDRESS`, which is the address of the RAM vector table.
- Define the initial stack pointer, `INITIAL_SP`, in `mbed_rtx.h`. This file is typically in `mbed-os\targets\TARGET_VENDOR\mbed_rtx.h`.
- Add an entry for your device in `mbed-os\targets\targets.json`

#### Finishing

Now verify that your target compiles by using `mbed compile -m MCU_NAME -t <toolchain>`.

The next step to port a target is to enable the test harness dependencies. To run the test suite, your target must support GPIO, microsecond ticker and serial.
