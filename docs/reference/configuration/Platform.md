<h1 id="configuration-platform">Platform</h1>

The platform configurations allow for customization of platform level OS options. These options include error handling properties and serial communication configuration settings for STDIO. They work out of platform because they affect system level `printf` calls, not Serial objects, with the exception of `default-serial-baud-rate`.

This is the complete list of platform configuration parameters. To view all configuration parameters, run the `--config -v` command. Please see [the configuration system documentation](configuration.html) for details on how you may use or override these settings.

```
Configuration parameters
------------------------
Name: platform.all-stats-enabled
    Description: Set to 1 to enable all platform stats. When enabled the functions mbed_stats_*_get returns non-zero data. See mbed_stats.h for more information
    Defined by: library:platform
    No value set
Name: platform.cpu-stats-enabled
    Description: Set to 1 to enable cpu stats. When enabled the function mbed_stats_cpu_get returns non-zero data. See mbed_stats.h for more information
    Defined by: library:platform
    No value set
Name: platform.crash-capture-enabled
    Description: Enables crash context capture when the system enters a fatal error/crash.
    Defined by: library:platform
    Macro name: MBED_CONF_PLATFORM_CRASH_CAPTURE_ENABLED
    Value: 1 (set by library:platform[K64F])
Name: platform.cthunk_count_max
    Description: The maximum CThunk objects used at the same time. This must be greater than 0 and less 256
    Defined by: library:platform
    Macro name: MBED_CONF_PLATFORM_CTHUNK_COUNT_MAX
    Value: 8 (set by library:platform)
Name: platform.default-serial-baud-rate
    Description: Default baud rate for a Serial or RawSerial instance (if not specified in the constructor)
    Defined by: library:platform
    Macro name: MBED_CONF_PLATFORM_DEFAULT_SERIAL_BAUD_RATE
    Value: 9600 (set by library:platform)
Name: platform.error-all-threads-info
    Description: Reports all the threads in the system as part of error report.
    Defined by: library:platform
    No value set
Name: platform.error-filename-capture-enabled
    Description: Enables capture of filename and line number as part of error context capture, this works only for debug and develop builds. On release builds, filename capture is always disabled
    Defined by: library:platform
    No value set
Name: platform.error-hist-enabled
    Description: Enable for error history tracking.
    Defined by: library:platform
    No value set
Name: platform.error-hist-size
    Description: Set the number of most recent errors the system keeps in its history, needs error-hist-enabled set to true for this to work.
    Defined by: library:platform
    Macro name: MBED_CONF_PLATFORM_ERROR_HIST_SIZE
    Value: 4 (set by library:platform)
Name: platform.error-reboot-max
    Description: Maximum number of auto reboots permitted when an error happens.
    Defined by: library:platform
    Macro name: MBED_CONF_PLATFORM_ERROR_REBOOT_MAX
    Value: 1 (set by library:platform)
Name: platform.fatal-error-auto-reboot-enabled
    Description: Setting this to true enables auto-reboot on a fatal error.
    Defined by: library:platform
    Macro name: MBED_CONF_PLATFORM_FATAL_ERROR_AUTO_REBOOT_ENABLED
    Value: 1 (set by library:platform[K64F])
Name: platform.force-non-copyable-error
    Description: Force compile time error when a NonCopyable object is copied
    Defined by: library:platform
    No value set
Name: platform.heap-stats-enabled
    Description: Set to 1 to enable heap stats. When enabled the function mbed_stats_heap_get returns non-zero data. See mbed_stats.h for more information
    Defined by: library:platform
    No value set
Name: platform.max-error-filename-len
    Description: Sets the maximum length of buffer used for capturing the filename in error context. This needs error-filename-capture-enabled feature.
    Defined by: library:platform
    Macro name: MBED_CONF_PLATFORM_MAX_ERROR_FILENAME_LEN
    Value: 16 (set by library:platform)
Name: platform.memory-tracing-enabled
    Description: Enable tracing of each memory call by invoking a callback on each memory operation. See mbed_mem_trace.h in the HAL API for more information
    Defined by: library:platform
    No value set
Name: platform.poll-use-lowpower-timer
    Description: Enable use of low power timer class for poll(). May cause missing events.
    Defined by: library:platform
    No value set
Name: platform.stack-stats-enabled
    Description: Set to 1 to enable stack stats. When enabled the functions mbed_stats_stack_get and mbed_stats_stack_get_each return non-zero data. See mbed_stats.h for more information
    Defined by: library:platform
    No value set
Name: platform.stdio-baud-rate
    Description: Baud rate for stdio
    Defined by: library:platform
    Macro name: MBED_CONF_PLATFORM_STDIO_BAUD_RATE
    Value: 9600 (set by library:platform)
Name: platform.stdio-buffered-serial
    Description: Use UARTSerial driver to obtain buffered serial I/O on stdin/stdout/stderr. If false, unbuffered serial_getc and serial_putc are used directly.
    Defined by: library:platform
    No value set
Name: platform.stdio-convert-newlines
    Description: Enable conversion to standard newlines on stdin/stdout/stderr
    Defined by: library:platform
    No value set
Name: platform.stdio-convert-tty-newlines
    Description: Enable conversion to standard newlines on any tty FILE stream
    Defined by: library:platform
    No value set
Name: platform.stdio-flush-at-exit
    Description: Enable or disable the flush of standard I/O's at exit.
    Defined by: library:platform
    Macro name: MBED_CONF_PLATFORM_STDIO_FLUSH_AT_EXIT
    Value: 1 (set by library:platform)
Name: platform.sys-stats-enabled
    Description: Set to 1 to enable system stats. When enabled the function mbed_stats_sys_get returns non-zero data. See mbed_stats.h for more information
    Defined by: library:platform
    No value set
Name: platform.thread-stats-enabled
    Description: Set to 1 to enable thread stats. When enabled the function mbed_stats_thread_get_each returns non-zero data. See mbed_stats.h for more information
    Defined by: library:platform
    No value set
Name: platform.use-mpu
    Description: Use the MPU if available to fault execution from RAM and writes to ROM. Can be disabled to reduce image size.
    Defined by: library:platform
    Macro name: MBED_CONF_PLATFORM_USE_MPU
    Value: 1 (set by library:platform)
```
