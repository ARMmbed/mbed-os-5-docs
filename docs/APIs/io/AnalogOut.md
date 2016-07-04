# AnalogOut

The AnalogOut Interface is used to set the voltage of an analog output pin. The AnalogOut Interface can be used to set a voltage on pin somewhere in the range of VSS to VCC. Not all pins are capable of being AnalogOut so check the documentation. For more information on what it takes to convert an digital value to its analog representation see [http://en.wikipedia.org/wiki/Digital-to-analog_converter](http://en.wikipedia.org/wiki/Digital-to-analog_converter).   

## API

[![View code](https://www.mbed.com/embed/?type=library)](https://developer.mbed.org/users/mbed_official/code/mbed/docs/tip/classmbed_1_1AnalogOut.html) 

## Hello World!

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed/code/AnalogOut-HelloWorld/)](https://developer.mbed.org/teams/mbed/code/AnalogOut-HelloWorld/file/tip/main.cpp) 


## Example

```
#include "mbed.h"

// The sinewave is created on this pin
AnalogOut aout(p18);

int main()
{
    const double pi = 3.141592653589793238462;
    const double amplitude = 0.5f;
    const double offset = 65535/2;
    double rads = 0.0;
    uint16_t sample = 0;
    
    while(1) {
        // sinewave output
        for (int i = 0; i < 360; i++) {
            rads = (pi * i) / 180.0f;
            sample = (uint16_t)(amplitude * (offset * (cos(rads + pi))) + offset);
            aout.write_u16(sample);
        }
    }
}
 
```   
