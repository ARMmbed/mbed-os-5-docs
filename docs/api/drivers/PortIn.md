# PortIn

Use the PortIn interface to define which pins of a hardware GPIO port are set as an input and to read the value of those pins. The port name is device specific and defined in the device's `PortNames.h` file in the `mbed-os/targets` folder.

A bit mask defines which pins of the GPIO port are set as an input (`1b` = include, `0b` = ignore). The default mask value is `0xFFFFFFFF`, which sets all pins as an input.

The device-specific `PinNames.h` and the respective datasheet or reference manual define the pins associated with a GPIO port.

<span class="notes">**Note:** You can combine pins from different GPIO ports using the [BusIn](busin.html) interface. Use [PortOut](portout.html) to define which GPIO pins are to be used as digital output.</span>

## PortIn class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_port_in.html)

## PortIn hello, world

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/users/mbed_official/code/PortIn_HelloWorld/)](https://os.mbed.com/teams/mbed_example/code/PortIn_HelloWorld/file/e78266d48649/main.cpp)

## Related content

- [BusIn](busin.html) API reference.
- [PortOut](portout.html) API reference.
