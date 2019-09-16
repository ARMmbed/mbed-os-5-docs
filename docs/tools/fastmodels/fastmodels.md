# Fast Models

Arm Fast Models are software models of Arm cores, subsystems, peripherals and so on. You can run Mbed OS on the software model instead of the hardware.

This document explains how to build, run and debug Arm Mbed OS applications with Arm Fast Models. Due to licensing, Mbed OS does not provide any Fast Models. If you do not have a Fast Models license yet, you can visit [Arm Fast Models](https://developer.arm.com/products/system-design/fast-models) to obtain an evaluation license.

Fixed Virtual Platforms (FVPs) are prebuilt system-level models after Arm’s reference platforms by Fast Models.

For more details on Fast Models and FVPs, please reference further documentation about [Arm Fast Models](https://developer.arm.com/products/system-design/fast-models) or [FVPs](https://developer.arm.com/products/system-design/fixed-virtual-platforms).

## Supported Fast Models FVPs

Mbed OS has enabled working with following FVPs Cortex-M family with the MPS2 platforms:

Fast Models platforms | Target name in Mbed OS
---|---
FVP_MPS2_Cortex-M0 | FVP_MPS2_M0
FVP_MPS2_Cortex-M0plus | FVP_MPS2_M0P
FVP_MPS2_Cortex-M3 | FVP_MPS2_M3
FVP_MPS2_Cortex-M4 | FVP_MPS2_M4
FVP_MPS2_Cortex-M7 | FVP_MPS2_M7

## Mbed OS examples on Fast Models

Fast Models can run most of the Mbed OS examples.

Examples you can successfully run include:

- [`mbed-os-example-blinky`](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-blinky/).
- [`mbed-os-example-tls`](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-tls-benchmark/).
- [`mbed-os-example-devicekey`](../apis/devicekey.html#devicekey-example).
- [`mbed-os-example-nvstore`](../apis/nvstore.html#nvstore-example).
- [`mbed-os-example-thread-statistics`](../apis/mbed-statistics.html#thread-statistics-example).
- [`mbed-os-example-sys-info`](../apis/mbed-statistics.html#system-information-example).
- [`mbed-os-example-cpu-usage`](../apis/mbed-statistics.html#cpu-usage-example).
- [`mbed-os-example-cpu-stats`](../apis/mbed-statistics.html#cpu-statistics-example).
- [`mbed-os-example-error-handling`](../apis/error-handling.html#error-handling-example).
- [`mbed-os-example-filesystem`](../apis/filesystem.html#file-system-example).
- [`mbed-os-example-blockdevice`](../apis/blockdevice.html#blockdevice-example).
- [`mbed-os-example-sockets`](../apis/socket.html#socket-example).

The following examples use `mbed-os-example-blinky`.

To run Mbed OS examples with Fast Models, you need to install the Fast Models product and set up the license. The [Arm DS-5 Development Studio](https://developer.arm.com/products/software-development-tools/ds-5-development-studio) also provides Fast Models targets. To load a compiled Mbed OS image onto a Fast Models platform, such as the FVP_MPS2_Cortex-M0, you need to add your installation's `bin` folder to your system `PATH`. For example: `C:\Program Files\DS-5 v5.29.1\bin`.

### Import the example with Arm Mbed CLI

Import the blinky example:

```
$ mbed import mbed-os-example-blinky
$ cd mbed-os-example-blinky
```

### Build the example with Mbed CLI

Fast Models targets are enabled to be built with all three major toolchains: ARM, GCC_ARM and IAR. To build the blinky example for the FVP_MPS2_Cortex-M3 target with the GCC complier, run:

```
$ mbed compile -t GCC_ARM -m FVP_MPS2_M3
```

### Run Mbed OS examples with Fast Models

Load the compiled example image to the FVP_MPS2_Cortex-M3 target. To do so, pass the `-a` option to the Fast Models target. For example:

```
$ FVP_MPS2_Cortex-M3 -a BUILD/FVP_MPS2_M3/GCC_ARM/mbed-os-example-blinky.elf
```

The FVPs start running, and the LEDs on the FVP blink, like:

<span class="images">![](../../images/fastmodel_cm3.png)<span>A screen shot of FVPs running</span></span>

<span class="notes">**Note:** FVP's `-a` option only takes `.elf` format images. To use the `--data` option with binary format images, please reference the [FVP reference guide](https://developer.arm.com/docs/100966/latest).</span>

### Run Mbed OS sockets examples with Fast Models ethernet

Fast Models ethernet is a special component not enabled by default.

<span class="notes">**Note:** The current version of Fast Model ethernet implementations requires Fast Models 11.3 or later or DS-5 5.29.0 or later. Also, the simulated IP routing only works on TCP and IP protocols, but neither the ICMP nor the IGMP protocol. This means ping does not work. For more details about how the Fast Models ethernet MAC works, please reference the [Fast Models reference manual](https://developer.arm.com/products/system-design/fast-models/docs/100964/latest/introduction/network-set-up/user-mode-networking).</span>

Here, the `mbed-os-example-sockets` example demonstrates ethernet function. You can build the example as usual:

```
$ mbed import mbed-os-example-sockets
$ cd mbed-os-example-sockets
$ mbed compile -t GCC_ARM -m FVP_MPS2_M3
```

While launching the Mbed OS socket example with the Fast Models Ethernet function, you need to pass the arguments  `-C fvp_mps2.smsc_91c111.enabled=1` and `-C fvp_mps2.hostbridge.userNetworking=1` in the command-line:

```
$ FVP_MPS2_Cortex-M3 -C fvp_mps2.smsc_91c111.enabled=1 -C fvp_mps2.hostbridge.userNetworking=1 -a BUILD/FVP_MPS2_M3/GCC_ARM/mbed-os-example-sockets.elf
```

The FVPs start running, and the console output looks like:

```
Mbed OS Socket example
Mbed OS version: 99.99.99

IP address: 172.20.51.1
Netmask: 255.255.255.0
Gateway: 172.20.51.254
sent 58 [GET / HTTP/1.1]
recv 181 [HTTP/1.1 200 OK]
External IP address: 217.140.106.54
Done
```

## Notes

1. Timing accuracy of Fast Models can't be guaranteed.
1. There is no support for external peripherals, such as ESP8266 expansion boards.
