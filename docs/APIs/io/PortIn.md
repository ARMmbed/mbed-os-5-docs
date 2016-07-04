# PortIn

The PortIn interface is used to read an underlying GPIO port as one value. This is much faster than [BusIn](BusIn) as you can read a port in one go, but much less flexible as you are constrained by the port and bit layout of the underlying GPIO ports.

A mask can be supplied so only certain bits of a port are used, allowing other bits to be used for other interfaces. 

## Hello World!

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/users/mbed_official/code/PortIn_HelloWorld/)](https://developer.mbed.org/users/mbed_official/code/PortIn_HelloWorld/file/92064442fd12/main.cpp) 

## API

[![View code](https://www.mbed.com/embed/?type=library)](https://developer.mbed.org/users/mbed_official/code/mbed/docs/tip/classmbed_1_1PortIn.html) 

## Interface

The PortIn Interface can use any pin with a blue label, as long as all the pins used are in the same GPIO port

<span class="images">![](../Images/pin_out.png)</span>
