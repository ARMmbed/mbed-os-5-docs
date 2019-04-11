# Bootstrap

## Entry points

Mbed OS provides two entry points you as a developer to hook into:

- `main(void)` - Default entry point. All the standard application code goes here.
- `mbed_main(void)` - Executed directly before `main`. You can define this.

When execution reaches the entry points, you can expect a fully initialized system that is ready to execute application code. The Mbed OS boot sequence consists of four phases: target setup, toolchain setup, starting the RTOS and starting the Mbed application. You can see these phases below:

1. Set up target.
   1. Configure clocks.
   1. Configure watchdog (if applicable).
   1. Turn on RAM (if applicable).
   1. Jump to set up toolchain.
1. Set up toolchain.
   1. Initialize RAM.
   1. Initialize standard library.
   1. Call mbed_init.
      1. Vector table copied to RAM.
      1. Vendor SDK initialized.
      1. Jump to start RTOS.
1. Start RTOS.
     1. Create main thread.
     1. Start scheduler.
     1. Main thread calls start Mbed.
1. Start Mbed.
     1. Call `mbed_main`.
     1. Call `main`.

Sequence diagram of the boot sequence:

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/boot_sequence.png)<span>A diagram of the Arm Mbed OS 5 boot sequence</span></span>

## Retargeting

Mbed OS redefines multiple standard C library functions to enable them to work in a predictable and familiar way on a remote embedded target device:

- `stdin`, `stdout`, `stderr` - These file descriptors are pointing to the serial interface to enable users to use standard input/output functions, such as `printf` or `getc`.
- `fopen`, `fclose`, `fwrite`, `fread`, `fseek` and other standard file operations - Enable the user to work with the serial interface, as well as the built-in file system.
- `opendir`, `readdir`, `closedir` and other standard directory operations - Enable users to use built in file system.
- `exit` - It causes the board to stop current execution, flush the standard file handles, close the semihosting connection and enter an infinite loop. If the return code indicates an error, the board blinks error patterns on the built-in LED.
- `clock` - Overloaded to use platform's microsecond ticker.
