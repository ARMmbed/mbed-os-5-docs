# Ticker

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_ticker.png)<span>Ticker class hierarchy</span></span>

Use the Ticker interface to set up a recurring interrupt; it calls a function repeatedly and at a specified rate.

You can create any number of Ticker objects, allowing multiple outstanding interrupts at the same time. The function can be a static function, a member function of a particular object or a Callback object.

## Warnings and notes

- No blocking code in ISR: avoid any call to wait, infinite while loop or blocking calls in general.

- No printf, malloc or new in ISR: avoid any call to bulky library functions. In particular, certain library functions (such as printf, malloc and new) are not re-entrant, and their behavior could be corrupted when called from an ISR.

- While an event is attached to a Ticker, deep sleep is blocked to maintain accurate timing. If you don't need microsecond precision, consider using the LowPowerTicker class instead because that does not block deep sleep mode.

## Ticker class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_ticker.html)

## Ticker hello, world

Try this program to set up a Ticker to repeatedly invert an LED:

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/Ticker_HelloWorld/)](https://os.mbed.com/teams/mbed_example/code/Ticker_HelloWorld/file/1b2dcb20aad0/main.cpp)

## Ticker examples

Use this example to attach a member function to a ticker:

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/Ticker_Example/)](https://os.mbed.com/teams/mbed_example/code/Ticker_Example/file/982ebb531653/main.cpp)

## Related content

- [Application flow control tutorial](../tutorials/application-flow-control.html).
- [Office Hours video about low power, tickless and sleep](https://youtu.be/OFfOlBaegdg?t=669).
