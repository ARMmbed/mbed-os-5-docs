## Network interface overview

A socket requires a NetworkInterface instance when opened to indicate which NetworkInterface the socket should be created on. The NetworkInterface provides a network stack that implements the underlying socket operations.

Network interface is also the controlling API for application to specify network configuration.

### Existing network interfaces:

- [Ethernet](/docs/development/reference/ethernet.html): API for connecting to the internet over an Ethernet connection.
- [Wi-Fi](/docs/development/reference/wi-fi.html): API for connecting to the internet with a Wi-Fi device.
- [Cellular](/docs/development/reference/cellular-api.html): API for connecting to the internet using a cellular device.
- [Mesh networking interface](/docs/development/reference/mesh-api.html): Mbed OS provides two kinds of IPv6-based mesh networks - 6LoWPAN_ND and Thread.

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
            "target.network-default-interface-type": "WIFI",
            "nsapi.default-wifi-security": "WPA_WPA2",
            "nsapi.default-wifi-ssid": "\"ssid\"",
            "nsapi.default-wifi-password": "\"password\""
        }
    }
}
```

Please see [Selecting the default network interface](configuration-connectivity.html#selecting-the-default-network-interface) for information about how to supply required configuration parameters on different connections.

For targets that provide more than one type of connectivity, you may choose the default by overriding the `target.network-default-interface-type` configuration variable.

Applications may also ask for a specific type of connection, as the following table shows:

|Method|What connectivity is returned| Requirements |
|------|-----------------------------|--------------|
|`*WiFiInterface::get_default_instance()`| Wi-Fi interface | Requires security parameters (mode, SSID, password) |
|`*EthInterface::get_default_instance()` | Wired Ethernet interface, not Wi-Fi | none |
|`*MeshInterface::get_default_instance()` | Returns either `LoWPANNDInterface` or `ThreadInterface`, depending on which is set to default | Target provides a driver or macro `DEVICE_802_15_4_PHY` is enabled |
| `*CellularBase::get_default_instance` | Return cellular connectivity | Requires network parameters (pin, APN, username, password) |
| `*NetworkInterface::get_default_instance()` | First one from above that is found |  |

Please note that any of those functions may return `NULL` when the interface of this type or its configuration is not found.

### Related content

- [Configuring the default network interface](configuration-connectivity.html#selecting-the-default-network-interface).
- [Network connectivity](connectivity-tech.html).
- [IP networking](ip-networking.html).
- [Network status API](network-status.html).
- [Network sockets](network-socket.html).
