### Debugging Arm Mbed OS applications

At the heart of Arm Mbed is the [Online Compiler](/docs/v5.4/tools/online.html#arm-mbed-online-compiler-1). While that is incredibly convenient for getting a project started or while prototyping, chances are that at some point you'll miss a debugger, or you'll want to develop while not having an active internet connection. Through debugging, you can do things such as set breakpoints, set watchpoints, view registers, view disassembly, browse memory and examine the callstack. These docs will help you debug your applications.

The simplest way to debug your code is to augment your code with log statements, which you can observe from your computer.

#### Debugging from an IDE

Keil uVision natively supports debugging Mbed OS applications. To set up uVision, read [Debugging with Keil uVision](https://os.mbed.com/docs/v5.4/tutorials/debugging-applications.html#keil-uvision).

Mbed also supports debugging using any IDE that supports GDB. To set up the debugger, first read [Setting up your local debug toolchain](toolchain.md). Then read the section for your specific IDE. The same principles apply to any unlisted IDEs that supports GDB:

1. Producing [debug builds with Arm Mbed CLI](/docs/v5.4/tools/debugging.html#debugging-your-project).
1. Debugging with [Eclipse](https://os.mbed.com/docs/v5.4/tutorials/debugging-applications.html#eclipse).
1. Debugging with [Visual Studio Code](https://os.mbed.com/docs/v5.4/tutorials/debugging-applications.html#visual-studio-code).
1. Debugging with [other IDEs that support GDB](/docs/v5.4/tools/debugging.html).

#### Links to other sources

* [Using CMSIS-DAP to debug a device after it crashes](https://developer.mbed.org/blog/entry/Post-mortem-debugging-with-ARM-mbed/).
* [Debugging the micro:bit with pyOCD and GDB](https://os.mbed.com/docs/v5.4/tutorials/debugging-using-printf-statements.html#debug-microbit).
