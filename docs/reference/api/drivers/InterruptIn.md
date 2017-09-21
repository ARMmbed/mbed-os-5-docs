### InterruptIn

Use the InterruptIn interface to trigger an event when a [digital input pin](/docs/v5.4/reference/api-references.html#digitalin) changes. You can trigger interrupts on the rising edge (change from 0 to 1) or falling edge (change from 1 to 0) of signals.

#### InterruptIn class reference

[![View code](https://www.mbed.com/embed/?type=library)](/docs/v5.4/mbed-os-api-doxy/classmbed_1_1_interrupt_in.html)

**Warnings:**

* No blocking code in ISR: avoid any call to wait, infinite while loop or blocking calls in general.

* No printf, malloc or new in ISR: avoid any call to bulky library functions. In particular, certain library functions (such as printf, malloc and new) are non re-entrant, and their behavior could be corrupted when called from an ISR.

* For `printfs` from interrupt context, use [Events](/docs/v5.4/reference/api-references.html#events) instead.

#### Related

To read an input, see [DigitalIn](/docs/v5.4/reference/api-references.html#digitalin).

For timer-based interrupts, see [Ticker](/docs/v5.4/reference/api-references.html#ticker) (repeating interrupt) and [Timeout](/docs/v5.4/reference/api-references.html#timeout) (one-time interrupt).

#### InterruptIn Hello World!

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/InterruptIn_HelloWorld/)](https://developer.mbed.org/teams/mbed_example/code/InterruptIn_HelloWorld/file/f729f0421740/main.cpp)

#### InterruptIn example

Try the following example to count rising edges on a pin.

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/InterruptIn_ex_1/)](https://developer.mbed.org/teams/mbed_example/code/InterruptIn_ex_1/file/8c7b073576c5/main.cpp)
