# Timeout

<span class="images">![](https://os.mbed.com/docs/mbed-os/v6.7/mbed-os-api-doxy/classmbed_1_1_timeout.png)<span>Timeout class hierarchy</span></span>

Use the Timeout interface to set up an interrupt to call a function after a specified delay.

You can create any number of Timeout objects, allowing multiple outstanding interrupts at the same time.

## Warnings and notes

* No blocking code in ISR: avoid any call to wait, infinite while loop or blocking calls in general.

* No printf, malloc or new in ISR: Avoid any call to bulky library functions. In particular, certain library functions (such as printf, malloc and new) are not re-entrant, and their behavior could be corrupted when called from an ISR.

* While a Timeout is running, deep sleep is blocked to maintain accurate timing. If you don't need microsecond precision, consider using the LowPowerTimeout class instead because this does not block deep sleep mode.

## Timeout class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.7/mbed-os-api-doxy/classmbed_1_1_timeout.html)

## Timeout hello, world

Set up a Timeout to invert an LED after a given timeout:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Timeout_HelloWorld/tree/v6.7)](https://github.com/ARMmbed/mbed-os-snippet-Timeout_HelloWorld/blob/v6.7/main.cpp)

## Timeout example

Try this example to attach a member function:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Timeout_Example/tree/v6.7)](https://github.com/ARMmbed/mbed-os-snippet-Timeout_Example/blob/v6.7/main.cpp)
