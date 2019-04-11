# ScopedRamExecutionLock

The `ScopedRamExecutionLock` class provides an RAII object for enabling execution from RAM. In other words, creating a ScopedRamExecutionLock object calls its constructor, which increments the RAM execution lock. The ScopedRamExecutionLock object automatically releases the RAM execution lock in its destructor when the object goes out of scope. Another way to look at this is when the ScopedRamExecutionLock object exists, it allows execution from RAM.

## ScopedRamExecutionLock class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_scoped_ram_execution_lock.html)

## Example

This example shows how you can enable execution from RAM from main:

```C++ NOCI
#include "mbed.h"

int main()
{
    // Enable execution from RAM while in main
    ScopedRamExecutionLock make_ram_executable;

    some_function_in_ram();
}
```
## Related content

- [MPU Management API references](mpu-management.html).
