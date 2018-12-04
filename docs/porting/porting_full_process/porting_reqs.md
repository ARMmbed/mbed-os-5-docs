## Setting up

### Hardware setup

Porting Mbed OS requires the following hardware:

-  An evaluation board with a target MCU, debug probe or an integrated interface chip. The hardware [is reviewed in greater details later in this document]().

    The new target needs a unique board ID. [Contact Arm]()<!-- need a link here --> to get one.

- A storage device (SD or external flash).
- A micro SD card for the CI test shield.
- A USB cable to connect the evaluation board to your development PC.

You may also need:

- If the interface MCU is not on the evaluation board, choose a debug probe, such as [SWDAP-LPC11U35](https://os.mbed.com/platforms/SWDAP-LPC11U35/). You will then need a micro USB cable (in addition to the micro USB cable listed above).
- An FTDI TTL232R-3V3 USB cable, for the Tx and Rx pins of debug probes that do not have a serial connection.

The following items might help you test SPI, I2C and pins:

- A CI test shield v2.0.0. For details, refer to [https://github.com/ARMmbed/ci-test-shield](https://github.com/ARMmbed/ci-test-shield).

<span class="tips">Check the user guide of the evaluation board to see if anything needs to be done prior to using a debug probe and running Mbed OS programs.</span>

### Software setup

Please install the following:

- [Python](https://www.python.org/downloads).
- [Git](https://git-scm.com/downloads).
- [Mbed CLI](../tools/installation-and-setup.html).
- Choose an IDE and debugger. The three commonly used IDEs are [Eclipse](https://www.eclipse.org/ide/), [IAR Embedded Workbench](https://www.iar.com/iar-embedded-workbench/) and [Keil MDK](http://www.keil.com/). Note: If a board has DAPLink support, we recommend you use pyOCD.

    Limitations:

    - Eclipse is license free, whereas both IAR and Keil IDE require licenses.
    - Your target may not be supported in certain IDEs.
    - If your interface firmware does not support mass storage device, you won't be able to do automated testing. If your target has another method of flashing, such as self-programming or through a debugger, use the [manual testing path](../porting/manual-testing.html).

- (Optional) [FTDI serial driver](http://www.ftdichip.com/Drivers/VCP.htm).

<span class="notes">The [tools documentation](../tools/index.html) contains the exact third party tool versions supported in a specific Mbed OS release.</span>
