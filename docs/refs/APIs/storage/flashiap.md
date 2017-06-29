### Flash IAP

The flash in application programming provides an interface for access to MCU internal flash memory.

Flash IAP devices have different sized blocks for different operations. They allow you to read and program in defined-sized pages, but you must erase them in defined-sized sectors. The sector size must be a multiple of the page size. Sector sizes can differ within a device.

Flash IAP provides the following functionality:

- Read from a flash device.
- Program data to flash device pages.
- Erase flash device sectors.
- Get sector/flash or page sizes.
- Get the start address of the flash device.

Flash devices have some requirements and limitations based on the operation. Please read the documentation for each operation.

Be aware that Flash IAP might disable interrupts for a long time. This can affect the application latency.

This class is thread-safe.

#### API

View the full C++ API:

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/FlashIAP_8h_source.html)

#### Example

For an example that uses the `FlashIAP` driver, please see the [bootloader example](https://github.com/ARMmbed/mbed-os-example-bootloader).
