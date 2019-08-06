# Mbed-ls

Mbed-ls is a Python module that detects and lists Mbed Enabled boards connected to a computer through USB.

## Defined behavior

Mbed-ls needs the following information to correctly detect an Mbed Enabled board:

 - A four-digit hexadecimal identifier of a board class.
 - A vendor string for detection on Windows.

Further, Mbed-ls only detects devices that meet the following criteria:

 - Devices have a mass storage device (MSD) endpoint.
 - The MSD endpoint has a FAT file system.

## Implementation

Please see the [implementation guide](https://github.com/ARMmbed/mbed-os-tools/tree/master/packages/mbed-ls#adding-platform-support) in Mbed LS for more details.
