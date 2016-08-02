# Blinky on mbed CLI

mbed CLI is an offline tool, meaning you'll have to install it before you can work. You will also need to install a toolchain. Please follow the installation instructions on the [mbed CLI page](../dev_tools/cli.md), and come back here when you're done.

## Get Blinky

[Blinky is on GitHub](https://github.com/ARMmbed/mbed-os-example-blinky), but you don't need to go through GitHub to get it into mbed CLI - mbed CLI can do that for you.

From the command line, import the example:

```
mbed import mbed-os-example-blinky
cd mbed-os-example-blinky
```

## Compile

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

## Program your board

1. Connect your mbed device to the computer over USB.
1. Copy the binary file to the mbed device.
1. Press the reset button to start the program.

You should see the LED of your platform turning on and off.
