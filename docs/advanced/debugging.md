# Debugging

This guide examines some techniques for generating debug information to help find and fix problems with your code, and how to deal with problems you see.

## Compile time errors

Compile time errors and warnings are caused by incorrect syntax, or misuse of variables or functions. An error will prevent the compile process from completing (and therefore no binary file will be created). A warning will not prevent the binary from being created, but you should still review the warning as it may mean that your code is not going to do what you had intended.

Common errors are: 

* Missing declarations of variables and interfaces, leading to "Identifier undefined" errors. 
* Missing semicolons ";". Semicolons are required at the end of each line. 
* Missing quotes of brackets, "",(),[] or {}. These are used in pairs to contain various types of statement. The compiler will report an error if you have not used them in correct pairings. 

Always tackle the very first error that is reported, as later errors might be as a result of the first one, and will disappear when the first one is corrected.

If you are seeing a compile time error or warning that you do not understand, Google will usually find explanations of the error message; you can also post a question to the mbed [forum](https://forums.mbed.com/).

## Run time errors

Run time errors are caused either by code that is correct but tries to do something that is invalid, or when malfunctioning hardware cannot be accessed.

The example below shows a PwmOut interface being configured on pin p20. The PwmOut interface is correctly used, and so the code compiles without warning or error. But when the code runs, it tries to create a PwmOut to pin p20. Because PwmOut is not available on pin p20, a run time error is triggered.

<span class="tips">**Tip: Siren Lights:** When a run time error is encountered, the board flashs its LEDs in a distinctive pattern to let you know that an error has occurred and that the program has stopped running.
</span>

### Example: run time error

When the program below starts running on the board it causes a run time error, leading to the siren lights:

```c++

	#include "mbed.h"

	PwmOut led(p20);
	int main() {
		while(1) {
			for(float p = 0.0f; p < 1.0f; p += 0.1f) {
				led = p;
				wait(0.1);
			}
		}
	}
```

## Run time bugs

When your code compiles and runs without error and warning, it still may not behave as you'd expect or hope. This is usually because the code you have written is correct, but not what you had intended. This is usually caused by the program flowing in a way you'd not intended because of a logical mistake or values being computed incorrectly due to an incorrect expression.

Fortunately there are some useful techniques that you can apply to help find and correct these bugs:

* Debug messages: print messages and variable values over the serial port, as [explained below](#debug-messaging).
* Flash LEDs: turn LEDs on and off in response to state changes, and to indicate where the program is, as [explained below](#debugging-program-flow-control-with-leds). More information is available [in our Bluetooth Low Energy documents](https://docs.mbed.com/docs/ble-intros/en/latest/Introduction/Debugging/#the-quick-method-leds).

### Debug messaging

The mbed libraries contain some features for reporting run time errors. You can print debug information over the USB serial port; this is generally the way to debug running applications on your board.

The main things to use are:

* ``printf()``: print a formatted message to the USB Serial Port (stdout default).
* ``error()``: print a formatted message to the USB Serial Port, then die with "Siren Lights".

For more information on using the USB Serial port, see the [Board to PC communication over USB](../getting_started/serial_communication.md) page.

### Example: serial terminal debug messages

```c

	#include "mbed.h"

	DigitalIn button(p21);
	AnalogIn pot(p20);

	int main() {
		while(pot > 0.0) {
			printf("Pot value = %f", pot.read());
			wait(0.1);
		}
		error("Loop unexpectedly terminated");
	}
```

## Debugging program flow control with LEDs and printf()

Most programs of a even a low level of sophistication will have loops, if-else and case statements, all of which make a decision based on some logic or arithmetic. If your program is not flowing as expected, you can used LEDs and print data values to determine why.

### Using the LEDs

Here's an example using LEDs to determine the flow of a program: the status of the button is echoed to LED2, so you can easily tell whether the program sees the button as pressed. LED3 is set by the if-else statement, so it is clear how the program control flow is operating:

```c

	#include "mbed.h"

	DigitalIn button(p19);
	AnalogIn pot(p20);	
	PwmOut led1(LED1);
	DigitalOut led3(LED3); // use for debug

	int main() {
		while(1) {
			if (button && (pot < 0.7)) {
				led3 = 0;
				led1 = pot;
			} else {
				led3 = 1;
				led1 = 0.0;
			}
		}
	}
```

##Debugging incorrect data values

It is often useful to see the values of variables in your program at a given time. This example is the same as the one above, except that we are are now using the serial port to print out the value of the AnalogIn. You might need to use this method if you are using a data value to determine the program flow.

```c


	#include "mbed.h"

	DigitalIn button(p19);
	AnalogIn pot(p20);
	PwmOut led1(LED1);

	int main() {
		while(1) {
			printf("Value of pot is %.3f\n", pot.read());
			wait (0.1);
			if (button && (pot < 0.7)) {
				led1 = pot;
			} else {
				led1 = 0.0;
			}
		}
	}
```

## Video tutorials 

For Windows:

<span class="images">[![Video tutorial](http://img.youtube.com/vi/jAMTXK9HjfU/0.jpg)](http://www.youtube.com/watch?v=jAMTXK9HjfU&feature=youtu.be&t=31s)</span>


For Mac:

<span class="images">[![Video tutorial](http://img.youtube.com/vi/IR8Di53AGSk/0.jpg)](http://www.youtube.com/watch?v=IR8Di53AGSk&feature=youtu.be&t=34s)</span>

## What's next

All the different techniques mentioned previously are sometimes inefficient and have strong disadvantages:

* It considerably slows down the execution and introduces delays, so if a piece of code is time dependent, it can change the original behavior of a program.

* It is very ad hoc. Code is temporarily added, to be removed as soon as the bug is solved. For the next bug, similar code is added again, then again, then again...

A better solution might be using the [CMSIS-DAP interface with Keil MDK](http://mbed.org/handbook/CMSIS-DAP-MDK), if you need full debug capabilities:

* Set breakpoints to stop the program at some event or at a specified instruction to examine the current state.

* Step by step program execution to track the control flow.

* Check variables values.

* Inspect and modify memory contents.

## Further reading

You can find out more in our [debugging documentation](https://docs.mbed.com/docs/debugging-on-mbed/en/latest/).
