## Terms

[A document that briefly explains the differences between mbed, mbed-rtos, mbed-dev, mbed-src and mbed-rpc]


[TODO: This will need a massive edit, and additional info]


[TODO]: All below is not getting started. Maybe for porting but not handbook

### Bootstrap Process

From a reset state the following hooks and conditions are expected.

* `ResetHandler` - vector table entry at start of Flash (main stack pointer).
* `SystemInit` - imported from CMSIS-CORE (main stack pointer).
* RW/ZI initialization (main stack pointer).
* `mbed_sdk_init` - used for HAL initialization (main stack pointer).
* `osKernelInitialize` - starts kernel and scheduler (main stack pointer).
* `pre_main` - C++ static initializers (process stack pointer).
* `mbed_main` - application hook before main (process stack pointer).
* `main` - application entry point (process stack pointer).

