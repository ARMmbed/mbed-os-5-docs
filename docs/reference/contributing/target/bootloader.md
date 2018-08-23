## Bootloader

To enable firmware update capability via bootloader on a new target instructions as well as an example of how to do it can be found in the mbed OS 5 handbook.

### Dependencies

The target needs to support the Flash HAL API. The guide to porting the flash api can be found [here](https://os.mbed.com/docs/latest/reference/flash.html).


### Porting the bootloader

The guide to porting the update client bootloader to new targets can be found [here](https://cloud.mbed.com/docs/current/porting/porting-the-update-client.html).

An example walkthrough of porting the bootloader to the K64F platform can be found [here](https://cloud.mbed.com/docs/current/porting/update-k64f-port.html).

### Creating and using a new bootloader

A tutorial on creating and using a new bootloader can be found [here](https://os.mbed.com/docs/latest/tutorials/bootloader.html).
