# SPI

The SPI Interface provides a Serial Peripheral Interface Master. 

This interface can be used for communication with SPI slave devices, such as FLASH memory, LCD screens and other modules or integrated circuits.

## Hello World!

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/users/mbed_official/code/SPI_HelloWorld_Mbed/)](https://developer.mbed.org/users/mbed_official/code/SPI_HelloWorld_Mbed/file/tip/main.cpp) 

## API

[![View code](https://www.mbed.com/embed/?type=library)](https://developer.mbed.org/users/mbed_official/code/mbed/docs/tip/classmbed_1_1SPI.html) 

## Interface

<span class="images">![](../Images/pin_out.png)</span>
  
The default settings of the SPI interface are 1MHz, 8-bit, Mode 0

The SPI Interface can be used to write data words out of the SPI port, returning the data received back from the SPI slave. The SPI clock frequency and format can also be configured. The format is set to data word length 8 to 16 bits, and the mode as per the table below:

Mode |  Polarity |  Phase  
---|---|---  
0 | 0 | 0  
1 | 0 | 1  
2 | 1 | 0  
3 | 1 | 1  
  
The SPI master generates a clock to synchronously drive a serial bit stream slave. The slave returns a bit stream, also synchronous to the clock. 

## Reference

  * [SPI on Wikipedia](http://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus)
