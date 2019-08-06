# BusIn

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_bus_in.png)<span>BusIn class hierarchy</span></span>

With the BusIn API, you can combine number of DigitalIn pins to read them at once. This abstraction is useful for checking multiple inputs together as single interface instead of individual pins.

You can use any of the numbered Arm Mbed pins as a DigitalIn in the BusIn.

**Tips:**
* You can have up to 16 pins in a Bus.
* The order of pins in the constructor is the reverse order of the pins in the byte order. If you have `BusIn(a,b,c,d,e,f,g,h)` then the order of bits in the byte would be `hgfedcba` with `a` being bit 0, `b` being bit 1, `c` being bit 2 and so on.

## BusIn class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_bus_in.html)

## BusIn hello, world

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/BusIn_HelloWorld/)](https://os.mbed.com/teams/mbed_example/code/BusIn_HelloWorld/file/1e81bff34109/main.cpp)
