# SPI

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_s_p_i.png)<span>SPI class hierarchy</span></span>

The SPI Interface provides a Serial Peripheral Interface Master.

You can use this interface for communication with SPI slave devices, such as FLASH memory, LCD screens and other modules or integrated circuits.

## Interface

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/pin_out.png)<span>A pinout map.</span></span>

The default settings of the SPI interface are 1MHz, 8-bit, Mode 0.

You can use the SPI interface to write data words out of the SPI port, returning the data received back from the SPI slave. You can also configure the SPI clock frequency and format. The format is set to data word length 8 to 16 bits, and the mode as per the table below:

Mode |  Polarity |  Phase
---|---|---
0 | 0 | 0
1 | 0 | 1
2 | 1 | 0
3 | 1 | 1

The SPI master generates a clock to synchronously drive a serial bit stream slave. The slave returns a bit stream, also synchronous to the clock. To communicate with multiple slave devices connected over the same SPI peripheral, you must use multiple SPI objects, one for each slave, but instantiate them with a different Slave select (SSEL) and configuration corresponding to each slave. Note that the SPI object automatically configures the SPI peripheral with the current object's configuration when the application code invokes the interfaces on the SPI object.

## SPI class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_s_p_i.html)

## SPI hello, world

The following example uses the WHOAMI register. The WHOAMI register is an ID register of the slave device. In other words, it's just an example that you can write to a slave's register. In this example, Mbed OS acts as the SPI master, and DigitalOut acts as the slave chip select (cs).

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/SPI_HelloWorld/)](https://os.mbed.com/teams/mbed_example/code/SPI_HelloWorld/file/3789302f33bc/main.cpp)
