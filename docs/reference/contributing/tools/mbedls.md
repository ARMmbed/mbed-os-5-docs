### mbed-ls

Mbed-ls is a Python module that detects and lists Mbed Enabled boards connected to a host computer.

### Defined behavior

Mbed-ls needs the following information to correctly detect an Mbed Enabled target:

 - A four-digit hexadecimal identifier of a board class.
 - A vendor string for detection on Windows.
 
Further, mbed-ls only detects devices that meet the following criteria:

 - Devices have a mass storage device (MSD) endpoint.
 - The MSD endpoint has a FAT file system.
 
### Implementation

When adding a target to mbed-ls, you typically need to add a new definition to the platform database. You can add a new target to the platform database by adding entry mapping from your platform's four-digit hexadecimal identifier to the name of the board to the `DEFAULT_PLATFORM_DB` variable in [`mbed_lstools/platform_database.py`](https://github.com/ARMmbed/mbed-ls/blob/master/mbed_lstools/platform_database.py).

You may also need to add a new vendor string for detection on windows. If you need to add a new vendor string, add it to the `usb_vendor_list` member of the `MbedLsToolsBase` class in [`mbed_lstools/lstools_base.py`](https://github.com/ARMmbed/mbed-ls/blob/master/mbed_lstools/lstools_base.py).
