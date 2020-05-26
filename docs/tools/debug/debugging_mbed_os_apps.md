# Debugging methods for Arm Mbed OS applications

At the heart of Arm Mbed is the [Online Compiler](../build-tools/mbed-online-compiler.html). While that is incredibly convenient for getting a project started or while prototyping, chances are that at some point you'll miss a debugger, or you'll want to develop while not having an active internet connection. Through debugging, you can do things such as set breakpoints, set watchpoints, view registers, view disassembly, browse memory and examine the callstack. These docs will help you debug your applications.

The simplest way to debug your code is to augment your code with [printf](../tutorials/debugging-using-printf-statements.html) statements, which you can observe from your PC using a [serial monitor](../tutorials/serial-comm.html).

## Debugging from an IDE

Keil uVision natively supports debugging Mbed OS applications. To set up uVision, read [Debugging with Keil uVision](../debug-test/keil-uvision.html).

Mbed also supports debugging using any IDE that supports GDB. To set up the debugger, first read [Setting up your local debug toolchain](../debug-test/setting-up-a-local-debug-toolchain.html). Then read the section for your specific IDE. The same principles apply to any unlisted IDEs that supports GDB:

1. Producing [debug builds with Arm Mbed CLI](../program-setup/debug-builds-cli.html).
1. Debugging with [Eclipse](../debug-test/third-party-tools.html).
1. Debugging with [Visual Studio Code](../debug-test/visual-studio-code.html).
1. Debugging with [other IDEs that support GDB](../debug-test/index.html).

## Links to other sources

- [Using CMSIS-DAP to debug a device after it crashes](https://os.mbed.com/blog/entry/Post-mortem-debugging-with-ARM-mbed/).
- [Debugging the micro:bit with pyOCD and GDB](../debug-test/debug-microbit.html).
