## Network Socket overview

This section covers the main connectivity APIs in Arm Mbed OS, which are:

- [Ethernet](/docs/v5.6/reference/ethernet.html): API for connecting to the internet over an Ethernet connection.
- [Wi-Fi](/docs/v5.6/reference/wi-fi.html): API for connecting to the internet with a Wi-Fi device.
- [Cellular](/docs/v5.6/reference/cellular-api.html): API for connecting to the internet using a cellular device.
- [Mesh networking](/docs/v5.6/reference/mesh.html): Mbed OS provides two kinds of IPv6-based mesh networks - 6LoWPAN_ND and Thread.
- [UDPSocket](/docs/v5.6/reference/udpsocket.html): This class provides the ability to send packets of data over UDP, using the sendto and recvfrom member functions.
- [TCPSocket](/docs/v5.6/reference/tcpsocket.html): This class provides the ability to send a stream of data over TCP.
- [TCPServer](/docs/v5.6/reference/tcpserver.html): This class provides the ability to accept incoming TCP connections.
- [SocketAddress](/docs/v5.6/reference/socketaddress.html): You can use this class to represent the IP address and port pair of a unique network endpoint.

Continue reading for detailed reference material about some of these APIs.

#### Network Sockets

The network-socket API provides a common interface for using sockets on network devices. It's a class-based interface, which should be familiar to users experienced with other socket APIs.

##### Network errors

The convention of the network-socket API is for functions to return negative error codes to indicate failure. On success, a function may return zero or a non-negative integer to indicate the size of a transaction. On failure, a function must return a negative integer, which should be one of the error codes in the `nsapi_error_t` enum ([here](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/group__netsocket.html#gac21eb8156cf9af198349069cdc7afeba)):

``` cpp
/** Enum of standardized error codes
 *
 *  Valid error codes have negative values and may
 *  be returned by any network operation.
 *
 *  @enum nsapi_error
 */
enum nsapi_error {
    NSAPI_ERROR_OK                  =  0,        /*!< no error */
    NSAPI_ERROR_WOULD_BLOCK         = -3001,     /*!< no data is not available but call is non-blocking */
    NSAPI_ERROR_UNSUPPORTED         = -3002,     /*!< unsupported functionality */
    NSAPI_ERROR_PARAMETER           = -3003,     /*!< invalid configuration */
    NSAPI_ERROR_NO_CONNECTION       = -3004,     /*!< not connected to a network */
    NSAPI_ERROR_NO_SOCKET           = -3005,     /*!< socket not available for use */
    NSAPI_ERROR_NO_ADDRESS          = -3006,     /*!< IP address is not known */
    NSAPI_ERROR_NO_MEMORY           = -3007,     /*!< memory resource not available */
    NSAPI_ERROR_NO_SSID             = -3008,     /*!< ssid not found */
    NSAPI_ERROR_DNS_FAILURE         = -3009,     /*!< DNS failed to complete successfully */
    NSAPI_ERROR_DHCP_FAILURE        = -3010,     /*!< DHCP failed to complete successfully */
    NSAPI_ERROR_AUTH_FAILURE        = -3011,     /*!< connection to access point failed */
    NSAPI_ERROR_DEVICE_ERROR        = -3012,     /*!< failure interfacing with the network processor */
    NSAPI_ERROR_IN_PROGRESS         = -3013,     /*!< operation (eg connect) in progress */
    NSAPI_ERROR_ALREADY             = -3014,     /*!< operation (eg connect) already in progress */
    NSAPI_ERROR_IS_CONNECTED        = -3015,     /*!< socket is already connected */
    NSAPI_ERROR_CONNECTION_LOST     = -3016,     /*!< connection lost */
    NSAPI_ERROR_CONNECTION_TIMEOUT  = -3017,     /*!< connection timed out */
};
```

##### Nonblocking operation

The network-socket API also supports nonblocking operations. The `set_blocking` member function changes the state of a socket. When a socket is in nonblocking mode, socket operations return `NSAPI_ERROR_WOULD_BLOCK` when a transaction cannot be immediately completed.

To allow efficient use of nonblocking operations, the socket classes provide an `attach` member function to register a callback on socket state changes. When the socket can successfully receive, send or accept, or when an error occurs, the system triggers a callback. It may call the callback spuriously without reason.

The callback may be called in interrupt context and should not perform operations such as receiving and sending calls. Do not make any read or write calls until it is on a thread.

##### Socket

You can use the [Socket](/docs/v5.6/mbed-os-api-doxy/class_socket.html) classes for managing network sockets. Once opened, a socket provides a pipe through which data can be sent to and received by a specific endpoint. The type of the instantiated socket indicates the underlying protocol to use. Our Socket classes include UDPSocket, TCPSocket and TCPServer.

##### NetworkInterface

A socket requires a NetworkInterface instance when opened to indicate which NetworkInterface the socket should be created on. The NetworkInterface provides a network stack that implements the underlying socket operations.

Existing network interfaces:

- [EthInterface](/docs/v5.6/reference/ethernet.html).
- [WiFiInterface](/docs/v5.6/reference/wi-fi.html).

##### Example applications

Here are example applications that are built on top of the network-socket API:

* [HTTP and HTTPS](https://os.mbed.com/teams/sandbox/code/http-example/).
* [MQTT](https://os.mbed.com/teams/mqtt/code/HelloMQTT/).
* [CoAP](https://os.mbed.com/teams/sandbox/code/coap-example/).
* [Websockets](https://os.mbed.com/cookbook/Websockets-Server).

##### Example

Here is an example of an HTTP client program. The program brings up Ethernet as the underlying network interface, and uses it to perform an HTTP transaction over a TCPSocket:

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/TCPSocket_Example/)](https://os.mbed.com/teams/mbed_example/code/TCPSocket_Example/file/6b383744246e/main.cpp)

#### Arm Mbed Mesh

The Arm Mbed Mesh API allows the application to use the IPv6 mesh network topologies through the [Nanostack](/docs/v5.6/tutorials/mesh.html#nanostack) networking stack.

Mbed OS provides two types of IPv6 based mesh networks:

* 6LoWPAN_ND, loosely following the Zigbee-IP specification.
* Thread, following the specification from Thread Group.

Nanostack is the networking stack which provides both of these protocols. For more information on the stack internals, refer to [Nanostack documentation](/docs/v5.6/tutorials/mesh.html#nanostack). Application developers use Nanostack through Mbed Mesh API.

The application can use the `LoWPANNDInterface` or `ThreadInterface` object for connecting to the mesh network and when successfully connected, the application can use the [Mbed C++ socket APIs](/docs/v5.6/reference/network-socket.html) to create a socket to start communication with a remote peer.

The `NanostackEthernetInterface` is provided for Ethernet.

##### Supported mesh networking modes

Currently, 6LoWPAN-ND (neighbor discovery) and Thread bootstrap modes are supported.

#### Cellular

The [CellularBase](/docs/v5.6/mbed-os-api-doxy/class_cellular_base.html) provides a C++ API for connecting to the internet over a Cellular device.

Arm Mbed OS provides a reference implementation of CellularBase, which you can find [here](https://github.com/ARMmbed/mbed-os/tree/master/features/netsocket/cellular/generic_modem_driver).

##### Getting started

1. Choose an [Mbed board that supports cellular](https://os.mbed.com/platforms/?mbed-enabled=15&connectivity=1), such as the [UBLOX-C027](https://os.mbed.com/platforms/u-blox-C027/) or [MTS-DRAGONFLY](https://os.mbed.com/platforms/MTS-Dragonfly/).

1. Clone [`mbed-os-example-cellular`](https://github.com/ARMmbed/mbed-os-example-cellular). Follow the instructions in the repository.

    1. Compile the code.
    1. Flash the board.

   You see output similar to the excerpt below:

```

mbed-os-example-cellular, Connecting...


Connection Established.
UDP: Sent 4 Bytes to echo.u-blox.com
Received from echo server 4 Bytes


Success. Exiting

```

##### Basic working principles

You can use and extend a cellular interface in various different ways. For example,

- Using AT commands to control sockets in an existing IP stack built into the cellular modem.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/Cell_AT.png)</span>

- Using a PPP (Point-to-Point Protocol) pipe to pass IP packets between an Mbed OS supported IP stack and cellular modem device.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/Cell_PPP.png)</span>

[`mbed-os-example-cellular`](https://github.com/ARMmbed/mbed-os-example-cellular) uses [a generic modem driver](https://github.com/ARMmbed/mbed-os/tree/master/features/netsocket/cellular/generic_modem_driver). In other words, CellularInterface uses PPP. We can summarize this particular design as follows:

* It uses an external IP stack (for example, LWIP) instead of on-chip network stacks.
* The generic modem driver uses standard 3GPP AT 27.007 AT commands to set up the cellular modem and registers to the network.
* After registration, the driver opens up a PPP (Point-to-Point Protocol) pipe using LWIP with the cellular modem and connects to the internet.

##### Module configuration

This module supports static configuration via the **Mbed configuration system**. The application needs to create an `mbed_app.json` configuration file if you want to use other than default settings.

An example of the configuration file:

```
{
    "target_overrides": {
        "*": {
            "target.features_add": ["IPV6"],
            "mbed-mesh-api.6lowpan-nd-channel": 12,
            "mbed-mesh-api.6lowpan-nd-channel-mask": "(1<<12)",
            "mbed-mesh-api.heap-size": 10000
        }
    }
}
```

**Configurable parameters in the `mbed-mesh-api` section**

| Parameter name  | Value         | Description |
| --------------- | ------------- | ----------- |
| `heap-size`       | number [0-0xfffe] | Nanostack's internal heap size |

**Thread related configuration parameters**

| Parameter name  | Value         | Description |
| --------------- | ------------- | ----------- |
| `thread-pskd`     | string [6-255 chars] | Human-scaled commissioning credentials. |
| `thread-use-static-link-config` | boolean | True: Use the below link config, False: Use commissioning, ignore the below link config. |
| `thread-device-type` | enum from `mesh_device_type_t` | Supported device operating modes:<br> `MESH_DEVICE_TYPE_THREAD_ROUTER`<br> `MESH_DEVICE_TYPE_THREAD_SLEEPY_END_DEVICE`<br> `MESH_DEVICE_TYPE_THREAD_MINIMAL_END_DEVICE` |
| `thread-config-channel-mask` | number [0-0x07fff800] | Channel mask, 0x07fff800 scans all channels. |
| `thread-config-channel-page` | number [0]| Channel page, 0 for 2,4 GHz radio. |
| `thread-config-channel`      | number [11-26] | RF channel to use. |
| `thread-config-panid`        | number [0-0xFFFF] | Network identifier. |
| `thread-config-network-name` | string [1-16] |
| `thread-config-commissioning-dataset-timestamp` | [0-0xFFFFFFFFFFFFFFFF] | [48 bit timestamp seconds]-[15 bit timestamp ticks]-[U bit] |
| `thread-config-extended-panid` | byte array [8] | Extended PAN ID. |
| `thread-master-key`      | byte array [16]| Network master key. |
| `thread-config-ml-prefix` | byte array [8] | Mesh local prefix. |
| `thread-config-pskc`      | byte array [16] | Pre-Shared Key for the Commissioner. |
| `thread-security-policy` | number [0-0xFF] | Commissioning security policy bits. |

**6LoWPAN related configuration parameters**

| Parameter name  | Type     | Description |
| --------------- | ---------| ----------- |
| `6lowpan-nd-channel-mask`    | number [0-0x07fff800] | Channel mask, bit-mask of channels to use. |
| `6lowpan-nd-channel-page`   | number [0, 2] | 0 for 2,4 GHz and 2 for sub-GHz radios. |
| `6lowpan-nd-channel`        | number [0-26] | RF channel to use when `channel_mask` is not defined. |
| `6lowpan-nd-panid-filter` | number [0-0xffff] | Beacon PAN ID filter, 0xffff means no filtering. |
| `6lowpan-nd-security-mode` | "NONE" or "PSK" | To use either no security, or Pre shared network key. |
| `6lowpan-nd-psk-key-id` | number | PSK key ID when PSK is enabled. |
| `6lowpan-nd-psk-key` | byte array [16] | Pre-Shared network key. |
| `6lowpan-nd-sec-level` | number [1-7] | Network security level. Use default `5`. |
| `6lowpan-nd-device-type` | "NET_6LOWPAN_ROUTER" or "NET_6LOWPAN_HOST" | Device mode. Router is routing packets from other device, creating a mesh network. |

**Network connection states**

After the initialization, the network state is `MESH_DISCONNECTED`. After a successful connection, the state changes to `MESH_CONNECTED` and when disconnected from the network the state is changed back to `MESH_DISCONNECTED`.

In case of connection errors, the state is changed to some of the connection error states. In an error state, there is no need to make a `disconnect` request and the application is allowed to attempt connecting again.

##### Getting started

See the example application [mbed-os-example-mesh-minimal](https://github.com/ARMmbed/mbed-os-example-mesh-minimal) for usage.
