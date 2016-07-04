# PortOut

The PortInOut interface is used to read and write an underlying GPIO port as one value. This is much faster than [BusInOut](BusInOut) as you can write a port in one go, but much less flexible as you are constrained by the port and bit layout of the underlying GPIO ports.

A mask can be supplied so only certain bits of a port are used, allowing other bits to be used for other interfaces. 

## Hello World!

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/users/mbed_official/code/PortInOut_HelloWorld/)](https://developer.mbed.org/users/mbed_official/code/PortInOut_HelloWorld/file/018ca8a43b33/main.cpp) 

## API

[![View code](https://www.mbed.com/embed/?type=library)](https://developer.mbed.org/users/mbed_official/code/mbed/docs/0954ebd79f59/classmbed_1_1PortInOut.html) 

## Interface

The PortInOut Interface can use any pins with a blue label, as long as they are in the same port.

<span class="images">![](../Images/pin_out.png)</span>
