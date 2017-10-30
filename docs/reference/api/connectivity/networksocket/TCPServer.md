## TCPServer

The TCPServer class provides the ability to accept incoming TCP connections. The `listen` member function sets up the server to listen for incoming connections, and the `accept` member function sets up a stateful TCPSocket instance on an incoming connection.

The constructor takes in the NetworkStack pointer to open the socket on the specified NetworkInterface. If you do not pass the NetworkStack pointer in the constructor, then you must call open to initialize the socket.

Refer to [TCPSocket](/docs/v5.6/reference/tcpsocket.html) class for TCP `connect`, `send` and `recv` API's.

### TCPServer class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_t_c_p_server.html)

### TCPServer example

Here is a TCP server example. It accepts single telnet client connection and sends buffer data.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/mbed-os-example-tcp-server/)](https://os.mbed.com/teams/mbed_example/code/mbed-os-example-tcp-server/file/ddb5698aa782/main.cpp)
