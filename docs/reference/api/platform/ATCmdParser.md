## ATCmdParser

ATCmdParser is a mbed-OS compatible AT command parser. 

It's used for sending and receiving AT commands to a communication 
device implementing [FileHandle](./FileHandle.md) interface. It also implements AT 
command parsing which validates the data format and seperate 
command and data portion of AT transactions. For example, 
the UARTSerial communication driver implements FileHandle 
interface and can be used with ATCmdParser to send/receive 
AT commands. The actual format of AT commands used depends 
on the communication device used.  

In order to use ATCmdParser a reference of object implementing 
[FileHandle](./FileHandle.md) interface is passed ATCmdParser constructor during
ATCmdParser object creation. ATCmdParser also supports configuring 
specific output delimiter character sequence depending upon the 
actual interface/device connected to the communication interface. 

### ATCmdParser class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/classmbed_1_1_a_t_cmd_parser.html)

### Example 1

This shows an example of ATCmdParser usage with UARTSerial driver.

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

### Example 2

Another real world example can be found at WiFi driver implementation 
for [ESP8266 device](https://github.com/ARMmbed/esp8266-driver). ESP8266 is a WiFi module which can be connected to an SoC over UART for WiFi support. 

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/atcmdparser_esp8266.png)<span>The above diagram shows how ESP8266 WiFi driver uses ATCmdParser to communicate with ESP8266 device</span></span>


