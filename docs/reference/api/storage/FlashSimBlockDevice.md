## FlashSimBlockDevice

<span class="images">![](https://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_slicing_block_device.png)<span>FlashSimBlockDevice class hierarchy</span></span>

The FlashSimBlockDevice class is a block device adpator, whose purpose is to simulate the behavior of a flash component, if the underlying block device doesn't support such a behavior. This includes the following:
- Support the `erase` API (fills the erase unit with the predefined erase value).
- Only allow programming of erased areaa or ones whose content is the same as the one given by the user.
- Support the `get\_erase\_value` API, returning the predefined erase value.       

The constructor requires the following:

  - _bd_           -  Block device to back the FlashSimBlockDevice.
  - _erase\_value_ -  Value given to each byte of the erase unit following an erase operation (defaults to 0xFF).

### FlashSimBlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_slicing_block_device.html)

### FlashSimBlockDevice example

This FlashSimBlockDevice example takes a [HeapBlockDevice](/docs/development/reference/heapblockdevice.html) and turns it into a simulated flash BD, showing all basic flash operations. 

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/FlashSimBlockDevice_ex_1/)](https://os.mbed.com/teams/mbed_example/code/FlashSimBlockDevice_ex_1/file/62c01cd06ff7/main.cpp)

### Related content

- [FlashSimBlockDevice](/docs/development/reference/FlashSimBlockDevice.html) API reference.
