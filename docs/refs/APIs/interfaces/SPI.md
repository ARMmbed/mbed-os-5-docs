### SPI

The SPI Interface provides a Serial Peripheral Interface Master.

You can use this interface for communication with SPI slave devices, such as FLASH memory, LCD screens and other modules or integrated circuits.

#### API

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/SPI_8h_source.html)

#### Hello World!

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/SPI_HelloWorld/)](https://developer.mbed.org/teams/mbed_example/code/SPI_HelloWorld/file/dd9e7d208cbd/main.cpp)


#### Interface

<span class="images">![](../../images/pin_out.png)</span>

The default settings of the SPI interface are 1MHz, 8-bit, Mode 0.

You can use the SPI interface to write data words out of the SPI port, returning the data received back from the SPI slave. You can also configure the SPI clock frequency and format. The format is set to data word length 8 to 16 bits, and the mode as per the table below:

Mode |  Polarity |  Phase  
---|---|---  
0 | 0 | 0  
1 | 0 | 1  
2 | 1 | 0  
3 | 1 | 1  

The SPI master generates a clock to synchronously drive a serial bit stream slave. The slave returns a bit stream, also synchronous to the clock.
