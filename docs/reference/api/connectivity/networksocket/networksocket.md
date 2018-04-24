<h2 id="network-socket">Network socket overview</h2>

This section covers the Socket APIs in Arm Mbed OS, which are:

- [UDPSocket](udpsocket.html): This class provides the ability to send packets of data over UDP, using the sendto and recvfrom member functions.
- [TCPSocket](tcpsocket.html): This class provides the ability to send a stream of data over TCP.
- [TCPServer](tcpserver.html): This class provides the ability to accept incoming TCP connections.
- [SocketAddress](socketaddress.html): You can use this class to represent the IP address and port pair of a unique network endpoint.

Continue reading for detailed reference material about some of these APIs.

#### Network sockets

The network-socket API provides a common interface for using sockets on network devices. It's a class-based interface, which should be familiar to users experienced with other socket APIs.

##### Network errors

The convention of the network-socket API is for functions to return negative error codes to indicate failure. On success, a function may return zero or a non-negative integer to indicate the size of a transaction. On failure, a function must return a negative integer, which should be one of the error codes in the `nsapi_error_t` [enum](/docs/development/mbed-os-api-doxy/group__netsocket.html#gac21eb8156cf9af198349069cdc7afeba):

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

You can use the [Socket](/docs/development/mbed-os-api-doxy/class_socket.html) classes for managing network sockets. Once opened, a socket provides a pipe through which data can be sent to and received by a specific endpoint. The type of the instantiated socket indicates the underlying protocol to use. Our Socket classes include UDPSocket, TCPSocket and TCPServer.

##### Example applications

Here are example applications that are built on top of the network-socket API:

- [HTTP and HTTPS](https://os.mbed.com/teams/sandbox/code/http-example/).
- [MQTT](https://os.mbed.com/teams/mqtt/code/HelloMQTT/).
- [CoAP](https://os.mbed.com/teams/sandbox/code/coap-example/).
- [Websockets](https://os.mbed.com/cookbook/Websockets-Server).
- [TCP ping-pong with a computer](https://github.com/armmbed/mbed-tcp-ping-pong).
- [UDP ping-pong with a computer](https://github.com/armmbed/mbed-udp-ping-pong).

##### Example

Here is an example of an HTTP client program. The program brings up Ethernet as the underlying network interface, and uses it to perform an HTTP transaction over a TCPSocket:

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/TCPSocket_Example/)](https://os.mbed.com/teams/mbed_example/code/TCPSocket_Example/file/6b383744246e/main.cpp)
