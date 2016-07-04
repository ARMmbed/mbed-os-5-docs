# PwmOut

The PwmOut interface is used to control the frequency and mark-space ratio of a digital pulse train.

## Hello World!

This code example uses the default period of 0.020s and ramps the duty cycle from 0% to 100% in incriments of 10%. 

** MISSING ** 

## API

API summary

[![View code](https://www.mbed.com/embed/?type=library)](https://developer.mbed.org/users/mbed_official/code/mbed/docs/tip/classmbed_1_1PwmOut.html) 

## Details

The default period is 0.020s, and the default pulsewidth is 0.

The PwmOut interface can express the pulse train in many ways depening on how it is to be used. The period and pulse width can be expressed directly in units of seconds, millisecond or microseconds. The pulsewidth can also be expressed as a percentage of the the period.

## Implementation details

### LPC1768

You can also specify the LED1-LED4 as PwmOut. Note that these are just different pinout options for the same underlying PWM hardware, so they are just alternative routing rather than extra PWM channels. So you can pin them out can't be used at the same time:

PWM H/W Channel | Pinout Options   
---|---  
PWM_1 | P2_0/p26 or P1_18/LED1   
PWM_2 | P2_1/p25 or P1_20/LED2   
PWM_3 | P2_2/p24 or P1_21/LED3   
PWM_4 | P2_3/p23 or P1_23/LED4   
PWM_5 | P2_4/p22   
PWM_6 | P2_5/p21   
  
On the mbed LPC1768, the PwmOut hardware is limited to share the period value between all outputs. Therefore, if you change the period of one output, you change them all. The pulsewidth can be set independently for each output.

### LPC11U24

Pin under the same "Timer" share the same period:

Timer/Match Register | Pinout Options   
---|---  
CT16B0/MR0 | p5 (P0_9)   
CT16B0/MR1 | p6 (P0_8)   
CT16B0/MR2 | p34 (P1_15)   
CT16B1/MR0 | p36 (P0_21)   
CT16B1/MR1 | p20 (P0_22) and p14 (P1_23)   
CT32B0/MR0 | p25 (P1_24)   
CT32B0/MR1 | p26 (P1_25) and USBTX (P0_19)   
CT32B0/MR2 | p10 (P1_26)   
  
## Code Examples

This code example sets the period in seconds and the duty cycle as a percentage of the period in floating point (0 to 1 range). The effect of this code snippet will be to blink LED2 over a 4 second cycle, 50% on, for a pattern of 2 seconds on, 2 seconds off.

```
#include "mbed.h"

PwmOut led(LED2);

int main() {
    // specify period first, then everything else
    led.period(4.0f);  // 4 second period
    led.write(0.50f);  // 50% duty cycle
    while(1);          // led flashing
}
```   
The following example does the same thing. Instead of specifying the duty cycle as a relative percentage of the period it specifies it as an absolute value in seconds. In this case we have a 4 second period and a 2 second duty cycle, meaning the led will be on for 2 seconds and off for 2 seconds. 

```
#include "mbed.h"

PwmOut led(LED2);

int main() {
    // specify period first, then everything else
    led.period(4.0f);  // 4 second period
    led.pulsewidth(2); // 2 second pulse (on)
    while(1);          // led flashing
}

```

This code example is for an RC Servo. In RC Servo's you set the position based on duty cycle or pulse width of the pwm signal. This example code uses a period of 0.020s and increases the pulse width by 0.0001s on each pass. This will cause an increase of .5% of the servo's range every .25s. In effect the servo will move 2% of its range per second, meaning after 50 seconds the servo will have gone from 0% to 100% of its range. 

```

#include "mbed.h"

PwmOut servo(p21);

int main() {
    servo.period(0.020);          // servo requires a 20ms period
    while (1) {
        for(float offset=0.0; offset<0.001; offset+=0.0001) {
            servo.pulsewidth(0.001 + offset); // servo position determined by a pulsewidth between 1-2ms
            wait(0.25);
        }
    }
}
```
