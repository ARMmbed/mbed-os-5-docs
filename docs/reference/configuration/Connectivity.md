<h1 id="configuration-connectivity">Connectivity</h1>

This page describes build-time configurable parameters for connectivity in Mbed OS.

<span class="notes">**Note:** You can find settings for Mesh networking under [6LoWPAN and Thread Mesh](configuration-mesh.html).</span>

This is the complete list of connectivity configuration parameters. To view all configuration parameters, run the `--config -v` command. Please see [the configuration system documentation](configuration.html) for details on how you may use or override these settings.

```
Configuration parameters
------------------------
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
Name: lwip.mem-size
    Description: Size of heap (bytes) - used for outgoing packets, and also used by some drivers for reception. Current default (used if null here) is set to 1600 in opt.h, unless overridden by target Ethernet drivers.
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_MEM_SIZE
    Value: 33270 (set by library:lwip[Freescale])
Name: lwip.memp-num-tcp-seg
    Description: Number of simultaneously queued TCP segments. Current default (used if null here) is set to 16 in opt.h, unless overridden by target Ethernet drivers.
    Defined by: library:lwip
    No value set
Name: lwip.pbuf-pool-bufsize
    Description: Size of pbufs in pool. If set to null, lwIP will base the size on the TCP MSS, which is 536 unless overridden by the target
    Defined by: library:lwip
    No value set
Name: lwip.pbuf-pool-size
    Description: Number of pbufs in pool - usually used for received packets, so this determines how much data can be buffered between reception and the application reading. If a driver uses PBUF_RAM for reception, less pool may be needed. Current default (used if null here) is set to 5 in lwipopts.h, unless overridden by target Ethernet drivers.
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
Name: lwip.tcp-maxrtx
    Description: Maximum number of retransmissions of data segments.
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_TCP_MAXRTX
    Value: 6 (set by library:lwip)
Name: lwip.tcp-mss
    Description: TCP Maximum segment size. Current default (used if null here) is set to 536 in opt.h, unless overridden by target Ethernet drivers.
    Defined by: library:lwip
    No value set
Name: lwip.tcp-server-max
    Description: Maximum number of open TCPServer instances allowed.  Each requires 72 bytes of pre-allocated RAM
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_TCP_SERVER_MAX
    Value: 4 (set by library:lwip)
Name: lwip.tcp-snd-buf
    Description: TCP sender buffer space (bytes). Current default (used if null here) is set to (2 * TCP_MSS) in opt.h, unless overridden by target Ethernet drivers.
    Defined by: library:lwip
    No value set
Name: lwip.tcp-socket-max
    Description: Maximum number of open TCPSocket instances allowed.  Each requires 196 bytes of pre-allocated RAM
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_TCP_SOCKET_MAX
    Value: 4 (set by library:lwip)
Name: lwip.tcp-synmaxrtx
    Description: Maximum number of retransmissions of SYN segments. Current default (used if null here) is set to 6 in opt.h
    Defined by: library:lwip
    No value set
Name: lwip.tcp-wnd
    Description: TCP sender buffer space (bytes). Current default (used if null here) is set to (4 * TCP_MSS) in opt.h, unless overridden by target Ethernet drivers.
    Defined by: library:lwip
    No value set
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
```

## Selecting the default network interface

Applications can use the default network interface without directly specifying its type. This requires settings from `mbed_app.json` to work.

Example application code can be as simple as:

```
    NetworkInterface *net = NetworkInterface::get_default_instance();
    if (!net) {
        // There is no default...
    }
    net->connect();
```

Boards that provide only Ethernet connectivity do not require any configuration. The default settings are sufficient. Boards that provide other connectivity options require selecting the default interface type and providing settings for it.

Select the default interface type by using one of the following `target.network-default-interface-type` parameters:

| `target.network-default-interface-type` | Configuration parameters |
|-----------------------------------------|------------------------|
| `ETHERNET` | nothing |
| `WIFI`     | `nsapi.default-wifi-security`, `nsapi.default-wifi-ssid` and `nsapi.default-wifi-password` |
| `CELLULAR` | `nsapi.default-cellular-sim-pin`, `nsapi.default-cellular-apn`, `nsapi.default-cellular-username` and `nsapi.default-cellular-password`, `nsapi.default-cellular-plmn` |
| `MESH`     | `nsapi.default-mesh-type` |

```
Configuration parameters
------------------------
Name: target.boot-stack-size
    Description: Define the boot stack size in bytes. This value must be a multiple of 8
    Defined by: target:Target
    Macro name: MBED_CONF_TARGET_BOOT_STACK_SIZE
    Value: 0x400 (set by library:rtos[*])
Name: target.console-uart-flow-control
    Description: Console hardware flow control. Options: null, RTS, CTS, RTSCTS.
    Defined by: target:Target
    No value set
Name: target.deep-sleep-latency
    Description: Time in ms required to go to and wake up from deep sleep (max 10)
    Defined by: target:Target
    No value set
Name: target.mpu-rom-end
    Description: Last address of ROM protected by the MPU
    Defined by: target:Target
    Macro name: MBED_CONF_TARGET_MPU_ROM_END
    Value: 0x0fffffff (set by target:Target)
Name: target.network-default-interface-type
    Description: Default network interface type. Typical options: null, ETHERNET, WIFI, CELLULAR, MESH
    Defined by: target:Target
    Macro name: MBED_CONF_TARGET_NETWORK_DEFAULT_INTERFACE_TYPE
    Value: ETHERNET (set by target:K64F)
```

```
Configuration parameters
------------------------
Name: nsapi.default-cellular-apn
    Defined by: library:nsapi
    No value set
Name: nsapi.default-cellular-password
    Defined by: library:nsapi
    No value set
Name: nsapi.default-cellular-plmn
    Defined by: library:nsapi
    No value set
Name: nsapi.default-cellular-sim-pin
    Defined by: library:nsapi
    No value set
Name: nsapi.default-cellular-username
    Defined by: library:nsapi
    No value set
Name: nsapi.default-mesh-type
    Description: Configuration type for MeshInterface::get_default_instance(). [LOWPAN/THREAD]
    Defined by: library:nsapi
    Macro name: MBED_CONF_NSAPI_DEFAULT_MESH_TYPE
    Value: THREAD (set by library:nsapi)
Name: nsapi.default-stack
    Defined by: library:nsapi
    Macro name: MBED_CONF_NSAPI_DEFAULT_STACK
    Value: LWIP (set by library:nsapi)
Name: nsapi.default-wifi-password
    Defined by: library:nsapi
    No value set
Name: nsapi.default-wifi-security
    Defined by: library:nsapi
    Macro name: MBED_CONF_NSAPI_DEFAULT_WIFI_SECURITY
    Value: NONE (set by library:nsapi)
Name: nsapi.default-wifi-ssid
    Defined by: library:nsapi
    No value set
Name: nsapi.dns-cache-size
    Description: Number of cached host name resolutions
    Defined by: library:nsapi
    Macro name: MBED_CONF_NSAPI_DNS_CACHE_SIZE
    Value: 3 (set by library:nsapi)
Name: nsapi.dns-response-wait-time
    Description: How long the DNS translator waits for a reply from a server in milliseconds
    Defined by: library:nsapi
    Macro name: MBED_CONF_NSAPI_DNS_RESPONSE_WAIT_TIME
    Value: 5000 (set by library:nsapi)
Name: nsapi.dns-retries
    Description: Number of DNS query retries that the DNS translator makes per server, before moving on to the next server. Total retries/attempts is always limited by dns-total-attempts.
    Defined by: library:nsapi
    No value set
Name: nsapi.dns-total-attempts
    Description: Number of total DNS query attempts that the DNS translator makes
    Defined by: library:nsapi
    Macro name: MBED_CONF_NSAPI_DNS_TOTAL_ATTEMPTS
    Value: 3 (set by library:nsapi)
Name: nsapi.present
    Defined by: library:nsapi
    Macro name: MBED_CONF_NSAPI_PRESENT
    Value: 1 (set by library:nsapi)
Name: nsapi.socket-stats-enable
    Description: Enable network socket statistics
    Defined by: library:nsapi
    No value set
Name: nsapi.socket-stats-max-count
    Description: Maximum number of socket statistics cached
    Defined by: library:nsapi
    Macro name: MBED_CONF_NSAPI_SOCKET_STATS_MAX_COUNT
    Value: 10 (set by library:nsapi)
```
