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

### Using terminal applications on Windows / OSX

#### Installing an application

There are many terminal applications for Windows, including:
* [CoolTerm](http://freeware.the-meiers.org/) - this is the application we use in this example and the mbed preferred terminal as it usually 'just works'.
* [Tera Term](http://sourceforge.jp/projects/ttssh2/files)
* [Putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/)
* Some Windows PCs come with **Hyperterminal** installed.

#### Configuring the Connection
[TODO]: Coolterm, not teraterm instructions
1. Plug in mbed board
2. Open CoolTerm
3. Press **Connect** (this opens up a 8-n-1 9600baud connection to the first available serial port, you may need to change the port under **Options > Serial Port > Port** if you have multiple boards plugged in)

Check your connection parameters:

1. Select **Setup > Serial Port**.
1. You should see 9600 baud, 8 bits, 1 stop bit, no parity (9600-8-N-1).
2. If you do not see your board listed try pressing **Re-Scan Peripherals**

Your terminal program is now configured and connected. 

### Using terminal applications on Linux
[TODO]: Coolterm for sure!
#### Installing an application
CoolTerm should work under Linux, but if for some reason it doesnt work on your machine then you can try using any of the following. 

1. [minicom](https://help.ubuntu.com/community/Minicom)
1. [GNU Screen](https://www.gnu.org/software/screen/manual/screen.html)
1. [Any of These](https://encrypted.google.com/search?hl=en&q=COM%20Port%20terminal%20program%20Linux)

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
