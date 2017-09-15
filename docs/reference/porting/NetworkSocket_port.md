### The network socket API

#### New device

The NetworkSocketAPI is designed to make porting new devices as easy as possible and only requires a handful of methods for a minimal implementation.

A new device must implement a [NetworkInterface](https://github.com/ARMmbed/mbed-os/blob/master/features/NetworkSocketAPI/NetworkInterface.h), with the naming convention of **DeviceInterface** - where **Device** is a unique name that represents the device or network processor. 

The **DeviceInterface** should also inherit one of the following (unless it is an abstract device):

* [EthInterface](https://github.com/ARMmbed/mbed-os/blob/master/features/NetworkSocketAPI/EthInterface.h)
* [WiFiInterface](https://github.com/ARMmbed/mbed-os/blob/master/features/NetworkSocketAPI/WiFiInterface.h)
* [CellularInterface](https://github.com/ARMmbed/mbed-os/blob/master/features/NetworkSocketAPI/CellularInterface.h)
* [MeshInterface](https://github.com/ARMmbed/mbed-os/blob/master/features/NetworkSocketAPI/MeshInterface.h)

The **NetworkInterface** implementation provides the following methods:

```
    /** Get the internally stored IP address
    /return     IP address of the interface or null if not yet connected
     */
    virtual const char *get_ip_address() = 0;

    /** Get the stack this interface is bound to
    /return     The stack this interface is bound to or null if not yet connected
     */
    virtual NetworkStack * get_stack(void) = 0;
    
    /** Free NetworkInterface resources
     */
    virtual ~NetworkInterface() {};
```

If a custom stack is required then a device must implement its own [NetworkStack](https://github.com/ARMmbed/mbed-os/blob/master/features/NetworkSocketAPI/NetworkStack.h).

The **NetworkStack** implementation provides the following methods:

```cpp
/** Get the local IP address
 *
 *  @return         Null-terminated representation of the local IP address
 *                  or null if not yet connected
 */
virtual const char *get_ip_address() = 0;

/** Translates a hostname to an IP address
 *
 *  The hostname may be either a domain name or an IP address. If the
 *  hostname is an IP address, no network transactions will be performed.
 *  
 *  If no stack-specific DNS resolution is provided, the hostname
 *  will be resolve using a UDP socket on the stack.
 *
 *  @param address  Destination for the host SocketAddress
 *  @param host     Hostname to resolve
 *  @return         0 on success, negative error code on failure
 */
virtual int gethostbyname(SocketAddress *address, const char *host);

/*  Set stack-specific stack options
 *
 *  The setstackopt allow an application to pass stack-specific hints
 *  to the underlying stack. For unsupported options,
 *  NSAPI_ERROR_UNSUPPORTED is returned and the stack is unmodified.
 *
 *  @param level    Stack-specific protocol level
 *  @param optname  Stack-specific option identifier
 *  @param optval   Option value
 *  @param optlen   Length of the option value
 *  @return         0 on success, negative error code on failure
 */    
virtual int setstackopt(int level, int optname, const void *optval, unsigned optlen);

/*  Get stack-specific stack options
 *
 *  The getstackopt allow an application to retrieve stack-specific hints
 *  from the underlying stack. For unsupported options,
 *  NSAPI_ERROR_UNSUPPORTED is returned and optval is unmodified.
 *
 *  @param level    Stack-specific protocol level
 *  @param optname  Stack-specific option identifier
 *  @param optval   Destination for option value
 *  @param optlen   Length of the option value
 *  @return         0 on success, negative error code on failure
 */    
virtual int getstackopt(int level, int optname, void *optval, unsigned *optlen);

/** Opens a socket
 *
 *  Creates a network socket and stores it in the specified handle.
 *  The handle must be passed to following calls on the socket.
 *
 *  A stack may have a finite number of sockets, in this case
 *  NSAPI_ERROR_NO_SOCKET is returned if no socket is available.
 *
 *  @param handle   Destination for the handle to a newly created socket
 *  @param proto    Protocol of socket to open, NSAPI_TCP or NSAPI_UDP
 *  @return         0 on success, negative error code on failure
 */
virtual int socket_open(void **handle, nsapi_protocol_t proto) = 0;

/** Close the socket
 *
 *  Closes any open connection and deallocates any memory associated
 *  with the socket.
 *
 *  @param handle   Socket handle
 *  @return         0 on success, negative error code on failure
 */
virtual int socket_close(void *handle) = 0;

/** Bind a specific address to a socket
 *
 *  Binding a socket specifies the address and port on which to receive
 *  data. If the IP address is zeroed, only the port is bound.
 *
 *  @param handle   Socket handle
 *  @param address  Local address to bind
 *  @return         0 on success, negative error code on failure.
 */
virtual int socket_bind(void *handle, const SocketAddress &address) = 0;

/** Listen for connections on a TCP socket
 *
 *  Marks the socket as a passive socket that can be used to accept
 *  incoming connections.
 *
 *  @param handle   Socket handle
 *  @param backlog  Number of pending connections that can be queued
 *                  simultaneously
 *  @return         0 on success, negative error code on failure
 */
virtual int socket_listen(void *handle, int backlog) = 0;

/** Connects TCP socket to a remote host
 *
 *  Initiates a connection to a remote server specified by the
 *  indicated address.
 *
 *  @param handle   Socket handle
 *  @param address  The SocketAddress of the remote host
 *  @return         0 on success, negative error code on failure
 */
virtual int socket_connect(void *handle, const SocketAddress &address) = 0;

/** Accepts a connection on a TCP socket
 *
 *  The server socket must be bound and set to listen for connections.
 *  On a new connection, creates a network socket and stores it in the
 *  specified handle. The handle must be passed to following calls on
 *  the socket.
 *
 *  A stack may have a finite number of sockets, in this case
 *  NSAPI_ERROR_NO_SOCKET is returned if no socket is available.
 *
 *  This call is non-blocking. If accept would block,
 *  NSAPI_ERROR_WOULD_BLOCK is returned immediately.
 *
 *  @param handle   Destination for a handle to the newly created socket
 *  @param server   Socket handle to server to accept from
 *  @return         0 on success, negative error code on failure
 */
virtual int socket_accept(void **handle, void *server) = 0;

/** Send data over a TCP socket
 *
 *  The socket must be connected to a remote host. Returns the number of
 *  bytes sent from the buffer.
 *
 *  This call is non-blocking. If send would block,
 *  NSAPI_ERROR_WOULD_BLOCK is returned immediately.
 *
 *  @param handle   Socket handle
 *  @param data     Buffer of data to send to the host
 *  @param size     Size of the buffer in bytes
 *  @return         Number of sent bytes on success, negative error
 *                  code on failure
 */
virtual int socket_send(void *handle, const void *data, unsigned size) = 0;

/** Receive data over a TCP socket
 *
 *  The socket must be connected to a remote host. Returns the number of
 *  bytes received into the buffer.
 *
 *  This call is non-blocking. If recv would block,
 *  NSAPI_ERROR_WOULD_BLOCK is returned immediately.
 *
 *  @param handle   Socket handle
 *  @param data     Destination buffer for data received from the host
 *  @param size     Size of the buffer in bytes
 *  @return         Number of received bytes on success, negative error
 *                  code on failure
 */
virtual int socket_recv(void *handle, void *data, unsigned size) = 0;

/** Send a packet over a UDP socket
 *
 *  Sends data to the specified address. Returns the number of bytes
 *  sent from the buffer.
 *
 *  This call is non-blocking. If sendto would block,
 *  NSAPI_ERROR_WOULD_BLOCK is returned immediately.
 *
 *  @param handle   Socket handle
 *  @param address  The SocketAddress of the remote host
 *  @param data     Buffer of data to send to the host
 *  @param size     Size of the buffer in bytes
 *  @return         Number of sent bytes on success, negative error
 *                  code on failure
 */
virtual int socket_sendto(void *handle, const SocketAddress &address, const void *data, unsigned size) = 0;

/** Receive a packet over a UDP socket
 *
 *  Receives data and stores the source address in address if address
 *  is not NULL. Returns the number of bytes received into the buffer.
 *
 *  This call is non-blocking. If recvfrom would block,
 *  NSAPI_ERROR_WOULD_BLOCK is returned immediately.
 *
 *  @param handle   Socket handle
 *  @param address  Destination for the source address or NULL
 *  @param data     Destination buffer for data received from the host
 *  @param size     Size of the buffer in bytes
 *  @return         Number of received bytes on success, negative error
 *                  code on failure
 */
virtual int socket_recvfrom(void *handle, SocketAddress *address, void *buffer, unsigned size) = 0;

/** Register a callback on state change of the socket
 *
 *  The specified callback will be called on state changes such as when
 *  the socket can recv/send/accept successfully and on when an error
 *  occurs. The callback may also be called spuriously without reason.
 *
 *  The callback may be called in an interrupt context and should not
 *  perform expensive operations such as recv/send calls.
 *
 *  @param handle   Socket handle
 *  @param callback Function to call on state change
 *  @param data     Argument to pass to callback
 */
virtual void socket_attach(void *handle, void (*callback)(void *), void *data) = 0;

/*  Set stack-specific socket options
 *
 *  The setsockopt allow an application to pass stack-specific hints
 *  to the underlying stack. For unsupported options,
 *  NSAPI_ERROR_UNSUPPORTED is returned and the socket is unmodified.
 *
 *  @param handle   Socket handle
 *  @param level    Stack-specific protocol level
 *  @param optname  Stack-specific option identifier
 *  @param optval   Option value
 *  @param optlen   Length of the option value
 *  @return         0 on success, negative error code on failure
 */    
virtual int setsockopt(void *handle, int level, int optname, const void *optval, unsigned optlen);

/*  Get stack-specific socket options
 *
 *  The getstackopt allow an application to retrieve stack-specific hints
 *  from the underlying stack. For unsupported options,
 *  NSAPI_ERROR_UNSUPPORTED is returned and optval is unmodified.
 *
 *  @param handle   Socket handle
 *  @param level    Stack-specific protocol level
 *  @param optname  Stack-specific option identifier
 *  @param optval   Destination for option value
 *  @param optlen   Length of the option value
 *  @return         0 on success, negative error code on failure
 */    
virtual int getsockopt(void *handle, int level, int optname, void *optval, unsigned *optlen);
```

#### Sockets

As a part of implementing the NetworkStack interface, a new device must implement a series of **socket_** functions. A `void *` is provided to pass socket-specific context between these functions. The socket functions are managed by the [Socket](https://github.com/ARMmbed/mbed-os/blob/master/features/NetworkSocketAPI/Socket.cpp) classes and implementation functions are hidden from the user.

#### Errors

The convention for the NetworkSocketAPI is to have functions that may fail and return a signed integer. To indicate success, the function should return a **non-negative integer**, which may also contain the size of a transaction. To indicate failure the function should return a negative integer, which should be one of the following error codes from the **nsapi_error_t** enum:

```cpp
/** Enum of standardized error codes
 *
 *  Valid error codes have negative values and may
 *  be returned by any network operation.
 *
 *  @enum nsapi_error_t
 */
enum nsapi_error_t {
    NSAPI_ERROR_WOULD_BLOCK   = -3001,     /*!< no data is not available but call is non-blocking */
    NSAPI_ERROR_UNSUPPORTED   = -3002,     /*!< unsupported functionality */
    NSAPI_ERROR_PARAMETER     = -3003,     /*!< invalid configuration */
    NSAPI_ERROR_NO_CONNECTION = -3004,     /*!< not connected to a network */
    NSAPI_ERROR_NO_SOCKET     = -3005,     /*!< socket not available for use */
    NSAPI_ERROR_NO_ADDRESS    = -3006,     /*!< IP address is not known */
    NSAPI_ERROR_NO_MEMORY     = -3007,     /*!< memory resource not available */
    NSAPI_ERROR_DNS_FAILURE   = -3008,     /*!< DNS failed to complete successfully */
    NSAPI_ERROR_DHCP_FAILURE  = -3009,     /*!< DHCP failed to complete successfully */
    NSAPI_ERROR_AUTH_FAILURE  = -3010,     /*!< connection to access point failed */
    NSAPI_ERROR_DEVICE_ERROR  = -3011,     /*!< failure interfacing with the network processor */
};
```

#### Testing

When adding new device support, you can use a test harness to verify implementations. The test program is very simple, since it only needs to instantiate the new network interface; all further operations are performed against the managed classes.

[![View code](https://www.mbed.com/embed/?url=https://github.com/iriark01/test_docs)](https://developer.mbed.org/teams/NetworkSocketAPI/code/ESP8266InterfaceTests/file/tip/main.cpp)

```cpp
// replace 0.0.0.0 with the ip address of the host pc running the echo_server.py script
nsapi_tests("ESP8266Interface Tests", &iface, "0.0.0.0", 4000);
```

The test harness library is **NSAPITests.** It relies on a Python echo server, which is also part of that repo. Make sure to change the IP address in the interface test program to point at the computer that is running the script.

[![View code](https://www.mbed.com/embed/?url=https://github.com/iriark01/test_docs)](https://developer.mbed.org/teams/components/code/ESP8266InterfaceTests/)

#### References

- The [ESP8266Interface](https://github.com/ARMmbed/esp8266-driver) class and header.
- The [EthernetInterface](https://github.com/ARMmbed/mbed-os/tree/master/features/FEATURE_IPV4/LWIPInterface) class and header.
