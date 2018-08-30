<h2 id="configuration-storage">Storage</h2>

This page describes the build-time configurable parameters for storage in Mbed OS. There are no standard shared configuration options for different storage module. Instead, each module has its own implementation-specific set of configuration options.

- [LittleFS configuration](#littlefs-configuration).
- [NVStore configuration](#nvstore-configuration).
- [Default BlockDevice configuration](#Default-BlockDevice-configuration).
- [Default FileSystem configuration](#Default-FileSystem-configuration).

The following is the complete list of storage configuration parameters and how to use and override default implementation if needed.
For more details regarding configuration parameters please refer [the configuration system documentation](configuration.md).

### LittleFS configuration

LittleFS provides several configuration options that you can use to tweak the performance of the file system on different hardware. By default, this file system finds the optimal configuration from the underlying block device's geometry, but you can override this to optimize special situations. For example, if your device has a large amount of RAM, you can increase the `read_size` and `prog_size` configuration options for a minor speed improvement.

Note that LittleFS has 4 levels of debug logging. By default, all logging is enabled except for `enable_debug`. Setting `enable_debug` to `true` makes the log output very verbose, and the output is useful for bug reports.

```
Configuration parameters
------------------------

Name: littlefs.block_size
    Description: Size of an erasable block. This does not impact ram consumption and may be larger than the physical erase size. However, this should be kept small as each file currently takes up an entire block.
    Defined by: library:littlefs
    Macro name: MBED_LFS_BLOCK_SIZE
    Value: 512 (set by library:littlefs)
Name: littlefs.prog_size
    Description: Minimum size of a block program. This determines the size of program buffers. This may be larger than the physical program size to improve performance by caching more of the block device.
    Defined by: library:littlefs
    Macro name: MBED_LFS_PROG_SIZE
    Value: 64 (set by library:littlefs)
Name: littlefs.read_size
    Description: Minimum size of a block read. This determines the size of read buffers. This may be larger than the physical read size to improve performance by caching more of the block device.
    Defined by: library:littlefs
    Macro name: MBED_LFS_READ_SIZE
    Value: 64 (set by library:littlefs)
Name: littlefs.lookahead
    Description: Number of blocks to lookahead during block allocation. A larger lookahead reduces the number of passes required to allocate a block. The lookahead buffer requires only 1 bit per block so it can be quite large with little ram impact. Should be a multiple of 32.
    Defined by: library:littlefs
    Macro name: MBED_LFS_LOOKAHEAD
    Value: 512 (set by library:littlefs)
Name: littlefs.intrinsics
    Description: Enable intrinsics for bit operations such as ctz, popc, and le32 conversion. Can be disabled to help debug toolchain issues
    Defined by: library:littlefs
    Macro name: MBED_LFS_INTRINSICS
    Value: 1 (set by library:littlefs)
Name: littlefs.enable_assert
    Description: Enables asserts, true = enabled, false = disabled, null = disabled only in release builds
    Defined by: library:littlefs
    No value set
Name: littlefs.enable_debug
    Description: Enables debug logging, true = enabled, false = disabled, null = disabled only in release builds
    Defined by: library:littlefs
    No value set
Name: littlefs.enable_error
    Description: Enables error logging, true = enabled, false = disabled, null = disabled only in release builds
    Defined by: library:littlefs
    No value set
Name: littlefs.enable_info
    Description: Enables info logging, true = enabled, false = disabled, null = disabled only in release builds
    Defined by: library:littlefs
    No value set
Name: littlefs.enable_warn
    Description: Enables warn logging, true = enabled, false = disabled, null = disabled only in release builds
    Defined by: library:littlefs
    No value set
```

### NVStore configuration

NVStore does not need much configuration. It relies only on the regions of internal flash specified in the `area_*_address` and `area_*_size` for the two areas. Additionally, you can use `max_keys` to manage the amount of RAM NVStore keys needs. Note that `max_keys` defaults to the number of keys Mbed OS needs. You only need to modify it if an application uses NVStore directly.

```
Configuration parameters
------------------------

Name: nvstore.area_1_address
    Description: Area 1 address
    Defined by: library:nvstore
    No value set
Name: nvstore.area_1_size
    Description: Area 1 size
    Defined by: library:nvstore
    No value set
Name: nvstore.area_2_address
    Description: Area 2 address
    Defined by: library:nvstore
    No value set
Name: nvstore.area_2_size
    Description: Area 2 size
    Defined by: library:nvstore
    No value set
Name: nvstore.max_keys
    Description: Maximal number of allowed NVStore keys
    Defined by: library:nvstore
    Macro name: NVSTORE_MAX_KEYS
    Value: 16 (set by library:nvstore)
```

### BlockDevice - default configuration
Mbed-os configuration allows you to add block devices as components using the targets json file or target overrides in application config file.

When one of the following components is enabled a default block device will be set in the system.

    1. SPIF component.
    2. DATAFLASH component.
    3. SD component.

Components can coexist in the system. A device can have SPIF and SD or any combination of block devices enabled but only one default block device.

The list above is in precedence order and show which block device will be the default one if more than one component will be enabled.

#### configuring component:
Adding "components": ["???"] in targets.json:
```
    "K64F": {
        "supported_form_factors": ["ARDUINO"],
        "components": ["SD"],
        "core": "Cortex-M4F",
        "supported_toolchains": ["ARM", "GCC_ARM", "IAR"],
        "extra_labels": ["Freescale", "MCUXpresso_MCUS", "KSDK2_MCUS", "FRDM", "KPSDK_MCUS", "KPSDK_CODE", "MCU_K64F", "Freescale_EMAC"],
        "is_disk_virtual": true,
        "macros": ["CPU_MK64FN1M0VMD12", "FSL_RTOS_MBED"],
        "inherits": ["Target"],
        "detect_code": ["0240"],
        "device_has": ["USTICKER", "LPTICKER", "RTC", "CRC", "ANALOGIN", "ANALOGOUT", "EMAC", "I2C", "I2CSLAVE", "INTERRUPTIN", "PORTIN", "PORTINOUT", "PORTOUT", "PWMOUT", "SERIAL", "SERIAL_FC", "SERIAL_ASYNCH", "SLEEP", "SPI", "SPI_ASYNCH", "SPISLAVE", "STDIO_MESSAGES", "STORAGE", "TRNG", "FLASH"],
        "features": ["STORAGE"],
        "release_versions": ["2", "5"],
        "device_name": "MK64FN1M0xxx12",
        "bootloader_supported": true,
        "overrides": {
            "network-default-interface-type": "ETHERNET"
        }
    },
```
Adding "target.components_add": ["???"] in application config file:
```     
       "MTB_ADV_WISE_1570": {
            "target.components_add": ["SPIF"],
            "target.features_add": ["LWIP"],
            "platform.default-serial-baud-rate": 9600
       }
```

Please note that while a default block device exists an application is not enforced to use it and can create its own one.

#### Overriding default block device implementation 
The get default instance is implemented as [MBED_WEAK](https://github.com/ARMmbed/mbed-os/blob/40058871de290edc758a21ae6d8f2ec1d1b3533d/platform/mbed_toolchain.h#L120) at features/storage/system_storage/SystemStorage.cpp. That means that it can be overridden by implementing the function without MBED_WEAK and change the default block device for a given application.

```
#include "HeapBlockDevice.h"

BlockDevice *BlockDevice::get_default_instance()
{
    static HeapBlockDevice default_bd(32 *1024);
    return &default_bd;
}
```

### FileSystem - default configuration

Mbed-os configuration allows you to add block devices as components using the targets json file or target overrides in application config file.
When a component of SPIF, DATAFLASH or SD are configured then the system will support one default file system.

Please note that while a default file system exists an application is not enforced to use it and can create its own one.

The default file system will be created based on the default block device due to performance considerations.
SPIF and DATAFLASH block devices will support Little file system while SD block device will support FAT file system.

#### Overriding default block device implementation

The get default instance is implemented as MBED_WEAK at features/storage/system_storage/SystemStorage.cpp. That means that it can be overridden by implementing the function without MBED_WEAK and change the default block device for a given application.

The following example will override the get default instance of and will always return a FAT file system regardless of the block device type.

```
#include "FATFileSystem.h"

FileSystem *FileSystem::get_default_instance()
{
    static FATFileSystem default_fs("fs" BlockDevice::get_default_instance());

    return &default_fs;
}

```