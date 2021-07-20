# SocketAddress

Use the SocketAddress class to represent the IP address and port pair of a unique network endpoint. Most network functions are also overloaded to accept string representations of IP addresses, but you can use SocketAddress to avoid the overhead of parsing IP addresses during repeated network transactions, and you can pass it around as a first class object.

## SocketAddress class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.13/mbed-os-api-doxy/class_socket_address.html)

## SocketAddress example

Here is an example to read current UTC time. This example uses the SocketAddress class to get the server IP address and port.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-UDPSocket/tree/v6/13)](https://github.com/ARMmbed/mbed-os-snippet-UDPSocket/blobl/v6/13/main.cpp)

## Related content

- [IP networking architecture](../apis/connectivity-architecture.html).
