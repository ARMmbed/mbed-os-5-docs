<h1 id="light-control">Light control tutorial</h1>

The application below demonstrates a simple light control application, where devices can control the LED status of all devices in the network. You can build the application for the unsecure 6LoWPAN-ND.

## Download the application

```
mbed import mbed-os-example-mesh-minimal
cd mbed-os-example-mesh-minimal
```

Or click `Import into Mbed IDE` in the example below:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-mesh-minimal)](https://github.com/ARMmbed/mbed-os-example-mesh-minimal/blob/mastermesh_led_control_example.cpp)

## Change the channel settings (optional)

See the file `mbed_app.json` for an example of defining an IEEE 802.15.4 channel to use.

## Selecting optimal Nanostack configuration

To optimize the flash usage, select a proper configuration for Nanostack. The configuration depends mostly on the preferred use case.

The network is based on 6LoWPAN-ND. Select the device role:

- Mesh network. A router. (default)
- Star network. Nonrouting device. Also known as a host or sleepy host.

Modify your `mbed_app.json` file to see which Nanostack and [Mbed Mesh API](../apis/mesh-api.html) configuration to use.

An example configuration file is provided under `configs/` directory. You may override the `mbed_app.json`. The configuration file is `configs/mesh_6lowpan.json` and is used for 6LoWPAN-ND based mesh network. For example, the `mbed_app.json` file can be set to:

``` json
    "target_overrides": {
        "*": {
            "nanostack.configuration": "lowpan_router",
            "nsapi.default-mesh-type": "LOWPAN",
            "mbed-mesh-api.6lowpan-nd-panid-filter": "0xffff",
            "mbed-mesh-api.6lowpan-nd-channel-page": 0,
            "mbed-mesh-api.6lowpan-nd-channel": 12,
            "mbed-mesh-api.6lowpan-nd-channel-mask": "(1<<12)",
            "mbed-mesh-api.heap-size": 14000,
            "mbed-trace.enable": false,
            "platform.stdio-convert-newlines": true,
            "platform.stdio-baud-rate": 115200,
            "atmel-rf.provide-default": true,
            "mcr20a.provide-default": false,
            "target.device_has_add": ["802_15_4_PHY"],
            "target.network-default-interface-type": "MESH"
        }
    }
```

### Values for 6LoWPAN-ND

For a 6LoWPAN-ND based network, use `nsapi.default-mesh-type: LOWPAN`.

In addition, you can use:

| Device role | `nanostack.configuration` value | `mbed-mesh-api.6lowpan-nd-device-type` value |
| --- | --- | --- |
| Mesh router (default) | `lowpan_router` | `NET_6LOWPAN_ROUTER` |
| Nonrouting device | `lowpan_host` | `NET_6LOWPAN_HOST` |

## Requirements for hardware

The networking stack in this example requires TLS functionality to be enabled on Mbed TLS. On devices where hardware entropy is not present, TLS is disabled by default. This results in compile time failures or linking failures.

To learn why entropy is required, read the [TLS porting guide](../porting/entropy-sources.html).

See [Notes on different hardware](https://github.com/ARMmbed/mbed-os-example-mesh-minimal/blob/master/Hardware.md) for known combinations of development boards and RF shields that have been tested.

You also need to check how LEDs and buttons are configured for your hardware, and update the `.json` file accordingly.

## Changing the radio driver

To run a 6LoWPAN-ND network, you need a working RF driver for Nanostack. This example uses the Atmel AT86RF233 by default.

To change the RF driver, modify the `mbed_app.json` file by setting preferred RF driver `provide_default` value to true, For example, to use MCR20a RF driver:

```json
"atmel-rf.provide-default": false,
"mcr20a.provide-default": true
```

## Compile the application

```
mbed compile -m K64F -t GCC_ARM
```

A binary is generated in the end of the build process.

## Connect the RF shield to the board

This example uses the Atmel AT86RF233, which you can [purchase](https://firefly-iot.com/product/firefly-arduino-shield-2-4ghz/). Place the shield on top of your board, and power it on.

## Program the target

Drag and drop the binary to the target to program the application.

## Update the firmware of the border router

This example supports the following border router:

[Nanostack-border-router](https://github.com/ARMmbed/nanostack-border-router).

The border router supports static and dynamic backhaul configuration. The static configuration is good for testing, but the dynamic one works if your network infrastructure is supplying an IPv6 address. Make sure that you use the appropiate mode.

Remember to connect the Ethernet cable between the border router and your router. Then power on the board.

## Testing

By default, the application is built for the LED control demo, in which the device sends a multicast message to all devices in the network when the button is pressed. All devices that receive the multicast message will change the LED status (red LED on/off) to the state defined in the message.

As soon as both the border router and the target are running, you can verify the correct behavior. Open a serial console, and see the IP address obtained by the device.

<span class="notes">**Note:** This application uses the baud rate of 115200.</span>

```
connected. IP = 2001:db8:a0b:12f0::1
```

You can use this IP address to `ping` from your PC and verify that the connection is working correctly.

## Memory optimizations

On some limited platforms, for example NCS36510 or KW24D, building this application might run out of RAM or ROM. In those cases, you can try these instructions to optimize the memory use.

### Mbed TLS configuration

You can set the custom Mbed TLS configuration by adding `"macros": ["MBEDTLS_USER_CONFIG_FILE=\"mbedtls_config.h\""]` to the `.json` file. The [example Mbed TLS configuration](https://github.com/ARMmbed/mbed-os-example-mesh-minimal/blob/master/mbedtls_config.h) minimizes the RAM and ROM use of the application. The is not guaranteed to work on every Mbed Enabled platform.

This configuration file saves you 8.7 kB of RAM but uses 6.8 kB of more flash.

### Disabling the LED control example

You can disable the LED control example by specifying `enable-led-control-example": false` in `mbed_app.json`.

This saves you about 2.5 kB of flash.

### Change network stack's event loop stack size

Nanostack's internal event loop is shared with Mbed Client and therefore requires lots of stack to complete the security handshakes using TLS protocols. If you're not using client functionality, you can define the following to use 2 kB of stack:

`"nanostack-hal.event_loop_thread_stack_size": 2048`

This saves you 4 kB of RAM.

### Change Nanostack's heap size

Nanostack uses internal heap, which you can configure in the `mbed_app.json`:

```
"mbed-mesh-api.heap-size": 12000
```

For 6LoWPAN, you can try 12 kB. For the smallest memory use, configure the node to be in nonrouting mode. See [module-configuration](https://github.com/ARMmbed/mbed-os/tree/master/features/nanostack/FEATURE_NANOSTACK/mbed-mesh-api#module-configuration) for more detail.

### Move Nanostack's heap inside the system heap

You can move Nanostack's internal heap within the system heap. This helps on devices with split RAM and on devices in which the compiler fails to fit statically allocated symbols into one section, for example, the NXP KW24D device.

The Mesh API has the [use-malloc-for-heap](https://github.com/ARMmbed/mbed-os/blob/master/features/nanostack/FEATURE_NANOSTACK/mbed-mesh-api/README.md#configurable-parameters-in-section-mbed-mesh-api) option to help this.

Add the following line to `mbed_app.json` to test:

```
"mbed-mesh-api.use-malloc-for-heap": true
```

### Use release profile

For devices with small memory, we recommend using release profiles for building and exporting. Please see the documentation about [build profiles](../program-setup/build-profiles-and-rules.html).

Example:

```
$ mbed compile -m KW24D -t ARM --profile release
```

## Troubleshooting

If you have problems, you can review the [documentation](../debug-test/troubleshooting-common-issues.html) for suggestions on what could be wrong and how to fix it.
