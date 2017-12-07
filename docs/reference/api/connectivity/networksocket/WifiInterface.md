## Wi-Fi

The WifiInterface provides a simple C++ API for connecting to the internet over a Wi-Fi device.

There are multiple <a href="https://os.mbed.com/components/cat/wifi/" target="_blank">Wi-Fi components</a> that implement the WiFiInterface class. The example below uses the <a href="https://github.com/armmbed/esp8266-driver" target="_blank">ESP8266Interface</a>.

### Wi-Fi class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.7/mbed-os-api-doxy/class_wi_fi_interface.html)

### Usage

To bring up the network interface:

1. Instantiate an implementation of the WiFiInterface class (for example, the ESP8266Interface).
1. Call the `connect` function with an SSID and password for the Wi-Fi network.
1. Once connected, the WiFiInterface can be used as a target for opening <a href="/docs/v5.7/reference/network-socket.html" target="_blank">network sockets</a>.

### Wi-Fi example

Here is an example of an HTTP client program. The program brings up an ESP8266 as the underlying network interface, and uses it to perform an HTTP transaction over a TCPSocket:

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/TCPSocketWiFi_Example/)](https://os.mbed.com/teams/mbed_example/code/TCPSocketWiFi_Example/file/6a4e57edc2b2/main.cpp)

### Related content

- <a href="https://os.mbed.com/components/cat/wifi/" target="_blank">Wi-Fi components</a>.
- <a href="/docs/v5.7/reference/network-socket.html" target="_blank">Network socket</a> API overview.
