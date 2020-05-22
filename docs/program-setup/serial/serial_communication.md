<h1 id="serial-comm">Board to PC communication over USB</h1>

The Arm Mbed microcontroller on your board can communicate with a host PC over the same USB cable that you use for programming.

<span class="tips">If you're working on Windows earlier than Windows 10, you might need to [install a serial driver](../program-setup/windows-serial-driver.html).</span>

This allows you to:

- Print out messages to a PC terminal (useful for debugging).
- Read input from a PC keyboard.
- Communicate with applications running on a PC to exchange data.

## Hello World - printing messages

This program prints a "Hello World!" message that you can view on a serial terminal. Mbed OS redirects any `printf()` statements to the board's debug USB serial.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Serial_STDOUT/tree/v6.0)](https://github.com/ARMmbed/mbed-os-snippet-Serial_STDOUT/blob/v6.0/main.cpp)

## Viewing output in a serial terminal

Serial terminals run on your host PC. They provide an interface where your Mbed board can print and where you can type characters back to your board.

Mbed CLI provides a serial terminal that is configured with a default baud rate of `9600`. When a single board is connected, run:

```
mbed sterm
```

(If you have multiple boards connected, please refer to [Additional options of mbed sterm](#additional-options-of-mbed-sterm).)

`mbed sterm` starts message printing.

Restart the application using the board's reset button, or by entering <kbd>Ctrl + B</kbd> in the serial terminal.
The example prints "Hello World!" to the terminal after the reset.

To close the serial terminal, enter <kbd>Ctrl + C</kbd>.

## Additional options of mbed sterm

- If you have multiple boards connected:
    1. Run `mbedls` to find the port of the board you want to use.
    1. Run `mbed sterm -p <PORT>`.

- If your application uses a baud rate other than 9600, specify it with `-b <BAUDRATE>` when opening the serial terminal.

- To list all options, run `mbed sterm -h`:

    ```
    usage: mbed sterm [-h] [-m TARGET] [-p PORT] [-b BAUDRATE] [-e ECHO] [-r] [-v] [-vv]

    Open serial terminal to connected target (usually board), or connect to a user-specified COM port

    optional arguments:
    -h, --help            show this help message and exit
    -m TARGET, --target TARGET
                            Compile target MCU. Example: K64F, NUCLEO_F401RE,
                            NRF51822...
    -p PORT, --port PORT  Communication port. Default: auto-detect. Specifying
                            this will also ignore the -m/--target option above.
    -b BAUDRATE, --baudrate BAUDRATE
                            Communication baudrate. Default: 9600
    -e ECHO, --echo ECHO  Switch local echo on/off. Default: on
    -r, --reset           Reset the targets (via SendBreak) before opening
                            terminal.
    -v, --verbose         Verbose diagnostic output
    -vv, --very_verbose   Very verbose diagnostic output
    ```

## Auto-opening a serial terminal after compilation

To compile, flash and open a serial terminal in one command line:

```
mbed compile -t <TOOLCHAIN> -m <TARGET> --flash --sterm
```

## Additional examples - reading user inputs

In addition to printing messages, Mbed OS applications can also read keyboard inputs from the user using the [BufferedSerial](../apis/bufferedserial.html) and [UnbufferedSerial](../apis/unbufferedserial.html) classes.

Use your terminal application to interact with the following examples.

If you're not sure how to build these examples and run them on your board, please see our [build tools section](../build-tools/index.html).

### Echo back characters you type

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Serial_EchoBack/tree/v6.0)](https://github.com/ARMmbed/mbed-os-snippet-Serial_EchoBack/blob/v6.0/main.cpp)

### Use the U and D keys to make LED1 brighter or dimmer

<span class="tips">**Note:** This example only works if LED1 is on the Pwm pin of the board you are using, such as the NUCLEO-F401RE. </span>

<span class="images">![](../../images/NUCLEOF401RE.png)<span>The pin map of the NUCLEO-F401RE shows LED1 on the Pwm pin.</span></span>

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Serial_LEDControl/tree/v6.0)](https://github.com/ARMmbed/mbed-os-snippet-Serial_LEDControl/blob/v6.0/main.cpp)

### Pass characters in both directions

Tie pins together to see characters echoed back.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Serial_PassCharacters/tree/v6.0)](https://github.com/ARMmbed/mbed-os-snippet-Serial_PassCharacters/blob/v6.0/main.cpp)

### Read to a buffer

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Serial_ReadToBuffer/tree/v6.0)](https://github.com/ARMmbed/mbed-os-snippet-Serial_ReadToBuffer/blob/v6.0/main.cpp)
