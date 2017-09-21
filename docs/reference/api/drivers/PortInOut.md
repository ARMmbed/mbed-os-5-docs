### PortInOut

Use the PortInOut interface to read and write an underlying GPIO port as one value. This is much faster than [BusInOut](/docs/v5.4/reference/api-references.html#businout) because you can write a port all at once, but it is much less flexible because you are constrained by the port and bit layout of the underlying GPIO ports.

A mask can be supplied so you only use certain parts of a port, allowing other bits to be used for other interfaces.

#### PortInOut class reference

[![View code](https://www.mbed.com/embed/?type=library)](/docs/v5.4/mbed-os-api-doxy/classmbed_1_1_port_in_out.html)

#### PortInOut Hello World!

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/users/mbed_official/code/PortInOut_HelloWorld/)](https://developer.mbed.org/users/mbed_official/code/PortInOut_HelloWorld/file/018ca8a43b33/main.cpp)
