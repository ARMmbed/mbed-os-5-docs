## Porting guide

This document provides guidelines for adding a new MCU target to Mbed OS and the Pelion IoT Platform.

### Scope and milestones

You will usually need to go through all of these steps to port Mbed OS:

1. Set up a development environment (including IDE and debugger) and your target.

1. Locate reusable code to port to Mbed OS.
<!--Are the reusable code and SDK related? Are they the same thing?-->
    If there is an SDK available to speed up the porting process, we recommend reusing it (assuming copyright of the existing code is preserved).

    <!--I actually don't quite understand this. Is it mandatory to find reusable code (which is implied in the first line), or is it "if you have it, use it"?-->


1. The [Mbed Enabled](https://www.mbed.com/en/about-mbed/mbed-enabled/introduction/) program requires pyOCD, so ultimately pyOCD needs to support the new target. To allow parallel development in porting targets, connectivity and storage while pyOCD is still under development, you can use other IDEs supported on the evaluation board in the beginning phase.

1. Implement and test CMSIS pack, bootstrap, linker script and startup code.

A basic framework is ready after this step. You can do the rest of the porting work in parallel:

1. Implement and test porting APIs<!--we call the modules everywhere else-->. This porting guide provides the recommended porting order and links to full porting information about each module.

1. Test Mbed OS and Pelion example applications. This steps verifies that your new port is fully functional.
