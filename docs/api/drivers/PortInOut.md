# PortInOut

Use the PortInOut interface to read and write an underlying GPIO port as one value. This is much faster than [BusInOut](businout.html) because you can write a port all at once, but it is much less flexible because you are constrained by the port and bit layout of the underlying GPIO ports.

A mask can be supplied so you only use certain parts of a port, allowing other bits to be used for other interfaces.

## PortInOut class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_port_in_out.html)

## PortInOut hello, world

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/users/mbed_official/code/PortInOut_HelloWorld/)](https://os.mbed.com/teams/mbed_example/code/PortInOut_HelloWorld/file/3f1944b9de6a/main.cpp)

## Related content

- [BusInOut](businout.html) API reference.
