## Porting guide

This document provides guidelines for adding a new MCU target to Mbed OS and the Pelion IoT Platform.

### Scope and milestones

You will usually need to go through all of these steps to port Mbed OS:

1. Set up a development environment (including IDE and debugger) and your target.

1. If there is an SDK (or drivers package) already available for your target, you may use it to speed up the porting process. Please ensure that the SDK licensing permits its existence along with `mbed-os` code base.

1. The [Mbed Enabled](https://www.mbed.com/en/about-mbed/mbed-enabled/introduction/) program requires pyOCD, so ultimately pyOCD needs to support the new target. While pyOCD support is being enabled, it is recommended to use any supported IDEs to develop the target's connectivity and storage.

1. Implement and test CMSIS pack, bootstrap, linker script and startup code.

A basic framework is ready after this step. You can do the rest of the porting work in parallel:

1. Implement and test ported APIs<!--we call the modules everywhere else-->. This porting guide provides the recommended porting order and links to full porting information about each module.

1. Test Mbed OS and Pelion example applications. This steps verifies that your new port is fully functional.
