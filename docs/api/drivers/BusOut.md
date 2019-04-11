# BusOut

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_bus_out.png)<span>BusOut class hierarchy</span></span>

Use the BusOut interface to combine a number of [DigitalOut](digitalout.html) pins to write them at once. This API is useful for writing to multiple pins together as single interface instead of individual pins.

You can use any of the numbered Arm Mbed pins as a DigitalOut in the BusOut.

**Tips:**

- You can have up to 16 pins in a Bus.
- The order of pins in the constructor is the reverse order of the pins in the byte order. So if you have `BusOut(a,b,c,d,e,f,g,h)`, then the order of bits in the byte would be `hgfedcba` with `a` being bit 0, `b` being bit 1, `c` being bit 2 and so on.

## BusOut class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_bus_out.html)

## BusOut hello, world

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/BusOut_HelloWorld/)](https://os.mbed.com/teams/mbed_example/code/BusOut_HelloWorld/file/b07a5ecb7618/main.cpp)

## Related content

- [DigitalOut](digitalout.html) API reference.
