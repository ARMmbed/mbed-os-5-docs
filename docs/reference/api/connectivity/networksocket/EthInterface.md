## Ethernet

The EthInterface provides a C++ API for connecting to the internet over Ethernet.

### EthInterface class reference

[![View code](http://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/v5.7/mbed-os-api-doxy/class_eth_interface.html)

### Usage

To bring up the network interface:

1. Instantiate the `EthInterface` class.
1. Call the `connect` function.
1. Once you connect the EthInterface, you can use it as a
target for opening <a href="/docs/v5.7/reference/network-socket.html" target="_blank">network sockets</a>.

### EthInterface example

Here is an example of an HTTP client program. The program brings up Ethernet as the underlying network interface and uses it to perform an HTTP transaction over a TCPSocket:

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/TCPSocket_Example/)](https://os.mbed.com/teams/mbed_example/code/TCPSocket_Example/file/6b383744246e/main.cpp)

### Related content

- <a href="/docs/v5.7/reference/network-socket.html" target="_blank">Network socket</a> API reference overview.
