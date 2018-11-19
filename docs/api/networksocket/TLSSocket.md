## TLSSocket

`TLSSocket` and `TLSSocketWrapper` are implementing TLS stream over existing `Socket` transport. Design and implementation details are explained in [Secure Socket](../reference/securesocket.html) page.

For using secure TLS connections, application utilise the `TLSSocketWrapper` through Socket API, so existing applications and libraries should be compatible.

### TLSSocket class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_t_l_s_socket.html)

### TLSSocket Example

TLSSocket example creates TLS connection to HTTPS server and receives a simple response from the server.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/tree/master/TLSSocket)](https://github.com/ARMmbed/mbed-os-examples-docs_only/tree/master/TLSSocket/main.cpp)

### Related content

- [Secure Socket](../reference/securesocket.html)
