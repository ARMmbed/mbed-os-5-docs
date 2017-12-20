### Build time configuration of the stack

To minimize the size of the produced stack, Nanostack defines a set of build options.

#### Build options

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

See [6LoWPAN overview](/docs/v5.6/tutorials/using-the-apis.html#overview-of-the-6lowpan-network) for the definition of star and mesh networks. These same principles apply also to Thread protocol.

Select the protocol the network is based on:

- 6LoWPAN-ND.
- Thread.

Select the device role:

- Mesh network. A router. (default)
- Star network. A non-routing device. Also known as a host, or sleepy host.

Modify your `mbed_app.json` file to tell which Nanostack configuration to choose and which configrations to use on [Mbed Mesh API](/docs/v5.6/reference/mesh.html).

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

