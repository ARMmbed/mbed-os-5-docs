# Your first application

We have an example application called [Blinky](https://github.com/ARMmbed/mbed-blinky-morpheus) that you can use to get to know mbed OS and the build tools.

You can try any of these tools:

* [mbed Studio](#blinky-on-mbed-studio)
* [mbed Online Compiler](#blinky-on-mbed-online-compiler)
* [mbed CLI](#blinky-on-mbed-cli)

## What the tools do

All of the build tools perform the same process:

* Bring the mbed OS source code from GitHub, along with all dependencies.
* Compile your code with the mbed OS code so that you have a single file to flash to your board.
* Allow you to set a build target, so that the compiled code matches your hardware (and build toolchain, if you're using mbed CLI).

## Before you begin

There are two things you need to be able to use our sample application (and mbed OS in general):

1. A [developer account on mbed](https://developer.mbed.org/account/signup/).
2. An understanding of what we mean when we say "build target". A build target is a combination of your board - for example an [FRDM-K64F or a Nucleo-F401RE](https://www.mbed.com/en/development/hardware/boards/) and a toolchain. Selecting a target is how you tell the build tools exactly how to compile your code; different boards and toolchains have different compilation requirements. If you're working with the *mbed Online Compiler* or *mbed Studio*, the toolchain is the IDE itself, so you only need to select the right hardware. If you're working with *mbed CLI*, you also need to select a toolchain. Exact instructions are provided in the following sections.

## Blinky on mbed Studio

Working with mbed Studio requires a Cloud9 account on top of your mbed developer account. You can use an existing Cloud9 account or create a new one; either way, you'll have to follow the instructions on mbed Studio to link the Cloud9a and mbed developer accounts. 

mbed Studio does all the complicated work for you - it fetches Blinky along with the mbed OS code base it requires, and builds to whichever [target you]() need.

## Blinky on mbed Online Compiler


## Blinky on mbed CLI

mbed CLI is an offline tool, meaning you'll have to install it before you can work. 

Please follow the installation instructions on the mbed CLI page, and come back here when you're done.

### Get Blinky

From the command line, import the example:

```
mbed import mbed-os-example-blinky
cd mbed-os-example-blinky
```

### Compile

Invoke `mbed compile` specifying the name of your platform and your favorite toolchain (`GCC_ARM`, `ARM`, `IAR`). For example, for the ARM Compiler 5:

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
