#### BusInOut

BusInOut is an abstraction that takes up to 16 [DigitalInOut](DigitalInOut.md) pins and makes them appear as though they are linearly memory mapped for ease of use. This abstraction is useful for reading or writing multiple pins at the same time. In general this abstraction can be used to make code less cluttered, clearer, and take less time to write. 

You can use any of the numbered Arm Mbed pins as a [DigitalInOut](DigitalInOut.md).

**Tips:**
* You can have up to 16 pins in a Bus. 
* The order of pins in the constructor is the reverse order of the pins in the byte order. So if you have BusInOut(a,b,c,d) then the order of bits in the nibble would be `dcba` with `a` being bit 0, `b` being bit 1, `c` being bit 2 and so on.

##### API

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classmbed_1_1BusInOut.html)

##### Hello World!

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/BusInOut_HelloWorld/)](https://developer.mbed.org/teams/mbed_example/code/BusInOut_HelloWorld/file/68629c6c4970/main.cpp)
