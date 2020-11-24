# CMake target porting

## Add CMakeLists.txt

Add `CMakeLists.txt` to folders where target's files are located. Please follow logical directory structure (do not create more `CMakeLists.txt` than are required). If there is 3rd party driver, it should have own `CMakeLists.txt`.

The directory tree could look like:

```
/targets/new_target/CMakeLists.txt
/targets/new_target/drivers/CMakeLists.txt
```

## Add your sources and includes

New directory is added using  `add_subdirectory`. You can use conditional inclusion based on
`MBED_TARGET_LABELS` or `MBED_TOOLCHAIN` or similar available CMake variables.

```
# add sdk_driver only for specific target
if("NEW_TARGET" IN_LIST MBED_TARGET_LABELS)
    add_subdirectory(sdk_driver)
endif()

add_subdirectory(driver_always_added)
```

Sources are added using `target_sources` where all code files must be added for `mbed-core` library.

```
target_sources(mbed-core
    INTERFACE
        analogin_api.c
        pinmap.c
        port_api.c
        pwmout_api.c
        reset_reason.c
        rtc_api.c
        serial_api.c
        sleep.c
        spi_api.c
        us_ticker.c
        watchdog_api.c
)
```

Include paths are added using `target_include_directories`.

```
target_include_directories(mbed-core
    INTERFACE
        .
        device
        driver/sdk
)
```

### Linker script file

Each target must set global property `MBED_TARGET_LINKER_FILE`. The path must be prefixed with
`${CMAKE_CURRENT_SOURCE_DIR}`.

``` 
if(${MBED_TOOLCHAIN} STREQUAL "GCC_ARM")
    set(LINKER_FILE device/TOOLCHAIN_GCC_ARM/NEW_TARGET.ld)
elseif(${MBED_TOOLCHAIN} STREQUAL "ARM")
    set(LINKER_FILE device/TOOLCHAIN_ARM_STD/NEW_TARGET.sct)
endif()

set_property(GLOBAL PROPERTY MBED_TARGET_LINKER_FILE ${CMAKE_CURRENT_SOURCE_DIR}/${LINKER_FILE})
```

### Adding pre-compiled target libraries

Pre-compiled libraries are added using `target_link_libraries`. The path must be prefixed with
`${CMAKE_CURRENT_SOURCE_DIR}`.

```
target_link_libraries(mbed-core
    INTERFACE
        ${CMAKE_CURRENT_SOURCE_DIR}/pre_compiled_driver
)
```
