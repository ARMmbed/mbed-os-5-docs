<h1 id="serial-comm">Board to PC communication over USB</h1>

The Arm Mbed microcontroller on your board can communicate with a host PC over the same USB cable that you use for programming.

<span class="tips">If you're working on Windows earlier than Windows 10, you might need to [install a serial driver](windows-serial-driver.html).</span>

This allows you to:

- Print out messages to a [host PC terminal (useful for debugging)](#terminal-applications).
- Read input from the host PC keyboard.
- Communicate with applications and programming languages running on the host PC that can communicate with a serial port. Examples are Perl, Python and Java.

## Hello, world

This program prints a "Hello World" message that you can view on a [terminal application](#terminal-applications). Communication over the USB serial port uses the standard serial interface. Specify the internal (USBTX, USBRX) pins to connect to the serial port routed over USB:


```cpp
#include "mbed.h"

Serial pc(USBTX, USBRX); // tx, rx

int main() {
    pc.printf("Hello World!\n");
    while(1);
}
```

## Using terminal applications

Terminal applications run on your host PC. They provide a window where your Mbed board can print and where you can type characters back to your board.

<span class="tips">**Serial configuration:** The standard setup for the USB serial port is 9600 baud, 8 bits, 1 stop bit, no parity (9600-8-N-1)</span>

### Installing an application for Windows

There are many terminal applications for Windows, including:

- [CoolTerm](http://freeware.the-meiers.org/) - this is the application we use in this example. We use it often because it usually "just works".
- [Tera Term](http://sourceforge.jp/projects/ttssh2/files).
- [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/).
- Some Windows PCs come with **Hyperterminal** installed.

### Configuring the connection

1. Plug in your Mbed board.
1. Open CoolTerm.
1. Click **Connect**. This opens up an 8-n-1 9600 baud connection to the first available serial port. If you have more than one board plugged in, you may need to change the port under **Options > Serial Port > Port**.

Check your connection parameters:

1. Select **Options > Serial Port**.
1. You should see 9600 baud, 8 bits, 1 stop bit, no parity (9600-8-N-1).
1. If you do not see your board, click **Re-Scan Peripherals**.

Your terminal program is now configured and connected.

## Using terminal applications on Linux

CoolTerm should work under Linux. If for some reason it doesn't, you can try one of the following:

- [Minicom](https://help.ubuntu.com/community/Minicom).
- [GNU Screen](https://www.gnu.org/software/screen/manual/screen.html).

## Minimal Printf

For low memory devices you may optionally use the [ArmMbed minimal printf library](https://github.com/ARMmbed/minimal-printf). 

## Additional examples

Use your terminal application to interact with the following examples.

If you're not sure how to build these examples and run them on your board, please see our [build tools section](../tools/index.html).

### Echo back characters you type

```cpp
#include "mbed.h"

Serial pc(USBTX, USBRX);

int main() {
    pc.printf("Echoes back to the screen anything you type\n");
    while(1) {
        pc.putc(pc.getc());
    }
}
```

### Use the U and D keys to make LED1 brighter or dimmer

<span class="tips">**Note:** This example only works if LED1 is on the Pwm pin of the board you are using, such as the NUCLEO-F401RE. </span>

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/NUCLEOF401RE.png)<span>The pin map of the NUCLEO-F401RE shows LED1 on the Pwm pin.</span></span>

```cpp
#include "mbed.h"

Serial pc(USBTX, USBRX); // tx, rx
PwmOut led(LED1);

float brightness = 0.0;

int main() {
    pc.printf("Press U to turn LED1 brightness up, D to turn it down\n");

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

Tie pins together to see characters echoed back.

```cpp
#include "mbed.h"

Serial pc(USBTX, USBRX);
Serial uart(D1, D0);

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

By default, the C `stdin`, `stdout` and `stderr file` handles map to the PC serial connection:

```cpp
#include "mbed.h"

int main() {
    printf("Hello World!\n");
    while(1);
}
```

### Read to a buffer

```cpp
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
