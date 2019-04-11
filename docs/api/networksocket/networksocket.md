<h1 id="network-socket">Network socket overview</h1>

The application programming interface for IP networking is the Socket API. As described in the [IP networking](../reference/ip-networking.html) section, the Socket API relates to OSI layer 4, the Transport layer. In Mbed OS, the Socket API is abstract and supports various protocols such as TCP, UDP and non-IP data delivery for NB-IoT cellular networks.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/ip-networking.png)<span>Sockets</span></span>

In Mbed OS, this socket API is C++ based but closely follows the functionality from the POSIX standard (IEEE Std 1003.1) and relevant RFC standards. The Socket interface is abstract and protocol agnostic and requires you to specify the protocol only when creating the socket. With libraries and interfaces, you may use the abstract base class, which allows you to port applications from one protocol to another.

## General use

The following steps describe the typical application flow:

1. Initialize a network interface.
1. Create a socket.
1. Connect (optional step for datagram protocols).
1. Send data.
1. Receive data.
1. Close the socket.

The following code demonstrates those steps by sending an HTTP query to a server:

```
// Initialize network interface
EthernetInterface eth;
eth.connect();

// Create a socket
TCPSocket sock;
sock.open(&eth);

// Connect
sock.connect("arm.com", 80);

// Send data
sock.send("GET / HTTP/1.0\r\n\r\n", 18);

// Receive data
char buf[100];
sock.recv(buf, 100);

// Close the socket
sock.close();
```

## Changes in Mbed OS 5.10

The 5.10 release refactors the Mbed OS Socket API. For most of the applications, these changes are not noticeable because the `TCPSocket` and `UDPSocket` classes still emulate legacy behavior.

The new design contains an abstract socket interface that applications can use directly. Casting `Socket` pointers back to `TCPSocket` or `UDPSocket` is no longer necessary.

Upcasting any protocol specific class to `Socket` has no side effect and is a recommended API design. Knowing the exact type is only required when you create the socket.

The new design also emphasizes use of `SocketAddress` for holding the IP addresses, instead on textual format. `SocketAddress` is a container class that protocols other than IP can use in the future. Legacy string versions of `connect()`, `bind()` and `sendto()` functions do not exist in the `Socket` base class, but they exist in `TCPSocket` and `UDPSocket` classes.

The new design also renders the TCPServer API unnecessary, moving its functionality directly into TCPSocket itself. The legacy TCPServer class still exists and is fully functional.

## Using DNS names

IP stacks operate only on binary IP addresses, but in Internet, servers are known by their symbolic domain name (DNS). To use these names with Socket interface, each name has to be resolved before.

Previously Socket interface contained methods that can directly accept DNS names and port numbers and do the resolving internally. These APIs are not recommended as they might hide problems in DNS system.

Recommended way is to use [DNS resolver](dns-resolver.html) to convert symbolic names to IP addresses. The following example shows how to use DNS in Mbed OS:

```
NetworkInteface *net;    // Initialized elsewhere

SocketAddress addr;
nsapi_error_t ret = net->gethostbyname("www.arm.com", &addr);  // Resolve www.arm.com and store into addr

if (ret == NSAPI_ERROR_OK) {
    // Resolving was succesfull
}
```

See [DNS resolver](dns-resolver.html) for more information.

## Server sockets

Some connection oriented protocols, for example TCP, can also be used for listening incomming connections. To do this

1. Bind socket to specific port by calling `Socket::bind()`
1. Set socket to listening mode by calling `Socket::listen()`
1. Accept incomming connection by calling `Socket::accept()`

Accepting new connection return you a pointer to a new `Socket` object that can be used to communicate with the connected peer. When done, you should call this socket's `close()` function to shut down the connection and clean up the reserved resources.

Accepting a connection will leave the original socket to listening mode. You can continue to accept new connections until you destroy the listening socket, or call its `close()` method.

For connectionless protocols, like UDP, each socket can receive from any peer. Therefore `listen()` and `accept()` are not required.

## Network socket interfaces and classes

The network socket API provides a common interface for using sockets on network devices. It's a class-based interface, which is familiar to users experienced with other socket APIs.

- [Socket](socket.html): Abstract base class for all protocols. Specifies the API.
- [UDPSocket](udpsocket.html): This class provides the ability to send packets of data over UDP.
- [TCPSocket](tcpsocket.html): This class provides the ability to send a stream of data over TCP.
- [SocketAddress](socketaddress.html): You can use this class to represent the IP address and port pair of a unique network endpoint.
- [CellularNonIPSocket](../apis/non-ip-cellular-socket.html): This class provides the ability to send and receive 3GPP non-IP datagrams (NIDD) using the cellular IoT feature.
- [Network status](network-status.html): API for monitoring network status changes.
- [DNS resolver](dns-resolver.html): API for resolving DNS names

## Network errors

The convention of the network socket API is for functions to return negative error codes to indicate failure. On success, a function may return zero or a non-negative integer to indicate the size of a transaction. On failure, a function must return a negative integer, which is one of the error codes in the `nsapi_error_t` [enum](../mbed-os-api-doxy/group__netsocket.html#gac21eb8156cf9af198349069cdc7afeba):

``` cpp NOCI
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

## Nonblocking operation

The network socket API also supports nonblocking operations. The `set_blocking()` member function changes the state of a socket. When a socket is in nonblocking mode, socket operations return `NSAPI_ERROR_WOULD_BLOCK` when a transaction cannot immediately complete.

To allow efficient use of nonblocking operations, the socket classes provide a `sigio()` member function to register a callback on socket state changes. When the socket can successfully receive, send or accept or when an error occurs, the system triggers a callback. It may call the callback spuriously without reason.

You may call the callback in interrupt context, but do not make any read or write calls until it is on a thread.

The following example shows how to set up an asynchronous handler for socket:

```
nsapi_size_or_error_t send_query(TCPSocket *socket) {
    return socket->send(QUERY, QUERY_LEN);
}

nsapi_size_or_error_t receive_data(TCPSocket *socket) {
    // Simplified example, does not properly handle streaming and appending to buffer
    return socket->recv(my_buffer, remaining_len);
}

void handle_socket_sigio(EventFlags *evt, TCPSocket *socket)
{
    static enum {
        CONNECTING,
        SEND,
        RECEIVE,
        CLOSE,
    } next_state = CONNECTING;

    switch (next_state) {
        case CONNECTING:
            switch(socket->connect("api.ipify.org", 80)) {
                case NSAPI_ERROR_IN_PROGRESS:
                    // Connecting to server
                    break;
                case NSAPI_ERROR_ALREADY:
                    // Now connected to server
                    next_state = SEND;
                    break;
                default:
                    // Error in connection phase
                    next_state = CLOSE;
            }
        case SEND:
            if (send_query(socket) > 0)
                next_state = RECEIVE;
            else
                next_state = CLOSE; // Error
            break;
        case RECEIVE:
            if (receive_data(socket) == NSAPI_ERROR_WOULD_BLOCK)
                break;
            next_state = CLOSE;
            break;
        case CLOSE:
            socket->close();
            evt->set(1); // Signal the main thread
            break;
    }
}

int main() {
    EthernetInterface net;
    net.connect();

    TCPSocket socket;
    socket.open(&net);

    EventFlags completed;
    EventQueue *queue = mbed_event_queue();

    Event<void()> handler = queue->event(handle_socket_sigio, &completed, &socket);

    socket.set_blocking(false);
    socket.sigio(handler);
    handler();                   // Kick the state machine to start connecting

    completed.wait_any(1);
}
```
