<h1 id="light-control">Light control tutorial</h1>

The application below demonstrates a simple light control application, where devices can control the LED status of all other devices in the network. You can build the application for the unsecure 6LoWPAN-ND network.

See the [6LoWPAN overview](../reference/mesh-tech.html) for the definition of star and mesh networks.

[Please install Mbed CLI to complete the tutorial](../tools/installation-and-setup.html).

## Requirements

This tutorial requires:

- Hardware that supports entropy.
- A radio.
- An RF driver.
- A separate application, `nanostack-border-router` to test the border router.

## Import the application

If using Mbed CLI:

```
mbed import mbed-os-example-mesh-minimal
cd mbed-os-example-mesh-minimal
```

If using the Mbed Online Compiler, click **Import into Mbed IDE** below:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-mesh-minimal)](https://github.com/ARMmbed/mbed-os-example-mesh-minimal/blob/mbed-os-6.7.0/mesh_led_control_example.cpp)

## Change the channel settings (optional)

See the file `mbed_app.json` in the imported folder for an example of defining an IEEE 802.15.4 channel.

## Select the optimal Nanostack configuration

<!--what does that mean? what am I doing and why?-->

To optimize the flash usage, set the Nanostack and [Mbed Mesh API](../apis/mesh-api.html) configuration to use. The configuration depends mostly on the preferred use case.

The network is based on 6LoWPAN-ND. Select the device role:

- Mesh network: a router. (default)
- Star network: nonrouting device. Also known as a host or sleepy host.

### 6LoWPAN-ND

**nsapi.default-mesh-type: LOWPAN**

|Device role|`nanostack.configuration` value|`mbed-mesh-api.6lowpan-nd-device-type` value|
|-----------|-------------------------|------------------------------------|
|Mesh router (default) | lowpan_router | NET_6LOWPAN_ROUTER |
|Nonrouting device | lowpan_host | NET_6LOWPAN_HOST |

### Configuration example

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


## Security-based hardware requirements

The networking stack in this example requires TLS functionality. On devices where hardware entropy is not present, TLS is disabled by default. This results in compile time failures or linking failures.

To learn why entropy is required, read the [TLS porting guide](../porting/entropy-sources.html).

See [Notes on different hardware](https://github.com/ARMmbed/mbed-os-example-mesh-minimal/blob/master/Hardware.md) for combinations of development boards and RF shields that we have tested.

## Input and output configuration

Check how LEDs and buttons are configured for your hardware, and update the `.json` file accordingly.

## Radio and radio driver

To run a 6LoWPAN-ND network, you need a working RF driver for Nanostack. This example uses the Atmel AT86RF233 by default. Place the shield on top of your board.

To change the RF driver, set the preferred RF driver `provide_default` value to `true` in `mbed_app.json`. For example, to use the MCR20a RF driver:

```json
"atmel-rf.provide-default": false,
"mcr20a.provide-default": true
```

## Compiling and flashing the application

1. To compile the application:

    ```
    mbed compile -m K64F -t GCC_ARM
    ```

1. A binary is generated at the end of the build process.
1. Connect the board to your computer, and power on the board.
1. To program the application, drag and drop the binary to the board (shown as storage device on the computer).

## Update the firmware of the border router
<!--do I have to do this? do I have to do this at this point in the process, or can I put it as one of the requirements that should have been listed earlier in the doc?-->

This example supports the [Nanostack-border-router](https://github.com/ARMmbed/nanostack-border-router).

The border router supports static and dynamic backhaul configuration. Use the static configuration if your network infrastructure does not supply an IPv6 address. If your network infrastructure provides IPv6 connectivity, then the border router learns an IPv6 prefix from the router advertisements, and you can use the dynamic configuration.

Remember to connect the Ethernet cable between the board and your router. Then power cycle on the board.

## Testing with border router

By default, the application is built for the LED control demo, in which the device sends a multicast message to all devices in the network when the button is pressed. All devices that receive the multicast message will change the LED status (red LED on/off) to the state defined in the message.

As soon as both the border router and the target are running, you can verify the correct behavior<!--is this verifying the full behavior, or just that I connected to the network?-->. Open a serial console, and see the IP address obtained by the device.

<span class="notes">**Note:** This application uses the baud rate of 115200.</span>

```
connected. IP = 2001:db8:a0b:12f0::1
```

You can use this IP address to `ping` from your PC and verify that the connection is working correctly.

## Memory optimizations
<!--there's no clear flow to this tutorial. Some of it is steps I need to take, and some of it is background info, but the two are not clearly flagged-->

On some limited boards, for example NCS36510 or KW24D, running this application might cause the device to run out of RAM or ROM. In those cases, you can try optimizing memory use.

### Use a customized Mbed TLS configuration

The [example Mbed TLS configuration](https://github.com/ARMmbed/mbed-os-example-mesh-minimal/blob/master/mbedtls_config.h) minimizes the RAM and ROM use of the application; it saves you 8.7 kB of RAM but uses 6.8 kB of additional flash. This is not guaranteed to work on every Mbed Enabled platform.<!--what does it do? and why isn't the smaller version the default? what are its disadvantages?-->

You can customize the Mbed TLS configuration by adding `"macros": ["MBEDTLS_USER_CONFIG_FILE=\"mbedtls_config.h\""]` to the `.json` file.

### Disable the LED control example

You can disable the LED control example by specifying `enable-led-control-example": false` in `mbed_app.json`.

This saves you about 2.5 kB of flash.

### Change the network stack's event loop stack size

Nanostack's internal event loop is shared with Device Managmenet Client, and therefore requires lots of stack to complete the security handshakes using TLS protocols. If you're not using client functionality, you can define the following to use 2 kB of stack:

`"nanostack-hal.event_loop_thread_stack_size": 2048`

This saves you 4 kB of RAM.

### Change the Nanostack's heap size

Nanostack uses internal heap, which you can configure in the `mbed_app.json`:

In `mbed_app.json`, you find the following line:

```
"mbed-mesh-api.heap-size": 15000
```

For 6LoWPAN, you can try 12 kB. For the smallest memory use, configure the node to be in nonrouting mode. See [module-configuration](https://github.com/ARMmbed/mbed-os/tree/master/features/nanostack/FEATURE_NANOSTACK/mbed-mesh-api#module-configuration) for more detail.

### Move the Nanostack's heap to the system heap

You can move the Nanostack's internal heap to the system heap. This helps on devices with split RAM, and on devices in which the compiler fails to fit statically allocated symbols into one section, for example the NXP KW24D device.

The Mesh API has the [use-malloc-for-heap](https://github.com/ARMmbed/mbed-os/blob/master/features/nanostack/FEATURE_NANOSTACK/mbed-mesh-api/README.md#configurable-parameters-in-section-mbed-mesh-api) option to help this.

Add the following line to `mbed_app.json` to test:

```
"mbed-mesh-api.use-malloc-for-heap": true
```

### Use release profile

For devices with a small memory, we recommend using release profiles for building and exporting. Please see the documentation about [build profiles](../tools/build-profiles.html).

Examples:

```
$ mbed export -m KW24D -i make_iar --profile release
OR
$ mbed compile -m KW24D -t IAR --profile release
```

## Troubleshooting

If you have problems, you can review the [debugging documentation](../tutorials/debugging.html) for suggestions on what could be wrong and how to fix it.
