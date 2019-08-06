# Flash

Update target to support bootloader.

1. Update linker script.
1. Add required metadata to `targets.json`.
1. Implement `mbed_start_application`.
1. Implement flash HAL API.
1. Verify changes with tests.

## Linker script updates

When building a bootloader application or an application that uses a bootloader, the Arm Mbed OS build system automatically defines values for the start of application flash, `MBED_APP_START`, and size of application flash, `MBED_APP_SIZE`, when preprocessing the linker script. When updating a target to support this functionality, linker scripts must place all flash data in a location starting at `MBED_APP_START` and must limit the size of that data to `MBED_APP_SIZE`. This change must occur for the linker scripts of all toolchains - GCC Arm (.ld), Arm (.sct) and IAR (.icf). You can find examples of this for the [k64f](https://github.com/ARMmbed/mbed-os/commit/579b2fbe40c40a443dc2aaa6850304eccf1dd87e), [stm32f429](https://github.com/ARMmbed/mbed-os/commit/ca8873b160eb438d18f7b4186f8f84e7578a9959), [odin-w2](https://github.com/ARMmbed/mbed-os/commit/bcab66c26d18d837362ea92afca9f4de1b668070).

Use these 2 defines in place of flash start and size for a target:
- `MBED_APP_START` - defines an address where an application space starts.
- `MBED_APP_SIZE` - the size of the application.

<span class="notes">**Note:** When an application does not use any of the bootloader functionality, then `MBED_APP_START` and `MBED_APP_SIZE` are not defined. For this reason, the linker script must define default values that match flash start and flash size..</span>

An example of how a target could define `MBED_APP_START` and `MBED_APP_SIZE` in the linker script file:

```
#if !defined(MBED_APP_START)
  #define MBED_APP_START 0
#endif

#if !defined(MBED_APP_SIZE)
  #define MBED_APP_SIZE 0x100000
#endif
```

Be careful with these defines because they move the application flash sections. Therefore, you should move any sections within flash sectors accordingly.

<span class="notes">**Note:** The VTOR must be relative to the region in which it is placed. To confirm, search for `NVIC_FLASH_VECTOR_ADDRESS` and `SCB->VTOR`, and ensure the flash address is not hardcoded.</span>

Problematic declaration of flash VTOR address:

```
#define NVIC_RAM_VECTOR_ADDRESS   (0x20000000)
#define NVIC_FLASH_VECTOR_ADDRESS (0x00000000)
```

Bootloader-ready declaration of flash VTOR address:

```
#define NVIC_RAM_VECTOR_ADDRESS   (0x20000000)
#if defined(__ICCARM__)
    #pragma section=".intvec"
    #define NVIC_FLASH_VECTOR_ADDRESS   ((uint32_t)__section_begin(".intvec"))
#elif defined(__CC_ARM)
    extern uint32_t Load$$LR$$LR_IROM1$$Base[];
    #define NVIC_FLASH_VECTOR_ADDRESS   ((uint32_t)Load$$LR$$LR_IROM1$$Base)
#elif defined(__GNUC__)
    extern uint32_t vectors[];
    #define NVIC_FLASH_VECTOR_ADDRESS   ((uint32_t)vectors)
#else
    #error "Flash vector address not set for this toolchain"
#endif
```

## `targets.json` metadata

The managed and unmanaged bootloader builds require some target metadata from CMSIS Packs. Add a `"device_name"` attribute to your target as [Adding and configuring targets](../reference/adding-and-configuring-targets.html) describes.

## Start application

The `mbed_start_application` implementation exists only for Cortex-M3, Cortex-M4 and Cortex-M7. You can find it in [the Arm Mbed_application code file](https://github.com/ARMmbed/mbed-os/blob/master/platform/mbed_application.c). If `mbed_start_application` does not support your target, you must implement this function in the target HAL.

## Flash HAL

For a bootloader to perform updates, you must implement the flash API. This consists of implementing the function in [flash_api.h](https://github.com/ARMmbed/mbed-os/blob/master/hal/flash_api.h) and adding the correct fields to targets.json.

There are two options to implement flash HAL:

### Option 1: CMSIS flash algorithm routines

These are quick to implement. They use CMSIS device packs and scripts to generate binary blobs. Because these flash algorithms do not have well-specified behavior, they might disable cache, reconfigure clocks and other actions you may not expect. Therefore, proper testing is required. First, make sure CMSIS device packs support your device. Run a script in `mbed-os` to generate flash blobs. Check the flash blobs into the target's HAL. Arm provides an [example](https://github.com/ARMmbed/mbed-os/commit/071235415e3f0b6d698df6e944c522bdae8ff4ae) of how to do this.

To enable a CMSIS flash algorithm common layer, a target should define `FLASH_CMSIS_ALGO`. This macro enables the wrapper between CMSIS flash algorithm functions from the flash blobs and flash HAL.

```
"TARGET_NAME": {
    "extra_labels": [FLASH_CMSIS_ALGO]
}
```

The CMSIS algorithm common layer provides a [trampoline](https://github.com/ARMmbed/mbed-os/blob/master/hal/TARGET_FLASH_CMSIS_ALGO/flash_common_algo.c), which uses a flash algorithm blob. It invokes CMSIS FLASH API, which the [CMSIS-Pack Algorithm Functions page](http://arm-software.github.io/CMSIS_5/Pack/html/algorithmFunc.html) defines.

### Option 2: Your own HAL driver

If CMSIS packs do not support a target, you can implement flash HAL by writing your own HAL driver.

Functions to implement:

```
int32_t flash_init(flash_t *obj);
int32_t flash_free(flash_t *obj);
int32_t flash_erase_sector(flash_t *obj, uint32_t address);
int32_t flash_program_page(flash_t *obj, uint32_t address, const uint8_t *data, uint32_t size);
uint32_t flash_get_sector_size(const flash_t *obj, uint32_t address);
uint32_t flash_get_page_size(const flash_t *obj);
uint32_t flash_get_start_address(const flash_t *obj);
uint32_t flash_get_size(const flash_t *obj);
```

To enable flash HAL, define `FLASH` in targets.json file inside `device_has`:

```
"TARGET_NAME": {
   "device_has": ["FLASH"]
}
```

Finally, to indicate that your device fully supports bootloaders, set the field `bootloader_supported` to `true` for the target in the `targets.json` file:

```
"bootloader_supported": true
```

## Tests

The following tests for the `FlashIAP` class and flash HAL are located in the `mbed-os/TESTS` folder.

- Flash IAP unit tests: `tests-mbed_drivers-flashiap`.
- Flash HAL unit tests: `tests-mbed_hal-flash`.

They test all flash API functionality. To run the tests, use these commands:

- Flash IAP: `mbed test -m TARGET_NAME -n tests-mbed_drivers-flashiap`.
- Flash HAL: `mbed test -m TARGET_NAME -n tests-mbed_hal-flash`.

## Troubleshooting

- For targets with VTOR, a target might have a VTOR address defined to a hardcoded address as mentioned in the [Linker script updates](#linker-script-updates) section.

- Using Flash IAP might introduce latency as it might disable interrupts for longer periods of time.

- Program and erase functions might operate on different sized blocks - page size might not equal to a sector size. The function erase erases a sector, the program function programs a page. Use accessor methods to get the values for a sector or a page.

- Sectors might have different sizes within a device.
