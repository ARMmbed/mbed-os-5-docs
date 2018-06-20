## Bootstrap

### Entry points

Mbed OS provides two entry points for developers to hook into:

- `main(void)` - Default entry point. All the standard application code goes here.
- `mbed_main(void)` - Executed directly before `main`. The user can define this.

When execution reaches the entry points, a user can expect a fully initialized system that is ready to execute application code. For this to happen, the following must have occurred prior to this point:

- Low-level platform initialization.
- Stack and heap initialization.
- Vector table copied to RAM.
- Standard library initialized.
- RTOS initialized and scheduler started.

### Retargeting

Mbed OS redefines multiple standard C library functions to enable them to work in a predictable and familiar way on a remote embedded target device:

- `stdin`, `stdout`, `stderr` - These file descriptors are pointing to the serial interface to enable users to use standard input/output functions, such as `printf` or `getc`.
- `fopen`, `fclose`, `fwrite`, `fread`, `fseek` and other standard file operations - Enable the user to work with the serial interface, as well as the built-in file system.
- `opendir`, `readdir`, `closedir` and other standard directory operations - Enable users to use built in file system.
- `exit` - It causes the board to stop current execution, flush the standard file handles, close the semihosting connection and enter an infinite loop. If the return code indicates an error, the board blinks error patterns on the built-in LED.
- `clock` - Overloaded to use platform's microsecond ticker.

### Process

From a reset state the following hooks and conditions are expected:

- `ResetHandler` - vector table entry at start of Flash main stack pointer.
- `SystemInit` - imported from CMSIS-CORE main stack pointer.
- RW/ZI initialization main stack pointer.
- `mbed_sdk_init` - used for HAL initialization main stack pointer.
- `osKernelInitialize` - starts kernel and scheduler main stack pointer.
- `pre_main` - C++ static initializers process stack pointer.
- `mbed_main` - application hook before main process stack pointer.
- `main` - application entry point process stack pointer.
