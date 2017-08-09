## Memory Optimization

Beginning with Mbed OS 5, new features such as RTOS created an increase in flash and RAM usage. This guide explains how to optimize program memory usage for release builds using Mbed OS 5.

**Note:** More information about the memory usage differences between Mbed OS 2 and Mbed OS 5 is available [here](https://developer.mbed.org/blog/entry/Optimizing-memory-usage-in-mbed-OS-52/).

### Removing Unused Modules

For a simple program like [Blinky](https://github.com/ARMmbed/mbed-os-example-blinky), a program that flashes an LED, typical memory usage is split between the following modules: 

```
+---------------------+-------+-------+-------+
| Module              | .text | .data |  .bss |
+---------------------+-------+-------+-------+
| Fill                |   132 |     4 |  2377 |
| Misc                | 28807 |  2216 |    88 |
| features/frameworks |  4236 |    52 |   744 |
| hal/common          |  2745 |     4 |   325 |
| hal/targets         | 12172 |    12 |   200 |
| rtos/rtos           |   119 |     4 |     0 |
| rtos/rtx            |  5721 |    20 |  6786 |
| Subtotals           | 53932 |  2312 | 10520 |
+---------------------+-------+-------+-------+
```

Even though we are creating a release build, the `features/frameworks` module includes the Mbed OS test tools. Because of this, we are building one of our test harnesses into every binary. Since we do not need a testing framework for a release build, [removing this module](https://github.com/ARMmbed/mbed-os/pull/2559) will save a significant amount of RAM and flash memory.

#### Printf and UART

Other modules that are not used in your program can also be removed by the linker. For example, in [Blinky](https://github.com/ARMmbed/mbed-os-example-blinky) neither `printf` or UART drivers are used within its `main` program. However, every Mbed OS module handles traces and assertions by redirecting their error messages to `printf` on serial output - forcing the `printf` and UART drivers to be compiled in, requiring a large amount of flash memory.

To disable error logging to serial output, set the `NDEBUG` macro and the following configuration parameter in your program's mbed_app.json file:

```
{
    "macros": [ 
        "NDEBUG=1"
    ],
    "target_overrides": {
        "*": {
            "platform.stdio-flush-at-exit": false
        }
    }
}
```

**Note:** Different compilers, different results; compiling with one compiler with yield different memory usage savings than when compiling with another.

#### Embedded Targets

We can also take advantage of the fact that we run our programs only on embedded targets. When you run a C++ application on a desktop computer, the runtime constructs every global C++ object before `main` is called. It also registers a handle to destroy these objects when the program ends. The compiler injects this and has some implications for the application:

* The code injected by the compiler consumes memory.
* It implies dynamic memory allocation, and thus requires `malloc` to be included in the binary, even when not used by the application.

When we run an application on an embedded device we don't need handlers to destroy objects when the program exits, because the application will never end. By [removing destructor registration](https://github.com/ARMmbed/mbed-os/pull/2745) on application startup, and by eliminating the code to destruct objects when `exit()` is called, saving even more RAM and flash memory usage.
