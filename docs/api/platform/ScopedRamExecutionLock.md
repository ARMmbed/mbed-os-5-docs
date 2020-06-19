# ScopedRamExecutionLock

<span class="images">![](https://os.mbed.com/docs/mbed-os/v6.1/mbed-os-api-doxy/classmbed_1_1_scoped_ram_execution_lock.png)<span>ScopedRamExecutionLock class hierarchy</span></span>

The `ScopedRamExecutionLock` class provides an RAII object for enabling execution from RAM. In other words, creating a ScopedRamExecutionLock object calls its constructor, which increments the RAM execution lock. The ScopedRamExecutionLock object automatically releases the RAM execution lock in its destructor when the object goes out of scope. Another way to look at this is when the ScopedRamExecutionLock object exists, it allows execution from RAM.

## ScopedRamExecutionLock class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/v6.1/mbed-os-api-doxy/classmbed_1_1_scoped_ram_execution_lock.html)

## Example

This example shows how you can enable execution from RAM from main:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-ScopedRamExecutionLock/tree/v6.1)](https://github.com/ARMmbed/mbed-os-snippet-ScopedRamExecutionLock/blob/v6.1/main.cpp)

## Related content

- [MPU Management API references](mpu-management.html).
