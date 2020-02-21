# LowPowerTicker

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_low_power_ticker.png)<span>LowPowerTicker class hierarchy</span></span>

The LowPowerTicker class has the same methods as the Ticker class but operates in deep sleep mode and has less resolution. Use the LowPowerTicker interface to set up a recurring interrupt when you only need millisecond accuracy; it calls a function repeatedly and at a specified rate. Because the LowPowerTicker class can operate in deep sleep mode, it does not block deep sleep when active.

You can create any number of LowPowerTicker objects, allowing multiple outstanding interrupts at the same time. The function can be a static function, a member function of a particular object or a Callback object.

## Warnings and notes

- No blocking code in ISR: avoid any calls to wait, infinite while loops or blocking calls in general.

- No printf, malloc or new in ISR: avoid any calls to bulky library functions. In particular, certain library functions (such as printf, malloc and new) are not re-entrant, and their behavior could be corrupted when called from an ISR.

## LowPowerTicker class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_low_power_ticker.html)

## LowPowerTicker example

Try this program to set up a LowPowerTicker to repeatedly invert an LED:

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/LowPowerTicker_HelloWorld/)](https://os.mbed.com/teams/mbed_example/code/LowPowerTicker_HelloWorld/file/3ef1e3fe0d3b/main.cpp)

## Related content

- [Office Hours video about low power, tickless and sleep](https://www.youtube.com/watch?v=OFfOlBaegdg).
