## UARTSerial

The UARTSerial class provides an alternative and enhanced version of the [Serial](https://os.mbed.com/docs/v5.6/reference/serial.html) interface. 


Features:

* It uses the latest FileHandle API that permits non-blocking and device operations. It is now possible to use a serial device with the C library file handling functions.
E.g

        UARTSerial serial(RX, TX);

        FILE *in = fdopen(&serial, “r”);

        FILE *out = fdopen(&serial, “w”);

        while (1) {

            fscanf(in, “%s”, buffer);
            fprintf(out, “Hello %s\r\n”, buffer);
        }
  

* It has built-in buffering, making input and output more efficient.

* It also implements a poll() function which is useful for juggling multiple streams.


### UARTSerial class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/classmbed_1_1_uartserial.html)

<span class="notes">**Note**: On a Windows machine, you will need to install a USB serial driver. See [Windows serial configuration](/docs/v5.6/tutorials/serial-communication.html#windows-serial-driver).</span>


### UARTSerial examples

#### Example one

Write a "Hello world" message to a device at a baud rate of 19200.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/UARTSerial_HelloWorld/)](https://os.mbed.com/teams/mbed_example/code/UARTSerial_HelloWorld/file/7376f17bb36e/main.cpp)  **LINK TBC**

#### Example two

Provide a serial pass-through between the PC and an external UART.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/UARTSerial_Example2/)](https://os.mbed.com/teams/mbed_example/code/UARTSerial_Example2/file/8d318218bac1/main.cpp) **LINK TBC**

#### Example three

Schedule a callback on the global event queue whenever there is a UART interrupt. The callback checks if a character has been typed and if so reads it and echoes it back to the terminal. It also toggles the LED state on each key press.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/UARTSerial_Example3)](https://os.mbed.com/teams/mbed_example/code/UARTSerial_Example3/file/3b040f367dd8/main.cpp) **LINK TBC**
