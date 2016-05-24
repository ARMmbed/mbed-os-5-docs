#Serial Communication with a PC

The mbed Microcontroller can communicate with a host PC through a "USB Virtual Serial Port" over the same USB cable that is used for programming.

This enables you to:

* Print out messages to a host PC terminal (useful for debugging!)

* Read input from the host PC keyboard

* Communicate with applications and programming languages running on the host PC that can communicate with a serial port, e.g. perl, python, java and so on.

##Hello World!

```c

	#include "mbed.h"

	Serial pc(USBTX, USBRX); // tx, rx

	int main() {
		pc.printf("Hello World!\n");
	}
```

##Host interface and terminal applications

Your mbed Microcontroller can appear on your computer as a serial port. On Mac and Linux, this will happen by default. For Windows, you need to install a driver:

<span style="background-color:lightyellow; color:black; display:block; height:100%; padding:10px">
**Warning:** See [Windows serial configuration](http://developer.mbed.org/handbook/Windows-serial-configuration) for full details about setting up Windows for *serial communication* with your mbed Microcontroller.
</span>

It is common to use a //terminal application// on the host PC to communicate with the mbed Microcontroller. This allows the mbed Microcontroller to print to your PC screen, and for you to send characters back.

* [Terminals](/Going_Further/Terminals/) - Using Terminal applications to communicate between the Host PC and the mbed Micrcontroller.

Some terminal programs (e.g. TeraTerm) list the available serial ports by name. However, if you do need to know the identity of the serial port so that you can attach a terminal or an application to it:

* *Windows* - Look under the "Ports" section in "Device Manager" (''Start -> Control Panel -> System -> Hardware -> Device Manager''). The name will be ''mbed Serial Port (COMx)'', where ''x'' is the number of the COM port allocated.

* *Mac OS X* - Use the command ls /dev/tty.usbmodem*

* *Linux* - Use the command ls /dev/ttyACM*

##Terminal Applications

###Details

Communication over the USB Serial port simply uses the standard [Serial](/Going_Further/Serial/) Interface, specifying the internal (USBTX, USBRX) pins to connect to the Serial Port routed over USB. 

The Serial Interface defaults to a 9600 baud standard serial connection (8 bits, 1 stop bit, no parity), so your host program should be set to the same settings. If you want to communicate at a different standard baud rate, ensure you modify the settings of both the Serial Interface and the Host PC application!

###Examples

####Echo back characters you type

```c

	#include "mbed.h"

	Serial pc(USBTX, USBRX);

	int main() {
		pc.printf("Echoes back to the screen anything you type\n");
		while(1) {
			pc.putc(pc.getc());
		}
	}
```


####Connect to your mbed Microcontroller with a Terminal program and uses the 'u' and 'd' keys to make LED1 brighter or dimmer

```c


	#include "mbed.h"

	Serial pc(USBTX, USBRX); // tx, rx
	PwmOut led(LED1);

	float brightness = 0.0;

	int main() {
		pc.printf("Press 'u' to turn LED1 brightness up, 'd' to turn it down\n");

		while(1) {
			char c = pc.getc();
			if((c == 'u') && (brightness < 0.5)) {
				brightness += 0.01;
				led = brightness;
			}
			if((c == 'd') && (brightness > 0.0)) {
				brightness -= 0.01;
				led = brightness;
			} 
		}
	}
```

####Pass through characters in both directions between the PC and Serial Port

```c

	#include "mbed.h"

	Serial pc(USBTX, USBRX);
	Serial uart(p28, p27);

	DigitalOut pc_activity(LED1);
	DigitalOut uart_activity(LED2);

	int main() {
		while(1) {
			if(pc.readable()) {
				uart.putc(pc.getc());
				pc_activity = !pc_activity;
			}
			if(uart.readable()) {
				pc.putc(uart.getc());
				uart_activity = !uart_activity;
			}
		}
	}
```

####The C stdin, stdout and stderr file handles are also defaulted to the PC serial connection

```c

	#include "mbed.h"

	int main() {
		printf("Hello World!\n");
	}
```

####Read in to a buffer

```c
	
	#include "mbed.h"

	DigitalOut myled(LED1);
	Serial pc(USBTX, USBRX);

	int main() {
		char c;
		char buffer[128];

		pc.gets(buffer, 4);

		pc.printf("I got '%s'\n", buffer);
	}
```

<span style="background-color:lightyellow; color:black; display:block; height:100%; padding:10px">
**Troubleshooting** 
<br />
<br />If you have difficulties with USB serial communication:
<br />1. Make sure you have installed the driver if you are working on Windows - [Windows Serial Configuration](/Going_Further/Serial_Conf).
<br />2. Learn how to use the [Serial](/Going_Further/Serial/) port.
<br />3. Read up on using [Terminals](/Going_Further/Terminals/) programs.
<br /><br />**If you have any problems, or think this tutorial could be improved, please tell us in the [forum](http://developer.mbed.org/forum)** 
</span>