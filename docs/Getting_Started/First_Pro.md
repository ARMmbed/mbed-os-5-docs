#Blinky

The first program we'll use is a test program - it's meant to show you that your board is functional and that you're compiling for the right platform. It's called [Blinky](http://developer.mbed.org/teams/mbed/code/mbed_blinky/). 

#What you need

To get this program going, all you need is: 

+ A BLE-enabled mbed board. Don't forget to [add it to your compiler and select it as the target](/Getting_Started/User_Plat_Reg#Platform/).

+ A user account on [developer.mbed.org](https://developer.mbed.org/account/signup/) to access the compiler.

#Getting Blinky on your board

You can get Blinky working in just a few minutes.

2. Import [``Blinky``](http://developer.mbed.org/teams/mbed/code/mbed_blinky/) to your compiler. If you forgot how that's done, see the [IDE section](/Getting_Started/Using_IDE/).

3. Compile the code. When prompted, save it to your Downloads folder.

4. Drag and drop the compiled file to your board.

5. If your board does not restart itself, restart it manually by pressing the Restart button.

6. The LED will flash.

#Understanding and changing the code

The [next section](#understand) explains the code line by line. If you're comfortable with the code, skip to the fun bits - [changing the code](#change) - to see some more possibilities. 

<a name="understand">
##Understanding the code
</a>

``Blinky`` is a very short piece of code. In the compiler, click ``main.cpp`` to see the code.

<span style="text-align:center; display:block;">
![Blinky main.cpp](/Getting_Started/Images/Blinky/OpeningBlinky.png)
</span>
<span style="background-color:lightblue; color:gray; display:block; height:100%; padding:10px;">*Clicking on ``main.cpp`` in the tree opens that file in the main area*</span>

Let's review it line by line:

``#include "mbed.h"``

Our program relies on pre-existing code, available in a file called ``mbed.h`` that was imported along with ``main.cpp()``. But just because we imported them together doesn't mean that the compiler will know to keep them together; if we want the file to be included when we build our program (and we do, because we're using code that exists in it) we have to explicitly tell the compiler to include it.

``DigitalOut myled(LED1);``

DigitalOut is the [API class](http://developer.mbed.org/handbook/DigitalOut) that handles output to digital pins. In this line, we created a new object of type ``DigitalOut``, call it "myled" and specify that it refers to ``LED1`` - the first LED on the board.

<span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">
**Tip:** exactly which LED is LED1 depends on your board. You can see the full schematics, including LEDs, on your board's [platform page](http://developer.mbed.org/platforms/).
</span>

``int main()``

This line declares that we've reached the main function - the function that runs be default every time the board is switched on (or restarted). You'll see soon that it contains a loop; if it didn't, it would stop running when it reached the last line of the code.

``while(1)``

While is a type of loop that says "keep running the code I contain so long as my condition is met, ie held to be true". The condition of this particular loop is "1". "1" means "TRUE", to a computer, so this loop's condition is always met, and the loop will never stop running. If we didn't use this loop, we'd turn the LED on and off only once, instead of continuously.

``myled = 1;``

As we said above, "1" to a computer means "TRUE". In the context of output (sending a command) to a digital pin (our LED), this means "send high current". If the LED is positive, it will be turned on; if it's negative, it will be turned off.

``wait(0.2);``

"Wait" is a delay in the function's run. Since the program runs from line to line (sequentially) as fast as it can, if we want the LED to be on or off for a period that the human eye can actually perceive, we have to ask the program to wait between turning the LED on and off. In this case, we tell it to wait 0.2 seconds.

<span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">
**Tip:** we don't need to specify that it's seconds; the ``wait`` function, as defined on the API, simply assumes that any value you send is in seconds. There are other functions that use different values, such as microseconds (``wait_us``) or milliseconds (``wait_ms``).
</span>

``myled = 0``

"0" is the opposite of "1", and means "FALSE". In the context of output (sending a command) to a digital pin (our LED), this means "send low current". If the LED is positive, it will be turned off; if it's negative, it will be turned on.


``wait(0.2)``

We again ask the program to wait before moving on to the next line. 

This is the end of the loop; since the loop's condition is "1", meaning it's always TRUE and never stops running, we'll now go back to our first line: ``myled = 1``, and turn the LED on again. And so on and so forth.
 
<a name="change">
##Changing the code
</a>

You can use ``Blinky`` to get used to mbed and the compiler before moving on to [your prototyping](/Introduction/Rapid_Prototyping/).

###Sequential LEDs

Your board likely has more than one LED; you can have your LEDs blink in sequence:

```c

	#include "mbed.h"

	DigitalOut myled1(LED1);
	DigitalOut myled2(LED2); //adds another myled object, referring to the second LED on the board

	int main() {
    		while(1) {
        		myled1 = 1; //turn on first LED
        		wait(0.2);
        		myled1 = 0; //turn off first LED
        		wait(0.2);
        		myled2 = 1; //turn on second LED
        		wait(0.2);
        		myled2 = 0; //turn off second LED
        		wait(0.2);
    		}
	}
```

###Concurrent LEDs

Alternatively, you can have both LEDs blink at the same time:

```c

	#include "mbed.h"

	DigitalOut myled1(LED1);
	DigitalOut myled2(LED2);


	int main() {
    		while(1) {
        		myled1 = 1;
        		myled2 = 1; //although these lines are executed one after the other, not both at once, the time between them is so short that to us it seems concurrent
        		wait(0.2);
        		myled1 = 0;
        		myled2 = 0;
        		wait(0.2);
    		}
	}
```

###Changing LED timing

The ``wait()`` function delays the execution of the next line of code. We can change its values to change the timing of the LED sequence:

```c

	#include "mbed.h"

	// My board has four LEDs, numbered from 1 to 4, so I create four LED objects
	DigitalOut myled1(LED1);
	DigitalOut myled2(LED2);
	DigitalOut myled3(LED3);
	DigitalOut myled4(LED4);

	int main() {
		while(1) {
		// The total time for each LED is five seconds, made up of (time on) + (time off)
			myled1 = 1; //my board's LEDs are positive, so the output 1 (high current) turns them on
			wait(1);
			myled1 = 0;
			wait(4);
			myled2 = 1;
			wait(2);
			myled2 = 0;
			wait(2);
			myled3 = 1;
			wait(3);
			myled3 = 0;
			wait(4);
			myled4 = 1;	
			wait(4);
			myled4 = 0;
			wait(1);   
		}
	}
```

###Multi-colour LEDs

Some boards have LEDs with more than one colour. For example, [this platform](http://developer.mbed.org/platforms/FRDM-K64F/) has three LEDs: red, green and blue. The platform's page shows as a schematic that - among other things - shows us the pins that are mapped to each LED:

<span style="text-align:center; display:block;">
![LED mapping](/Getting_Started/Images/Blinky/RGB_LEDs.png)
</span>
<span style="background-color:lightblue; color:gray; display:block; height:100%; padding:10px;">*LED1 is red, LED2 is green and LED3 is blue*</span>

Because the multi-colour LEDs are mapped to LED1, LED2 and LED3 we can use one of our earlier Blinky variations to run the multi-coloured LEDs. For example, if I want to run the program from the pervious section (which focused on ``wait()``), the only thing I need to do is remove the fourth LED from the code (since there are only three LEDs on my multi-colour board):

```c

	#include "mbed.h"

	// This board has three LEDs, so I create three objects
	DigitalOut myled1(LED1);
	DigitalOut myled2(LED2);
	DigitalOut myled3(LED3);
	
	int main() {
		while(1) {
			myled1 = 1; //this is the red LED
			wait(1);
			myled1 = 0;
			wait(4);
			myled2 = 1; //this is the green LED
			wait(2);
			myled2 = 0;
			wait(2);
			myled3 = 1; //this is the blue LED
			wait(3);
			myled3 = 0;
			wait(4);
		}
	}
```

It would have been neater to change the timings, as the five-second total was designed for a four-LED board, but we wanted to see that the only important change is accounting for the correct number of LEDs.

#Summary

mbed boards require a knowledge of C++, but thanks to the API abstractions you don't have to understand the hardware other than at the basic level of recognising the correct name of the circuit you're trying to work with (using the schematics available for each board). As we saw in the Blinky samples, the APIs also provide commonly used functions such as ``wait()``.

To explore other samples and learn of more API functions and abstractions, see our [code samples](http://developer.mbed.org/teams/mbed_example/) and the [API breakdown](/Development/API_Libs_Breakdown/).
