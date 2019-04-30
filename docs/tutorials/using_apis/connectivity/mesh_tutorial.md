<h1 id="mesh-tutorial">Selecting Mesh protocol</h1>

## Selecting Mesh protocol

Mbed OS supports variety of 802.15.4 based Mesh protocols. There is support for [Wi-SUN](../reference/wisun.html), [Thread](../reference/thread-tech.html) and [6LoWPAN-ND](../reference/6LoWPAN-ND-tech.html) protocols and they all have their own unique characteristics. For example, Thread is designed for Home automation use while Wi-SUN and 6LoWPAN-ND are targeted more for Utilities and Smart metering. In addition, Wi-SUN and Thread are having certification programs to ensure interoperability between devices from different vendors.

What Mesh protocol to select?
TBD



## Mesh application design principles

6LoWPAN-based 802.15.4 Mesh networks are designed to work on a lossy network. They operate on licence-exempt frequency band and are therefore prone to RF channel interference that may cause network connection to drop unexpectedly. Application must be designed so that it can recover from the instantaneous network shortage. If a network request fails, then the application must be able retry the request again.

Mesh networks usually have bigger latency than what wired networks have. Application should adopt its functionality to the longer network delays.

Mesh network has limited network throughput and therefore it is not recommended to fill RF channel with redundant traffic. Especially when dealing with multi-hop network the network throughput can drop dramatically and RF channel becomes easily saturate due retransmission.

Mesh operates on license exempt RF band and there are also other users utilizing the same radio spectrum. For example, Wi-Fi channels are overlapping with some Mesh channels in 2.4 GHz frequency range.

The application should not consume too much device constrained resources, like CPU, memory and other peripherals. Mesh protocols require certain amount of CPU cycles in order to operate properly. Application must not hog all CPU power to itself. Also, tracing should be limited to debugging purposes only.

Sometimes Mesh application is running on the battery-operated device and therefore battery life is critical for the device lifetime. To optimize device energy consumption application can utilize device sleep modes. 

Application may need to store data permanently to the device storage that may have finite number of write and erase times. After certain number of write and erase cycles the storage integrity suffers. 


## Mesh Application Programming Interfaces

The following Mbed APIs are useful with the Mesh application:

* [Mbed Mesh API](../apis/mesh-api.html) to create a Mesh Network. 
* [Network Status API](../apis/network-interface.html) to receive indications about Mesh network connectivity status. 
* [Mbed Socket API](../apis/socket.html) to communicate with a remote peer using IP sockets once Mesh network is established.

Next chapters give you quick overview of the API mentioned and also code examples.

### Mbed Mesh API
Mbed Mesh API allows application to create, connect and disconnect to Mesh network. Mbed Mesh API provides easy to use API for Mesh application developers by hiding complexity of the Nanostack API.

### Configuration
Mesh default configuration values are defined in the Mbed Mesh API file `mbed_lib.json`and they can be overwritten in application configuration file `mbed_app.json`. 

### Connecting to Mesh network

Connecting to the Mesh network is described in the following code snipplet.

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
            return error;
        }
    }

Mesh network type (Wi-SUN, Thread or 6LoWPAN-ND), RF radio shield and other configuration parameters are defined in the application configuration file `mbed_app.json`.  Below is an example configuration file for Thread device that has Atmel RF AT86RF233 shield connected.

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


You can find more example configuration files from the [Mesh minimal example](https://github.com/ARMmbed/mbed-os-example-mesh-minimal).

### Mbed Network Status API
If application need to be aware of the changes in the network connection status, then Mbed Network status API provides API for it. Application needs to implement callback method and register it to the used interface.

For more details see Network Status API in [Network Status API](FIX TO POINT TO API)

### Mbed Socket API
The following code snipplet illutrates how data can be sent to remote peer using Mbed Socket API. 


    #include "mbed.h"
    #include "nanostack/socket_api.h"
    #include "ip6string.h"

    #define UDP_PORT 1234
    #define REMOTE_ADDR_STR "ff15::810a:64d1"

    void socket_example(NetworkInterface *mesh)
    {
        uint8_t addr[16];
        UDPSocket* my_socket;
        char send_buf[20] = {0};
        
        my_socket = new UDPSocket();
        my_socket->open(mesh);
        stoip6(REMOTE_ADDR_STR, strlen(REMOTE_ADDR_STR), addr); 
        SocketAddress send_sockAddr(addr, NSAPI_IPv6, UDP_PORT);
        my_socket->sendto(send_sockAddr, send_buf, 20);
        my_socket->close();
    }

### Example Application

What comes here?


## Mesh Border Router

Mesh Border Router can connect Mesh network to another IP-based network. It allows end-to-end IP connectivity between devices in a Mesh network and devices in an external IP network.

Mbed OS provides an example Border Router implementation in GitHub repository https://github.com/ARMmbed/nanostack-border-router. The Border router can be configured to operate on **Wi-SUN**, **Thread** or **6LoWPAN-ND** networks.

In Wi-SUN and 6LoWPAN-ND mesh network a Border Router is mandatory part of the network because all traffic is routed through the Border Router. In Thread network Border Router is not mandatory as Thread network can be established with only router devices available. However, if Thread Mesh application wants to connect to a server in another network then Border Router is mandatory.

Border Router provides IPv6 prefix for the Mesh network. The Border Router can receive this backbone-prefix:

 * from router advertisements (RA) from IPv6 backbone or,
 * from static configuration. Border Router can be configured to use static backhaul-prefix by setting configuration value `backhaul-dynamic-bootstrap` to `false` in the `mbed_app.json` configuration file. Then connection to external IP network is not possible.

Once the backbone-prefix is received the Border Router will start DHCPv6 server and advertise the new prefix to the Mesh network. Then devices in the Mesh network reacts to the advertised prefix and can solicit a new IPv6 address from the DHCPv6 server running in the Border Router.

### Configuration

Border Router can be configured compile time by modifying flags in the configuration file `mbed_app.json`. 

There is plenty of configuration options available for the Border Router. The following tables lists some of the most important configuration values:

| Configuration value | Description |
|--------------------------------|-------------------|
| heap-size                | Size of Heap reserved for the Border Router. The bigger the network the more Heap should be allocated. Typically, more than 64kB is required. |
| radio-type               | Type of attached 802.15.4 radio shield. Can be `ATMEL`, `MCR20`, `S2LP`, `SPIRIT1`. |
| mesh-mode           | Type of Mesh network, can be either `LOWPAN_WS`, `THREAD` or `LOWPAN_ND`. |
| backhaul-dynamic-bootstrap | By default set to `true` to learn backhaul-prefix from backbone IPv6 Router Advertisement (RA). Set to `false` to use static backhaul-prefix configured in `backhaul-prefix` field. |

The `target_overrides` section in `mbed_app.json` allows you to overwrite platform specific default values:

| Configuration value      | Description |
|------------------------------------|-------------------|
| nanostack.configuration  | Nanostack configuration. To minimize Nanostack footprint select suitable configuration for Nanostack.  Use either `lowpan_border_router`, `ws_border_router` or `thread_border_router`. |
| mbed-trace.enable        | Enable (`true`) or disable (`false`) Border Router trace output. |

[Nanostack-border-router](https://github.com/ARMmbed/nanostack-border-router) repository contains readymade configuration files for `Wi-SUN`, `Thread` and `6LoWPAN-ND`in the [configs](https://github.com/ARMmbed/nanostack-border-router/tree/master/configs)-directory.

 

