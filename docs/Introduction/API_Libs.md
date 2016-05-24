#High-level Peripheral APIs

The mbed SDK gives you an API-driven approach to microcontroller coding.

We've done all the hard work of implementing drivers for the different [mbed platforms](http://developer.mbed.org/platforms/) so you won't have to. It is liberating to fire up an interface, knowing it'll just work!

You can code using meaningful abstract objects and API calls, so you don't need to learn the microcontroller hardware details to get going. There is even a **Hello World!** example for every peripheral, just to get you started.

Take a look at some of these interfaces to get a feel of how it works: [digital out](http://developer.mbed.org/handbook/DigitalOut), [analog in](http://developer.mbed.org/handbook/AnalogIn), [SPI](http://developer.mbed.org/handbook/SPI), [USB mouse](http://developer.mbed.org/handbook/USBMouse), [Timer](http://developer.mbed.org/handbook/Timer) or [CAN](http://developer.mbed.org/handbook/CAN).

If needed, you can bypass the APIs and talk directly to the microcontroller hardware using the low-level [Cortex Microcontroller Software Interface Standard (CMSIS) APIs](/CMSIS/CMSIS/). Ideal when just one aspect needs specific low-level control.

<span style="background-color:lightgray; color:purple; display:block; height:100%;padding:10px;">
For all the mbed C/C++ SDK APIs, see the [API breakdown](/Development/API_Libs_Breakdown/)<br />
To read more about mbed SDK coding style, see the [mbed SDK coding style guide](/Going_Further/Coding_Style/)
</span>

