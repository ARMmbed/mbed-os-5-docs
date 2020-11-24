# CMake target porting

You can use conditional inclusion based on
`MBED_TARGET_LABELS` or `MBED_TOOLCHAIN` or similar available CMake variables.

Important variables we provide for targets:

- `MBED_TARGET_LABELS` - Target's labels coming from targets.json
- `MBED_TARGET_DEFINITIONS` - Definitions coming from targets.json
- `MBED_CONFIG_DEFINITIONS` - Config definitions prefixed with `-D`
- `MBED_TARGET_SUPPORTED_C_LIBS` - C libraries supported (small/std)
- `MBED_TARGET_SUPPORTED_APPLICATION_PROFILES` - Application profiles supported (bare-metal/full)

## targets CMakelists structure

### Vendor targets

`targets/CMakeLists.txt` contains vendors selection.

```
if("Cypress" IN_LIST MBED_TARGET_LABELS)
    add_subdirectory(TARGET_Cypress/TARGET_PSOC6)   
endif()
```

### MCU family targets

`targets/TARGET_Cypress/TARGET_PSOC6` contains different MCU families. This is implementation specific folder. It can include 3rd party drivers, components, sub-MCU families.

```
add_subdirectory(common)
add_subdirectory(psoc6pdl)

target_include_directories(mbed-core
    INTERFACE
        .
)

target_sources(mbed-core
    INTERFACE
        analogin_api.cpp
)
```

## Add target's CMakeLists.txt

Add `CMakeLists.txt` to folders where target's files are located. Please follow logical directory structure and do not create more `CMakeLists.txt` than it is required. 
If there is 3rd party driver, it should have own `CMakeLists.txt`.

The directory tree could look like:

```
# This is new vendor's CMakeLists
/targets/new_vendor/CMakeLists.txt
# This is driver's CMakeLists
/targets/new_vendor/driver/CMakeLists.txt
# This is target's CMakeLists
/targets/new_vendor/new_target/CMakeLists.txt

```

### Add your sources and includes

New directory is added using  `add_subdirectory`.

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
