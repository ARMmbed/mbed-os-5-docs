## Adding target support to mbed OS 5

Adding a new microcontroller to mbed OS depends on CMSIS-CORE and CMSIS-Pack. Please make sure that the microcontroller already has these available.

### Adding a new microcontroller and board

First fork the mbed-os repository on GitHub into your own user account. We will use the placeholder `USERNAME` to refer to your username in the following documentation, `MCU_NAME` to refer to the new microcontroller you are adding and `BOARD_NAME` to refer to the new board you are adding. Import an mbed OS example, and add your fork of mbed-os using:

```
mbed import mbed-os-example-blinky
cd mbed-os-example-blinky\mbed-os
git checkout master
git pull
git checkout -b my-new-target
git remote add USERNAME https://github.com/USERNAME/mbed-os
git branch my-new-target -u USERNAME
cd ..
```

#### Target description

Add the target description to ```mbed-os\targets\targets.json```:

``` json
"MCU_NAME": {
    "inherits": ["Target"],
    "core": "Cortex-M3",
    "supported_toolchains": ["ARM", "GCC_ARM", "IAR"],
    "device_has": ["SERIAL", "STDIO_MESSAGES"]
},
"BOARD_NAME": {
    "inherits": ["MCU_NAME"],
    "macros_add": []
}
```

See the [mbed Target Documentation](mbed_targets.md) for more details on what this definition means.

#### Coding requirements

Please see the contributing guide's section on [contributing code](../cont/code_style.md) for style and ABI requirements.

#### Bootstrap code

You need CMSIS-CORE files for startup and peripheral memory addresses, and you need linker scripts for ARM, IAR and GCC toolchains. These files are usually in the ```mbed-os\targets\TARGET_VENDOR\TARGET_MCU_FAMILY\TARGET_MCUNAME\device``` directory.

mbed OS requires dynamic vector relocation, which requires extensions to CMSIS-CORE. Extend CMSIS-CORE by adding an `mbed-os\targets\TARGET_VENDOR\TARGET_MCUNAME\cmsis.h` file. This header file defines the vector relocation additions and device-specific headers that include CMSIS-CORE. Next add a relocation function in `mbed-os\targets\TARGET_VENDOR\TARGET_MCUNAME\cmsis_nvic.c and .h`. This relocation function changes the contents of the Interrupt Vector Table at run time.

CMSIS-RTOS needs a few macros to initialize the SYS_TICK. These macros are usually configured in`mbed-os\targets\TARGET_VENDOR\mbed-rtx.h`.

Now verify that your target compiles by using `mbed compile -m MCU_NAME -t <toolchain>`.

The next step to port a target is to enable the test harness dependencies. To run the test suite, your target must support GPIO, microsecond ticker and serial.

#### GPIO

Implement the api declared in `mbed-os/hal/gpio_api.h`. You must define the struct `gpio_t`. This struct is commonly defined in an `objects.h` file within the `mbed-os/targets/TARGET_VENDOR/`, `mbed-os/targets/TARGET_VENDOR/TARGET_MCU_FAMILY` or `mbed-os/targets/TARGET_VENDOR/TARGET_MCU_FAMILY/TARGET_MCUNAME` directories.

#### Microsecond ticker

The microsecond ticker is a system resource that many APIs use. The microsecond ticker needs a one microsecond resolution and uses a free-running hardware counter or timer with match register. Implement the api declared in `mbed-os\hal\us_ticker_api.h`.

At this point, we should be able to compile a handful of tests:

``mbed test -m BOARD_NAME --compile -t <toolchain>``

To execute the tests, you need to support [mbed-ls](https://github.com/armmbed/mbed-ls).

#### Serial

Implement the API declared in `mbed-os/hal/serial_api.h`. You must define the `serial_t` struct in `objects.h`. You may use the `serial_t` struct for referencing memory-mapped serial registers and passing related pin and peripheral operation information data that the HAL needs.

#### All the others

There are many more APIs to implement. You enable the following APIs by adding a `device_has` attribute to the MCU_NAME target definition in `targets.json` and providing an implementation of the API declared in the API header.

device_has       |   API header
-----------------|------------------
ANALOGIN         |   analog_in.h
ANALOGOUT        |   analog_out.h
CAN              |   can_api.h
EMAC             |   emac_api.h
INTERRUPTIN      |   gpio_irq_api.h
I2C I2CSLAVE     |   i2c_api.h
LOWPOWERTIMER    |   lp_ticker_api.h
PORT_IN PORT_OUT |   port_api.h
PWMOUT           |   pwmout_api.h
RTC              |   rtc_api.h
SLEEP            |   sleep_api.h
SPI SPISLAVE     |   spi_api.h
TRNG             |   trng_api.h
FLASH            |   flash_api.h
