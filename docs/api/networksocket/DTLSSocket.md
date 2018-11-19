## DTLSSocket

`DTLSSocket` and `DTLSSocketWrapper` are implementing DTLS stream over existing `Socket` transport. Design and implementation details are explained in [Secure Socket](../reference/securesocket.html) page.

For using secure DTLS connections, application utilise the `DTLSSocketWrapper` through Socket API, so existing applications and libraries should be compatible.

`DTLSSocketWrapper` is inheriting `TLSSocketWrapper` and uses exactly same API. Only difference is that it uses timers for keeping track of DTLS timeouts. See TLSSocket for usage example.

### DTLSSocket class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_d_t_l_s_socket.html)

### Related content

- [Secure Socket](../reference/securesocket.html)
- [TLSSocket](tlssocket.html)
