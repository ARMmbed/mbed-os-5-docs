## Setting up

### Hardware setup

Porting Mbed OS requires the following hardware:

- An evaluation board with the targeted MCU.

    The new target needs a unique board ID. [Contact Arm]() to get one.

- A micro USB cables. One Micro USB cable connects the evaluation board to your development PC.

You may also need:

- If the interface MCU is not on the evaluation board, choose a debug probe, such as [SDWAP-LPC11U35](https://os.mbed.com/platforms/SWDAP-LPC11U35/). You will then need a micro USB cable (in addition to the micro USB cable listed above).
- An FTDI TTL232R-3V3 USB cable, for the Tx and Rx pins of debug probes that do not have a serial connection.
<!--I reversed the order because it seemed that the second will only be relevant if the first one is true. -->

The following items might help you test SPI, I2C and Pins:

- A CI test shield v2.0.0. For details, refer to [https://github.com/ARMmbed/ci-test-shield](https://github.com/ARMmbed/ci-test-shield).
- A micro SD card for the CI test shield.

<span class="tips">Check the user guide of the evaluation board to see if anything needs to be done prior to using a debug probe and running Mbed OS programs.</span>

### Software setup

Please install the following:

- [Python 2.7](https://www.python.org/downloads/release/python-2715/).
- [Git](https://git-scm.com/downloads).
- [Mbed CLI](../tools/installation-and-setup.html).
- (Optional) [FTDI serial driver](http://www.ftdichip.com/Drivers/VCP.htm).
- Toolchains:
   - [GNU Arm Embedded Toolchain (GCC)](https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads).
   - [IAR](https://www.iar.com/iar-embedded-workbench/).
   - [Arm Compiler 5 or 6](https://developer.arm.com/products/software-development-tools/compilers/arm-compiler/downloads/version-5).

<span class="notes">The [tools documentation](../tools/index.html) contains the exact third party tool versions supported in a specific Mbed OS release.</span>
