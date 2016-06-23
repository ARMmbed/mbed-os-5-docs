# AnalogIn

The AnalogIn API is used to read an external voltage applied to an analog input pin. Only certain pins are capable of making these measurement so check the documentation for compatible pins. For more information on what it takes to convert an analog signal to its digital representation see [http://en.wikipedia.org/wiki/Analog-to-digital_converter](http://en.wikipedia.org/wiki/Analog-to-digital_converter).   

## API

[![View code](https://www.mbed.com/embed/?type=library)](https://developer.mbed.org/users/mbed_official/code/mbed/docs/tip/classmbed_1_1AnalogIn.html) 

## Hello World!

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed/code/AnalogIn-HelloWorld/)](https://developer.mbed.org/teams/mbed/code/AnalogIn-HelloWorld/file/tip/main.cpp) 


## Examples

```
#include "mbed.h"

AnalogIn position(A0);
PwmOut servo(D3);

int main() {
    // servo requires a 20ms period    
    servo.period(0.020f);
    while (1) {
        // servo position determined by a pulse width between 1-2ms
        servo.pulsewidth(0.001f + 0.001f * position);
    }
}
```   


```
#include "mbed.h"

AnalogIn input(A0);

int main() {
    uint16_t samples[1024];

    for(int i=0; i<1024; i++) {
        samples[i] = input.read_u16();
        wait(0.001f);
    }

    printf("Results:\n");
    for(int i=0; i<1024; i++) {
        printf("%d, 0x%04X\n", i, samples[i]);
    }
}   
```   


```
#include "mbed.h"

AnalogIn ain(A0);
DigitalOut led1(LED1);
DigitalOut led2(LED2);
DigitalOut led3(LED3);
DigitalOut led4(LED4);

int main() {
    while (1){
        led1 = (ain > 0.2f) ? 1 : 0;
        led2 = (ain > 0.4f) ? 1 : 0;
        led3 = (ain > 0.6f) ? 1 : 0;
        led4 = (ain > 0.8f) ? 1 : 0;
    }
}
```
