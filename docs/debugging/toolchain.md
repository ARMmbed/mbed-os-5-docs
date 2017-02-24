# Setting up a local debug toolchain

Most mbed Enabled development boards contain two chips: the target microcontroller and a CMSIS-DAP interface chip. The most common use case of the interface chip is mounting the development board as a USB mass-storage device, making it easy to flash new firmware. However, you can also use this interface chip to debug the target microcontroller without an external debugger, such as a JTAG.

This offers debugging capabilities for stack trace analysis, register dumps and inspection of program execution (breakpoints, watchpoints and so on). When combined with a source-level debugger on the development host, such as the GNU Project Debugger (GDB), SWD offers a rich debugging experience - much more powerful than `printf()`.

<span class="tips">**Tip:** The CMSIS-DAP interface chip does not have to be on the development board. You can also use it as an off-board solution with the [SWDAP debugging probe](https://developer.mbed.org/teams/mbed/wiki/SWDAP). This is a good solution if you're making a custom board and do not want the added cost (or space required) of an extra interface chip and USB port.</span>

## Running a debug server

To connect to the debug interface, [pyOCD](https://github.com/mbedmicro/pyOCD) and [OpenOCD](http://openocd.org) support most boards. If the debug interface on your board is classified as 'CMSIS-DAP' or 'DAPLink' (most boards), you can use pyOCD. If not, use OpenOCD.

First, make sure you have installed the [GNU ARM Embedded Toolchain](https://launchpad.net/gcc-arm-embedded/4.9/4.9-2015-q3-update) and added it to your PATH. To verify that you have the correct version installed, open a terminal and run:

```
$ arm-none-eabi-gdb --version
GNU gdb (GNU Tools for ARM Embedded Processors) 7.8.0.20150604-cvs
Copyright (C) 2014 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
```

### pyOCD

If pyOCD supports your board, install [Python 2.7](https://www.python.org/downloads/). Then install pyOCD:

```
$ pip install pyocd
```

With your development board connected over USB, run:

```
$ pyocd-gdbserver

INFO:root:DAP SWD MODE initialized
INFO:root:K64F not in secure state
# ...
INFO:root:CPU core is Cortex-M4
INFO:root:FPU present
INFO:root:6 hardware breakpoints, 4 literal comparators
INFO:root:4 hardware watchpoints
INFO:root:Telnet: server started on port 4444
INFO:root:GDB server started at port:3333
```

A GDB server is now listening at localhost:3333.

### OpenOCD

If OpenOCD supports your board, first install [OpenOCD](http://openocd.org). OpenOCD cannot automatically detect the connected board, so you must determine what configuration you need for your development board. In general, searching for 'chipset openOCD' yields useful results.

For example, for the STM32F4-Discovery series, you use:

```
$ PATH_TO_OPENOCD/bin/openocd
        -f PATH_TO_OPENOCD/scripts/board/stm32f4discovery.cfg
        -f PATH_TO_OPENOCD/scripts/interface/stlink-v2-1.cfg
        -c init
        -c "reset init"

GNU ARM Eclipse 64-bits Open On-Chip Debugger 0.10.0-dev-00498-gbbfb673 (2016-10-28-19:13)
Licensed under GNU GPL v2
For bug reports, read
	http://openocd.org/doc/doxygen/bugs.html
Info : The selected transport took over low-level target control. The results might differ compared to plain JTAG/SWD
adapter speed: 2000 kHz
adapter_nsrst_delay: 100
none separate
srst_only separate srst_nogate srst_open_drain connect_deassert_srst
# ...
stm32f4x.cpu: target state: halted
target halted due to debug-request, current mode: Thread
xPSR: 0x01000000 pc: 0x08000504 msp: 0x20020000
adapter speed: 4000 kHz
```

A GDB server is now listening at localhost:3333.

## Connecting GDB

You can now verify that the debug connection works via GDB. Open another terminal window and run:

```
$ arm-none-eabi-gdb
```

In the CLI, type `target remote localhost:3333`. Verify that GDB connects to your development board.

```
$ arm-none-eabi-gdb
GNU gdb (GNU Tools for ARM Embedded Processors) 7.8.0.20150604-cvs
Copyright (C) 2014 Free Software Foundation, Inc.
For help, type "help".
Type "apropos word" to search for commands related to "word".
(gdb) target remote localhost:3333
Remote debugging using localhost:3333
0x0001602a in ?? ()
```

You now have set up a debug connection. From here, you can flash debug builds, step through code and use any IDE that supports GDB to debug mbed OS applications. For instructions, see:

1. Producing [debug builds with mbed CLI](debug_builds.md).
1. Debugging with [Eclipse](Debugging_Eclipse_pyOCD.md).
1. Debugging with [Keil uVision](Keil.md).
1. Debugging with [Visual Studio Code](vscode.md).

## Semihosting messages

It's possible to send messages from the development board to your computer over the debug port using [semihosting](http://www.keil.com/support/man/docs/armcc/armcc_pge1358787046598.htm). Some parts of mbed OS 5 also use this, such as uVisor. To see semihosting messages:

1. Install [Netcat](https://en.wikipedia.org/wiki/Netcat).
2. Connect pyOCD or OpenOCD to your board.
3. Run `nc localhost 4444`.

<span class="notes">**Note:** uVisor sends most of its messages during startup, so attach Netcat before starting your program.</span>