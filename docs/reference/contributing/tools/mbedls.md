## Mbed-ls

Mbed-ls is a Python module that detects and lists Mbed Enabled boards connected to a computer through USB.

### Defined behavior

Mbed-ls needs the following information to correctly detect an Mbed Enabled board:

 - A four-digit hexadecimal identifier of a board class.
 - A vendor string for detection on Windows.

Further, Mbed-ls only detects devices that meet the following criteria:

 - Devices have a mass storage device (MSD) endpoint.
 - The MSD endpoint has a FAT file system.

### Implementation

When adding a board to Mbed-ls, you typically need to add a new definition to the platform database. Before you add your board to the Mbed-ls platform database, you need the Unique product code, a four-digit hexadecimal identifier, you obtained through the mbed enabled program. You can add a new board to the platform database by adding an entry mapping from your board's unique product code to the name of the board into the `DEFAULT_PLATFORM_DB` dictionary in [`mbed_lstools/platform_database.py`](https://github.com/ARMmbed/mbed-ls/blob/master/mbed_lstools/platform_database.py).

If your board uses an interface firmware other than J-Link, STLink, DAPLink or OpenSDA, you need to add a new vendor string for detection on windows. If you need to add a new vendor string, add it to the `usb_vendor_list` member of the `MbedLsToolsBase` class in [`mbed_lstools/lstools_base.py`](https://github.com/ARMmbed/mbed-ls/blob/master/mbed_lstools/lstools_base.py).
