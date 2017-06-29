### PortIn

Use the PortIn interface to read an underlying GPIO port as one value. This is much faster than [BusIn](BusIn.md) because you can read a port in one go, but it is much less flexible because you are constrained by the port and bit layout of the underlying GPIO ports.

A mask can be supplied so only certain bits of a port are used, allowing other bits to be used for other interfaces.

#### API

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/PortIn_8h_source.html)

#### Hello World!

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/users/mbed_official/code/PortIn_HelloWorld/)](https://developer.mbed.org/users/mbed_official/code/PortIn_HelloWorld/file/92064442fd12/main.cpp)
