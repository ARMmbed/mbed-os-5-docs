# Bootstrap

## Bring in CMSIS-Core files

To work with Mbed OS, you need to implement CMSIS-Core support for your device as the [CMSIS-Core documentation](http://www.keil.com/pack/doc/CMSIS/Core/html/index.html) describes. CMSIS-Core files are usually in the `mbed-os\targets\TARGET_<VENDOR>\TARGET_MCU_<FAMILY>\TARGET_<MCUNAME>\device` directory.

### Startup files

The startup file contains interrupt vectors and low-level core and platform initialization routines. You need to provide a version of this file for each Mbed OS supported toolchain.

For more information about startup files, please see the [CMSIS documentation](http://www.keil.com/pack/doc/CMSIS/Core/html/startup_s_pg.html).

The template startup file in the CMSIS documentation includes heap and stack regions in the assembler. Omit these regions in Mbed OS because they come from the [linker script](#linker-scripts).

The initial stack pointer the vector table specifies should be derived from the linker script (as `|ARM_LIB_STACK$$ZI$$Limit|`, `__StackTop` or `sfe(CSTACK)`), rather than hardcoded in the startup file.

### Linker scripts

After adding the core files, the next step is to add linker scripts for Mbed OS. To do this, you can either use the linker scripts below and change the defines for your target or you can  modify an existing linker script to be compatible with Mbed OS. You need to provide a version of the linker script for each Mbed OS supported toolchain.

If you are updating your own linker script, you must:

- Reserve space for the RAM vector table.
- Define the heap region:
    - Arm - The heap is the `ARM_LIB_HEAP` region.
    - GCC_ARM - The heap starts at the symbol `__end__` and ends at the `__HeapLimit` symbol.
    - IAR - The heap is the `HEAP` region.
- Define the boot stack region:
    - Arm - The boot stack is the `ARM_LIB_STACK` region.
    - GCC_ARM - The boot stack starts at the symbol `__StackLimit` and ends at the symbol `__StackTop`.
    - IAR - The boot stack is the `CSTACK` region.
- Add defines for a relocatable application - `MBED_APP_START` and `MBED_APP_SIZE`.
- Add the define for boot stack size - `MBED_BOOT_STACK_SIZE`.
- Add preprocessing directive `#! armcc -E` (ARM compiler only).

If you are using the below linker script, then you need to update all the defines in the `/* Device specific values */` section for your target.

Arm linker script template:

```
#! armcc -E

/* Device specific values */

/* Tools provide -DMBED_ROM_START=xxx -DMBED_ROM_SIZE=xxx -DMBED_RAM_START=xxx -DMBED_RAM_SIZE=xxx */

#define VECTORS     xx   /* This value must match NVIC_NUM_VECTORS */

/* Common - Do not change */

#if !defined(MBED_APP_START)
  #define MBED_APP_START  MBED_ROM_START
#endif

#if !defined(MBED_APP_SIZE)
  #define MBED_APP_SIZE  MBED_ROM_SIZE
#endif

#if !defined(MBED_BOOT_STACK_SIZE)
/* This value is normally defined by the tools to 0x1000 for bare metal and 0x400 for RTOS */
  #define MBED_BOOT_STACK_SIZE  0x400
#endif

/* Round up VECTORS_SIZE to 8 bytes */
#define VECTORS_SIZE  (((VECTORS * 4) + 7) AND ~7)

LR_IROM1  MBED_APP_START  MBED_APP_SIZE  {

  ER_IROM1  MBED_APP_START  MBED_APP_SIZE  {
    *.o (RESET, +First)
    *(InRoot$$Sections)
    .ANY (+RO)
  }

  RW_IRAM1  (RAM_START + VECTORS_SIZE)  {  ; RW data
    .ANY (+RW +ZI)
  }

  ARM_LIB_HEAP  AlignExpr(+0, 16)  EMPTY  (MBED_RAM_START + MBED_RAM_SIZE - MBED_BOOT_STACK_SIZE - AlignExpr(ImageLimit(RW_IRAM1), 16))  { ; Heap growing up
  }

  ARM_LIB_STACK  (RAM_START + RAM_SIZE)  EMPTY  -MBED_BOOT_STACK_SIZE  { ; Stack region growing down
  }
}
```

IAR linker script template:

```
/* Device specific values */

/* Tools provide -DMBED_ROM_START=xxx -DMBED_ROM_SIZE=xxx -DMBED_RAM_START=xxx -DMBED_RAM_SIZE=xxx */

define symbol VECTORS     = xx; /* This value must match NVIC_NUM_VECTORS */
define symbol HEAP_SIZE   = 0x10000;

/* Common - Do not change */

if (!isdefinedsymbol(MBED_APP_START)) {
    define symbol MBED_APP_START = MBED_ROM_START;
}

if (!isdefinedsymbol(MBED_APP_SIZE)) {
    define symbol MBED_APP_SIZE = MBED_ROM_SIZE;
}

if (!isdefinedsymbol(MBED_BOOT_STACK_SIZE)) {
    /* This value is normally defined by the tools 
        to 0x1000 for bare metal and 0x400 for RTOS */
    define symbol MBED_BOOT_STACK_SIZE = 0x400;
}

/* Round up VECTORS_SIZE to 8 bytes */
define symbol VECTORS_SIZE = ((VECTORS * 4) + 7) & ~7;
define symbol RAM_REGION_START = MBED_RAM_START + VECTORS_SIZE;
define symbol RAM_REGION_SIZE = MBED_RAM_SIZE - VECTORS_SIZE;

define memory mem with size = 4G;
define region ROM_region = mem:[from MBED_APP_START size MBED_APP_SIZE];
define region RAM_region = mem:[from RAM_REGION_START size RAM_REGION_SIZE];

define block CSTACK    with alignment = 8, size = MBED_BOOT_STACK_SIZE   { };
define block HEAP      with alignment = 8, size = HEAP_SIZE     { };

initialize by copy { readwrite };
do not initialize  { section .noinit };

place at address mem: MBED_APP_START { readonly section .intvec };

place in ROM_region   { readonly };
place in RAM_region   { readwrite,
                        block CSTACK, block HEAP };

```

GCC linker script template:

```
/* Device specific values */

/* Tools provide -DMBED_ROM_START=xxx -DMBED_ROM_SIZE=xxx -DMBED_RAM_START=xxx -DMBED_RAM_SIZE=xxx */

#define VECTORS     xx   /* This value must match NVIC_NUM_VECTORS */

/* Common - Do not change */

#if !defined(MBED_APP_START)
  #define MBED_APP_START  MBED_ROM_START
#endif

#if !defined(MBED_APP_SIZE)
  #define MBED_APP_SIZE  MBED_ROM_SIZE
#endif

#if !defined(MBED_BOOT_STACK_SIZE)
    /* This value is normally defined by the tools 
       to 0x1000 for bare metal and 0x400 for RTOS */
    #define MBED_BOOT_STACK_SIZE 0x400
#endif

/* Round up VECTORS_SIZE to 8 bytes */
#define VECTORS_SIZE (((VECTORS * 4) + 7) & 0xFFFFFFF8)

MEMORY
{
    FLASH (rx)   : ORIGIN = MBED_APP_START, LENGTH = MBED_APP_SIZE
    RAM (rwx)    : ORIGIN = MBED_RAM_START + VECTORS_SIZE, LENGTH = MBED_RAM_SIZE - VECTORS_SIZE
}

/* Linker script to place sections and symbol values. Should be used together
 * with other linker script that defines memory regions FLASH and RAM.
 * It references following symbols, which must be defined in code:
 *   Reset_Handler : Entry of reset handler
 *
 * It defines following symbols, which code can use without definition:
 *   __exidx_start
 *   __exidx_end
 *   __etext
 *   __data_start__
 *   __preinit_array_start
 *   __preinit_array_end
 *   __init_array_start
 *   __init_array_end
 *   __fini_array_start
 *   __fini_array_end
 *   __data_end__
 *   __bss_start__
 *   __bss_end__
 *   __end__
 *   end
 *   __HeapLimit
 *   __StackLimit
 *   __StackTop
 *   __stack
 */
ENTRY(Reset_Handler)

SECTIONS
{
    .text :
    {
        KEEP(*(.isr_vector))
        *(.text*)

        KEEP(*(.init))
        KEEP(*(.fini))

        /* .ctors */
        *crtbegin.o(.ctors)
        *crtbegin?.o(.ctors)
        *(EXCLUDE_FILE(*crtend?.o *crtend.o) .ctors)
        *(SORT(.ctors.*))
        *(.ctors)

        /* .dtors */
         *crtbegin.o(.dtors)
         *crtbegin?.o(.dtors)
         *(EXCLUDE_FILE(*crtend?.o *crtend.o) .dtors)
         *(SORT(.dtors.*))
         *(.dtors)

        *(.rodata*)

        KEEP(*(.eh_frame*))
    } > FLASH

    .ARM.extab :
    {
        *(.ARM.extab* .gnu.linkonce.armextab.*)
    } > FLASH

    __exidx_start = .;
    .ARM.exidx :
    {
        *(.ARM.exidx* .gnu.linkonce.armexidx.*)
    } > FLASH
    __exidx_end = .;

    /* Location counter can end up 2byte aligned with narrow Thumb code but
       __etext is assumed by startup code to be the LMA of a section in RAM
       which must be 8-byte aligned */
    __etext = ALIGN (8);

    .data : AT (__etext)
    {
        __data_start__ = .;
        *(vtable)
        *(.data*)

        . = ALIGN(8);
        /* preinit data */
        PROVIDE_HIDDEN (__preinit_array_start = .);
        KEEP(*(.preinit_array))
        PROVIDE_HIDDEN (__preinit_array_end = .);

        . = ALIGN(8);
        /* init data */
        PROVIDE_HIDDEN (__init_array_start = .);
        KEEP(*(SORT(.init_array.*)))
        KEEP(*(.init_array))
        PROVIDE_HIDDEN (__init_array_end = .);

        . = ALIGN(8);
        /* finit data */
        PROVIDE_HIDDEN (__fini_array_start = .);
        KEEP(*(SORT(.fini_array.*)))
        KEEP(*(.fini_array))
        PROVIDE_HIDDEN (__fini_array_end = .);

        KEEP(*(.jcr*))
        . = ALIGN(8);
        /* All data end */
        __data_end__ = .;

    } > RAM

    /* Uninitialized data section
     * This region is not initialized by the C/C++ library and can be used to
     * store state across soft reboots. */
    .uninitialized (NOLOAD):
    {
        . = ALIGN(32);
        __uninitialized_start = .;
        *(.uninitialized)
        KEEP(*(.keep.uninitialized))
        . = ALIGN(32);
        __uninitialized_end = .;
    } > RAM
    
    .bss :
    {
        . = ALIGN(8);
        __bss_start__ = .;
        *(.bss*)
        *(COMMON)
        . = ALIGN(8);
        __bss_end__ = .;
    } > RAM

    .heap (COPY):
    {
        __end__ = .;
        PROVIDE(end = .);
        *(.heap*)
        . = ORIGIN(RAM) + LENGTH(RAM) - MBED_BOOT_STACK_SIZE;
        __HeapLimit = .;
    } > RAM

    /* .stack_dummy section doesn't contains any symbols. It is only
     * used for linker to calculate size of stack sections, and assign
     * values to stack symbols later */
    .stack_dummy (COPY):
    {
        *(.stack*)
    } > RAM

    /* Set stack top to end of RAM, and stack limit move down by
     * size of stack_dummy section */
    __StackTop = ORIGIN(RAM) + LENGTH(RAM);
    __StackLimit = __StackTop - MBED_BOOT_STACK_SIZE;
    PROVIDE(__stack = __StackTop);

    /* Check if data + heap + stack exceeds RAM limit */
    ASSERT(__StackLimit >= __HeapLimit, "region RAM overflowed with stack")
}
```

### Other required files

- Make sure your CMSIS-Core implementation contains the [`device.h` header](http://www.keil.com/pack/doc/CMSIS/Core/html/device_h_pg.html).
- Extend CMSIS-Core by adding the file `mbed-os\targets\TARGET_VENDOR\TARGET_MCUNAME\cmsis.h`. This header file includes device-specific headers that include CMSIS-Core. It must also include `cmsic_nvic.h`.
- Add the `mbed-os\targets\TARGET_VENDOR\TARGET_MCUNAME\cmsis_nvic.h` header file. This contains the define `NVIC_NUM_VECTORS`, which is the number of vectors the devices has, and `NVIC_RAM_VECTOR_ADDRESS`, which is the address of the RAM vector table. Mbed OS relocates the vectors from the initial location in ROM to the provided address in RAM and updates the `VTOR` register. NOTE: For devices without the `VTOR` register, you need to make sure the vectors are in the read-write memory before execution reaches the `main` function. In this case, you may also need to provide visualization of NVIC access functions. For details, please see the [CMSIS NVIC documentation](https://www.keil.com/pack/doc/CMSIS/Core/html/group__NVIC__gr.html).
- Define the initial stack pointer, `INITIAL_SP`, in `mbed_rtx.h`. This file is typically in `mbed-os\targets\TARGET_VENDOR\mbed_rtx.h`.

# Entry points

Except the reset vector, which is the standard entry point for Cortex-M cores, Mbed OS provides `mbed_sdk_init`, which the target can overload to perform higher level initialization. Mbed OS internals call this function later in the bootstrap process, after the basic initialization is done but before RTOS starts and before the `main` function is called.

Mbed OS provides another entry point that will be executed before `main` called `mbed_main`. This function is reserved for application use, and the target code should not define it.
