<h1 id="configuration-connectivity">Connectivity configurations</h1>

This page describes build-time configurable parameters for connectivity in Mbed OS.

<span class="notes">**Note:** You can find settings for Mesh networking under [6LoWPAN Mesh](configuration-mesh.html).</span>

This is the complete list of connectivity configuration parameters. To view all configuration parameters, run the `--config -v` command. Please see [the configuration system documentation](../program-setup/advanced-configuration.html) for details on how you may use or override these settings.

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
Name: lwip.dhcp-timeout
    Description: DHCP timeout value
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_DHCP_TIMEOUT
    Value: 60 (set by library:lwip)
Name: lwip.enable-ppp-trace
    Description: Enable trace support for PPP interfaces (obsolete: use netsocket/ppp configuration instead)
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
Name: lwip.l3ip-enabled
    Description: Enable support for L3IP interfaces
    Defined by: library:lwip
    No value set
Name: lwip.mbox-size
    Description: mailbox size
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_MBOX_SIZE
    Value: 8 (set by library:lwip)
Name: lwip.mem-size
    Description: Size of heap (bytes) - used for outgoing packets, and also used by some drivers for reception, see LWIP's opt.h for more information. Current default is 1600.
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_MEM_SIZE
    Value: 2310 (set by library:lwip[STM])
Name: lwip.memp-num-tcp-seg
    Description: Number of simultaneously queued TCP segments, see LWIP opt.h for more information. Current default is 16.
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_MEMP_NUM_TCP_SEG
    Value: 16 (set by library:lwip)
Name: lwip.memp-num-tcpip-msg-inpkt
    Description: Number of simultaneously queued TCP messages that are received
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_MEMP_NUM_TCPIP_MSG_INPKT
    Value: 8 (set by library:lwip)
Name: lwip.num-netbuf
    Description: Number of netbufs, each netbuf requires 64 bytes of RAM, see LWIP's opt.h for more information. Current default is 8.
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_NUM_NETBUF
    Value: 8 (set by library:lwip)
Name: lwip.num-pbuf
    Description: Number of non-pool pbufs, each needs 92 bytes of RAM, see LWIP's opt.h for more information. Current default is 8.
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_NUM_PBUF
    Value: 8 (set by library:lwip)
Name: lwip.pbuf-pool-bufsize
    Description: Size of pbufs in pool, see LWIP's opt.h for more information.
    Defined by: library:lwip
    No value set
Name: lwip.pbuf-pool-size
    Description: Number of pbufs in pool - usually used for received packets, so this determines how much data can be buffered between reception and the application reading, see LWIP's opt.h for more information. If a driver uses PBUF_RAM for reception, less pool may be needed. Current default  is 5.
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_PBUF_POOL_SIZE
    Value: 5 (set by library:lwip)
Name: lwip.ppp-enabled
    Description: Enable support for PPP interfaces (obsolete: use netsocket/ppp configuration instead)
    Defined by: library:lwip
    No value set
Name: lwip.ppp-ipv4-enabled
    Description: Enable support for ipv4 PPP interface (obsolete: use netsocket/ppp configuration instead)
    Defined by: library:lwip
    No value set
Name: lwip.ppp-ipv6-enabled
    Description: Enable support for ipv6 PPP interface (obsolete: use netsocket/ppp configuration instead)
    Defined by: library:lwip
    No value set
Name: lwip.ppp-thread-stacksize
    Description: Thread stack size for PPP (obsolete: use netsocket/ppp configuration instead)
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_PPP_THREAD_STACKSIZE
    Value: 768 (set by library:lwip)
Name: lwip.present
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_PRESENT
    Value: 1 (set by library:lwip)
Name: lwip.raw-socket-enabled
    Description: Enable lwip raw sockets, required for Mbed OS ICMPSocket
    Defined by: library:lwip
    No value set
Name: lwip.socket-max
    Description: Maximum number of open TCPSocket and UDPSocket instances allowed, including one used internally for DNS.  Each requires 236 bytes of pre-allocated RAM
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_SOCKET_MAX
    Value: 4 (set by library:lwip)
Name: lwip.tcp-close-timeout
    Description: Maximum timeout (ms) for TCP close handshaking timeout
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_TCP_CLOSE_TIMEOUT
    Value: 1000 (set by library:lwip)
Name: lwip.tcp-enabled
    Description: Enable TCP
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_TCP_ENABLED
    Value: 1 (set by library:lwip)
Name: lwip.tcp-maxrtx
    Description: Maximum number of retransmissions of data segments, see LWIP's opt.h for more information. Current default is 6.
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_TCP_MAXRTX
    Value: 6 (set by library:lwip)
Name: lwip.tcp-mss
    Description: TCP Maximum segment size, see LWIP opt.h for more information. Current default is 536.
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_TCP_MSS
    Value: 536 (set by library:lwip)
Name: lwip.tcp-server-max
    Description: Maximum number of open TCP server instances allowed.  Each requires 72 bytes of pre-allocated RAM
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_TCP_SERVER_MAX
    Value: 4 (set by library:lwip)
Name: lwip.tcp-snd-buf
    Description: TCP sender buffer space (bytes), see LWIP's opt.h for more information. Current default is (2 * TCP_MSS).
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_TCP_SND_BUF
    Value: (2 * TCP_MSS) (set by library:lwip)
Name: lwip.tcp-socket-max
    Description: Maximum number of open TCPSocket instances allowed.  Each requires 196 bytes of pre-allocated RAM
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_TCP_SOCKET_MAX
    Value: 4 (set by library:lwip)
Name: lwip.tcp-synmaxrtx
    Description: Maximum number of retransmissions of SYN segments, see LWIP's opt.h for more information. Current default is 6.
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_TCP_SYNMAXRTX
    Value: 6 (set by library:lwip)
Name: lwip.tcp-wnd
    Description: TCP sender buffer space (bytes), see LWIP's opt.h for more information. Current default is (4 * TCP_MSS).
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_TCP_WND
    Value: (4 * TCP_MSS) (set by library:lwip)
Name: lwip.tcpip-thread-priority
    Description: Priority of lwip TCPIP thread
    Defined by: library:lwip
    Macro name: MBED_CONF_LWIP_TCPIP_THREAD_PRIORITY
    Value: osPriorityNormal (set by library:lwip)
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
Name: target.app_offset
    Description: Application start offset in ROM
    Defined by: target:Target
    No value set
Name: target.boot-stack-size
    Description: Define the boot stack size in bytes. This value must be a multiple of 8
    Defined by: target:Target
    Macro name: MBED_CONF_TARGET_BOOT_STACK_SIZE
    Value: 0x400 (set by library:rtos[*])
Name: target.clock_source
    Description: Mask value : USE_PLL_HSE_EXTC (need HW patch) | USE_PLL_HSE_XTAL (need HW patch) | USE_PLL_HSI | USE_PLL_MSI
    Defined by: target:DISCO_L475VG_IOT01A
    Macro name: CLOCK_SOURCE
    Value: USE_PLL_MSI (set by target:DISCO_L475VG_IOT01A)
Name: target.console-uart
    Description: Target has UART console on pins STDIO_UART_TX, STDIO_UART_RX. Value is only significant if target has SERIAL device.
    Defined by: target:Target
    Macro name: MBED_CONF_TARGET_CONSOLE_UART
    Value: 1 (set by target:Target)
Name: target.console-uart-flow-control
    Description: Console hardware flow control. Options: null, RTS, CTS, RTSCTS.
    Defined by: target:Target
    No value set
Name: target.deep-sleep-latency
    Description: Time in ms required to go to and wake up from deep sleep (max 10)
    Defined by: target:Target
    Macro name: MBED_CONF_TARGET_DEEP_SLEEP_LATENCY
    Value: 4 (set by target:MCU_STM32)
Name: target.default-form-factor
    Description: Default form factor of this board taken from supported_form_factors. This must be a lowercase string such as 'arduino'
    Defined by: target:Target
    No value set
Name: target.header_offset
    Description: Application header offset in ROM
    Defined by: target:Target
    No value set
Name: target.init-us-ticker-at-boot
    Description: Initialize the microsecond ticker at boot rather than on first use, and leave it initialized. This speeds up wait_us in particular.
    Defined by: target:Target
    Macro name: MBED_CONF_TARGET_INIT_US_TICKER_AT_BOOT
    Value: 1 (set by target:MCU_STM32)
Name: target.lpticker_delay_ticks
    Description: https://os.mbed.com/docs/latest/porting/low-power-ticker.html
    Defined by: target:MCU_STM32
    No value set
Name: target.lpticker_lptim
    Description: This target supports LPTIM. Set value 1 to use LPTIM for LPTICKER, or 0 to use RTC wakeup timer
    Defined by: target:DISCO_L475VG_IOT01A
    Macro name: MBED_CONF_TARGET_LPTICKER_LPTIM
    Value: 1 (set by target:DISCO_L475VG_IOT01A)
Name: target.lpticker_lptim_clock
    Description: Default value for LPTIM clock (lpticker_lptim == 1). Value is the dividing factor. Choose 1, 2 or 4
    Defined by: target:MCU_STM32
    Macro name: MBED_CONF_TARGET_LPTICKER_LPTIM_CLOCK
    Value: 1 (set by target:MCU_STM32)
Name: target.lpuart_clock_source
    Description: Define the LPUART clock source. Mask values: USE_LPUART_CLK_LSE, USE_LPUART_CLK_PCLK1, USE_LPUART_CLK_HSI
    Defined by: target:MCU_STM32
    Macro name: MBED_CONF_TARGET_LPUART_CLOCK_SOURCE
    Value: USE_LPUART_CLK_LSE|USE_LPUART_CLK_PCLK1 (set by target:MCU_STM32)
Name: target.lse_available
    Description: Define if a Low Speed External xtal (LSE) is available on the board (0 = No, 1 = Yes). If Yes, the LSE will be used to clock the RTC, LPUART, ... otherwise the Low Speed Internal clock (LSI) will be used
    Defined by: target:MCU_STM32
    Macro name: MBED_CONF_TARGET_LSE_AVAILABLE
    Value: 1 (set by target:MCU_STM32)
Name: target.mpu-rom-end
    Description: Last address of ROM protected by the MPU
    Defined by: target:Target
    Macro name: MBED_CONF_TARGET_MPU_ROM_END
    Value: 0x0fffffff (set by target:Target)
Name: target.network-default-interface-type
    Description: Default network interface type. Typical options: null, ETHERNET, WIFI, CELLULAR, MESH
    Defined by: target:Target
    No value set
Name: target.stdio_uart_rx
    Description: default RX STDIO pins is defined in PinNames.h file, but it can be overridden
    Defined by: target:MCU_STM32
    No value set
Name: target.stdio_uart_tx
    Description: default TX STDIO pins is defined in PinNames.h file, but it can be overridden
    Defined by: target:MCU_STM32
    No value set
Name: target.tickless-from-us-ticker
    Description: Run tickless from the microsecond ticker rather than the low power ticker. Running tickless off of the microsecond ticker improves interrupt latency on targets which use lpticker_delay_ticks
    Defined by: target:Target
    No value set
Name: target.xip-enable
    Description: Enable Execute In Place (XIP) on this target. Value is only significant if the board has executable external storage such as QSPIF. If this is enabled, customize the linker file to choose what text segments are placed on external storage
    Defined by: target:Target
    No value set
```

```
Configuration parameters
------------------------
Name: nsapi.default-cellular-apn
    Description: Default cellular Access Point Name.
    Defined by: library:nsapi
    No value set
Name: nsapi.default-cellular-password
    Description: Password for the default cellular network.
    Defined by: library:nsapi
    No value set
Name: nsapi.default-cellular-plmn
    Description: Default Public Land Mobile Network for cellular connection.
    Defined by: library:nsapi
    No value set
Name: nsapi.default-cellular-sim-pin
    Description: PIN for the default SIM card.
    Defined by: library:nsapi
    No value set
Name: nsapi.default-cellular-username
    Description: Username for the default cellular network.
    Defined by: library:nsapi
    No value set
Name: nsapi.default-mesh-type
    Description: Configuration type for MeshInterface::get_default_instance(). [LOWPAN/THREAD/WISUN]
    Defined by: library:nsapi
    Macro name: MBED_CONF_NSAPI_DEFAULT_MESH_TYPE
    Value: THREAD (set by library:nsapi)
Name: nsapi.default-stack
    Description: Default stack to be used, valid values: LWIP, NANOSTACK.
    Defined by: library:nsapi
    Macro name: MBED_CONF_NSAPI_DEFAULT_STACK
    Value: LWIP (set by library:nsapi)
Name: nsapi.default-wifi-password
    Description: Password for the default Wi-Fi network.
    Defined by: library:nsapi
    No value set
Name: nsapi.default-wifi-security
    Description: Wi-Fi security protocol, valid values are WEP, WPA, WPA2, WPA/WPA2.
    Defined by: library:nsapi
    Macro name: MBED_CONF_NSAPI_DEFAULT_WIFI_SECURITY
    Value: NONE (set by library:nsapi)
Name: nsapi.default-wifi-ssid
    Description: Default Wi-Fi SSID.
    Defined by: library:nsapi
    No value set
Name: nsapi.dns-addresses-limit
    Description: Max number IP addresses returned by  multiple DNS query
    Defined by: library:nsapi
    Macro name: MBED_CONF_NSAPI_DNS_ADDRESSES_LIMIT
    Value: 10 (set by library:nsapi)
Name: nsapi.dns-cache-size
    Description: Number of cached host name resolutions
    Defined by: library:nsapi
    Macro name: MBED_CONF_NSAPI_DNS_CACHE_SIZE
    Value: 3 (set by library:nsapi)
Name: nsapi.dns-response-wait-time
    Description: How long the DNS translator waits for a reply from a server in milliseconds
    Defined by: library:nsapi
    Macro name: MBED_CONF_NSAPI_DNS_RESPONSE_WAIT_TIME
    Value: 10000 (set by library:nsapi)
Name: nsapi.dns-retries
    Description: Number of DNS query retries that the DNS translator makes per server, before moving on to the next server. Total retries/attempts is always limited by dns-total-attempts.
    Defined by: library:nsapi
    Macro name: MBED_CONF_NSAPI_DNS_RETRIES
    Value: 1 (set by library:nsapi)
Name: nsapi.dns-total-attempts
    Description: Number of total DNS query attempts that the DNS translator makes
    Defined by: library:nsapi
    Macro name: MBED_CONF_NSAPI_DNS_TOTAL_ATTEMPTS
    Value: 10 (set by library:nsapi)
Name: nsapi.offload-tlssocket
    Description: Use external TLSSocket implementation. Used network stack must support external TLSSocket setsockopt values (see nsapi_types.h)
    Defined by: library:nsapi
    No value set
Name: nsapi.present
    Defined by: library:nsapi
    Macro name: MBED_CONF_NSAPI_PRESENT
    Value: 1 (set by library:nsapi)
Name: nsapi.socket-stats-enabled
    Description: Enable network socket statistics
    Defined by: library:nsapi
    No value set
Name: nsapi.socket-stats-max-count
    Description: Maximum number of socket statistics cached
    Defined by: library:nsapi
    Macro name: MBED_CONF_NSAPI_SOCKET_STATS_MAX_COUNT
    Value: 10 (set by library:nsapi)
```
