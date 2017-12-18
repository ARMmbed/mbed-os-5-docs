## Network socket overview

This section covers the main connectivity APIs in Arm Mbed OS, which are:

- <a href="/docs/v5.7/reference/ethernet.html" target="_blank">Ethernet</a>: API for connecting to the internet over an Ethernet connection.
- <a href="/docs/v5.7/reference/wi-fi.html" target="_blank">Wi-Fi</a>: API for connecting to the internet with a Wi-Fi device.
- <a href="/docs/v5.7/reference/cellular-api.html" target="_blank">Cellular</a>: API for connecting to the internet using a cellular device.
- <a href="/docs/v5.7/reference/mesh.html" target="_blank">Mesh networking</a>: Mbed OS provides two kinds of IPv6-based mesh networks - 6LoWPAN_ND and Thread.
- <a href="/docs/v5.7/reference/udpsocket.html" target="_blank">UDPSocket</a>: This class provides the ability to send packets of data over UDP, using the sendto and recvfrom member functions.
- <a href="/docs/v5.7/reference/tcpsocket.html" target="_blank">TCPSocket</a>: This class provides the ability to send a stream of data over TCP.
- <a href="/docs/v5.7/reference/tcpserver.html" target="_blank">TCPServer</a>: This class provides the ability to accept incoming TCP connections.
- <a href="/docs/v5.7/reference/socketaddress.html" target="_blank">SocketAddress</a>: You can use this class to represent the IP address and port pair of a unique network endpoint.

Continue reading for detailed reference material about some of these APIs.

#### Network sockets

The network-socket API provides a common interface for using sockets on network devices. It's a class-based interface, which should be familiar to users experienced with other socket APIs.

##### Network errors

The convention of the network-socket API is for functions to return negative error codes to indicate failure. On success, a function may return zero or a non-negative integer to indicate the size of a transaction. On failure, a function must return a negative integer, which should be one of the error codes in the `nsapi_error_t` <a href="https://os-doc-builder.test.mbed.com/docs/v5.7/mbed-os-api-doxy/group__netsocket.html#gac21eb8156cf9af198349069cdc7afeba" target="_blank">enum</a>):

``` cpp
/** Enum of standardized error codes
 *
 *  Valid error codes have negative values and may
 *  be returned by any network operation.
 *
 *  @enum nsapi_error
 */
enum nsapi_error {
    NSAPI_ERROR_OK                  =  0,        /*!< no error */
    NSAPI_ERROR_WOULD_BLOCK         = -3001,     /*!< no data is not available but call is non-blocking */
    NSAPI_ERROR_UNSUPPORTED         = -3002,     /*!< unsupported functionality */
    NSAPI_ERROR_PARAMETER           = -3003,     /*!< invalid configuration */
    NSAPI_ERROR_NO_CONNECTION       = -3004,     /*!< not connected to a network */
    NSAPI_ERROR_NO_SOCKET           = -3005,     /*!< socket not available for use */
    NSAPI_ERROR_NO_ADDRESS          = -3006,     /*!< IP address is not known */
    NSAPI_ERROR_NO_MEMORY           = -3007,     /*!< memory resource not available */
    NSAPI_ERROR_NO_SSID             = -3008,     /*!< ssid not found */
    NSAPI_ERROR_DNS_FAILURE         = -3009,     /*!< DNS failed to complete successfully */
    NSAPI_ERROR_DHCP_FAILURE        = -3010,     /*!< DHCP failed to complete successfully */
    NSAPI_ERROR_AUTH_FAILURE        = -3011,     /*!< connection to access point failed */
    NSAPI_ERROR_DEVICE_ERROR        = -3012,     /*!< failure interfacing with the network processor */
    NSAPI_ERROR_IN_PROGRESS         = -3013,     /*!< operation (eg connect) in progress */
    NSAPI_ERROR_ALREADY             = -3014,     /*!< operation (eg connect) already in progress */
    NSAPI_ERROR_IS_CONNECTED        = -3015,     /*!< socket is already connected */
    NSAPI_ERROR_CONNECTION_LOST     = -3016,     /*!< connection lost */
    NSAPI_ERROR_CONNECTION_TIMEOUT  = -3017,     /*!< connection timed out */
};
```

##### Nonblocking operation

The network-socket API also supports nonblocking operations. The `set_blocking` member function changes the state of a socket. When a socket is in nonblocking mode, socket operations return `NSAPI_ERROR_WOULD_BLOCK` when a transaction cannot be immediately completed.

To allow efficient use of nonblocking operations, the socket classes provide an `attach` member function to register a callback on socket state changes. When the socket can successfully receive, send or accept, or when an error occurs, the system triggers a callback. It may call the callback spuriously without reason.

The callback may be called in interrupt context and should not perform operations such as receiving and sending calls. Do not make any read or write calls until it is on a thread.

##### Socket

You can use the <a href="/docs/v5.7/mbed-os-api-doxy/class_socket.html" target="_blank">Socket</a> classes for managing network sockets. Once opened, a socket provides a pipe through which data can be sent to and received by a specific endpoint. The type of the instantiated socket indicates the underlying protocol to use. Our Socket classes include UDPSocket, TCPSocket and TCPServer.

##### NetworkInterface

A socket requires a NetworkInterface instance when opened to indicate which NetworkInterface the socket should be created on. The NetworkInterface provides a network stack that implements the underlying socket operations.

Existing network interfaces:

- <a href="/docs/v5.7/reference/ethernet.html" target="_blank">EthInterface</a>.
- <a href="/docs/v5.7/reference/wi-fi.html" target="_blank">WiFiInterface</a>.

##### Example applications

Here are example applications that are built on top of the network-socket API:

* <a href="https://os.mbed.com/teams/sandbox/code/http-example/" target="_blank">HTTP and HTTPS</a>.
* <a href="https://os.mbed.com/teams/mqtt/code/HelloMQTT/" target="_blank">MQTT</a>.
* <a href="https://os.mbed.com/teams/sandbox/code/coap-example/" target="_blank">CoAP</a>.
* <a href="https://os.mbed.com/cookbook/Websockets-Server" target="_blank">Websockets</a>.
* <a href="https://github.com/armmbed/mbed-tcp-ping-pong" target="_blank">TCP ping-pong with a computer</a>.
* <a href="https://github.com/armmbed/mbed-udp-ping-pong" target="_blank">UDP ping-pong with a computer</a>.

##### Example

Here is an example of an HTTP client program. The program brings up Ethernet as the underlying network interface, and uses it to perform an HTTP transaction over a TCPSocket:

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/TCPSocket_Example/)](https://os.mbed.com/teams/mbed_example/code/TCPSocket_Example/file/6b383744246e/main.cpp)

#### Arm Mbed Mesh

The Arm Mbed Mesh API allows the application to use the IPv6 mesh network topologies through the <a href="/docs/v5.7/tutorials/mesh.html#nanostack" target="_blank">Nanostack</a> networking stack.

Mbed OS provides two types of IPv6 based mesh networks:

* 6LoWPAN_ND, loosely following the Zigbee-IP specification.
* Thread, following the specification from Thread Group.

Nanostack is the networking stack which provides both of these protocols. For more information on the stack internals, refer to <a href="/docs/v5.7/tutorials/mesh.html#nanostack" target="_blank">Nanostack documentation</a>. Application developers use Nanostack through Mbed Mesh API.

The application can use the `LoWPANNDInterface` or `ThreadInterface` object for connecting to the mesh network and when successfully connected, the application can use the Mbed C++ socket APIs to create a socket to start communication with a remote peer.

The `NanostackEthernetInterface` is provided for Ethernet.

##### Supported mesh networking modes

Currently, 6LoWPAN-ND (neighbor discovery) and Thread bootstrap modes are supported.

#### Cellular

The <a href="/docs/v5.7/mbed-os-api-doxy/class_cellular_base.html" target="_blank">CellularBase</a> provides a C++ API for connecting to the internet over a Cellular device.

Arm Mbed OS provides a <a href="https://github.com/ARMmbed/mbed-os/tree/master/features/netsocket/cellular/generic_modem_driver" target="_blank">reference implementation of CellularBase</a>.

##### Getting started

1. Choose an <a href="https://os.mbed.com/platforms/?mbed-enabled=15&connectivity=1" target="_blank">Mbed board that supports cellular</a>, such as the <a href="https://os.mbed.com/platforms/u-blox-C027/" target="_blank">UBLOX-C027</a> or <a href="https://os.mbed.com/platforms/MTS-Dragonfly/" target="_blank">MTS-DRAGONFLY</a>.

1. Clone <a href="https://github.com/ARMmbed/mbed-os-example-cellular" target="_blank">`mbed-os-example-cellular`</a>. Follow the instructions in the repository.

    1. Compile the code.
    1. Flash the board.

   You see output similar to the excerpt below:

```

mbed-os-example-cellular, Connecting...


Connection Established.
UDP: Sent 4 Bytes to echo.u-blox.com
Received from echo server 4 Bytes


Success. Exiting

```

##### Basic working principles

You can use and extend a cellular interface in various different ways. For example,

- Using AT commands to control sockets in an existing IP stack built into the cellular modem.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/Cell_AT.png)</span>

- Using a PPP (Point-to-Point Protocol) pipe to pass IP packets between an Mbed OS supported IP stack and cellular modem device.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/Cell_PPP.png)</span>

<a href="https://github.com/ARMmbed/mbed-os-example-cellular" target="_blank">`mbed-os-example-cellular`</a> uses <a href="https://github.com/ARMmbed/mbed-os/tree/master/features/netsocket/cellular/generic_modem_driver" target="_blank">a generic modem driver</a>. In other words, CellularInterface uses PPP. We can summarize this particular design as follows:

- It uses an external IP stack (for example, LWIP) instead of on-chip network stacks.
- The generic modem driver uses standard 3GPP AT 27.007 AT commands to set up the cellular modem and registers to the network.
- After registration, the driver opens up a PPP (Point-to-Point Protocol) pipe using LWIP with the cellular modem and connects to the internet.
