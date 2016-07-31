# Your first application

We have an example application called Blinky that you can use to get to know mbed OS and the development tools. It's one of the simplest examples of mbed OS. It shows the use of a DigitalOut object to represent an LED and the non-blocking ``Thread::wait()`` call. This is good practice as if there were other threads, they could be scheduled and run while the first thread is waiting.



You can try any of these tools:

* [mbed CLI](#blinky-on-mbed-cli)
* [mbed Online Compiler](#blinky-on-mbed-online-compiler)
* [mbed Studio](#blinky-on-mbed-studio)

## What the tools do

All of the development tools perform the same process:

* Bring the mbed OS source code from GitHub, along with all dependencies.
* Compile your code with the mbed OS code so that you have a single file to flash to your board.
* Allow you to set a build target, so that the compiled code matches your hardware (and development toolchain, if you're using mbed CLI).

## Before you begin

Please get a [developer account on mbed](https://developer.mbed.org/account/signup/).

You might want to read the page [explaining how to connect your board to your computer](serial_communication.md) - especial if you're using Windows.

## Blinky on mbed CLI

mbed CLI is an offline tool, meaning you'll have to install it before you can work. You will also need to install a toolchain. Please follow the installation instructions on the [mbed CLI page](../dev_tools/cli.md), and come back here when you're done.

### Get Blinky

[Blinky is on GitHub](https://github.com/ARMmbed/mbed-os-example-blinky), but you don't need to go through GitHub to get it into mbed CLI - mbed CLI can do that for you.

From the command line, import the example:

```
mbed import mbed-os-example-blinky
cd mbed-os-example-blinky
```

### Compile

Invoke `mbed compile`, specifying:

* Your board: ``-m <board_name>``
* Your  toolchain ``-t <GCC_ARM`, `ARM` or `IAR`>``.

For example, for the board K64F and the ARM Compiler 5:

```
mbed compile -m K64F -t ARM
```

Your PC may take a few minutes to compile your code. At the end you should get the following result:

```
[snip]
+----------------------------+-------+-------+------+
| Module                     | .text | .data | .bss |
+----------------------------+-------+-------+------+
| Misc                       | 13939 |    24 | 1372 |
| core/hal                   | 16993 |    96 |  296 |
| core/rtos                  |  7384 |    92 | 4204 |
| features/FEATURE_IPV4      |    80 |     0 |  176 |
| frameworks/greentea-client |  1830 |    60 |   44 |
| frameworks/utest           |  2392 |   512 |  292 |
| Subtotals                  | 42618 |   784 | 6384 |
+----------------------------+-------+-------+------+
Allocated Heap: unknown
Allocated Stack: unknown
Total Static RAM memory (data + bss): 7168 bytes
Total RAM memory (data + bss + heap + stack): 7168 bytes
Total Flash memory (text + data + misc): 43402 bytes
Image: .\.build\K64F\ARM\mbed-os-example-blinky.bin             
```

### Program your board

1. Connect your mbed device to the computer over USB.
1. Copy the binary file to the mbed device.
1. Press the reset button to start the program.

You should see the LED of your platform turning on and off.

## Blinky on mbed Online Compiler

To get Blinky into the mbed Online Compiler, click the **Import to IDE** button below:

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed-os-examples/code/mbed-os-example-blinky/)](https://developer.mbed.org/teams/mbed-os-examples/code/mbed-os-example-blinky/file/tip/main.cpp) 


## Blinky on mbed Studio

Working with mbed Studio requires a Cloud9 account on top of your mbed developer account. You can use an existing Cloud9 account or create a new one; either way, you'll have to follow the instructions on mbed Studio to link the Cloud9a and mbed developer accounts. 

mbed Studio does all the complicated work for you - it fetches Blinky along with the mbed OS code base it requires, and builds to whichever [target you]() need.


## Where next

We have a few more examples you might enjoy:

!{https://raw.githubusercontent.com/ARMmbed/Handbook/master/docs/getting_started/examples.md?token=AKWAjchqxTiW4Wz6mk9VTmb9YWNE0gMoks5Xpz8lwA%3D%3D}
