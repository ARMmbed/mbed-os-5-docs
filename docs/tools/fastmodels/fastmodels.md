## Fast Models

Arm Fast Models are accurate, flexible programmer's view software models of Arm cores, subsystems and peripherals etc. Users can run Mbed OS on the software model instead of the hardware.

This document explains how to build, run and debug Arm Mbed OS applications with ARM Fast Models. Due to license reason, Mbed OS do not provide any Fast Models. If you already have a valid license to use Fast Models, you can follow this documentation to start.  If you do not have a Fast Models license yet, you can visit [Arm Fast Models](https://developer.arm.com/products/system-design/fast-models) to obtain an evaluation license.

FVPs (Fixed Virtual Platforms) are pre-built system-level models after arm’s reference platforms by Fast Models

For more details on Fast Models and FVPs, please referencing [Arm Fast Models](https://developer.arm.com/products/system-design/fast-models) or [FVPs](https://developer.arm.com/products/system-design/fixed-virtual-platforms)


## Mbed OS Supported Fast Model FVPs
Mbed OS is enabled working with following FVPs Cortex-M family with MPS2 platforms:

Fast Models Platforms | Target name in Mbed OS
---|---
FVP_MPS2_Cortex-M0 | FVP_MPS2_M0
FVP_MPS2_Cortex-M0plus | FVP_MPS2_M0P
FVP_MPS2_Cortex-M3 | FVP_MPS2_M3
FVP_MPS2_Cortex-M4 | FVP_MPS2_M4
FVP_MPS2_Cortex-M7 | FVP_MPS2_M7



## Mbed OS examples on Fast Models
Currently Fast Models able run most of the Mbed OS examples which do not require networking or external peripherals[^1] .

[`mbed-os-example-thread-statistics`](https://github.com/ARMmbed/mbed-os-example-thread-statistics), [`mbed-os-example-tls`](https://github.com/ARMmbed/mbed-os-example-tls), [`mbed-os-example-devicekey`](https://github.com/ARMmbed/mbed-os-example-devicekey), [`mbed-os-example-nvstore`](https://github.com/ARMmbed/mbed-os-example-nvstore) etc. can be successfully run as of today

Here we take [`mbed-os-example-blinky`](https://github.com/ARMmbed/mbed-os-example-blinky) as an example

#### Import example with Mbed CLI 
Import blinky example as normal:
```
  $ mbed import mbed-os-example-blinky
  $ cd mbed-os-example-blinky
```

#### Build example with Arm Mbed CLI

Fast Models targets are enabled to build with all 3 major tool-chains: ARM GCC_ARM and IAR. To build blinky example for the FVP_MPS2_Cortex-M3 target with gcc complier, just run:
  ```
  $ mbed compile -t GCC_ARM -m FVP_MPS2_M3
  ```

#### Run Mbed OS examples with Fast Model

To run mbed OS example with Fast Model FVPs, you need to have Fast Models product installed and License set up.

>This document dose not including the section for Fast Models product installation and configuration. Because it is another topic, and we just assume that users had that done already. For more details about configuring and running Arm Fast Models can be found in [Fast Models Documentation](https://developer.arm.com/products/system-design/fast-models/docs)

Load the compiled example image to FVP_MPS2_Cortex-M3 target, you simple just need to pass the `-a` option to the Fast Model target, e.g. :
  ```
  $ FVP_MPS2_Cortex-M3 -a BUILD/FVP_MPS2_M3/GCC_ARM/mbed-os-example-blinky.elf
  ```
You should be able to see FVPs starts running, and serial output through telnet/xterm, or LEDs on the FVP is blinking, like:

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/fastmodel_cm3.png)<span>a screen-shot for FVPs running</span></span>

*NOTE:*

> *FVP's -a option only takes elf format images, if you need to use "--data" option with binary format images, detailed options please referencing [FVP Users' Guide](http://arminfo.emea.arm.com/help/index.jsp?topic=/com.arm.doc.100966_1103_00_en/index.html)*

## Known issues
1 Timing accuracy of Fast Model FVPs can't be guaranteed 
2 No support for external peripherals. e.g. esp8266, Expansion boards
3 Ethernet support for Fast Model FVPs is in working progress.

[^1]: *Because of known issue 2 and 3*, Fast Models not able to run all examples at moments
