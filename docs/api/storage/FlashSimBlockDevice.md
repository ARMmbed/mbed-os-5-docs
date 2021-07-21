# FlashSimBlockDevice

<span class="images">![](http://os.mbed.com/docs/v6.13/mbed-os-api-doxy/classmbed_1_1_flash_sim_block_device.png)<span>FlashSimBlockDevice class hierarchy</span></span>

The FlashSimBlockDevice class is a block device adapator, whose purpose is to simulate the behavior of a flash component if the underlying block device doesn't support such a behavior. This includes the following:

- Support the `erase` API (fills the erase unit with the predefined erase value).
- Only allow programming of erased area or ones whose content is the same as the one given by the user.
- Support the `get\_erase\_value` API, returning the predefined erase value.

The constructor requires the following:

  - _bd_           -  Block device to back the FlashSimBlockDevice.
  - _erase\_value_ -  Value given to each byte of the erase unit following an erase operation (defaults to 0xFF).

To configure this class, please see our [BlockDevice configuration documentation](../apis/data-options-and-config.html).

## FlashSimBlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/v6.13/mbed-os-api-doxy/classmbed_1_1_flash_sim_block_device.html)

## FlashSimBlockDevice example

This FlashSimBlockDevice example takes a [HeapBlockDevice](heapblockdevice.html) and turns it into a simulated flash BD.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-FlashSimBlockDevice/tree/v6.13)](https://github.com/ARMmbed/mbed-os-snippet-FlashSimBlockDevice/blob/v6.13/main.cpp)

## Related content

- [HeapBlockDevice](heapblockdevice.html) API reference.
- [BlockDevice configuration documentation](../apis/data-options-and-config.html).
