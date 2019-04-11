# ATCmdParser

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_a_t_cmd_parser.png)<span>ATCmdParser class hierarchy</span></span>

ATCmdParser is an Mbed OS AT command parser and serializer. AT commands are instructions used to communicate with a communication device such as a modem, phone or Wi-Fi module. Each command is a text string in ASCII format, and every command starts with "AT" characters followed by a command specifying the operation to be carried out.

The ATCmdParser class implements functionality to send and receive AT commands to the devices capable of communicating using AT commands. The ATCmdParser internally uses the driver for the communication channel to talk to the device. It expects the driver to implement the FileHandle interface to invoke the functions on the driver.

For example, the UARTSerial communication driver implements the FileHandle interface, and you can use it with ATCmdParser to send and receive AT commands to a device connected through UART. ATCmdParser also does AT command parsing, which validates the data format and separates command and data portion of AT transactions. The actual command set and the format of AT commands used depends on the communication device used. The vendor of the device you are communcating with specifies this command set and format.

To use the ATCmdParser, the entity creating the ATCmdParser object passes a reference of object implementing FileHandle interface as an argument to the ATCmdParser constructor. The ATCmdParser also supports configuring a specific output delimiter character sequence, depending on the interface or device connected to the communication interface.

## ATCmdParser class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_a_t_cmd_parser.html)

## ATCmdParser examples

### Example 1

[![View Example](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-atcmdparser)](https://github.com/ARMmbed/mbed-os-example-atcmdparser/blob/master/main.cpp)

### Example 2

You can find another real world example in the Wi-Fi driver implementation for an [ESP8266 device](https://github.com/ARMmbed/mbed-os/blob/master/components/wifi/esp8266-driver). ESP8266 is a Wi-Fi module that you can connect to an SoC over UART for Wi-Fi support.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/atcmdparser_esp8266.png)</span>

The above diagram shows how the ESP8266 Wi-Fi driver uses ATCmdParser to communicate with an ESP8266 device.
