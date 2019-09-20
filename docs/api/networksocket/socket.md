# Socket

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/class_socket.png)<span>Socket class hierarchy</span></span>

Socket is the abstract base class for all of the protocol-specific socket types. It defines all of the functions that comprise the Mbed OS Socket API. You cannot directly create a Socket object because it is abstract, but you can upcast any protocol-specific object to an abstract Socket object.

You can use this interface when designing portable application interfaces that do not require specific protocol to be defined. For example, instead of using `TCPSocket*` in methods, the application can use `Socket*` to allow either UDP or TCP to work, or even TLS.

The Socket class defines the Mbed OS Socket API and loosely follows the POSIX standard ([IEEE Std 1003.1](http://pubs.opengroup.org/onlinepubs/9699919799/)). The following table lists the methods from the Socket API and their relevant POSIX standards:

| Method | Description | POSIX standard |
|--------|-------------|----------------|
| `Socket::connect()`  | Connect socket to a remote address | [connect](http://pubs.opengroup.org/onlinepubs/9699919799/functions/connect.html) |
| `Socket::close`      | Closes any open connection and deallocates any memory associated with the socket | [close](http://pubs.opengroup.org/onlinepubs/9699919799/functions/close.html) |
| `Socket::send()`     | Send data over a socket | [send](http://pubs.opengroup.org/onlinepubs/9699919799/functions/send.html) |
| `Socket::recv()`     | Receive data from a socket | [recv](http://pubs.opengroup.org/onlinepubs/9699919799/functions/recv.html) |
| `Socket::sendto()`   | Sends data to the specified address. | [sendto](http://pubs.opengroup.org/onlinepubs/9699919799/functions/sendto.html) |
| `Socket::recvfrom()` | Receives data and stores the source address | [recvfrom](http://pubs.opengroup.org/onlinepubs/9699919799/functions/recvfrom.html) |
| `Socket::bind()`     | Bind a specific address to a socket | [bind](http://pubs.opengroup.org/onlinepubs/9699919799/functions/bind.html) |
| `Socket::listen()`   | Listen for incoming connections | [listen](http://pubs.opengroup.org/onlinepubs/9699919799/functions/listen.html) |
| `Socket::accept()`   | Accept incoming connection | [accept](http://pubs.opengroup.org/onlinepubs/9699919799/functions/accept.html) |
| `Socket::setsockopt()` | Set the socket options | [setsockopt](http://pubs.opengroup.org/onlinepubs/9699919799/functions/setsockopt.html) |
| `Socket::getsockopt()` | Get the socket options | [getsockopt](http://pubs.opengroup.org/onlinepubs/9699919799/functions/getsockopt.html) |

Not all protocols implement every function from the Socket API. For example, UDP does not implement the `listen()` and `accept()` functions. Also, socket options are mostly specific to the IP stack; they are not implemented on all stacks.

## Socket class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/class_socket.html)

## Socket example

Here is a client example of HTTP transaction over TCPSocket:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-sockets)](https://github.com/ARMmbed/mbed-os-example-tls-socket/blob/mbed-os-5.14/main.cpp)

## Related content

- [TCPSocket](tcpsocket.html) API reference.
- [UDPSocket](tcpsocket.html) API reference.
- [Socket](../reference/ip-networking.html#socket-api) architecture.
