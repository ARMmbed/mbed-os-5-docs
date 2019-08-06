# Alarm tutorial

This guide reviews the steps required to build and run a basic alarm application on an Mbed OS platform.

Please install [Mbed CLI](../tools/installation-and-setup.html).

## Import the example application

From the command-line, import the example:

```
mbed import mbed-os-example-alarm
cd mbed-os-example-alarm
```

If using the Mbed Online Compiler, use the **Import into Mbed IDE" button below:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/Alarm)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/Alarm/main.cpp)

### Compile

Invoke `mbed compile`, and specify the name of your platform and your favorite toolchain (`GCC_ARM`, `ARM`, `IAR`). For example, for the ARM Compiler 5:

```
mbed compile -m K64F -t ARM
```

Your PC may take a few minutes to compile your code.

### Program the board

1. Connect your Mbed device to the computer over USB.
1. Copy the binary file to the Mbed device.
1. Press the reset button to start the program.
1. Press **Button1** for the number of desired hours to delay. Press **Button2** to cycle to minutes, and repeat the previous step for the number of desired minutes.
1. Press **Button2** again to start the alarm.
1. Press **Button2** again once the alarm triggers to silence it. Both an LED and a digital out pin will go high on the alarm trigger and go back low on an alarm reset.

## Troubleshooting

If you have problems, you can review the [documentation](../tutorials/debugging.html) for suggestions on what could be wrong and how to fix it.
