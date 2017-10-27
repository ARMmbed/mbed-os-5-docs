## PortOut

Use the PortOut interface to write to an underlying GPIO port as one value. This is much faster than [BusOut](/docs/v5.6/reference/busout.html) because you can write a port in one go, but it is much less flexible because you are constrained by the port and bit layout of the underlying GPIO ports.

A mask can be supplied so only certain bits of a port are used, allowing other bits to be used for other interfaces.

### PortOut class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/classmbed_1_1_port_out.html)

### PortOut hello, world

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/PortOut_HelloWorld/)](https://os.mbed.com/teams/mbed_example/code/PortOut_HelloWorld/file/e4e6fab14d21/main.cpp)
