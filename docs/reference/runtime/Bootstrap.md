## Bootstrap

### Entry points

Mbed OS provides two entry points for developer to hook into:
* `main(void)` - default entry point, all the standard application code should go here.
* `mbed_main(void)` - executed directly before `main`, can be defined by the user.

### Retargeting

Mbed OS redefines multiple standard C library functions, to enable them to work in predictable and familiar way on a remote embedded target device:
* `stdin`, `stdout`, `stderr` - These file descriptor are pointing to serial interface, to enable users to use standard input/output functions, like printf or getc.
* `fopen`, `fclose`, `fwrite`, `fread`, `fseek` and other standard file operations - enable user to work with serial interface, as well as, built in file system.
* `opendir`, `readdir`, `closedir` and other standard directory operations - enable users to use built in file system.
* `exit` - it causes the board to stop current execution, flush standard file handles, close semi-hosting connection and enter infinite loop. If the return code indicates an error, the board will blink error patterns on built in LED.
* `clock` - overloaded to use platform's microsecond ticker.
