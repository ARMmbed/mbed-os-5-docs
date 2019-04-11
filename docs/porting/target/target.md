<h1 id="target-port">Targets</h1>

Adding a new microcontroller to Arm Mbed OS 5 depends on CMSIS-CORE and CMSIS-Pack. Please make sure that the microcontroller already has these available.

## Adding a new microcontroller and board

First fork the `mbed-os` repository on GitHub into your own user account. We will use the placeholder `USERNAME` to refer to your username in the following documentation, `MCU_NAME` to refer to the new microcontroller you are adding and `BOARD_NAME` to refer to the new board you are adding. Import an Mbed OS example, and add your fork of `mbed-os` using:

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

## Target description

Add the target description to `mbed-os\targets\targets.json` using keys that the [Adding and configuring targets section](../reference/adding-and-configuring-targets.html) describes. We recommend that you run the [targets lint script](../reference/adding-and-configuring-targets.html#style-guide) on your target hierarchy before submitting your pull request:

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

## HAL porting

There are many more APIs to implement. You enable the following APIs by adding a `device_has` attribute to the MCU_NAME target definition in `targets.json` and providing an implementation of the API declared in the API header.

device_has       |   API header
-----------------|------------------
ANALOGIN         |   analog_in.h
ANALOGOUT        |   analog_out.h
CAN              |   can_api.h
EMAC             |   emac_api.h
INTERRUPTIN      |   gpio_irq_api.h
I2C I2CSLAVE     |   i2c_api.h
LPTICKER         |   lp_ticker_api.h
LPTICKER         |   lp_ticker_api.h
MPU              |   mpu_api.h
PORT_IN PORT_OUT |   port_api.h
PWMOUT           |   pwmout_api.h
RTC              |   rtc_api.h
SLEEP            |   sleep_api.h
SPI SPISLAVE     |   spi_api.h
QSPI             |   qspi_api.h
TRNG             |   trng_api.h
FLASH            |   flash_api.h

## PinMap

All HAL APIs that use pins have functions to get the corresponding pin maps. These functions return a `PinMap` array with each entry containing a pin name, a peripheral and a function. The presence of an NC pin indicates the end of the pin map array. Below is an example implementation of the function to get the serial transmit pin map:

```C NOCI
const PinMap PinMap_UART_TX[] = {
    {P0_19, UART_0, 1},
    {P1_13, UART_0, 3},
    {P1_27, UART_0, 2},
    { NC  , NC    , 0}
};

const PinMap *serial_tx_pinmap()
{
    return PinMap_UART_TX;
}
```

Targets that don't use a pinmap, such as ones with peripherals that can connect to any pin, must still define pin maps because testing requires them. For these devices, the pin map does not need to be comprehensive. Instead, it should list a representative sample of pins and peripherals, so they can be tested appropriately.

## Testing

The Mbed OS HAL provides a set of conformance tests for the Mbed OS HAL APIs. You can use these tests to validate the correctness of your implementation. To run the all of the Mbed OS HAL API tests, use the following command:

```
mbed test -t <toolchain> -m <target> -n mbed-os-tests-mbed_hal*
```
