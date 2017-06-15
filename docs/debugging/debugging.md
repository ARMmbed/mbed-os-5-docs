# Debugging mbed OS applications

At the heart of mbed is the [Online Compiler](https://docs.mbed.com/docs/mbed-os-handbook/en/latest/dev_tools/online_comp/). While that is incredibly convenient for getting a project started or while prototyping, chances are that at some point you'll miss a debugger, or you'll want to develop while not having an active internet connection. Through debugging, you can do things such as set breakpoints, set watchpoints, view registers, view disassembly, browse memory and examine the callstack. These docs will help you debug your applications.

The simplest way to debug your code is to augment your code with log statements, which can be observed from your computer. To set this up, read [Debugging with printf() calls](printf.md).

## Compile time and runtime errors

If your program will not compile, first read [Debugging compile time errors](compile_time.md).

If your development board blinks very fast, or shows 'siren lights', see [Lights of dead](lights_of_dead.md).

## Debugging from an IDE

Keil uVision natively supports debugging mbed OS applications. To set up uVision, read [Debugging with Keil uVision](Keil.md).

mbed also supports debugging using any IDE that supports GDB. To set up the debugger, first read [Setting up your local debug toolchain](toolchain.md). Then read the section for your specific IDE. The same principles apply to any unlisted IDEs that supports GDB:

1. Producing [debug builds with mbed CLI](debug_builds.md).
1. Debugging with [Eclipse](debugging_eclipse_pyocd.md).
1. Debugging with [Visual Studio Code](vscode.md).
1. Debugging with [other IDEs that support GDB](other_ides.md).

## Links to other sources

* [Using CMSIS-DAP to debug a device after it crashes](https://developer.mbed.org/blog/entry/Post-mortem-debugging-with-ARM-mbed/).
* [Debugging the micro:bit with pyOCD and GDB](debugging_microbit.md).
