# mbed OS 5.0 HAL

Target porting starts with [`targets.json`](https://github.com/mbedmicro/mbed/blob/master/hal/targets.json).

`targets.json` is a description of the targets' capabilities. It contains all the definitions that enable or disable the inclusion of a certain set of peripherals, and the features of the OS it supports:

```json
"Target": {
    "core": null,
    "default_toolchain": "ARM",
    "supported_toolchains": null,
    "extra_labels": [],
    "is_disk_virtual": false,
    "macros": [],
    "device_has": [],
    "features": [],
    "detect_code": [],
    "public": false
}
```

Each target defines a set of `extra_labels`, which are special directories prefixed with `TARGET_` and containing source code for a target's HAL implementation:

* [hal/NXP/TARGET_LPC176X](https://github.com/mbedmicro/mbed/tree/master/hal/targets/hal/TARGET_NXP/TARGET_LPC176X)

There is a small subset of functionality that is needed to bootstrap a target port:

* [pinmap.h](https://github.com/mbedmicro/mbed/blob/master/hal/hal/analogin_api.h)
* [gpio_api.h](https://github.com/mbedmicro/mbed/blob/master/hal/hal/gpio_api.h)
* [gpio_irq_api.h](https://github.com/mbedmicro/mbed/blob/master/hal/hal/gpio_irq_api.h)
* [port_api.h](https://github.com/mbedmicro/mbed/blob/master/hal/hal/port_api.h)
* [lp_ticker_api.h](https://github.com/mbedmicro/mbed/blob/master/hal/hal/lp_ticker_api.h)
* [ticker_api.h](https://github.com/mbedmicro/mbed/blob/master/hal/hal/ticker_api.h)
* [us_ticker_api.h](https://github.com/mbedmicro/mbed/blob/master/hal/hal/us_ticker_api.h)

Having this initial block in place allows you to run simple programs like the mbed ``hello world``:

```cpp
#include "mbed.h"
#include "rtos.h"

DigitalOut led1(LED1);
DigitalOut led2(LED2);

void led2_thread(void const *args) {
    while (true) {
        led2 = !led2;
        Thread::wait(1000);
    }
}

int main()
{
    Thread thread(led2_thread);
    while (true) {
        led1 = !led1;
        Thread::wait(500);
    }
}
```

For each additional API you port, you'll first have to add the identifier to the target descritpion `device_has`. These are used to conditionally compile a HAL implementation and the API that makes use of it.

This is the full list of the mbed drivers APIs that could be potentially implemented for a target:

* [pinmap.h](https://github.com/mbedmicro/mbed/blob/master/hal/hal/pinmap.h)
* [gpio_api.h](https://github.com/mbedmicro/mbed/blob/master/hal/hal/gpio_api.h)
* [gpio_irq_api.h](https://github.com/mbedmicro/mbed/blob/master/hal/hal/gpio_irq_api.h)
* [port_api.h](https://github.com/mbedmicro/mbed/blob/master/hal/hal/port_api.h)
* [lp_ticker_api.h](https://github.com/mbedmicro/mbed/blob/master/hal/hal/lp_ticker_api.h)
* [ticker_api.h](https://github.com/mbedmicro/mbed/blob/master/hal/hal/ticker_api.h)
* [us_ticker_api.h](https://github.com/mbedmicro/mbed/blob/master/hal/hal/us_ticker_api.h)
* [sleep_api.h](https://github.com/mbedmicro/mbed/blob/master/hal/hal/sleep_api.h)
* [rtc_api.h](https://github.com/mbedmicro/mbed/blob/master/hal/hal/rtc_api.h)
* [pwmout_api.h](https://github.com/mbedmicro/mbed/blob/master/hal/hal/pwmout_api.h)
* [analogin_api.h](https://github.com/mbedmicro/mbed/blob/master/hal/hal/analogin_api.h)
* [analogout_api.h](https://github.com/mbedmicro/mbed/blob/master/hal/hal/analogout_api.h)
* [i2c_api.h](https://github.com/mbedmicro/mbed/blob/master/hal/hal/i2c_api.h)
* [serial_api.h](https://github.com/mbedmicro/mbed/blob/master/hal/hal/serial_api.h)
* [spi_api.h](https://github.com/mbedmicro/mbed/blob/master/hal/hal/spi_api.h)
* [can_api.h](https://github.com/mbedmicro/mbed/blob/master/hal/hal/can_api.h)
* [dma_api.h](https://github.com/mbedmicro/mbed/blob/master/hal/hal/dma_api.h)
* [ethernet_api.h](https://github.com/mbedmicro/mbed/blob/master/hal/hal/ethernet_api.h)
