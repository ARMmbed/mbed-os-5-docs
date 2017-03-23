# FLASH IAP porting guide

Update target to support bootloader.
   1. Update linker script
   1. Implement flash HAL API
   1. Verify changes with tests

## Linker script updates

When building a bootloader application or an application that uses a bootloader, the mbed OS build system automatically defines values for the start of application flash, `MBED_APP_START`, and size of application flash, `MBED_APP_SIZE`, when preprocessing the linker script. When updating a target to support this functionality, linker scripts must place all flash data in a location starting at `MBED_APP_START` and must limit the size of that data to `MBED_APP_SIZE`. This change must occur for the linker scripts of all toolchains - GCC_ARM (.ld), ARM (.sct) and IAR (.icf). You can find examples of this for the [k64f](https://github.com/ARMmbed/mbed-os/commit/579b2fbe40c40a443dc2aaa6850304eccf1dd87e), [stm32f429](https://github.com/ARMmbed/mbed-os/commit/ca8873b160eb438d18f7b4186f8f84e7578a9959), [odin-w2](https://github.com/ARMmbed/mbed-os/commit/bcab66c26d18d837362ea92afca9f4de1b668070).

Use these 2 defines in place of flash start and size for a target:
* `MBED_APP_START` - defines an address where an application space starts.
* `MBED_APP_SIZE` - the size of the application.

Note: When an application does not use any of the bootloader functionality, then `MBED_APP_START` and `MBED_APP_SIZE` are not defined. For this reason, the linker script must define default values that match flash start and flash size.

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

Note: The VTOR must be relative to the region in which it is placed. To confirm, search for `NVIC_FLASH_VECTOR_ADDRESS` and `SCB->VTOR`, and ensure the flash address is not hardcoded.

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

## Flash HAL

For a bootloader to perform updates, you must implement the flash API. This consists of implementing the function in [flash_api.h](https://github.com/ARMmbed/mbed-os/blob/master/hal/flash_api.h) and adding the correct fields to targets.json.

There are two options to implement flash HAL:

1. CMSIS flash algorithm routines.

These are quick to implement. They use CMSIS device packs and scripts to generate binary blobs. Because these flash algorithms do not have well-specified behavior, they might disable cache, reconfigure clocks and other actions you may not expect. Therefore, proper testing is required. First, make sure CMSIS device packs support your device. Run a script in mbed-os to generate flash blobs. Check the flash blobs into the target's HAL. See an example of how to do this [here](https://github.com/ARMmbed/mbed-os/commit/071235415e3f0b6d698df6e944c522bdae8ff4ae).

To enable a CMSIS flash algorithm common layer, a target should define ``FLASH_CMSIS_ALGO``. This macro enables the wrapper between CMSIS flash algorithm functions from the flash blobs and flash HAL.

    ```
    "TARGET_NAME": {
        "extra_labels": [FLASH_CMSIS_ALGO]
    }
    ```

The CMSIS algorithm common layer provides a [trampoline](https://github.com/ARMmbed/mbed-os/blob/master/hal/TARGET_FLASH_CMSIS_ALGO/flash_common_algo.c), which uses a flash algorithm blob. It invokes CMSIS FLASH API, which is defined [here](http://arm-software.github.io/CMSIS_5/Pack/html/algorithmFunc.html).

2. Your own HAL driver

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

The following tests for the `FlashIAP` class and flash HAL are located in the ``mbed-os/TESTS`` folder.

- FlashIAP unit tests: `tests-mbed_drivers-flashiap`.
- Flash HAL unit tests: `tests-mbed_hal-flash`.

They test all flash API functionality. To run the tests, use these commands:

- FlashIAP: `mbed test -m TARGET_NAME -n tests-mbed_drivers-flashiap`.
- Flash HAL: `mbed test -m TARGET_NAME -n tests-mbed_hal-flash`.
