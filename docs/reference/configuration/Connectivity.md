## Connectivity

TODO: page for netsocket config options
TODO: page for lwip config options
TODO: page for nanostack config options

```
Configuration parameters
------------------------

Name: ppp-cell-iface.apn-lookup
    Defined by: library:ppp-cell-iface
    No value set
Name: ppp-cell-iface.at-parser-buffer-size
    Defined by: library:ppp-cell-iface
    Macro name: MBED_CONF_PPP_CELL_IFACE_AT_PARSER_BUFFER_SIZE
    Value: 256 (set by library:ppp-cell-iface)
Name: ppp-cell-iface.at-parser-timeout
    Defined by: library:ppp-cell-iface
    Macro name: MBED_CONF_PPP_CELL_IFACE_AT_PARSER_TIMEOUT
    Value: 8000 (set by library:ppp-cell-iface)
Name: ppp-cell-iface.baud-rate
    Defined by: library:ppp-cell-iface
    Macro name: MBED_CONF_PPP_CELL_IFACE_BAUD_RATE
    Value: 115200 (set by library:ppp-cell-iface)

Name: lwip.addr-timeout
    Description: On dual-stack system how long to additionally wait for other stack's address in seconds
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_ADDR_TIMEOUT
    Value: 5 (set by library:lwip)
Name: lwip.addr-timeout-mode
    Description: Address timeout mode; true: wait both stack's addresses; false: wait for preferred stack's address
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_ADDR_TIMEOUT_MODE
    Value: 1 (set by library:lwip)
Name: lwip.debug-enabled
    Description: Enable debug trace support
    Defined by: library:lwip
    No value set
Name: lwip.default-thread-stacksize
    Description: Stack size for lwip system threads
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_DEFAULT_THREAD_STACKSIZE
    Value: 512 (set by library:lwip)
Name: lwip.enable-ppp-trace
    Description: Enable trace support for PPP interfaces
    Defined by: library:lwip
    No value set
Name: lwip.ethernet-enabled
    Description: Enable support for Ethernet interfaces
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_ETHERNET_ENABLED
    Value: 1 (set by library:lwip)
Name: lwip.ip-ver-pref
    Description: On dual-stack system the preferred stack: 4 for IPv4 and 6 for IPv6
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_IP_VER_PREF
    Value: 4 (set by library:lwip)
Name: lwip.ipv4-enabled
    Description: Enable IPv4
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_IPV4_ENABLED
    Value: 1 (set by library:lwip)
Name: lwip.ipv6-enabled
    Description: Enable IPv6
    Defined by: library:lwip
    No value set
Name: lwip.ppp-enabled
    Description: Enable support for PPP interfaces
    Defined by: library:lwip
    No value set
Name: lwip.ppp-ipv4-enabled
    Description: Enable support for ipv4 PPP interface
    Defined by: library:lwip
    Macro name: NSAPI_PPP_IPV4_AVAILABLE
    Value: 1 (set by library:lwip)
Name: lwip.ppp-ipv6-enabled
    Description: Enable support for ipv6 PPP interface
    Defined by: library:lwip
    No value set
Name: lwip.ppp-thread-stacksize
    Description: Thread stack size for PPP
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_PPP_THREAD_STACKSIZE
    Value: 768 (set by library:lwip)
Name: lwip.socket-max
    Description: Maximum number of open TCPServer, TCPSocket and UDPSocket instances allowed, including one used internally for DNS.  Each requires 236 bytes of pre-allocated RAM
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_SOCKET_MAX
    Value: 4 (set by library:lwip)
Name: lwip.tcp-enabled
    Description: Enable TCP
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_TCP_ENABLED
    Value: 1 (set by library:lwip)
Name: lwip.tcp-server-max
    Description: Maximum number of open TCPServer instances allowed.  Each requires 72 bytes of pre-allocated RAM
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_TCP_SERVER_MAX
    Value: 4 (set by library:lwip)
Name: lwip.tcp-socket-max
    Description: Maximum number of open TCPSocket instances allowed.  Each requires 196 bytes of pre-allocated RAM
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_TCP_SOCKET_MAX
    Value: 4 (set by library:lwip)
Name: lwip.tcpip-thread-stacksize
    Description: Stack size for lwip TCPIP thread
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_TCPIP_THREAD_STACKSIZE
    Value: 1200 (set by library:lwip)
Name: lwip.udp-socket-max
    Description: Maximum number of open UDPSocket instances allowed, including one used internally for DNS.  Each requires 84 bytes of pre-allocated RAM
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_UDP_SOCKET_MAX
    Value: 4 (set by library:lwip)
Name: lwip.use-mbed-trace
    Description: Use mbed trace for debug, rather than printf
    Defined by: library:lwip
    No value set
Name: nsapi.present
    Defined by: library:nsapi
    Macro name: MBED_CONF_NSAPI_PRESENT
    Value: 1 (set by library:nsapi)
```
