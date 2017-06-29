### PortInOut

Use the PortInOut interface to read and write an underlying GPIO port as one value. This is much faster than [BusInOut](BusInOut.md) because you can write a port in one go, but it is much less flexible because you are constrained by the port and bit layout of the underlying GPIO ports.

A mask can be supplied so only certain bits of a port are used, allowing other bits to be used for other interfaces.

#### API

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/PortInOut_8h_source.html)

#### Hello World!

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/users/mbed_official/code/PortInOut_HelloWorld/)](https://developer.mbed.org/users/mbed_official/code/PortInOut_HelloWorld/file/018ca8a43b33/main.cpp)
