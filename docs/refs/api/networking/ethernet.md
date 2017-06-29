### Ethernet

The [EthernetInterface](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classEthernetInterface.html) provides a C++ API for connecting to the internet over an Ethernet connection.

#### API

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classEthernetInterface.html)

#### Usage

To bring up the network interface:

1. Instantiate the ``EthernetInterface`` class.
1. Call the ``connect`` function.
1. Once you connect the EthernetInterface, you can use it as a
target for opening [network sockets](network_sockets.md).

#### Example

Here is an example of an HTTP client program. The program brings up Ethernet as the underlying network interface, and uses it to perform an HTTP transaction over a TCPSocket:

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/TCPSocket_Example/)](https://developer.mbed.org/teams/mbed_example/code/TCPSocket_Example/file/6b383744246e/main.cpp)
