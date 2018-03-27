## TCPSocket

The TCPSocket class provides the ability to send a stream of data over TCP. TCPSockets maintain a stateful connection that starts with the `connect` member function. After successfully connecting to a server, you can use the `send` and `recv` member functions to send and receive data (similar to writing or reading from a file).

The constructor takes in the NetworkStack pointer to open the socket on the specified NetworkInterface. If you do not pass in the constructor, then you must call `open` to initialize the socket.

Refer to [TCPServer](/docs/v5.7/reference/tcpserver.html) class for TCP server functionality.

### TCPSocket class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.7/mbed-os-api-doxy/class_t_c_p_socket.html)

### TCPSocket Example

Here is a TCP client example of HTTP transaction using the ESP8266 module.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/TCPSocketWiFi_Example/)](https://os.mbed.com/teams/mbed_example/code/TCPSocketWiFi_Example/file/6a4e57edc2b2/main.cpp)

Here is a TCP client example of HTTP transaction over Ethernet interface.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/TCPSocket_Example/)](https://os.mbed.com/teams/mbed_example/code/TCPSocket_Example/file/6b383744246e/main.cpp)

### Related content

- [TCPServer](/docs/v5.7/reference/tcpserver.html) API reference.
