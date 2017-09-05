### Connectivity

The main connectivity APIs in Arm Mbed OS are:

* [Network sockets](network_sockets.md): provide a common interface for using sockets on network devices.
* [Ethernet](ethernet.md): API for connecting to the internet over an Ethernet connection.
* [Wi-Fi](wifi.md): API for connecting to the internet with a Wi-Fi device.
* [Mesh networking](mesh.md): Mbed OS provides two kinds of IPv6-based mesh networks - 6LoWPAN_ND and Thread.
* [Bluetooth Low Energy (BLE)](ble.md): designed for small, energy-efficient BLE applications.
* [Cellular](cellular.md): API for connecting to the internet using a cellular device.


#### Arm Mbed Mesh

Mbed Mesh API allows the application to use the IPv6 mesh network topologies through the [nanostack](docs/tutorials/mesh/02_N_arch.md) netowrking stack.

Mbed OS provides two types of IPv6 based mesh networks:

* 6LoWPAN_ND, loosely following the Zigbee-IP specification.
* Thread, following the specification from Thread Group.

Nanostack is the networking stack which provides both of these protocols. For more information on the stack internals, refer to [Nanostack documentation](docs/tutorials/mesh/02_N_arch.md). Application developers use Nanostack through Mbed Mesh API.

The application can use the `LoWPANNDInterface` or `ThreadInterface` object for connecting to the mesh network and when successfully connected, the application can use the [Mbed C++ socket API](network_sockets.md) to create a socket to start communication with a remote peer.

The `NanostackEthernetInterface` is provided for Ethernet.

##### Supported mesh networking modes

Currently, 6LoWPAN-ND (neighbour discovery) and Thread bootstrap modes are supported.

##### Module Configuration

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

###### Configurable parameters in the `mbed-mesh-api` section

| Parameter name  | Value         | Description |
| --------------- | ------------- | ----------- |
| `heap-size`       | number [0-0xfffe] | Nanostack's internal heap size |

###### Thread related configuration parameters

| Parameter name  | Value         | Description |
| --------------- | ------------- | ----------- |
| `thread-pskd`     | string [6-255 chars] | Human-scaled commissioning credentials. |
| `thread-use-static-link-config` | boolean | True: Use the below link config, False: Use commissioning, ignore the below link config. |
| `thread-device-type` | enum from `mesh_device_type_t` | Supported device operating modes:<br> `MESH_DEVICE_TYPE_THREAD_ROUTER`<br> `MESH_DEVICE_TYPE_THREAD_SLEEPY_END_DEVICE`<br> `MESH_DEVICE_TYPE_THREAD_MINIMAL_END_DEVICE` |
| `thread-config-channel-mask` | number [0-0x07fff800] | Channel mask, 0x07fff800 scans all channels. |
| `thread-config-channel-page` | number [0, 2]| Channel page, 0 for 2,4 GHz and 2 for sub-GHz radios. |
| `thread-config-channel`      | number [0-27] | RF channel to use. |
| `thread-config-panid`        | number [0-0xFFFF] | Network identifier. |
| `thread-config-network-name` | string [1-16] |
| `thread-config-commissioning-dataset-timestamp` | [0-0xFFFFFFFFFFFFFFFF] | [48 bit timestamp seconds]-[15 bit timestamp ticks]-[U bit] |
| `thread-config-extended-panid` | byte array [8] | Extended PAN ID. |
| `thread-master-key`      | byte array [16]| Network master key. |
| `thread-config-ml-prefix` | byte array [8] | Mesh local prefix. |
| `thread-config-pskc`      | byte array [16] | Pre-Shared Key for the Commissioner. |
| `thread-security-policy` | number [0-0xFF] | Commissioning security policy bits. |

###### 6LoWPAN related configuration parameters

| Parameter name  | Type     | Description |
| --------------- | ---------| ----------- |
| `6lowpan-nd-channel-mask`    | number [0-0x07fff800] | Channel mask, bit-mask of channels to use. |
| `6lowpan-nd-channel-page`   | number [0, 2] | 0 for 2,4 GHz and 2 for sub-GHz radios. |
| `6lowpan-nd-channel`        | number [0-27] | RF channel to use when `channel_mask` is not defined. |
| `6lowpan-nd-panid-filter` | number [0-0xffff] | Beacon PAN ID filter, 0xffff means no filtering. |
| `6lowpan-nd-security-mode` | "NONE" or "PSK" | To use either no security, or Pre shared network key. |
| `6lowpan-nd-psk-key-id` | number | PSK key ID when PSK is enabled. |
| `6lowpan-nd-psk-key` | byte array [16] | Pre-Shared network key. |
| `6lowpan-nd-sec-level` | number [1-7] | Network security level. Use default `5`. |
| `6lowpan-nd-device-type` | "NET_6LOWPAN_ROUTER" or "NET_6LOWPAN_HOST" | Device mode. Router is routing packets from other device, creating a mesh network. |

###### Network connection states

After the initialization, the network state is `MESH_DISCONNECTED`. After a successful connection, the state changes to `MESH_CONNECTED` and when disconnected from the network the state is changed back to `MESH_DISCONNECTED`.

In case of connection errors, the state is changed to some of the connection error states. In an error state, there is no need to make a `disconnect` request and the application is allowed to attempt connecting again.

##### Getting started

See the example application [mbed-os-example-mesh-minimal](https://github.com/ARMmbed/mbed-os-example-mesh-minimal) for usage.
