# Porting guide

This document provides guidelines for adding a new MCU target to Mbed OS and the Pelion IoT Platform. By the end of this process, you will have ported a new target to Mbed OS, and your device will:

- Pass all Mbed OS tests.
- Run Device Management client.
- Meet technical requirements for Mbed Enabled program.

These guidelines use pyOCD, our debugger, and DAPLink, our interface firmware, in the porting process because they are free and open source. Please note that you can use other debuggers and interface firmware, but that is outside the scope of this document.

## Scope and milestones

You will usually need to go through all of these steps to port Mbed OS:

1. Set up a development environment (including IDE and debugger) and your target.

1. Locate reusable code to port to Mbed OS, or write your own.

    If there is a Partner SDK available to speed up the porting process, we recommend reusing it (assuming copyright of the existing code is preserved).

1. Implement and test CMSIS headers, linker script and startup code.

   A basic framework is ready after this step. You can do the rest of the porting work in parallel:

1. Implement and test the ported HAL modules. This porting guide provides the recommended porting order and links to full porting information about each module.

1. Test Mbed OS and Pelion example applications. This steps verifies that your new port is fully functional.
