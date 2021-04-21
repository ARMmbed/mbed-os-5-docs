# BufferedBlockDevice

<span class="images">![](http://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_buffered_block_device.png)<span>BufferedBlockDevice class hierarchy</span></span>

The BufferedBlockDevice class is a block device adpator, whose purpose is to reduce the read and program sizes of the underlying block device to 1. Large read and/or program sizes may make life difficult for block device users, so BufferedBlockDevice reduces both sizes to the minimum, where reads and writes to the underlying BD use an internal buffer. Calling the `sync` API ensures writes are flushed to the underlying BD.

The constructor only requires the underlying block device pointer.

  - _bd_ -  Block device to back the BufferedBlockDevice.

To configure this class, please see our [BlockDevice configuration documentation](../apis/data-options-and-config.html).

## BufferedBlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_buffered_block_device.html)

## BufferedBlockDevice example

This BufferedBlockDevice example takes a [HeapBlockDevice](heapblockdevice.html), whose read size is 256 bytes and program size is 512 bytes, and shows how one can read or program this block device with much smaller read/program sizes, using BufferedBlockDevice.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-BufferedBlockDevice/tree/v6.10)](https://github.com/ARMmbed/mbed-os-snippet-BufferedBlockDevice/blob/v6.10/main.cpp)

## Related content

- [HeapBlockDevice](heapblockdevice.html) API reference.
- [BlockDevice configuration documentation](../apis/data-options-and-config.html).
