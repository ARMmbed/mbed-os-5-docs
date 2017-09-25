## BusIn

With the BusIn API, you can create a number of DigitalIn pins that you can read as one value. This abstraction is useful for checking multiple inputs at once. You can use this API to write clearer code faster.

You can use any of the numbered Arm Mbed pins as a DigitalIn in the BusIn.

**Tips:**
* You can have up to 16 pins in a Bus.
* The order of pins in the constructor is the reverse order of the pins in the byte order. If you have `BusOut(a,b,c,d,e,f,g,h)` then the order of bits in the byte would be `hgfedcba` with `a` being bit 0, `b` being bit 1, `c` being bit 2 and so on.

### BusIn class reference

[![View code](https://www.mbed.com/embed/?type=library)](/docs/v5.4/mbed-os-api-doxy/classmbed_1_1_bus_in.html)

### BusIn Hello World!

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/BusIn_HelloWorld/)](https://os.mbed.com/teams/mbed_example/code/BusIn_HelloWorld/file/2ec7138ea637/main.cpp)
