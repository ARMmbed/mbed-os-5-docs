<h2 id="configuration-connectivity">Connectivity</h2>

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

Name: mbed-mesh-api.6lowpan-nd-channel
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_6LOWPAN_ND_CHANNEL
    Value: 12 (set by library:mbed-mesh-api)
Name: mbed-mesh-api.6lowpan-nd-channel-mask
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_6LOWPAN_ND_CHANNEL_MASK
    Value: (1<<12) (set by library:mbed-mesh-api)
Name: mbed-mesh-api.6lowpan-nd-channel-page
    Defined by: library:mbed-mesh-api
    No value set
Name: mbed-mesh-api.6lowpan-nd-device-type
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_6LOWPAN_ND_DEVICE_TYPE
    Value: NET_6LOWPAN_ROUTER (set by library:mbed-mesh-api)
Name: mbed-mesh-api.6lowpan-nd-panid-filter
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_6LOWPAN_ND_PANID_FILTER
    Value: 0xffff (set by library:mbed-mesh-api)
Name: mbed-mesh-api.6lowpan-nd-psk-key
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_6LOWPAN_ND_PSK_KEY
    Value: {0xa0, 0xa1, 0xa2, 0xa3, 0xa4, 0xa5, 0xa6, 0xa7, 0xa8, 0xa9, 0xaa, 0xab, 0xac, 0xad, 0xae, 0xaf} (set by library:mbed-mesh-api)
Name: mbed-mesh-api.6lowpan-nd-psk-key-id
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_6LOWPAN_ND_PSK_KEY_ID
    Value: 1 (set by library:mbed-mesh-api)
Name: mbed-mesh-api.6lowpan-nd-sec-level
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_6LOWPAN_ND_SEC_LEVEL
    Value: 5 (set by library:mbed-mesh-api)
Name: mbed-mesh-api.6lowpan-nd-security-mode
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_6LOWPAN_ND_SECURITY_MODE
    Value: NONE (set by library:mbed-mesh-api)
Name: mbed-mesh-api.heap-size
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_HEAP_SIZE
    Value: 32500 (set by library:mbed-mesh-api)
Name: mbed-mesh-api.thread-config-channel
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_THREAD_CONFIG_CHANNEL
    Value: 22 (set by library:mbed-mesh-api)
Name: mbed-mesh-api.thread-config-channel-mask
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_THREAD_CONFIG_CHANNEL_MASK
    Value: 0x7fff800 (set by library:mbed-mesh-api)
Name: mbed-mesh-api.thread-config-channel-page
    Defined by: library:mbed-mesh-api
    No value set
Name: mbed-mesh-api.thread-config-commissioning-dataset-timestamp
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_THREAD_CONFIG_COMMISSIONING_DATASET_TIMESTAMP
    Value: 0x10000 (set by library:mbed-mesh-api)
Name: mbed-mesh-api.thread-config-extended-panid
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_THREAD_CONFIG_EXTENDED_PANID
    Value: {0xf1, 0xb5, 0xa1, 0xb2,0xc4, 0xd5, 0xa1, 0xbd } (set by library:mbed-mesh-api)
Name: mbed-mesh-api.thread-config-ml-prefix
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_THREAD_CONFIG_ML_PREFIX
    Value: {0xfd, 0x0, 0x0d, 0xb8, 0x0, 0x0, 0x0, 0x0} (set by library:mbed-mesh-api)
Name: mbed-mesh-api.thread-config-network-name
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_THREAD_CONFIG_NETWORK_NAME
    Value: "Thread Network" (set by library:mbed-mesh-api)
Name: mbed-mesh-api.thread-config-panid
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_THREAD_CONFIG_PANID
    Value: 0x0700 (set by library:mbed-mesh-api)
Name: mbed-mesh-api.thread-config-pskc
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_THREAD_CONFIG_PSKC
    Value: {0xc8, 0xa6, 0x2e, 0xae, 0xf3, 0x68, 0xf3, 0x46, 0xa9, 0x9e, 0x57, 0x85, 0x98, 0x9d, 0x1c, 0xd0} (set by library:mbed-mesh-api)
Name: mbed-mesh-api.thread-device-type
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_THREAD_DEVICE_TYPE
    Value: MESH_DEVICE_TYPE_THREAD_ROUTER (set by library:mbed-mesh-api)
Name: mbed-mesh-api.thread-master-key
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_THREAD_MASTER_KEY
    Value: {0x10, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff} (set by library:mbed-mesh-api)
Name: mbed-mesh-api.thread-pskd
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_THREAD_PSKD
    Value: "abcdefghijklmno" (set by library:mbed-mesh-api)
Name: mbed-mesh-api.thread-security-policy
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_THREAD_SECURITY_POLICY
    Value: 255 (set by library:mbed-mesh-api)
Name: mbed-mesh-api.thread-use-static-link-config
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_THREAD_USE_STATIC_LINK_CONFIG
    Value: 1 (set by library:mbed-mesh-api)
Name: mbed-mesh-api.use-malloc-for-heap
    Defined by: library:mbed-mesh-api
    No value set
```
