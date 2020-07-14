# DTLSSocket

<span class="images">![](https://os.mbed.com/docs/mbed-os/v6.2/mbed-os-api-doxy/class_d_t_l_s_socket.png)<span>DTLSSocket class hierarchy</span></span>

`DTLSSocket` and `DTLSSocketWrapper` implement DTLS stream over the existing `Socket` transport. You can find design and implementation details in the [Secure Socket](../apis/secure-socket.html) page.

To use secure DTLS connections, application use the `DTLSSocketWrapper` through the Socket API, so existing applications and libraries are compatible.

`DTLSSocketWrapper` inherits `TLSSocketWrapper` and uses the same API. The only difference is that it uses timers to keep track of DTLS timeouts. Please see [TLSSocket](../apis/tlssocket.html) for an example.

## DTLSSocket class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.2/mbed-os-api-doxy/class_d_t_l_s_socket.html)

## DTLSSocket example

Please see the TLSSocket example:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-tls-socket/blob/mbed-os-6.2.0/)](https://github.com/ARMmbed/mbed-os-example-tls-socket/blob/mbed-os-6.2.0/main.cpp)

## Related content

- [Secure Socket](../apis/secure-socket.html).
- [TLSSocket](../apis/tlssocket.html).
