# BufferedBlockDevice

<span class="images">![](http://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_buffered_block_device.png)<span>BufferedBlockDevice class hierarchy</span></span>

The BufferedBlockDevice class is a block device adpator, whose purpose is to reduce the read and program sizes of the underlying block device to 1. Large read and/or program sizes may make life difficult for block device users, so BufferedBlockDevice reduces both sizes to the minimum, where reads and writes to the underlying BD use an internal buffer. Calling the `sync` API ensures writes are flushed to the underlying BD.

The constructor only requires the underlying block device pointer.

  - _bd_ -  Block device to back the BufferedBlockDevice.

To configure this class, please see our [BlockDevice configuration documentation](../reference/storage.html#blockdevice-default-configuration).

## BufferedBlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_buffered_block_device.html)

## BufferedBlockDevice example

This BufferedBlockDevice example takes a [HeapBlockDevice](heapblockdevice.html), whose read size is 256 bytes and program size is 512 bytes, and shows how one can read or program this block device with much smaller read/program sizes, using BufferedBlockDevice.

```C++ TODO

    HeapBlockDevice heap_bd(1024, 256, 512, 512);
    BufferedBlockDevice buf_bd(&heap_bd);

    // This initializes the buffered block device (as well as the underlying heap block device)
    int err = buf_bd.init();

    uint8_t buf[8];
    for (int i = 0; i < sizeof(buf); i++) {
         buf[i] = i;
    }

    // Now we can program an 8 byte buffer (couldn't do that in underlying BD, having 512-byte program size)
    err = buf_bd.program(buf, 0, sizeof(buf));

    // Now we can also read one byte
    err = buf_bd.read(buf, 0, 1);

    // Ensure programmed data is flushed to the underlying block device
    err = buf_bd.sync();
```

## Related content

- [HeapBlockDevice](heapblockdevice.html) API reference.
- [BlockDevice configuration documentation](../reference/storage.html#blockdevice-default-configuration).
