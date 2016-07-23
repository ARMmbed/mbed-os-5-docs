# Board to PC communication over USB

The mbed microcontroller on your board can communicate with a host PC over the same USB cable that is used for programming.

<span class="tips">If you're working on Windows, you might need to [install a serial driver](what_need.md#windows-serial-driver).</span>

This allows you to:

* Print out messages to a [host PC terminal (useful for debugging)](#terminal-applications).

* Read input from the host PC keyboard.

* Communicate with applications and programming languages running on the host PC that can communicate with a serial port. like Perl, Python, and Java.

## Hello World!

This program prints a "Hello World" message that you can view on a [terminal application](#terminal-applications). Communication over the USB Serial port uses the standard serial interface, specifying the internal (USBTX, USBRX) pins to connect to the serial port routed over USB:


```c
#include "mbed.h"

Serial pc(USBTX, USBRX); // tx, rx

int main() {
    pc.printf("Hello World!\n");
    while(1);
}
```

## Terminal applications


Terminal applications run on your host PC, and provide a window for your mbed board to print to, and a means for you to type characters back to your board. 

<span class="tips">**Serial configuration:** The standard setup for the USB Serial Port is 9600 baud, 8 bits, 1 stop bit, no parity (9600-8-N-1)</span>

### Using terminal applications on Windows

#### Installing an application

There are many terminal applications for Windows, including:
[TODO]: Link to Coolterm for win/mac/??linux??
* [Tera Term](http://sourceforge.jp/projects/ttssh2/files) - this is the application we use in this example.
* [Putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/)
* [Terminal by Bray](http://sites.google.com/site/braypp/terminal)
* Some Windows PCs come with **Hyperterminal** installed.

#### Configuring the Connection
[TODO]: Coolterm, not teraterm instructions
1. Open Tera Term.
1. Select **File > New Connection**.
1. Select the **Serial** radio button.
1. select **mbed Serial Port** from the drop down menu.
1. Click **OK**.

Set up new-line format (to print out new line characters correctly):
 
1. Select **Setup > Terminal**.
1. Under **New-line**, set **Receive** to **LF**.

Check your connection parameters:

1. Select **Setup > Serial Port**.
1. You should see 9600 baud, 8 bits, 1 stop bit, no parity (9600-8-N-1).

Your terminal program is now configured and connected. 

### Using terminal applications on Mac OS X or Linux
[TODO]: Coolterm for sure!
#### Installing an application

If you do not already have it, install [GNU Screen](http://en.wikipedia.org/wiki/GNU_Screen).

#### Configuring the Connection
  
1. Open a terminal or console window.
1. Use the command ``screen /dev/<devicename>`` to connect to your device. If you're not sure how to find your device's name:
	* *Windows*: look under the **Ports** section in **Device Manager** ('**Start > Control Panel > System > Hardware > Device Manager**'). The name will be ''mbed Serial Port (COMx)'', where ''x'' is the number of the COM port allocated.
	* *Mac OS X*: use the command ``ls /dev/tty.usbmodem*``
	* *Linux*: use the command ``ls /dev/ttyACM*``
1. Check that your connection is working by typing in the terminal application; the status light on the mbed board should flicker as each character is received. 


## Additional examples

Use your terminal application to interact with the following examples.

If you're not sure how to build these examples and run them on your board, please see out [build tools section](../build_tools/options.md).
[TODO]: all these examples should be import links, not hard coded

### Echo back characters you type

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


### Use the 'u' and 'd' keys to make LED1 brighter or dimmer

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

### Pass characters in both directions

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

### Using stdin, stdout and stderr

The C ``stdin``, ``stdout`` and ``stderr file`` handles are also defaulted to the PC serial connection:

```c
#include "mbed.h"

int main() {
    printf("Hello World!\n");
    while(1);
}
```

### Read to a buffer

```c
#include "mbed.h"

DigitalOut myled(LED1);
Serial pc(USBTX, USBRX);

int main() {
    char c;
    char buffer[128];

    pc.gets(buffer, 4);
    pc.printf("I got '%s'\n", buffer);
    while(1);
}
```
