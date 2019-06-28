# GPIO

Implement the api declared in `mbed-os/hal/gpio_api.h`. You must define the struct `gpio_t`. This struct is commonly defined in an `objects.h` file within the `mbed-os/targets/TARGET_VENDOR/`, `mbed-os/targets/TARGET_VENDOR/TARGET_MCU_FAMILY` or `mbed-os/targets/TARGET_VENDOR/TARGET_MCU_FAMILY/TARGET_MCUNAME` directories.

You should define the Physical LEDs and switches in the target's `PinNames.h` file. LED and switch names begin incrementing at 1 and follow the convention `LED1...LEDn` and `BUTTON1...BUTTONn`. You can see an [example](https://github.com/ARMmbed/mbed-os/blob/master/targets/TARGET_Freescale/TARGET_MCUXpresso_MCUS/TARGET_MCU_K64F/TARGET_FRDM/PinNames.h#L198) for more information.
