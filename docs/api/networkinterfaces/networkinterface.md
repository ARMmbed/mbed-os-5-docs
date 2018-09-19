## Network interface overview

A socket requires a NetworkInterface instance when opened to indicate which NetworkInterface the socket should be created on. The NetworkInterface provides a network stack that implements the underlying socket operations.

Network interface is also the controlling API for application to specify network configuration.

### Existing network interfaces:

- [Ethernet](ethernet.html): API for connecting to the internet over an Ethernet connection.
- [Wi-Fi](wi-fi.html): API for connecting to the internet with a Wi-Fi device.
- [Cellular](cellular-api.html): API for connecting to the internet using a cellular device.
- [Mesh networking interface](mesh-api.html): Mbed OS provides two kinds of IPv6-based mesh networks - 6LoWPAN_ND and Thread.

### Network connectivity states

When interface is created it starts from the disconnected state. When you call `NetworkInteface::connect()` method, the interface stays connected until `NetworkInterface::disconnect()` method is called. Following diagram illustrates the state changes.

![Network states](NetworkinterfaceStates.png)

All state changes between `Connecting`, `Local connectivity` and `Global route found` are handled by the interface itself. When calling `NetworkInterface::connect()` it might return when either local or global connectivity states are reached. This depends on the connectivity in question. For example Ethernet and WiFi interfaces return when global connectivity is reached. In 6LoWPAN based mesh networks it depends on the standard in use. 6LoWPAN-ND returns when it connects to border router that provides global connection. Thread returns when local mesh network is created and may later get global connection when border router is found.

When network is lost, route is lost or any other cause limits the connectivity, interface may change its state back to `Connecting` or `Local connectivity`. Interface tries reconnecting until application chooses to call `NetworkInterface::disconnect()`. Depending on the network, this reconnection might have internal back off periods.

An application may check the connection status by calling `nsapi_connection_status_t get_connection_status()` or register a callback to monitoring status changes. Following table lists defined network states with actions that appliction should take on the state change:

| State             |`nsapi_connection_status_t` | Actions to do on application |
|-------------------|----------------------------|------------------------------|
|Disconnected       | `NSAPI_STATUS_DISCONNECTED`| Call `connect()`             |
|Connecting         | `NSAPI_STATUS_CONNECTING`  | Close and destroy all open sockets. Wait until connection is established |
|Local connectivity | `NSAPI_STATUS_LOCAL_UP`    | You can create sockets and communicate with local devices in the same network |
|Global route found | `NSAPI_STATUS_GLOBAL_UP`   | You can create sockets and communicate with all hosts |


Use following API to register status callbacks:

- [Network status](network-status.html): API for monitoring network status changes.

### Default network interface

In Mbed OS, targets that provide network connectivity also provide a default network interface. This can be Ethernet, Wi-Fi, mesh or cellular. Using a default interface allows you to port applications to different targets and connectivity options.

The following example uses a default interface to connect to the network:

```
NetworkInterface *net = NetworkInterface::get_default_instance();

if (!net) {
    printf("Error! No network inteface found.\n");
    return 0;
}

net->connect();
```

This example works on all IP-based connectivity options that Mbed OS supports. The Mbed OS configuration system provides configuration for the default interface at build time, so at run time, you can just call `connect()` without any parameters.

For example, when providing Wi-Fi SSID and password, you may use the following `mbed_app.json`:

```
{
    "target_overrides": {
        "*": {
            "nsapi.default-wifi-security": "WPA_WPA2",
            "nsapi.default-wifi-ssid": "\"ssid\"",
            "nsapi.default-wifi-password": "\"password\""
        }
    }
}
```

Please see [Selecting the default network interface](/docs/development/reference/configuration-connectivity.html#selecting-the-default-network-interface) for information about how to supply required configuration parameters on different connections.

Targets with connectivity set the `target.network-default-interface-type` configuration variable appropriately, either to their only interface or the one most commonly used. For targets that provide more than one type of connectivity, you may choose the default by overriding the `target.network-default-interface-type` configuration variable.

Applications may also ask for a specific type of connection, as the following table shows:

|Method|What connectivity is returned| Requirements |
|------|-----------------------------|--------------|
|`*WiFiInterface::get_default_instance()`| Wi-Fi interface | Requires security parameters (mode, SSID, password) |
|`*EthInterface::get_default_instance()` | Wired Ethernet interface, not Wi-Fi | none |
|`*MeshInterface::get_default_instance()` | Returns either `LoWPANNDInterface` or `ThreadInterface`, depending on which is set to default | Target provides a driver or macro `DEVICE_802_15_4_PHY` is enabled |
| `*CellularBase::get_default_instance()` | Return cellular connectivity | Requires network parameters (pin, APN, username, password) |
| `*NetworkInterface::get_default_instance()` | One of the above, depending on `target.network-default-interface-type` |  |

Note that the calls for a specific interface type do not preconfigure credentials such as SSID because an interface-type-specific application is expected to configure these in code. `NULL` is returned if no interface of that type is available.

Calls for a NetworkInterface will request one of the interface types depending on `target.default-network-interface-type`, and preconfigure the credentials. If credentials can't be preconfigured (for example because `nsapi.default-wifi-ssid` isn't set), the call returns `NULL` rather than an unconfigured interface.

An application may check the type of the interface returned by `NetworkInterface::get_default_instance()` by using the "dynamic downcast" methods:

```
// net set from NetworkInterface::get_default_instance() as above
WiFiInterface *wifi = net->wifiInterface();
if (wifi) {
    printf("This is a Wi-Fi board.")
    // call WiFi-specific methods
}
```

### Related content

- [Configuring the default network interface](/docs/development/reference/configuration-connectivity.html#selecting-the-default-network-interface).
- [Network connectivity](/docs/development/reference/connectivity-stacks.html).
- [IP networking](/docs/development/reference/ip-networking.html).
- [Network status API](network-status.html).
- [Network sockets](/docs/development/apis/network-socket.html).
