## Network interface overview

A socket requires a NetworkInterface instance when opened to indicate which NetworkInterface the socket should be created on. The NetworkInterface provides a network stack that implements the underlying socket operations.

Network interface is also the controlling API for application to specify network configuration.

### Existing network interfaces:

- [Ethernet](ethernet.html): API for connecting to the internet over an Ethernet connection.
- [Wi-Fi](wi-fi.html): API for connecting to the internet with a Wi-Fi device.
- [Cellular](cellular-api.html): API for connecting to the internet using a cellular device.
- [Mesh networking interface](mesh-api.html): Mbed OS provides two kinds of IPv6-based mesh networks - 6LoWPAN_ND and Thread.

### Network status updates

An application may choose to register a callback to monitoring status changes from network interfaces. The application can do this by using the following API:

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

Please see [Selecting the default network interface](/docs/v5.10/reference/configuration-connectivity.html#selecting-the-default-network-interface) for information about how to supply required configuration parameters on different connections.

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

- [Configuring the default network interface](/docs/v5.10/reference/configuration-connectivity.html#selecting-the-default-network-interface).
- [Network connectivity](/docs/v5.10/reference/connectivity-tech.html).
- [IP networking](/docs/v5.10/reference/ip-networking.html).
- [Network status API](network-status.html).
- [Network sockets](/docs/v5.10/apis/network-socket.html).
