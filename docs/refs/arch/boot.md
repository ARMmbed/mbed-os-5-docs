### Boot process

From a reset state, you can expect the following hooks and conditions. You can find more information in [`mbed_boot.c`](https://github.com/ARMmbed/mbed-os/blob/master/rtos/mbed_boot.c).

- `ResetHandler` - vector table entry at start of Flash (main stack pointer).
- `SystemInit` - imported from CMSIS-CORE (main stack pointer).
- RW/ZI initialization (main stack pointer).
- `mbed_sdk_init` - used for HAL initialization (main stack pointer).
- `osKernelInitialize` - starts kernel and scheduler (main stack pointer).
- `pre_main` - C++ static initializers (process stack pointer).
- `mbed_main` - application hook before main (process stack pointer).
- `main` - application entry point (process stack pointer).
