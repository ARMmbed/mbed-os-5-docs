## QuadSPI

The QuadSPI driver in mbed-os provides functionality to configure and access QuadSPI devices connected over a QuadSPI interface.
The QuadSPI protocol provides a serial communication interface on four data lines between host and device. It uses up to six lines in total: one line for chip select, one line for clock and four lines for data in/out. You can use this interface for communication with QSPI devices such as Flash memory, display devices and other types of devices providing QuadSPI communication support. The QuadSPI interface can also be configured to work in Single-SPI(traditional SPI) mode or Dual-SPI mode.
The default configuration for the QuadSPI interface are 1 MHz, Single-SPI, Mode 0.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/quadspi.png)<span><br>The above diagram shows an example hardware configuration of a Flash memory connected over a QuadSPI interface.</span> For more information, please review the related content.

### QuadSPI class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/classmbed_1_1QSPI.html)

### QuadSPI example

[![View Example](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/mbed-os-example-qspi/)](https://os.mbed.com/teams/mbed_example/code/mbed-os-example-qspi/) 

### Related content
<a href="www.st.com/resource/en/application_note/dm00227538.pdf">STMicroelectronics Quad-SPI documentation</a>
<a href="http://www.macronix.com/Lists/Datasheet/Attachments/6270/MX25R6435F,%20Wide%20Range,%2064Mb,%20v1.4.pdf">Macronix MX25R6435F flash memory with Quad-SPI</a>
<a href="http://infocenter.nordicsemi.com/pdf/nRF52840_OPS_v0.5.pdf">Nordic Quad-SPI support in NRF52840</a>