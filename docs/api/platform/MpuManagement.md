# MPU management

Memory protection for Mbed OS is enabled automatically for devices that support the MPU API. The MPU management functions provided here allow libraries and applications to turn off these memory protections if necessary. The memory protection the MPU provides does the following:

- Prevents execution from RAM.
- Prevents writing to ROM.

Mbed OS handles MPU management automatically in the following situations:

- Memory protection is enabled as part of the boot sequence.
- Memory protection is disabled when starting a new application.
- Memory protection is disabled while flash programming.

<span class="notes">**Note:** Memory protection should be transparent to most applications and libraries because Mbed OS handles it automatically for operations that need to disable MPU protections, such as flash programming. This is an advanced feature intended for use by advanced developers; it is not required.</span>

<span class="notes">**Note:** The configuration value `platform.use-mpu` can be set to `false` to remove the MPU driver and save code space.</span>

### RAM execute lock

After boot, execution from RAM is not allowed. Libraries requiring the ability to execute from RAM can enable this by acquiring the RAM execution lock. The RAM execution lock has a count associated with it, and you can lock it multiple times. Execution from RAM is disabled only when all components have unlocked it.

### ROM write lock

After boot, writing to ROM is not allowed. Libraries requiring the ability to writing to ROM can enable this by acquiring the ROM write lock. The ROM write lock has a count associated with it, and you can lock it multiple times. Writing to ROM disablesd only when all components have unlocked it.

<span class="notes">**Note:** When the ROM write lock is held, many devices will still fault if code writes to ROM.</span>

## Function reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/development/mbed-os-api-doxy/group__platform__mpu__mgmt.html)

## Example

```C++ NOCI
#include "mbed.h"

// Permanently enable execute from RAM for this application
ScopedRamExecutionLock make_ram_executable;

int main()
{
    some_function_in_ram();
}
```

## Related content

- [ScopedRamExecutionLock API reference](scopedramexecutionlock.html).
- [ScopedRomWriteLock API reference](scopedromwritelock.html).
