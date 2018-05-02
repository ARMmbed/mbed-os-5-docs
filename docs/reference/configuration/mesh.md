<h2 id="mesh-configuration">6LoWPAN and Thread Mesh configuration</h2>

This page describes build-time configurable parameters for 6LoWPAN- and Thread-based mesh networks. Mbed OS supports two main mesh protocols: 6LoWPAN-ND and Thread. Depending on the selected protocol, you can configure different set of values.

There is one mesh-capable stack in Mbed OS called Nanostack.

This guide is divided in sections, and generic Nanostack configurations are first, followed by those for Thread and then 6LoWPAN-ND.

For understanding the technologies and APIs, please refer to following sections before this one:

- [Network connectivity in Mbed OS](connectivity-tech.html) technology page.
- [6LoWPAN Mesh technology](mesh-tech.html) page.
- [6LoWPAN Mesh class reference](mesh-api.html) user API.
- [Socket API](socket-api.html).

### Providing the configuration

The application needs to create an `mbed_app.json` configuration file if you want to use other than default settings. Values are either prefixed with `nanostack.*` or `mbed-mesh-api.*`, depending on which internal module they configure.

An example of the configuration file:

```
{
    "target_overrides": {
        "*": {
            "target.features_add": ["NANOSTACK", "COMMON_PAL"],
            "nanostack.configuration": "lowpan_router",
            "mbed-mesh-api.6lowpan-nd-device-type": "NET_6LOWPAN_ROUTER",
            "mbed-mesh-api.6lowpan-nd-channel": 12,
        }
    }
```

### Build time configuration of the stack

To minimize the size of the produced network stack, Nanostack defines a set of build options.

#### Build options for different mesh types

Option name | Features supported | Estimated binary size of Nanostack
------------| -------------------|------------------------------------
`ethernet_host` | Only Ethernet host support, no mesh networking. | 108 kB
`lowpan_border_router` | 6LoWPAN-ND border router support. | 219 kB
`lowpan_host` | 6LoWPAN-ND non routing host mode. | 122 kB
`lowpan_router` | 6LoWPAN-ND routing host mode. | 169 kB
`nanostack_full` | Everything. This is only for testing purposes. | 355 kB
`thread_border_router` | Thread router device with border router capability. | 212 kB
`thread_end_device` | Thread host without routing capability. | 166 kB
`thread_router` | Thread host with routing capability. | 199 kB

<span class="notes">**Note:** The binary sizes have been estimated using GNU Arm Embedded Toolchain version 4.9. They differ based on the toolchains or the status of the repository. The final size can only be estimated when linking the final application. The indicated size only gives you a guideline of what kind of changes to expect between different options.</span>

If you want to optimize the flash usage, you need to configure Nanostack. The configuration to choose depends mostly on the preferred use case.

See the [6LoWPAN technology overview](mesh-tech.html) for the definition of star and mesh networks. These same principles apply also to the Thread protocol.

Select the protocol the network is based on:

- 6LoWPAN-ND.
- Thread.

Select the device role:

- Mesh network. A router. (default)
- Star network. A nonrouting device, also known as a host or sleepy host.

In the application, choose from two supported interface classes:

- For 6LoWPAN-ND based network, use `LoWPANNDInterface`.
- For Thread based network, use `ThreadInterface`.

Then you may optionally choose to select the nonrouting mode for those networks. The following tables show the values to use in the `mbed_app.json` file for your devices in different networks.

**mesh-type: MESH_LOWPAN**

| Device role | `nanostack.configuration` value | `mbed-mesh-api.6lowpan-nd-device-type` |
|-----------|-------------------------|------------------------------------|
| Mesh router (default) | `lowpan_router` | `NET_6LOWPAN_ROUTER` |
| Nonrouting device | `lowpan_host` | `NET_6LOWPAN_HOST` |

**mesh-type: MESH_THREAD**

| Device role |`nanostack.configuration` value | `mbed-mesh-api.thread-device-type` |
|-----------|-------------------------|------------------------------------|
| Mesh router (default) | `thread_router` | `MESH_DEVICE_TYPE_THREAD_ROUTER` |
| Nonrouting device | `thread_end_device` | `MESH_DEVICE_TYPE_THREAD_SLEEPY_END_DEVICE` |

### Nanostack's configuration

```
Configuration parameters
------------------------

Name: nanostack-eventloop.exclude_highres_timer
    Description: Exclude high resolution timer from build
    Defined by: library:nanostack-eventloop
    No value set
Name: nanostack-eventloop.use_platform_tick_timer
    Description: Use platform provided low resolution tick timer for eventloop
    Defined by: library:nanostack-eventloop
    No value set
Name: nanostack-hal.critical-section-usable-from-interrupt
    Description: Make critical section API usable from interrupt context. Else a mutex is used as locking primitive. Consult arm_hal_interrupt.c for possible side effects on interrupt latency.
    Defined by: library:nanostack-hal
    No value set
Name: nanostack-hal.event-loop-dispatch-from-application
    Description: Application is responsible of message dispatch loop. Else launch a separate thread for event-loop.
    Defined by: library:nanostack-hal
    No value set
Name: nanostack-hal.event_loop_thread_stack_size
    Description: Define event-loop thread stack size. [bytes]
    Defined by: library:nanostack-hal
    Macro name: MBED_CONF_NANOSTACK_HAL_EVENT_LOOP_THREAD_STACK_SIZE
    Value: 6144 (set by library:nanostack-hal)
Name: nanostack-hal.nvm_cfstore
    Description: Use cfstore as a NVM storage. Else RAM simulation will be used
    Defined by: library:nanostack-hal
    No value set
Name: nanostack.configuration
    Description: Build time configuration. Refer to Handbook for valid values. Default: full stack
    Defined by: library:nanostack
    Macro name: MBED_CONF_NANOSTACK_CONFIGURATION
    Value: nanostack_full (set by library:nanostack)
```

### Generic Mbed mesh API configuration values

Generic configuration allows you to fine tune Nanostack's heap usage.

```
Configuration parameters
------------------------

Name: mbed-mesh-api.use-malloc-for-heap
    Description: Use `malloc()` for reserving the Nanostack's internal heap.
    Defined by: library:mbed-mesh-api
    No value set
Name: mbed-mesh-api.heap-size
    Description: Nanostack's heap size [bytes: 0-65534]
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_HEAP_SIZE
    Value: 32500 (set by library:mbed-mesh-api)

```

### Thread related configuration parameters

Following parameters are only valid for Thread mesh protocol. These are in use when application uses `ThreadInterface` class.

```
Configuration parameters
------------------------

Name: mbed-mesh-api.thread-config-channel
    Description: RF channel to use. [11-26]
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_THREAD_CONFIG_CHANNEL
    Value: 22 (set by library:mbed-mesh-api)
Name: mbed-mesh-api.thread-config-channel-mask
    Description: Channel bit mask, 0x7ffff800 scans all channels. [0-0x07fff800]
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_THREAD_CONFIG_CHANNEL_MASK
    Value: 0x7fff800 (set by library:mbed-mesh-api)
Name: mbed-mesh-api.thread-config-channel-page
    Description: Channel page, 0 for 2.4 GHz radio.
    Defined by: library:mbed-mesh-api
    No value set
Name: mbed-mesh-api.thread-config-commissioning-dataset-timestamp
    Description: [48 bit timestamp seconds]-[15 bit timestamp ticks]-[U bit] (0-0xFFFFFFFFFFFFFFFF)
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_THREAD_CONFIG_COMMISSIONING_DATASET_TIMESTAMP
    Value: 0x10000 (set by library:mbed-mesh-api)
Name: mbed-mesh-api.thread-config-extended-panid
    Description: Extended PAN ID. [8 byte array]
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_THREAD_CONFIG_EXTENDED_PANID
    Value: {0xf1, 0xb5, 0xa1, 0xb2,0xc4, 0xd5, 0xa1, 0xbd } (set by library:mbed-mesh-api)
Name: mbed-mesh-api.thread-config-ml-prefix
    Description: Mesh Local prefix. [8 byte array]
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_THREAD_CONFIG_ML_PREFIX
    Value: {0xfd, 0x0, 0x0d, 0xb8, 0x0, 0x0, 0x0, 0x0} (set by library:mbed-mesh-api)
Name: mbed-mesh-api.thread-config-network-name
    Description: Network name [string, max 16 characters]
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_THREAD_CONFIG_NETWORK_NAME
    Value: "Thread Network" (set by library:mbed-mesh-api)
Name: mbed-mesh-api.thread-config-panid
    Description: Network identifier [0-0xFFFF]
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_THREAD_CONFIG_PANID
    Value: 0x0700 (set by library:mbed-mesh-api)
Name: mbed-mesh-api.thread-config-pskc
    Description: Pre-Shared Key for the Commissioner. [16 byte array]
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_THREAD_CONFIG_PSKC
    Value: {0xc8, 0xa6, 0x2e, 0xae, 0xf3, 0x68, 0xf3, 0x46, 0xa9, 0x9e, 0x57, 0x85, 0x98, 0x9d, 0x1c, 0xd0} (set by library:mbed-mesh-api)
Name: mbed-mesh-api.thread-device-type
    Description: Supported device operating modes: MESH_DEVICE_TYPE_THREAD_ROUTER, MESH_DEVICE_TYPE_THREAD_SLEEPY_END_DEVICE, MESH_DEVICE_TYPE_THREAD_MINIMAL_END_DEVICE
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_THREAD_DEVICE_TYPE
    Value: MESH_DEVICE_TYPE_THREAD_ROUTER (set by library:mbed-mesh-api)
Name: mbed-mesh-api.thread-master-key
    Description: Network master key. [16 byte array]
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_THREAD_MASTER_KEY
    Value: {0x10, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff} (set by library:mbed-mesh-api)
Name: mbed-mesh-api.thread-pskd
    Description: Human-scaled commissioning credentials. Uppercase alphanumeric string (0-9, A-Y excluding I, O, Q and Z), 6-32 characters.
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_THREAD_PSKD
    Value: "ABCDEFGH" (set by library:mbed-mesh-api)
Name: mbed-mesh-api.thread-security-policy
    Description: Commissioning security policy bits [0-0xFF]
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_THREAD_SECURITY_POLICY
    Value: 255 (set by library:mbed-mesh-api)
Name: mbed-mesh-api.thread-use-static-link-config
    Description: True: Use the below link config, False: Use commissioning, ignore the below link config.
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_THREAD_USE_STATIC_LINK_CONFIG
    Value: 1 (set by library:mbed-mesh-api)
```

### 6LoWPAN related configuration parameters

The following parameters are only valid for the 6LoWPAN-ND mesh network. These are in use when the application uses the `LoWPANNDInterface` class.

```
Configuration parameters
------------------------

Name: mbed-mesh-api.6lowpan-nd-channel
    Description: RF channel to use when `channel_mask` is not defined. [0-26].
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_6LOWPAN_ND_CHANNEL
    Value: 14 (set by application[*])
Name: mbed-mesh-api.6lowpan-nd-channel-mask
    Description: Channel mask, bit-mask of channels to use. [0-0x07fff800]
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_6LOWPAN_ND_CHANNEL_MASK
    Value: 0x7fff800 (set by library:mbed-mesh-api)
Name: mbed-mesh-api.6lowpan-nd-channel-page
    Description: 0 for 2.4 GHz and 2 for sub-GHz radios.
    Defined by: library:mbed-mesh-api
    No value set
Name: mbed-mesh-api.6lowpan-nd-device-type
    Description: Device mode (NET_6LOWPAN_ROUTER or NET_6LOWPAN_HOST). Router is routing packets from other device, creating a mesh network.
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_6LOWPAN_ND_DEVICE_TYPE
    Value: NET_6LOWPAN_ROUTER (set by library:mbed-mesh-api)
Name: mbed-mesh-api.6lowpan-nd-panid-filter
    Description: Beacon PAN ID filter, 0xffff means no filtering. [0-0xffff]
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_6LOWPAN_ND_PANID_FILTER
    Value: 0xAB42 (set by application[*])
Name: mbed-mesh-api.6lowpan-nd-psk-key
    Description: Pre-shared network key. Byte array of 16 bytes. In form of: {0x00, 0x11, ... 0xff}
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_6LOWPAN_ND_PSK_KEY
    Value: {0xa0, 0xa1, 0xa2, 0xa3, 0xa4, 0xa5, 0xa6, 0xa7, 0xa8, 0xa9, 0xaa, 0xab, 0xac, 0xad, 0xae, 0xaf} (set by library:mbed-mesh-api)
Name: mbed-mesh-api.6lowpan-nd-psk-key-id
    Description: PSK key ID when PSK is enabled.
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_6LOWPAN_ND_PSK_KEY_ID
    Value: 1 (set by library:mbed-mesh-api)
Name: mbed-mesh-api.6lowpan-nd-sec-level
    Description: Network security level (1-7). Use default `5`.
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_6LOWPAN_ND_SEC_LEVEL
    Value: 5 (set by library:mbed-mesh-api)
Name: mbed-mesh-api.6lowpan-nd-security-mode
    Description: NONE or PSK to use either no security, or pre-shared network key.
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_6LOWPAN_ND_SECURITY_MODE
    Value: NONE (set by library:mbed-mesh-api)
```
