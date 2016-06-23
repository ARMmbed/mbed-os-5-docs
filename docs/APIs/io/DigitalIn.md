#DigitalIn

The DigitalIn interface is used to read the value of a digital input pin.

Any of the numbered mbed pins can be used as a DigitalIn. 

## Hello World!

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/users/mbed_official/code/DigitalIn_HelloWorld_Mbed/)](https://developer.mbed.org/users/mbed_official/code/DigitalIn_HelloWorld_Mbed/file/tip/main.cpp) 

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/users/mbed_official/code/DigitalIn_HelloWorld_FRDM-KL25Z/)](https://developer.mbed.org/users/mbed_official/code/DigitalIn_HelloWorld_FRDM-KL25Z/file/tip/main.cpp) 

## API

API summary

[![View code](https://www.mbed.com/embed/?type=library)](https://developer.mbed.org/users/mbed_official/code/mbed/docs/tip/classmbed_1_1DigitalIn.html) 

## Interface

The DigitalIn Interface can be used on any pin with a blue label.

The pin input is logic '0' for any voltage on the pin below 0.8v, and '1' for any voltage above 2.0v. By default, the DigitalIn is setup with an internal pull-down resistor.

<span class="images">![](../Images/pin_out.png)</span>

## Related

To handle an interrupt, see [InterruptIn](InterruptIn.md).

Examples of logical functions:

```
#include "mbed.h"
 
DigitalIn a(p5);
DigitalIn b(p6);
DigitalOut z_not(LED1);
DigitalOut z_and(LED2);
DigitalOut z_or(LED3);
DigitalOut z_xor(LED4);
 
int main() {
    while(1) {
        z_not = !a;
        z_and = a && b;
        z_or = a || b;
        z_xor = a ^ b;
    }
}
```
