# FLASH IAP porting guide

Flash IAP set-by-step list:

1. Update target to support bootloader
    * Update linker script
    * Implement flash HAL API
    * Add pack support to mbed-os
    * Verify changes with tests

## Linker script updates

When building a bootloader application or an application which uses a bootloader the mbed-os build system automatically defines values for the start of application flash, MBED_APP_START, and size of application flash, MBED_APP_SIZE, when pre-processing the linker script. When updating a target to support this functionality linker scripts must place all flash data in a location starting at MBED_APP_START and must limit the size of that data to MBED_APP_SIZE. This change must be made for the linker scripts of all toolchains - GCC_ARM (.ld), ARM (.sct) and IAR (.icf). Examples of this can be found for the [k64f](https://github.com/ARMmbed/mbed-os/commit/579b2fbe40c40a443dc2aaa6850304eccf1dd87e), [stm32f429](https://github.com/ARMmbed/mbed-os/commit/ca8873b160eb438d18f7b4186f8f84e7578a9959), [odin-w2](https://github.com/ARMmbed/mbed-os/commit/bcab66c26d18d837362ea92afca9f4de1b668070).

These 2 defines should be used in place of flash start and size for a target:

``MBED_APP_START`` - defines an address where an application space starts.

``MBED_APP_SIZE`` - the size of the application

Note - when none of the bootloader functionality is used by an application then MBED_APP_START and MBED_APP_SIZE are not defined. For this reason linker script must define default values which match flash start and flash size.

An example how a target could define it in the linker script file:

```
#if !defined(MBED_APP_START)
  #define MBED_APP_START 0
#endif

#if !defined(MBED_APP_SIZE)
  #define MBED_APP_SIZE 0x100000
#endif

```

Be careful with these defines, they move the application flash sections, thus any sections within flash sectors should be moved accordingly. For instance data section should start >= MBED_APP_SIZE.

Because of mbed application start changes, we should verify VTOR's address. VTOR address should be updated to reflect the application padding, not to be hard-coded to a specific address.

## Flash HAL

For a bootloader to perform updates the Flash API must be implemented. This consists of implementing the function in [flash_api.h](https://github.com/ARMmbed/mbed-os/blob/master/hal/flash_api.h) and adding the correct fields to targets.json.

There are two options how to implement flash HAL:

1. CMSIS flash algorithm routines - quick to implement (use CMSIS device packs and scripts to generate binary blobs). As these algos do not have well specified behavior, they might do things like disabling cache, reconfigure clocks or any other actions you might not expect. Therefore a proper testing is required. First, make sure your device is supported by CMSIS device packs. Run a script in the mbedmicro/FlashAlgo to generate flash blob that should be checked in into targets HAL.
To enable CMSIS flash algo common layer, a target should define ``FLASH_CMSIS_ALGO``. This macro enables the wrapper between CMSIS flash algo functions from the flash blobs and flash HAL.

    ```
    "TARGET_NAME": {
        "extra_labels": [FLASH_CMSIS_ALGO]
    }
    ```

    The CMSIS algo common layer provides a [trampoline](https://github.com/ARMmbed/mbed-os/blob/master/hal/TARGET_FLASH_CMSIS_ALGO/flash_common_algo.c) which uses a flash algo blob. It invokes CMSIS FLASH API that is defined [here](http://arm-software.github.io/CMSIS_5/Pack/html/algorithmFunc.html).

2. Own HAL driver

    If a target is not supported in CMSIS packs, you can implement flash HAL by writing own HAL driver.

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

To enable flash HAL, define ``FLASH`` in targets.json file inside ``device_has``:
```
"TARGET_NAME": {
    "device_has": ["FLASH"]
}
```

Finally, to indicate that your device fully supports bootloaders the field ``bootloader_supported`` should be set to ``true`` for your target in the ``targets.json`` file:
```
"bootloader_supported": true
```

### Tests

The tests are implemented for FlashIAP class and flash HAL own tests. They are located in ``mbed-os/TESTS`` folder.

- FlashIAP unit tests - tests-mbed_drivers-flashiap
- Flash HAL unit tests - tests-mbed_hal-flash

They test all flash API functionality. The commands to run the tests:

- FlashIAP: ``mbed test -m TARGET_NAME -n tests-mbed_drivers-flashiap``
- Flash HAL: ``mbed test -m TARGET_NAME -n tests-mbed_hal-flash``
