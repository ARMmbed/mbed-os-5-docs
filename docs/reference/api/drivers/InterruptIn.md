## InterruptIn

Use the InterruptIn interface to trigger an event when a digital input pin changes. You can trigger interrupts on the rising edge (change from 0 to 1) or falling edge (change from 1 to 0) of signals.

### InterruptIn class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.7/mbed-os-api-doxy/classmbed_1_1_interrupt_in.html)

**Warnings:**

* No blocking code in ISR: avoid any call to wait, infinite while loop or blocking calls in general.

* No printf, malloc or new in ISR: avoid any call to bulky library functions. In particular, certain library functions (such as printf, malloc and new) are non re-entrant, and their behavior could be corrupted when called from an ISR.

* For `printfs` from interrupt context, use <a href="/docs/v5.7/reference/event.html" target="_blank">Event</a> instead.

### Related

To read an input, see <a href="/docs/v5.7/reference/digitalin.html" target="_blank">DigitalIn</a>.

### InterruptIn hello, world

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/InterruptIn_HelloWorld/)](https://os.mbed.com/teams/mbed_example/code/InterruptIn_HelloWorld/file/f729f0421740/main.cpp)

### InterruptIn example

Try the following example to count rising edges on a pin.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/InterruptIn_ex_1/)](https://os.mbed.com/teams/mbed_example/code/InterruptIn_ex_1/file/8c7b073576c5/main.cpp)

### Related content

- <a href="/docs/v5.7/reference/event.html" target="_blank">Event</a> API reference.
- <a href="/docs/v5.7/reference/digitalin.html" target="_blank">DigitalIn</a> API reference.
