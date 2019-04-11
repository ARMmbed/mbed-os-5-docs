# PwmOut

Use the PwmOut interface to control the frequency and duty cycle of a PWM signal.

**Tips:**

* Set the cycle time first, and then set the duty cycle using either a relative time period via the write() function or an absolute time period using the pulsewidth() function.
* The default period is 0.020s, and the default pulse width is 0.

## PwmOut class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/_pwm_out_8h_source.html)


## PwmOut hello, world

This code example uses the default period of 0.020s and ramps the duty cycle from 0% to 100% in increments of 10%.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/PwmOut_HelloWorld/)](https://os.mbed.com/teams/mbed_example/code/PwmOut_HelloWorld/file/10bf740dc758/main.cpp)

## PwmOut code examples

### Example one

This code example sets the period in seconds and the duty cycle as a percentage of the period in floating point (range: 0 to 1). The effect of this code snippet will be to blink LED2 over a four-second cycle, 50% on, for a pattern of two seconds on, two seconds off.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/PwmOut_ex_1/)](https://os.mbed.com/teams/mbed_example/code/PwmOut_ex_1/file/3b6d08ebe2b0/main.cpp)

### Example two

The following example does the same thing, but instead of specifying the duty cycle as a relative percentage of the period, it specifies it as an absolute value in seconds. In this case we have a four-second period and a two-second duty cycle, meaning the LED will be on for two seconds and off for two seconds.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/PwmOut_ex_2/)](https://os.mbed.com/teams/mbed_example/code/PwmOut_ex_2/file/cab93cb2f242/main.cpp)
