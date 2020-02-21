<h1 id="mesh-tutorial">Mesh tutorial</h1>

A mesh network is a dynamically created network that relies on the intelligence of individual nodes to create working connectivity across longer distances than what is possible in the radio range of an individual device. Usually there are multiple paths to other nodes, which increases network resilience in case an individual node fails. The mesh network consists of routers and end devices to provide the IP connectivity to the application layer. Border router allows devices in mesh to connect to the external internet.

The mesh network allows wireless connectivity by operating on top of IEEE 802.15.4-based RF transceivers. The network operates on a license-exempt RF band and may therefore be vulnerable to interference from other devices operating on the same RF spectrum.

This tutorial:

- Guides you to select the correct mesh protocol based on mesh network characteristics.
- Gives you concepts to consider when designing an application that uses the mesh protocol.
- Describes what types of APIs are useful for mesh.
- Introduces mesh border routers.
- Introduces Nanostack, which contains implmentations of 6LoWPAN mMesh protocols.

## Selecting the correct mesh protocol

Mbed OS supports a variety of 802.15.4-based mesh protocols. There is support for [Wi-SUN](../reference/wisun-tech.html), [Thread](../reference/thread-tech.html) and [6LoWPAN-ND](../reference/6LoWPAN-ND-tech.html) protocols, each with its own characteristics. Selecting the best mesh protocol for your application depends on the application characteristics and interoperability requirements of installation. Different mesh networks are optimized for application-specific requirements.

### Thread mesh network characteristics

- Optimized point to point communication and network formation.
- No single point of failure. Operation is possible even inside rooms without any other infrastructure.
- Fast multicast communication.
- Low power sleeping end devices for battery operated applications.
- Interoperability enabled through certification process.

Example use cases: home automation, light control, building sensor networks and commercial building automation.

### Wi-SUN mesh network characteristics

- Certificate-based authentication.
- Large hop count networks for up to 24 hops from the border router.
- Frequency hopping to handle harsh radio conditions.
- Interoperability enabled through certification process.

Example use cases: street light control; electricity, gas and water meters; and municipal applications.

### 6LowPAN ND mesh network characteristics

- Certificate-based authentication.
- Large hop count networks for up to 24 hops.
- Optimized frequency hopping for high throughput and network size.

Example use cases: street light control; electricity, gas and water meters; and municipal applications.

## Mesh application design principles

6LoWPAN-based 802.15.4 mesh networks are designed to work on a lossy network. They operate on a licence-exempt frequency band and are therefore prone to RF channel interference that may cause the network connection to drop unexpectedly. Applications must be designed to recover from the instantaneous network shortage. If a network request fails, then the application must be able retry the request again.

Mesh networks usually have a larger latency than that of wired networks. An application should adopt its functionality to the longer network delays.

A mesh network has a limited network throughput. Therefore, we don't recommend you fill the RF channel with additional traffic. When dealing with a multihop network, the network throughput can drop dramatically, and the RF channel easily becomes saturated due to retransmission. We recommend you prefer UDP socket communication over TCP due to the higher throughput.

Mesh operates on a license-exempt RF band, and other users also use the same radio spectrum. For example, Wi-Fi channels overlap with some mesh channels in the 2.4 GHz frequency range. If possible, an application should select a Wi-Fi free channel for operation.

The application should not consume too many device constrained resources, such as CPU, memory and other peripherals. Mesh protocols require a certain number of CPU cycles to operate properly. The application must not hog all CPU power to itself. Also, tracing should be limited to debugging purposes only.

Sometimes a mesh application runs on the battery-operated device; therefore, battery life is critical for the device lifetime. To optimize device energy consumption, the application can use device sleep modes.

The application may need to store data permanently to the device storage, which may have a finite number of write and erase times. After a certain number of write and erase cycles, the storage integrity suffers. Estimate the used storage lifetime with the selected storage write interval.

## Mesh APIs

The following Mbed OS APIs are useful with the mesh application:

- [Mesh API](../apis/mesh-api.html) to create a mesh network.
- [NetworkStatus API](../apis/network-status.html) to receive indications about mesh network connectivity status.
- [Socket API](../apis/socket.html) to communicate with a remote peer using IP sockets once you establish the mesh network.

The Mesh API allows applications to create, connect and disconnect to Mesh network. Mbed OS provides the Mesh API to mesh application developers to hide the complexity of the Nanostack API.

### Configuration

The mesh API file `mbed_lib.json` defines the mesh default configuration values, which you can overwrite in the application configuration file `mbed_app.json`. For an explanation of configuration options, please see the [6LoWPAN mesh configuration document](../reference/configuration-mesh.html).

### Connecting to the mesh network

Connect to the mesh network:

```
    #include "mbed.h"
    #include "rtos.h"
    #include "NanostackInterface.h"

    int main(void)
    {
        MeshInterface *mesh;
        mesh = MeshInterface::get_default_instance();
        if (!mesh) {
            printf("Error! MeshInterface not found!\n");
            return -1;
        }
        int connect_status = mesh->connect();
        if (connect_status) {
            printf("Connection failed! %d\n", connect_status);
            return -1;
        }
    }
```

The application configuration file `mbed_app.json` defines the mesh network type (Wi-SUN, Thread or 6LoWPAN-ND), RF radio shield and other configuration parameters.

Below is an example configuration file for a Thread device connected to an Atmel RF AT86RF233 shield:

```
    {
        "target_overrides": {
            "*": {
                "nanostack.configuration": "thread_router",
                "nsapi.default-mesh-type": "THREAD",
                "atmel-rf.provide-default": true,
                "target.device_has_add": ["802_15_4_PHY"],
                "target.network-default-interface-type": "MESH"
            }
        }
    }
```

You can find more example configuration files in the [mesh minimal example](https://github.com/ARMmbed/mbed-os-example-mesh-minimal).

### NetworkStatus API

Mbed OS provides the NetworkStatus API for use cases in which an application needs to be aware of the changes in the network connection status. The application needs to implement the callback method and register it to the user interface.

For more details, please see the [NetworkStatus API](../apis/network-status.html).

### Socket API

The 6LoWPAN mesh network supports socket communication using the [Mbed OS Socket API](../apis/socket.html). You can find examples on how to use sockets in the Mbed OS API documentation:

- [Socket example](../apis/socket.html#socket-example).
- [UDPSocket example](../apis/udpsocket.html#udpsocket-example).
- [TCPSocket example](../apis/tcpsocket.html#tcpsocket-example).

## Mesh border router

A mesh border router can connect a mesh network to another IP-based network. It allows end-to-end IP connectivity between devices in a mesh network and devices in an external IP network.

Mbed OS provides [an example border router implementation](https://github.com/ARMmbed/nanostack-border-router). You can configure the border router to operate on **Wi-SUN**, **Thread** and **6LoWPAN-ND** networks.

In Wi-SUN and 6LoWPAN-ND mesh networks, a border router is a mandatory part of the network because all traffic is routed through the border router. In a Thread network, a border router is not mandatory because you can establish a Thread network with only router devices available. However, if a Thread mesh application wants to connect to a server in another network, then a border router is mandatory.

A border router provides an IPv6 prefix for the mesh network. The border router can receive this backbone-prefix from:

- Router advertisements (RA) from the IPv6 backbone.
- Static configuration. You can configure the border router to use the static backhaul-prefix by setting the configuration value `backhaul-dynamic-bootstrap` to `false` in the `mbed_app.json` configuration file. Then, connection to external IP network is not possible.

Once the backbone-prefix is received, the border router starts the DHCPv6 server and advertises the new prefix to the mesh network. Then, devices in the mesh network react to the advertised prefix and can solicit a new IPv6 address from the DHCPv6 server running in the border router.

### Configuration

You can compile the border router at compile time by modifying flags in the configuration file `mbed_app.json`.

There are many configuration options available for the border router. This table lists some of the most important configuration values:

| Configuration value | Description |
|--------------------------------|-------------------|
| heap-size                | Size of Heap reserved for the Border Router. The bigger the network the more Heap should be allocated. Typically, more than 64kB will be required for operation. |
| radio-type               | Type of attached 802.15.4 radio shield. Can be like `ATMEL`, `MCR20`, `S2LP`, `SPIRIT1`. More radio shileds will be added in the future. |
| mesh-mode           | Type of Mesh network, can be either `LOWPAN_WS`, `THREAD` or `LOWPAN_ND`. |
| backhaul-dynamic-bootstrap | By default set to `true` to learn backhaul-prefix from backbone IPv6 Router Advertisement (RA). Set to `false` to use static backhaul-prefix configured in `backhaul-prefix` field. |

The `target_overrides` section in `mbed_app.json` allows you to overwrite platform specific default values:

| Configuration value      | Description |
|------------------------------------|-------------------|
| nanostack.configuration  | Nanostack configuration. To minimize Nanostack footprint select suitable configuration for Nanostack.  Use either `lowpan_border_router`, `ws_border_router` or `thread_border_router`. |
| mbed-trace.enable        | Enable (`true`) or disable (`false`) Border Router trace output. |

The [`nanostack-border-router`](https://github.com/ARMmbed/nanostack-border-router) repository contains readymade configuration files for `Wi-SUN`, `Thread` and `6LoWPAN-ND`in the [`configs`](https://github.com/ARMmbed/nanostack-border-router/tree/master/configs)-directory.
