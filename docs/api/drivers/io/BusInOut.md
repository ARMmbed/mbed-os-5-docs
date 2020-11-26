# BusInOut

<span class="images">![](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/classmbed_1_1_bus_in_out.png)<span>BusInOut class hierarchy</span></span>

Use the BusInOut interface as a bidirectional bus that supports up to 16 [DigitalInOut](digitalinout.html) pins that you can read and write as one value.

You can create a BusInOut object from any microcontroller pins that are capable of performing digital input and output functions. There is no restriction on the port or bus that the pins are physically connected to.

**Tip:**

The order of pins in the constructor is the reverse order of the pins in the byte order. If you have `BusInOut(a,b,c,d,e,f,g,h)`, then the order of bits in the byte is `hgfedcba` with `a` being bit 0, `b` being bit 1, `c` being bit 2 and so on.

## BusInOut class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/classmbed_1_1_bus_in_out.html)

## BusInOut hello, world

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-BusInOut_ex_1/tree/v6.5)](https://github.com/ARMmbed/mbed-os-snippet-BusInOut_ex_1/blob/v6.5/main.cpp)

## Related content

- [DigitalInOut](digitalinout.html) API reference.
