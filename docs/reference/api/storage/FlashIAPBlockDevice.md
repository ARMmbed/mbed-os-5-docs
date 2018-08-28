## FlashIAPBlockDevice

The flash IAP block device is a block device driver built on top of the FlashIAP API.

## Warning

Improper use of this block device could kill your board's flash.

Only use this driver on platforms where the FlashIAP implementation uses external flash or in conjunction with a file system with wear leveling, that can operate on a page size granularity.

Additional concerns:

The FlashIAP may freeze code execution for a long period of time while writing to flash. Not even high-priority IRQs are allowed to run, which may interrupt background processes.

## FlashIAPBlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](<Should be added after doxygen run>)
