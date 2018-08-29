## Bootloader

Arm Mbed OS allows you to update your firmware. Our Pelion Device Management platform enables this capability. The following documentation includes instructions and examples on how to update firmware on a new target.

### Dependencies

The target needs to support the Flash HAL API. You can find the guide to porting the Flash API in the [Mbed OS porting guide](flash.html).

### Porting the bootloader

You can learn to port the update client bootloader to new targets in [the porting guide](https://cloud.mbed.com/docs/current/porting/porting-the-update-client.html).

An example walkthrough of porting the bootloader to the K64F platform can be found [here](https://cloud.mbed.com/docs/current/porting/update-k64f-port.html).

### Creating and using a new bootloader

You can learn to create and use a new bootloader in our [tutorials](/docs/development/tutorials/bootloader.html).
