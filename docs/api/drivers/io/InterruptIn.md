# InterruptIn

<span class="images">![](https://os.mbed.com/docs/mbed-os/v6.7/mbed-os-api-doxy/classmbed_1_1_interrupt_in.png)<span>InterruptIn class hierarchy</span></span>

Use the InterruptIn interface to trigger an event when a digital input pin changes. You can trigger interrupts on the rising edge (change from 0 to 1) or falling edge (change from 1 to 0) of signals.

## InterruptIn class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.7/mbed-os-api-doxy/classmbed_1_1_interrupt_in.html)

**Warnings:**

* No blocking code in ISR: avoid any call to wait, infinite while loop or blocking calls in general.

* No printf, malloc or new in ISR: avoid any call to bulky library functions. In particular, certain library functions (such as printf, malloc and new) are non re-entrant, and their behavior could be corrupted when called from an ISR.

* For `printfs` from interrupt context, use [Event](event.html) instead.

## Related

To read an input, see [DigitalIn](digitalin.html).

## InterruptIn hello, world

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-InterruptIn_ex_2/tree/v6.7)](https://github.com/ARMmbed/mbed-os-snippet-InterruptIn_ex_2/blob/v6.7/main.cpp)

## InterruptIn example

Try the following example to count rising edges on a pin.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-InterruptIn_ex_1/tree/v6.7)](https://github.com/ARMmbed/mbed-os-snippet-InterruptIn_ex_1/blob/v6.7/main.cpp)

## Related content

- [Event](event.html) API reference.
- [DigitalIn](digitalin.html) API reference.
