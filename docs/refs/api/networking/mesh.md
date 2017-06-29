### Mesh networking

mbed OS provides two types of IPv6 based mesh networks:

* 6LoWPAN_ND, loosely following Zigbee-IP specification.
* Thread, following specification from [Thread Group](http://threadgroup.org/).

One stack, called `Nanostack`, provides both protocols. For more information about stack internals, refer to [Nanostack's documentation](https://docs.mbed.com/docs/arm-ipv66lowpan-stack/en/latest/). Application developers use Nanostack through *mbed Mesh API*.

#### mbed Mesh API

ARM mbed mesh API allows the client to use the IPv6 mesh network.

The client can use the `LoWPANNDInterface` or `ThreadInterface` object for connecting to the mesh network. When successfully connected, the client can create a socket by using the [mbed socket API](network_sockets.md) to start communication with a remote peer.

#### Supported mesh networking modes

Currently, supported mesh networking modes include 6LoWPAN-ND (neighbor discovery) and Thread bootstrap modes.

#### Module Configuration

This module supports static configuration via **mbed configuration system** by using the `mbed_app.json` file. The application needs to create the configuration file if you want to use settings other than the default settings.

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

##### Configurable parameters in section mbed-mesh-api

| Parameter name  | Value         | Description |
| --------------- | ------------- | ----------- |
| heap-size       | number [0-0xfffe] | Nanostack's internal heap size |

##### Thread related configuration parameters

| Parameter name  | Value         | Description |
| --------------- | ------------- | ----------- |
| thread-pskd     | string [6-255 chars] | Human-scaled commissioning credentials. |
| thread-device-type | `MESH_DEVICE_TYPE_THREAD_ROUTER` or `MESH_DEVICE_TYPE_THREAD_SLEEPY_END_DEVICE` | Set device operating mode. |
| thread-config-channel-mask | number [0-0x07fff800] | Channel mask, 0x07fff800 scans all channels. |
| thread-config-channel-page | number [0, 2]| Channel page, 0 for 2,4 GHz and 2 for sub-GHz radios. |
| thread-config-channel      | number [0-27] | RF channel to use. |
| thread-config-panid        | number [0-0xFFFF] | Network identifier. |
| thread-master-key      | byte array [16]| Network master key. |
| thread-config-ml-prefix | byte array [8] | Mesh local prefix. |
| thread-config-pskc      | byte array [16] | Pre-shared key (PSK) for the Commissioner. |

##### 6LoWPAN related configuration parameters

| Parameter name  | Type     | Description |
| --------------- | ---------| ----------- |
| 6lowpan-nd-channel-mask    | number [0-0x07fff800] | Channel mask, bit-mask of channels to use. |
| 6lowpan-nd-channel-page   | number [0, 2] | 0 for 2,4 GHz and 2 for sub-GHz radios. |
| 6lowpan-nd-channel        | number [0-27] | RF channel to use when `channel_mask` is not defined. |
| 6lowpan-nd-panid-filter | number [0-0xffff] | Beacon PAN ID filter, 0xffff means no filtering. |
| 6lowpan-nd-security-mode | "NONE" or "PSK" | To use either no security, or pre-shared network key. |
| 6lowpan-nd-psk-key-id | number | PSK key id when PSK is enabled. |
| 6lowpan-nd-psk-key | byte array [16] | Pre-shared network key. |
| 6lowpan-nd-sec-level | number [1-7] | Network security level. Use default `5`. |
| 6lowpan-nd-device-type | "NET_6LOWPAN_ROUTER" or "NET_6LOWPAN_HOST" | Device mode. Router is routing packets from other device, creating a mesh network. |

#### Getting started

See the example application [mbed-os-example-mesh-minimal](https://github.com/ARMmbed/mbed-os-example-mesh-minimal) for usage.

#### Usage example for 6LoWPAN ND mode

Create a network interface and driver objects.

```
LoWPANNDInterface mesh;
NanostackRfPhyXX rf_phy;
```

Initialize interface with given PHY driver.

```
mesh.initialize(&rf_phy);
```

Then connect to network:

```
    if (mesh.connect()) {
        printf("Connection failed!\r\n");
        return -1;
    }

    printf("connected. IP = %s\r\n", mesh.get_ip_address());
```

#### Usage example for 6LoWPAN Thread mode

This is similar to that for ND, but the network interface uses a different class:

```
ThreadInterface mesh;
mesh.connect();
```
