#### BusOut

Use the BusOut interface to create a number of [DigitalOut](DigitalOut.md) pins that you can write as one value.This abstraction is useful for writing multiple outputs in a single pass. In general this abstraction can be used to make code less cluttered, clearer, and take less time to write. 

You can use any of the numbered Arm Mbed pins as a DigitalOut in the BusOut.

**Tips:**
* You can have up to 16 pins in a Bus. 
* The order of pins in the constructor is the reverse order of the pins in the byte order. So if you have BusOut(a,b,c,d) then the order of bits in the nibble would be `dcba` with `a` being bit 0, `b` being bit 1, `c` being bit 2 and so on.


##### API

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classmbed_1_1BusOut.html)

##### Hello World!

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/BusOut_HelloWorld/)](https://developer.mbed.org/teams/mbed_example/code/BusOut_HelloWorld/file/6337070122f8/main.cpp)
