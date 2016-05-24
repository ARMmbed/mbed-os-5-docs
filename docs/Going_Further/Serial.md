#The Serial Protocol

Serial is a generic protocol used by computers and electronic modules to send and receive control information and data. The Serial link has two unidirection channels, one for sending and one for receiving. The link is asynchronous, and so both ends of the serial link must be configured to use the same settings.

One of the Serial connections goes via the mbed USB port, allowing you to easily communicate with your host PC.

##Hello World!

<span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">
[Import the program](http://developer.mbed.org/users/mbed_official/code/Serial_HelloWorld_Mbed/docs/879aa9d0247b/main_8cpp_source.html)
</span>

##API summary
 
<div class="flashbox flibrary"><span style="background-color:lightyellow; color:gray; display:block; height:100%; padding:10px"><h4 class="ftitle"><a class="button small radius" style="font-weight: bold; position: relative; float: right;" href="https://developer.mbed.org/compiler/#import:/users/mbed_official/code/mbed/builds/82220227f4fa;mode:lib" target="compiler">Import library</a><a href="http://developer.mbed.org/users/mbed_official/code/mbed/docs/7e07b6fb45cf//classmbed_1_1Serial.html"><span></span></a><div class="wiki-api-header"><a href="http://developer.mbed.org/users/mbed_official/code/mbed/docs/7e07b6fb45cf//classmbed_1_1Serial.html"></a><a href="http://developer.mbed.org/users/mbed_official/code/mbed/docs/7e07b6fb45cf//classmbed_1_1Serial.html">mbed - Serial Class Reference</a></div></h4><div><div class="wiki-api-snippet"><table class="memberdecls">
<tbody>

<table style="width:100%" border="1">
<tr style="background-color:white">
  <td colspan="2">
   <h2>
    <a name="pub-methods">
    </a>
    Public Member Functions
   </h2>
  </td>
 </tr>
 <tr>
  <td class="memItemLeft" align="right" valign="top">
   &nbsp;
  </td>
  <td class="memItemRight" valign="bottom">
   <a class="el" href="http://developer.mbed.org/users/mbed_official/code/mbed/docs/7e07b6fb45cf/classmbed_1_1Serial.html#a38e24713e4321ab0d0a14923b0800d98">
    Serial
   </a>
   (PinName tx, PinName rx, const char *name=NULL)
  <br />Create a
   <a class="el" title="A serial port (UART) for communication with other serial devices." href="http://developer.mbed.org/users/mbed_official/code/mbed/docs/7e07b6fb45cf/classmbed_1_1Serial.html">
    Serial
   </a>
   port, connected to the specified transmit and receive pins.
   <a href="http://developer.mbed.org/users/mbed_official/code/mbed/docs/7e07b6fb45cf/#a38e24713e4321ab0d0a14923b0800d98">
   </a>
   <br>
  </td>
 </tr>
 <tr>
  <td class="memItemLeft" align="right" valign="top">
   void&nbsp;
  </td>
  <td class="memItemRight" valign="bottom">
   <a class="el" href="http://developer.mbed.org/users/mbed_official/code/mbed/docs/7e07b6fb45cf/classmbed_1_1SerialBase.html#a9afb7aa9321cd71a8a26a673157583d2">
    baud
   </a>
   (int baudrate)
  <br />
   Set the baud rate of the serial port.
   <a href="http://developer.mbed.org/users/mbed_official/code/mbed/docs/7e07b6fb45cf/#a9afb7aa9321cd71a8a26a673157583d2">
   </a>
   <br>
  </td>
 </tr>
 <tr>
  <td class="memItemLeft" align="right" valign="top">
   void&nbsp;
  </td>
  <td class="memItemRight" valign="bottom">
   <a class="el" href="http://developer.mbed.org/users/mbed_official/code/mbed/docs/7e07b6fb45cf/classmbed_1_1SerialBase.html#a8274461aa9a0611c28c4c6aeae665277">
    format
<br />
   Set the transmission format used by the serial port.
   <a href="http://developer.mbed.org/users/mbed_official/code/mbed/docs/7e07b6fb45cf/#a8274461aa9a0611c28c4c6aeae665277">
   </a>
   <br>
  </td>
 </tr>
 <tr>
  <td class="memItemLeft" align="right" valign="top">
   int&nbsp;
  </td>
  <td class="memItemRight" valign="bottom">
   <a class="el" href="http://developer.mbed.org/users/mbed_official/code/mbed/docs/7e07b6fb45cf/classmbed_1_1SerialBase.html#a54635d8d9d55acd3e8426767271e9d7b">
    readable
   </a>
   ()
<br />
   Determine if there is a character available to read.
   <a href="http://developer.mbed.org/users/mbed_official/code/mbed/docs/7e07b6fb45cf/#a54635d8d9d55acd3e8426767271e9d7b">
   </a>
   <br>
  </td>
 </tr>
 <tr>
  <td class="memItemLeft" align="right" valign="top">
   int&nbsp;
  </td>
  <td class="memItemRight" valign="bottom">
   <a class="el" href="http://developer.mbed.org/users/mbed_official/code/mbed/docs/7e07b6fb45cf/classmbed_1_1SerialBase.html#a9bb16b1f54af7224f26f865ab9b7dd86">
    writeable
   </a>
   ()
 <br />
   Determine if there is space available to write a character.
   <a href="http://developer.mbed.org/users/mbed_official/code/mbed/docs/7e07b6fb45cf/#a9bb16b1f54af7224f26f865ab9b7dd86">
   </a>
   <br>
  </td>
 </tr>
 <tr>
  <td class="memItemLeft" align="right" valign="top">
   void&nbsp;
  </td>
  <td class="memItemRight" valign="bottom">
   <a class="el" href="http://developer.mbed.org/users/mbed_official/code/mbed/docs/7e07b6fb45cf/classmbed_1_1SerialBase.html#ae67fb9b5a2ee2f4e98a39cdab10ed090">
    attach
   </a>
   (void(*fptr)(void), IrqType type=RxIrq)
 <br />
Attach a function to call whenever a serial interrupt is generated.
   <a href="http://developer.mbed.org/users/mbed_official/code/mbed/docs/7e07b6fb45cf/#ae67fb9b5a2ee2f4e98a39cdab10ed090">
   </a>
   <br>
  </td>
 </tr>
  </td>
 </tr>
 <tr>
  <td class="memTemplItemLeft" align="right" valign="top">
   void&nbsp;
  </td>
  <td class="memTemplItemRight" valign="bottom">
   <a class="el" href="http://developer.mbed.org/users/mbed_official/code/mbed/docs/7e07b6fb45cf/classmbed_1_1SerialBase.html#ae80b25534c94f8aad2799c5644ec8485">
    attach
   </a>
   (T *tptr, void(T::*mptr)(void), IrqType type=RxIrq)
 <br />
 Attach a member function to call whenever a serial interrupt is generated.
   <a href="http://developer.mbed.org/users/mbed_official/code/mbed/docs/7e07b6fb45cf/#ae80b25534c94f8aad2799c5644ec8485">
   </a>
   <br>
  </td>
 </tr>
 <tr>
  <td class="memItemLeft" align="right" valign="top">
   void&nbsp;
  </td>
  <td class="memItemRight" valign="bottom">
   <a class="el" href="http://developer.mbed.org/users/mbed_official/code/mbed/docs/7e07b6fb45cf/classmbed_1_1SerialBase.html#a7fca2a71c423b8e004c4abf6dc367fc2">
    send_break
   </a>
   ()
  <br />
   Generate a break condition on the serial line.
   <a href="http://developer.mbed.org/users/mbed_official/code/mbed/docs/7e07b6fb45cf/#a7fca2a71c423b8e004c4abf6dc367fc2">
   </a>
   <br>
  </td>
 </tr>
 <tr>
  <td class="memItemLeft" align="right" valign="top">
   void&nbsp;
  </td>
  <td class="memItemRight" valign="bottom">
   <a class="el" href="http://developer.mbed.org/users/mbed_official/code/mbed/docs/7e07b6fb45cf/classmbed_1_1SerialBase.html#a68a82a55bc262aa9ed7d2e1a16419389">
    set_flow_control
   </a>
   (Flow type, PinName flow1=NC, PinName flow2=NC)
 <br />
   Set the flow control type on the serial port.
   <a href="http://developer.mbed.org/users/mbed_official/code/mbed/docs/7e07b6fb45cf/#a68a82a55bc262aa9ed7d2e1a16419389">
   </a>
   <br>
  </td>
 </tr>
</tbody>
</table>
</div></div></div>

##Interface

The Serial Interface can be used on supported pins and USBTX/USBRX

<span style="text-align:center; display:block;">
![The pinout page](/Going_Further/Images/Serial_Pinout.png)
</span>
<span style="background-color:lightblue; color:gray; display:block; height:100%; padding:10px;">
[See the Pinout page for more details](http://developer.mbed.org/handbook/Pinouts).
</span>

Note that USBTX/USBRX are not DIP pins; they represent the pins that route to the interface USB Serial port so you can communicate with a host PC.

<span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">
If you want to send data to a host PC, take a look at [SerialPC](/Development/PC_Com/) - Communicating between mbed and a host PC.
<br /><br />
Note that on a windows machine, you will need to install a USB Serial driver, see: [Windows serial configuration](/Going_Further/Serial_Conf/).
</span>

Serial channels have a number of configurable parameters:

* *Baud Rate* - There are a number of standard baud rates ranging from a few hundred bits per seconds, to megabits per second. The default setting for a Serial connection on the mbed Microcontroller is 9600 baud.

* *Data length* - Data transferred can be either 7 or 8 bits long. The default setting for a Serial connection on the mbed Microcontroller is 8 bits.

* *Parity* - An optional parity bit can be added. The parity bit will be automatically set to make the number of 1's in the data either odd or even. Parity settings are Odd, Even or None. The default setting for a Serial connection on the mbed microcontroller is for the parity to be set to None.

* *Stop Bits* - After data and parity bits have been transmitted, 1 or 2 stop bit is inserted to "frame" the data. The default setting for a Serial connection on the mbed microcontroller is for one stop bit to be added.

The default settings for the mbed microcontroller are described as //9600 8N1//, and this is common notation for Serial port settings.

##See Also

  * [Communication with a PC](/Development/PC_Com/)

##Reference

  * [Serial Port on Wikipedia](http://en.wikipedia.org/wiki/Serial_port)

##Examples

``Write a message to a device at a 19200 baud``

```c

	#include "mbed.h"

	Serial device(p9, p10);  // tx, rx

	int main() {
		device.baud(19200);
		device.printf("Hello World\n");
	}
```

``Provide a serial pass-through between the PC and an external UART``

```c

	#include "mbed.h"

	Serial pc(USBTX, USBRX); // tx, rx
	Serial device(p9, p10);  // tx, rx

	int main() {
		while(1) {
			if(pc.readable()) {
				device.putc(pc.getc());
			}
			if(device.readable()) {
				pc.putc(device.getc());
			}
		}
	}
```

``Attach to RX Interrupt``

```c

	#include "mbed.h"
	
	DigitalOut led1(LED1);
	DigitalOut led2(LED2);

	Serial pc(USBTX, USBRX);

	void callback() {
		// Note: you need to actually read from the serial to clear the RX interrupt
		printf("%c\n", pc.getc());
		led2 = !led2;
	}

	int main() {
		pc.attach(&callback);

		while (1) {
			led1 = !led1;
			wait(0.5);
		}
	}
```

<span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">
See [full attach API](http://mbed.org/projects/libraries/api/mbed/trunk/Serial#Serial.attach)
</span>