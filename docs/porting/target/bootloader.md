# Bootloader

Arm Mbed OS allows you to update your device firmware, enabled by our Pelion IoT platform. One of the dependencies is a bootloader running on the device capable of updating the device firmware. The following documentation includes instructions and examples on how to update firmware on a target.

## Dependencies

The target needs to support the Flash HAL API. You can find the guide to porting the Flash API in the [Mbed OS porting guide](flash.html).

## Porting the bootloader

You can learn to port the Update Client bootloader to new targets in [the porting guide](https://cloud.mbed.com/docs/latest/porting/porting-the-device-management-update-client.html).

An example walkthrough of porting the bootloader to the K64F platform can be found [here](https://cloud.mbed.com/docs/latest/porting/update-k64f-port.html).

## Creating and using a new bootloader

You can learn to create and use a new bootloader in our [tutorials](../tutorials/bootloader.html).
