### mbed-ls

Mbed-ls is a python module that detects and lists mbed enabled board connected to a host computer. 

### Defined Behavoir

Mbed-ls needs the following information to correctly detect an Mbed Enabled target:
 - a 4 digit hexadecimal identifier of a board class
 - a vendor string for detection on Windows
 
Further, Mbed-ls only detects devices that meet the following criteria:
 - devices have a Mass Storage Device (MSD) endpoint
 - the MSD endpoint is formatted with a fat filesystem
 
### Implementation

When adding a target to Mbed-ls, you typically need to add a new definition to the platform database. You can add a new target to the platform database by adding an entry mapping from your platform's 4 diget hexadecimal identifier to the name of the board to the `DEFAULT_PLATFORM_DB` variable in [`mbed_lstools/platform_database.py`](https://github.com/ARMmbed/mbed-ls/blob/master/mbed_lstools/platform_database.py).

You may also need to add a new vendor string for detection on windows. If you need to add a new vendor string, add it to the `usb_vendor_list` member of the `MbedLsToolsBase` class in [`mbed_lstools/lstools_base.py`](https://github.com/ARMmbed/mbed-ls/blob/master/mbed_lstools/lstools_base.py).
