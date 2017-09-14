#### PwmOut

Use the PwmOut interface to control the frequency and duty cycle of a PWM signal.

**Tips:**

* Set the cycle time first, and then set the duty cycle using either a relative time period via the write() function or an absolute time period using the pulsewidth() function. 
* The default period is 0.020s, and the default pulse width is 0.

##### PwmOut class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classmbed_1_1PwmOut.html)


##### PwmOut Hello World!

This code example uses the default period of 0.020s and ramps the duty cycle from 0% to 100% in increments of 10%.

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/PwmOut_HelloWorld/)](https://developer.mbed.org/teams/mbed_example/code/PwmOut_HelloWorld/file/5160ea45399b/main.cpp)


##### PwmOut code examples

###### Example one

This code example sets the period in seconds and the duty cycle as a percentage of the period in floating point (range: 0 to 1). The effect of this code snippet will be to blink LED2 over a four-second cycle, 50% on, for a pattern of two seconds on, two seconds off.

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/PwmOut_ex_1/)](https://developer.mbed.org/teams/mbed_example/code/PwmOut_ex_1/file/07220dd760cc/main.cpp)

###### Example two

The following example does the same thing, but instead of specifying the duty cycle as a relative percentage of the period, it specifies it as an absolute value in seconds. In this case we have a four-second period and a two-second duty cycle, meaning the LED will be on for two seconds and off for two seconds.

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/PwmOut_ex_2/)](https://developer.mbed.org/teams/mbed_example/code/PwmOut_ex_2/file/248dfc85bbf9/main.cpp)

###### Example three

This code example is for an RC Servo. In RC Servos you set the position based on the PWM signal's duty cycle or pulse width. This example code uses a period of 0.020s and increases the pulse width by 0.0001s on each pass. This will cause an increase of .5% of the servo's range every .25s. In effect the servo will move 2% of its range per second, meaning after 50 seconds the servo will have gone from 0% to 100% of its range.

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/PwmOut_ex_3/)](https://developer.mbed.org/teams/mbed_example/code/PwmOut_ex_3/file/465d882e6939/main.cpp)
