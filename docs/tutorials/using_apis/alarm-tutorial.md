## Alarm tutorial

This guide reviews the steps required to build and run a basic alarm application on an Mbed OS platform.

Please install [Mbed CLI](../tools/installation-and-setup.html).

### Import the example application

From the command-line, import the example:

```
mbed import mbed-os-example-alarm
cd mbed-os-example-alarm
```

If using the Mbed Online Compiler, use the **Import into Mbed IDE" button below:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/Alarm)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/Alarm/main.cpp)

#### Compile

Invoke `mbed compile`, and specify the name of your platform and your favorite toolchain (`GCC_ARM`, `ARM`, `IAR`). For example, for the ARM Compiler 5:

```
mbed compile -m K64F -t ARM
```

Your PC may take a few minutes to compile your code. At the end, you see the following result:

```
[snip]
| Module               |         .text |     .data |        .bss |
|----------------------|---------------|-----------|-------------|
| [lib]/dl7M_tlf.a     | 10780(+10780) | 364(+364) |   716(+716) |
| [lib]/dlpp7M_tl_fc.a |       84(+84) |     0(+0) |       0(+0) |
| [lib]/m7M_tls.a      |   2358(+2358) |     0(+0) |       0(+0) |
| [lib]/rt7M_tl.a      |   1194(+1194) |     0(+0) |       0(+0) |
| [misc]               |     215(+215) |     0(+0) |       0(+0) |
| main.o               |     820(+820) |     0(+0) |   200(+200) |
| mbed-os/drivers      |     490(+490) |     0(+0) |       0(+0) |
| mbed-os/features     |     114(+114) |     0(+0) |   184(+184) |
| mbed-os/hal          |   2070(+2070) |     8(+8) |   132(+132) |
| mbed-os/platform     |   2938(+2938) | 112(+112) |   176(+176) |
| mbed-os/rtos         |   8928(+8928) | 168(+168) | 6437(+6437) |
| mbed-os/targets      | 10174(+10174) |   20(+20) | 1018(+1018) |
| Subtotals            | 40165(+40165) | 672(+672) | 8863(+8863) |
Total Static RAM memory (data + bss): 9535(+9535) bytes
Total Flash memory (text + data): 40837(+40837) bytes

Image: ./BUILD/K64F/IAR/mbed-os-example-alarm.bin
```

#### Program the board

1. Connect your Mbed device to the computer over USB.
1. Copy the binary file to the Mbed device.
1. Press the reset button to start the program.
1. Press **Button1** for the number of desired hours to delay. Press **Button2** to cycle to minutes, and repeat the previous step for the number of desired minutes.
1. Press **Button2** again to start the alarm.
1. Press **Button2** again once the alarm triggers to silence it. Both an LED and a digital out pin will go high on the alarm trigger and go back low on an alarm reset.

### Troubleshooting

If you have problems, you can review the [documentation](../tutorials/debugging.html) for suggestions on what could be wrong and how to fix it.
