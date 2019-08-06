# InterruptIn

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_interrupt_in.png)<span>InterruptIn class hierarchy</span></span>

Use the InterruptIn interface to trigger an event when a digital input pin changes. You can trigger interrupts on the rising edge (change from 0 to 1) or falling edge (change from 1 to 0) of signals.

## InterruptIn class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_interrupt_in.html)

**Warnings:**

* No blocking code in ISR: avoid any call to wait, infinite while loop or blocking calls in general.

* No printf, malloc or new in ISR: avoid any call to bulky library functions. In particular, certain library functions (such as printf, malloc and new) are non re-entrant, and their behavior could be corrupted when called from an ISR.

* For `printfs` from interrupt context, use [Event](event.html) instead.

## Related

To read an input, see [DigitalIn](digitalin.html).

## InterruptIn hello, world

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/InterruptIn_HelloWorld/)](https://os.mbed.com/teams/mbed_example/code/InterruptIn_HelloWorld/file/de061b559d35/main.cpp)

## InterruptIn example

Try the following example to count rising edges on a pin.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/InterruptIn_ex_1/)](https://os.mbed.com/teams/mbed_example/code/InterruptIn_ex_1/file/49002ccc54b5/main.cpp)

## Related content

- [Event](event.html) API reference.
- [DigitalIn](digitalin.html) API reference.
