## Network interface overview

A socket requires a NetworkInterface instance when opened to indicate which NetworkInterface the socket should be created on. The NetworkInterface provides a network stack that implements the underlying socket operations.

Network interface is also the controlling API for application to specify network configuration.

### Existing network interfaces:

- [Ethernet](/docs/development/reference/ethernet.html): API for connecting to the internet over an Ethernet connection.
- [Wi-Fi](/docs/development/reference/wi-fi.html): API for connecting to the internet with a Wi-Fi device.
- [Cellular](/docs/development/reference/cellular-api.html): API for connecting to the internet using a cellular device.
- [Mesh networking interface](/docs/development/reference/mesh-api.html): Mbed OS provides two kinds of IPv6-based mesh networks - 6LoWPAN_ND and Thread.

### Network status updates

Application may choose to registed callback for monitoring status changes from network interfaces. This is done by using following API.

- [Network status](network-status.html): API for monitoring network status changes.

### Default network interface

In Mbed OS, targets that provide network connectivity, provide also default network interface. This can be either Ethernet, WiFi, mesh or cellular. Using default interface allows applications to be easily ported to different targets and different connectivity options.

Following example uses default interface for connecting to network:
```
NetworkInterface *net = NetworkInterface::get_default_instance();

if (!net) {
    printf("Error! No network inteface found.\n");
    return 0;
}

net->connect();
```

This example works on all IP based connectivity options supported by Mbed OS. Configuration for default interface is provided by the Mbed OS configuration system on the build time, so on a run time you can just call `connect()` without any parameters.

For example, when providing WiFi SSID and password, following `mbed_app.json` may be used:
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

Please see [Selecting the default network interface](configuration-connectivity.html#selecting-the-default-network-interface) for information of how to supply required configuration parameters on different connections.

For targets that provide more than one type of connectivity, you may choose the default by overriding `target.network-default-interface-type` configuration variable.

Applications may also ask for specific type of connection, as shown in following table:

|Method|What connectivity is returned| Requirements |
|------|-----------------------------|--------------|
|`*WiFiInterface::get_default_instance()`| Wifi interface. | Requires security parameters (mode, SSID, password) |
|`*EthInterface::get_default_instance()` | Wired Ethernet interface, not WiFi. | none |
|`*MeshInterface::get_default_instance()` | Returns either `LoWPANNDInterface` or `ThreadInterface` depending on which is set to default | Target provides a driver or macro `DEVICE_802_15_4_PHY` is enabled |
| `*CellularBase::get_default_instance` | Return cellular connectivity | Requires network parameters (pin, APN, username, password) |
| `*NetworkInterface::get_default_instance()` | First one from above that is found |  |

Please note that any of those functions may return `NULL` when interface of this type or its configuration is not found.

### More information

* [Configuring the default network interface](configuration-connectivity.html#selecting-the-default-network-interface)
* [Network connectivity in Mbed OS](connectivity-tech.html)
* [IP networking](ip-networking.html)
* [Network status API](network-status.html)
* [Network Sockets](network-socket.html)
