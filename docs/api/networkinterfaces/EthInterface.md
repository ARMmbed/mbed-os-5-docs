# Ethernet

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/class_eth_interface.png)<span>EthInterface class hierarchy</span></span>

The `EthInterface` provides a C++ API for connecting to the internet over Ethernet.
By default, this class does not require any configuration. It is able to pick up the default
Ethernet driver for the target and select correct network stack.


## Usage

To statically initialize the driver, create an object without passing any parameters:

```cpp TODO
EthernetInterface eth;
```

Then, if the default configuration is enough, bring up the interface:

```cpp TODO
nsapi_error_t status = eth.connect();
```

Now, the interface is ready to be used for [network sockets](network-socket.html).

```cpp TODO
// Open a TCP socket
TCPSocket socket;
socket.open(&eth);

// Open a UDP socket
UDPSocket socket;
socket.open(&eth);
```

## Configuration

For EthernetInterface, there are two possible configurations:

- Use DHCP for network addressing. This is the default.
- Use statically configured IP addresses.

Refer to the API below for how to set the IP addresses by calling the `set_network()` function.

## Troubleshooting information

Network interface `connect` failure causes:

- `NSAPI_ERROR_NO_CONNECTION` indicates that the Ethernet link up has failed. Check that the Ethernet connection is working.
- `NSAPI_ERROR_DHCP_FAILURE` indicates that acquiring the IP address has failed. Check that the IP address configuration service is working.

## EthInterface class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/class_eth_interface.html)

## EthInterface example

Here is an example of an HTTP client program. The program brings up Ethernet as the underlying network interface and uses it to perform an HTTP transaction over a TCPSocket:

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/TCPSocket_Example/)](https://os.mbed.com/teams/mbed_example/code/TCPSocket_Example/file/50f1485931f1/main.cpp)

## Related content

- [Network socket](network-socket.html) API reference overview.
- [Ethernet architecture](../reference/ethernet-technology.html).
