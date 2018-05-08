## BufferedBlockDevice

<span class="images">![](https://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_slicing_block_device.png)<span>BufferedBlockDevice class hierarchy</span></span>

The BufferedBlockDevice class is a block device adpator, whose purpose is to reduce the read and program sizes of the underlying block device to 1. Large read and/or program sizes may make life difficult for block device users, so BufferedBlockDevice reduces both sizes to the minimum, where reads and writes to the underlying BD use an internal buffer. Calling the `sync` API ensures writes are flushed to the underlying BD.    

The constructor only requires the underlying block device pointer. 

  - _bd_ -  Block device to back the BufferedBlockDevice.

### BufferedBlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_slicing_block_device.html)

### BufferedBlockDevice example

This BufferedBlockDevice example takes a [HeapBlockDevice](/docs/development/reference/heapblockdevice.html), whose read size is 256 bytes and program size is 512 bytes, and shows how one can read or program this block device with much smaller read/program sizes, using BufferedBlockDevice.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/BufferedBlockDevice_ex_1/)](https://os.mbed.com/teams/mbed_example/code/BufferedBlockDevice_ex_1/file/62c01cd06ff7/main.cpp)

### Related content

- [BufferedBlockDevice](/docs/development/reference/bufferedblockdevice.html) API reference.
