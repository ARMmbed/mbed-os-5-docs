## ATCmdParser

ATCmdParser is an Mbed OS compatible AT command parser. 

It sends and receives AT commands to and from a communication device implementing the [FileHandle](./FileHandle.md) interface. It also implements AT command parsing, which validates the data format and separate command and data portion of AT transactions. For example, the UARTSerial communication driver implements the FileHandle interface, and you can use it with ATCmdParser to send and receive AT commands. The actual format of AT commands used depends on the communication device used.

To use ATCmdParser, a reference of object implementing [FileHandle](./FileHandle.md) interface is passed ATCmdParser constructor during ATCmdParser object creation. ATCmdParser also supports configuring specific output delimiter character sequence depending on the interface or device connected to the communication interface.

### ATCmdParser class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/classmbed_1_1_a_t_cmd_parser.html)

### ATCmdParser examples

#### Example 1

This shows an example of ATCmdParser usage with the UARTSerial driver.

```
UARTSerial serial = UARTSerial(D1, D0);
ATCmdParser at = ATCmdParser(&serial, "\r\n");
int value;
char buffer[100];

at.send("AT") && at.recv("OK");
at.send("AT+CWMODE=%d", 3) && at.recv("OK");
at.send("AT+CWMODE?") && at.recv("+CWMODE:%d\r\nOK", &value);
at.recv("+IPD,%d:", &value);
at.read(buffer, value);
at.recv("OK");
```

#### Example 2

You can find another real world example in the Wi-Fi driver implementation for an [ESP8266 device](https://github.com/ARMmbed/esp8266-driver). ESP8266 is a Wi-Fi module that you can connect to an SoC over UART for Wi-Fi support.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/atcmdparser_esp8266.png)<span>The above diagram shows how the ESP8266 Wi-Fi driver uses ATCmdParser to communicate with an ESP8266 device.</span></span>
