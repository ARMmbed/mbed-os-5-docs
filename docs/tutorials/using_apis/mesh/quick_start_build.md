### Build time configuration of the Nanostack

The build time configuration of Nanostack uses the Mbed configuration system. The application needs to create an `mbed_app.json` configuration file if you want to use settings other than default settings. You can also minimize the size of the produced stack by using different build options.

#### Build options

This table demonstrate the difference in binary size between builds:

Option Name | Features supported | Binary size in Mbed OS 5.5
------------| -------------------|------------------------------------
`ethernet_host` | Only Ethernet host support, no mesh networking. | 108 kB
`lowpan_border_router` | 6LoWPAN-ND border router support. | 219 kB
`lowpan_host` | 6LoWPAN-ND non routing host mode. | 122 kB
`lowpan_router` | 6LoWPAN-ND routing host mode. | 169 kB
`nanostack_full` | Everything. This is only for testing purposes. | 355 kB
`thread_border_router` | Thread router device with border router capability. | 212 kB
`thread_end_device` | Thread host without routing capability | 166 kB
`thread_router` | Thread host with routing capability | 199 kB

<span class="notes">**Note:** The binary sizes have been estimated using GNU Arm Embedded Toolchain version 4.9. They will differ based on the toolchains or the status of the repository. The final size can only be estimated when linking the final application. The indicated size only gives you a guideline of what kind of changes to expect between different options.</span>

#### Using configuration option on Mbed OS

If you want to optimize the flash usage, you need to select a proper configuration for Nanostack. The configuration depends mostly on the preferred use case.

See [6LoWPAN overview](/docs/v5.7/tutorials/mesh.html) for the definition of star and mesh networks. These same principles apply also to Thread protocol.

Select the protocol the network is based on:

- 6LoWPAN-ND.
- Thread.

Select the device role:

- Mesh network. A router. (default)
- Star network. A non-routing device. Also known as a host, or sleepy host.

Modify your `mbed_app.json` file to direct which Nanostack configuration to choose. The [Mbed Mesh API](https://github.com/ARMmbed/mbed-os/blob/master/features/nanostack/FEATURE_NANOSTACK/mbed-mesh-api/mbed_lib.json) lists all configurations (6LoWPAN and Thread).

An example of the `mbed_app.json` file:

```
...
    "target_overrides": {
        "*": {
            "target.features_add": ["NANOSTACK", "COMMON_PAL"],
            "nanostack.configuration": "lowpan_router",
            "mbed-mesh-api.6lowpan-nd-device-type": "NET_6LOWPAN_ROUTER",
            "mbed-mesh-api.thread-device-type": "MESH_DEVICE_TYPE_THREAD_ROUTER",
        }
    }
```

In the application, you need to choose from two supported interface classes:

- For 6LoWPAN-ND based network, use `LoWPANNDInterface`.
- For Thread based network, use `ThreadInterface`.

Then you may optionally choose to select the non-routing mode for those networks. The following tables show the values you should use in the `mbed_app.json` file for your devices in different networks.

##### 6LoWPAN-ND

**mesh-type: MESH_LOWPAN**

|Device role|`nanostack.configuration` value|`mbed-mesh-api.6lowpan-nd-device-type`|
|-----------|-------------------------|------------------------------------|
|Mesh router (default) | `lowpan_router` | `NET_6LOWPAN_ROUTER` |
|Non-routing device | `lowpan_host` | `NET_6LOWPAN_HOST` |

##### Thread

**mesh-type: MESH_THREAD**

|Device role|`nanostack.configuration` value|`mbed-mesh-api.thread-device-type`|
|-----------|-------------------------|------------------------------------|
|Mesh router (default) | `thread_router` | `MESH_DEVICE_TYPE_THREAD_ROUTER` |
|Non-routing device | `thread_end_device` | `MESH_DEVICE_TYPE_THREAD_SLEEPY_END_DEVICE` |

##### Configuration parameters for 6LoWPAN-ND and Thread

All 6LoWPAN and Thread configuration options are described below.
Make sure that all your devices use the same network configuration (both nodes and border router)

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
| `thread-config-channel-mask` | number [0-0x07fff800] | Channel mask, 0x07fff800 is used for Thread networks (2.4GHz). |
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
