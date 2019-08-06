# FlashSimBlockDevice

<span class="images">![](http://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_flash_sim_block_device.png)<span>FlashSimBlockDevice class hierarchy</span></span>

The FlashSimBlockDevice class is a block device adapator, whose purpose is to simulate the behavior of a flash component if the underlying block device doesn't support such a behavior. This includes the following:

- Support the `erase` API (fills the erase unit with the predefined erase value).
- Only allow programming of erased area or ones whose content is the same as the one given by the user.
- Support the `get\_erase\_value` API, returning the predefined erase value.

The constructor requires the following:

  - _bd_           -  Block device to back the FlashSimBlockDevice.
  - _erase\_value_ -  Value given to each byte of the erase unit following an erase operation (defaults to 0xFF).

To configure this class, please see our [BlockDevice configuration documentation](../reference/storage.html#blockdevice-default-configuration).

## FlashSimBlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_flash_sim_block_device.html)

## FlashSimBlockDevice example

This FlashSimBlockDevice example takes a [HeapBlockDevice](heapblockdevice.html) and turns it into a simulated flash BD.

```C++ TODO
    int erase_unit_size = 512;
    HeapBlockDevice heap_bd(4 * erase_unit_size, 1, 4, erase_unit_size);
    FlashSimBlockDevice flash_bd(&heap_bd, blank);

    // This initializes the flash simulator block device (as well as the underlying heap block device)
    int err = flash_bd.init();

    uint8_t buf[16];
    for (int i = 0; i < sizeof(buf); i++) {
        buf[i] = i;
    }

    // This will fail, as erase unit in address 0 has not been erased
    err = flash_bd.program(buf, 0, sizeof(buf));

    // Erase the erase unit at address 0
    err = flash_bd.erase(0, erase_unit_size);

    // This will succeed now after erasing
    err = flash_bd.program(buf, 0, sizeof(buf));
```

## Related content

- [HeapBlockDevice](heapblockdevice.html) API reference.
- [BlockDevice configuration documentation](../reference/storage.html#blockdevice-default-configuration).
