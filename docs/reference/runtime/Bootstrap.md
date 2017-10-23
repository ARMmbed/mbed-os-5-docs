## Bootstrap

### Entry points

Mbed OS provides two entry points for developers to hook into:

- `main(void)` - Default entry point. All the standard application code should go here.
- `mbed_main(void)` - Executed directly before `main`. The user can define this.

### Retargeting

Mbed OS redefines multiple standard C library functions to enable them to work in a predictable and familiar way on a remote embedded target device:

- `stdin`, `stdout`, `stderr` - These file descriptors are pointing to the serial interface to enable users to use standard input/output functions, such as `printf` or `getc`.
- `fopen`, `fclose`, `fwrite`, `fread`, `fseek` and other standard file operations - Enable the user to work with the serial interface, as well as the built-in file system.
- `opendir`, `readdir`, `closedir` and other standard directory operations - Enable users to use built in file system.
- `exit` - It causes the board to stop current execution, flush the standard file handles, close the semihosting connection and enter an infinite loop. If the return code indicates an error, the board blinks error patterns on the built-in LED.
- `clock` - Overloaded to use platform's microsecond ticker.
