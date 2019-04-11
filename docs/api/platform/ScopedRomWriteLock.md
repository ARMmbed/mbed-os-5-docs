# ScopedRomWriteLock

The `ScopedRomWriteLock` class provides an RAII object for enabling writing to ROM. In other words, creating a ScopedRomWriteLock object calls its constructor, which increments the ROM write lock. The ScopedRomWriteLock object automatically releases the ROM write lock in its destructor when the object goes out of scope. Another way to look at this is when the ScopedRomWriteLock object exists, it allows writing to ROM.

## ScopedRomWriteLock class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_scoped_rom_write_lock.html)

## Example

This example shows how you can enable writes to ROM from main.

```C++ NOCI
#include "mbed.h"

int main()
{
    // Enable execution from RAM while in main
    ScopedRomWriteLock make_rom_writable;

    custom_flash_programming();
}
```

## Related content

- [MPU Management API references](mpu-management.html).
