## PortOut

Use the PortOut interface to define which pins of a hardware GPIO port are set as an output and to write those pins. The port name is device specific and defined in the device's `PortNames.h` file in the `mbed-os/targets` folder.

A bit mask defines which pins of the GPIO port are set as an output (`1b` = include, `0b` = ignore). The default mask value is `0xFFFFFFFF` which sets all pins as an output.

The pins associated with a GPIO port are defined in the device-specific `PinNames.h` and the respective datasheet or reference manual.

Notes:

- Pins from different GPIO ports can be combined using the [BusOut](busout.html) interface.
- Use [PortIn](portin.html) to define which GPIO pins are to be used as digital output.

### PortOut class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_port_out.html)

### PortOut hello, world

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/PortOut_HelloWorld/)](https://os.mbed.com/teams/mbed_example/code/PortOut_HelloWorld/file/e4e6fab14d21/main.cpp)

### Related content

- [BusOut](busout.html) API reference.
- [PortIn](portin.html) API reference.
