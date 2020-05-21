<h1 id="configuration-mesh">6LoWPAN and Wi-SUN Mesh</h1>

This page describes build-time configurable parameters for 6LoWPAN and Wi-SUN based mesh networks. Mbed OS supports two main mesh protocols: 6LoWPAN-ND and Wi-SUN. Depending on the selected protocol, you can configure different set of values.

There is one mesh-capable stack in Mbed OS called Nanostack.

This guide is divided in sections, and generic Nanostack configurations are first, followed by those for 6LoWPAN-ND and Wi-SUN.

For understanding the technologies and APIs, please refer to following sections before this one:

- [Network connectivity in Mbed OS](../reference/networking.html) technology page.
- [Wi-SUN](../reference/wisun-tech.html) technology reference page.
- [6LowPAN](../reference/mesh-tech.html) technology reference page.
- [Mesh class reference](../apis/mesh-api.html) user API.
- [Socket API](../apis/network-socket.html).

## Providing the configuration

The application needs to create an `mbed_app.json` configuration file if you want to use other than default settings. Values are either prefixed with `nanostack.*` or `mbed-mesh-api.*`, depending on which internal module they configure.

An example of the configuration file:

```
{
    "target_overrides": {
        "*": {
            "nanostack.configuration": "lowpan_router",
            "mbed-mesh-api.6lowpan-nd-device-type": "NET_6LOWPAN_ROUTER",
            "mbed-mesh-api.6lowpan-nd-channel": 12,
        }
    }
```

<span class="notes">**Note:** The configuration files for 6LoWPAN and Wi-SUN are provided for development or testing purposes. When setting up the production configuration, the user needs to have a good understanding of the whole system.</span>

## Build time configuration of the stack

To minimize the size of the produced network stack, Nanostack defines a set of build options.

### Build options for different mesh types

Option name | Features supported | Estimated binary size of Nanostack
------------| -------------------|------------------------------------
`ethernet_host` | Only Ethernet host support, no mesh networking. | 108 kB
`lowpan_border_router` | 6LoWPAN-ND border router support. | 219 kB
`lowpan_host` | 6LoWPAN-ND non routing host mode. | 122 kB
`lowpan_router` | 6LoWPAN-ND routing host mode. | 169 kB
`nanostack_full` | Everything. This is only for testing purposes. | 355 kB

<span class="notes">**Note:** The binary sizes have been estimated using GNU Arm Embedded Toolchain version 4.9. They differ based on the toolchains or the status of the repository. The final size can only be estimated when linking the final application. The indicated size only gives you a guideline of what kind of changes to expect between different options.</span>

If you want to optimize the flash usage, you need to configure Nanostack. The configuration to choose depends mostly on the preferred use case.

See the [mesh technology overview](mesh-tech.html) for the definition of star and mesh networks. These same principles apply also to the Wi-SUN protocol.

Select the protocol the network is based on:

- 6LoWPAN-ND.
- Wi-SUN.


Select the device role:

- Mesh network. A router. (default)
- Star network. A nonrouting device, also known as a host or sleepy host.

In the application, choose from two supported interface classes:

- For 6LoWPAN-ND based network, use `LoWPANNDInterface`.
- For Wi-SUN FAN based network, use `WisunInterface`.

Then you may optionally choose to select the nonrouting mode for those networks. The following tables show the values to use in the `mbed_app.json` file for your devices in different networks.

**mesh-type: MESH_LOWPAN**

| Device role | `nanostack.configuration` value | `mbed-mesh-api.6lowpan-nd-device-type` |
|-----------|-------------------------|------------------------------------|
| Mesh router (default) | `lowpan_router` | `NET_6LOWPAN_ROUTER` |
| Nonrouting device | `lowpan_host` | `NET_6LOWPAN_HOST` |

## Nanostack's configuration

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
```
```
Name: nanostack.configuration
    Description: Build time configuration. Refer to Handbook for valid values. Default: full stack
    Defined by: library:nanostack
    Macro name: MBED_CONF_NANOSTACK_CONFIGURATION
    Value: nanostack_full (set by library:nanostack)
```
```
Name: nanostack-hal.critical-section-usable-from-interrupt
    Description: Make critical section API usable from interrupt context. Else a mutex is used as locking primitive. Consult arm_hal_interrupt.c for possible side effects on interrupt latency.
    Defined by: library:nanostack-hal
    No value set
Name: nanostack-hal.event-loop-dispatch-from-application
    Description: Application is responsible of message dispatch loop. Else launch a separate thread for event-loop.
    Defined by: library:nanostack-hal
    No value set
Name: nanostack-hal.event-loop-use-mbed-events
    Description: Use Mbed OS global event queue for Nanostack event loop, rather than our own thread.
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
```

## Generic Mbed mesh API configuration values

Generic configuration allows you to fine tune Nanostack's heap usage.

```heap
Configuration parameters
------------------------
Name: mbed-mesh-api.heap-size
    Description: Nanostack's heap size [bytes: 0-65534]
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_HEAP_SIZE
    Value: 32500 (set by library:mbed-mesh-api)
Name: mbed-mesh-api.heap-stat-info
    Description: Pointer to heap statistics `mem_stat_t` storage.
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_HEAP_STAT_INFO
    Value: NULL (set by library:mbed-mesh-api)
Name: mbed-mesh-api.heap-stat-info-definition
    Description: Definition of heap statistics `mem_stat_t` storage.
    Defined by: library:mbed-mesh-api
    No value set
Name: mbed-mesh-api.use-malloc-for-heap
    Description: Use `malloc()` for reserving the Nanostack's internal heap.
    Defined by: library:mbed-mesh-api
    No value set
```


## 6LoWPAN related configuration parameters

The following parameters are only valid for the 6LoWPAN-ND mesh network. These are in use when the application uses the `LoWPANNDInterface` class.

```6lowpan
Configuration parameters
------------------------
Name: mbed-mesh-api.6lowpan-nd-channel
    Description: RF channel to use when `channel_mask` is not defined. [0-26].
    Defined by: library:mbed-mesh-api
    No value set
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
    Value: 0xffff (set by library:mbed-mesh-api)
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

## Wi-SUN related configuration parameters

The following parameters are only valid for the Wi-SUN FAN mesh network. These are in use when the application uses the `WisunInterface` class.

```wisun
Configuration parameters
------------------------
Name: mbed-mesh-api.wisun-bc-channel-function
    Description: Broadcast channel function.
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_WISUN_BC_CHANNEL_FUNCTION
    Value: 255 (set by library:mbed-mesh-api)
Name: mbed-mesh-api.wisun-bc-dwell-interval
    Description: Broadcast dwell interval. Range: 15-255 milliseconds
    Defined by: library:mbed-mesh-api
    No value set
Name: mbed-mesh-api.wisun-bc-fixed-channel
    Description: Default fixed channel
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_WISUN_BC_FIXED_CHANNEL
    Value: 0xffff (set by library:mbed-mesh-api)
Name: mbed-mesh-api.wisun-bc-interval
    Description: Broadcast interval. Duration between broadcast dwell intervals. Range: 0-16777216 milliseconds
    Defined by: library:mbed-mesh-api
    No value set
Name: mbed-mesh-api.wisun-network-name
    Description: default network name for wisun network
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_WISUN_NETWORK_NAME
    Value: "NETWORK_NAME" (set by library:mbed-mesh-api)
Name: mbed-mesh-api.wisun-operating-class
    Description: Operating class.
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_WISUN_OPERATING_CLASS
    Value: 255 (set by library:mbed-mesh-api)
Name: mbed-mesh-api.wisun-operating-mode
    Description: Operating mode.
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_WISUN_OPERATING_MODE
    Value: 255 (set by library:mbed-mesh-api)
Name: mbed-mesh-api.wisun-regulatory-domain
    Description: Regulator domain.
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_WISUN_REGULATORY_DOMAIN
    Value: 3 (set by library:mbed-mesh-api)
Name: mbed-mesh-api.wisun-uc-channel-function
    Description: Unicast channel function.
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_WISUN_UC_CHANNEL_FUNCTION
    Value: 255 (set by library:mbed-mesh-api)
Name: mbed-mesh-api.wisun-uc-dwell-interval
    Description: Unicast dwell interval. Range: 15-255 milliseconds
    Defined by: library:mbed-mesh-api
    No value set
Name: mbed-mesh-api.wisun-uc-fixed-channel
    Description: Default fixed channel
    Defined by: library:mbed-mesh-api
    Macro name: MBED_CONF_MBED_MESH_API_WISUN_UC_FIXED_CHANNEL
    Value: 0xffff (set by library:mbed-mesh-api)
```
