## Debugging Arm Mbed OS applications

At the heart of Arm Mbed is the <a href="/docs/v5.6/tools/arm-online-compiler.html" target="_blank">Online Compiler</a>. While that is incredibly convenient for getting a project started or while prototyping, chances are that at some point you'll miss a debugger, or you'll want to develop while not having an active internet connection. Through debugging, you can do things such as set breakpoints, set watchpoints, view registers, view disassembly, browse memory and examine the callstack. These docs will help you debug your applications.

The simplest way to debug your code is to augment your code with log statements, which you can observe from your computer.

### Debugging from an IDE

Keil uVision natively supports debugging Mbed OS applications. To set up uVision, read <a href="/docs/v5.6/tutorials/keil-uvision.html" target="_blank">Debugging with Keil uVision</a>.

Mbed also supports debugging using any IDE that supports GDB. To set up the debugger, first read <a href="/docs/v5.6/tools/setting-up-a-local-debug-toolchain.html" target="_blank">Setting up your local debug toolchain</a>. Then read the section for your specific IDE. The same principles apply to any unlisted IDEs that supports GDB:

1. Producing <a href="/docs/v5.6/tools/debug-builds-cli.html" target="_blank">debug builds with Arm Mbed CLI</a>.
1. Debugging with <a href="/docs/v5.6/tutorials/eclipse.html" target="_blank">Eclipse</a>.
1. Debugging with <a href="/docs/v5.6/tutorials/visual-studio-code.html" target="_blank">Visual Studio Code</a>.
1. Debugging with <a href="/docs/v5.6/tools/debugging.html" target="_blank">other IDEs that support GDB</a>.

### Links to other sources

- <a href="https://os.mbed.com/blog/entry/Post-mortem-debugging-with-ARM-mbed/" target="_blank">Using CMSIS-DAP to debug a device after it crashes</a>.
- <a href="/docs/v5.6/tutorials/debug-microbit.html" target="_blank">Debugging the micro:bit with pyOCD and GDB</a>.
