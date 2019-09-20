# TLSSocket

<span class="images">![](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_t_l_s_socket.png)<span>TLSSocket class hierarchy</span></span>

`TLSSocket` and `TLSSocketWrapper` implement TLS stream over the existing `Socket` transport. You can find design and implementation details in the [SecureSocket](../reference/secure-socket.html) page.

To use secure TLS connections, the application uses the `TLSSocketWrapper` through the Socket API, so existing applications and libraries are compatible.

## TLSSocket class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/class_t_l_s_socket.html)

## TLSSocket example

The TLSSocket example creates TLS connection to the HTTPS server and receives a simple response from the server:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-tls-socket/blob/master/)](https://github.com/ARMmbed/mbed-os-example-tls-socket/blob/mbed-os-5.14/main.cpp)

## Related content

- [SecureSocket](../reference/secure-socket.html).
