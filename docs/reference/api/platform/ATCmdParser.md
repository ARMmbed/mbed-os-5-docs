## ATCmdParser

ATCmdParser is an Mbed-OS compatible AT command parser. AT commands are instructions used to communicate with a communication device like modem, phones, wifi-modules etc. Each command is a text string in ASCII format and every command starts with "AT" characters followed by a command specifying the operation to be carried out. ATCmdParser class in Mbed-OS implements functionality to send and receive AT commands to devices capable of communicating using AT commands. ATCmdParser internally uses the driver for the communication channel to talk to the device. It expects the driver to implement the [FileHandle](https://os.mbed.com/docs/v5.6/reference/filehandle.html) interface in order to invoke the functions on the driver. For example, the [UARTSerial](https://os.mbed.com/docs/v5.6/reference/classmbed_1_1UARTSerial.html) communication driver implements the [FileHandle](https://os.mbed.com/docs/v5.6/reference/filehandle.html) interface,and you can use it with ATCmdParser to send and receive AT commands to a device connected through UART. ATCmdParser also does AT command parsing, which validates the data format and separates command and data portion of AT transactions. The actual command set and the format of AT commands used depends on the communication device used and is specified by the vendor of the device you are communcating with. For example, [ESP8266](https://en.wikipedia.org/wiki/ESP8266) is Wi-Fi module from Espressif Systems capable of communicating using AT commands and the command set is specified by [Espressif AT command specification](https://www.espressif.com/sites/default/files/documentation/4a-esp8266_at_instruction_set_en.pdf).

To use ATCmdParser, a reference of object implementing [FileHandle](https://os.mbed.com/docs/v5.6/reference/filehandle.html) interface is passed as an argument to ATCmdParser constructor, by the entity creating the ATCmdParser object. ATCmdParser also supports configuring specific output delimiter character sequence depending on the interface or device connected to the communication interface.

### ATCmdParser class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/classmbed_1_1_a_t_cmd_parser.html)

### ATCmdParser examples

#### Example 1

[![View Example](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-atcmdparser)](https://github.com/ARMmbed/mbed-os-example-atcmdparser)

#### Example 2

You can find another real world example in the Wi-Fi driver implementation for an [ESP8266 device](https://github.com/ARMmbed/esp8266-driver). ESP8266 is a Wi-Fi module that you can connect to an SoC over UART for Wi-Fi support.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/atcmdparser_esp8266.png)<span>The above diagram shows how the ESP8266 Wi-Fi driver uses ATCmdParser to communicate with an ESP8266 device.</span></span>
