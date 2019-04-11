# Cellular device porting

This document provides guidelines how to make a cellular device adaptation for Mbed OS.

## Adding cellular on an Mbed OS target

For new targets, you may need to modify [targets.json](../reference/adding-and-configuring-targets.html), which defines all the target platforms that Mbed OS supports. If Mbed OS supports your specific target, an entry for your target is in this file. To tell the Mbed OS build configuration that your target board has an onboard cellular module, you need to define `modem_is_on_board` and `modem_data_connection_type`.

For example,

```json
    "MY_NEW_TARGET": {
        "supported_form_factors": ["ARDUINO"],
        "core": "Cortex-M3",
        "supported_toolchains": ["ARM", "uARM", "GCC_ARM", "GCC_CR", "IAR"],
        "extra_labels": ["LABEL", "ANOTHER_LABEL"],
        "config": {
            "modem_is_on_board": {
                "help": "Value: Tells the build system that the modem is on-board as opposed to a plug-in shield/module.",
                "value": 1,
                "macro_name": "MODEM_ON_BOARD"
            },
            "modem_data_connection_type": {
                "help": "Value: Defines how the modem is wired up to the MCU, e.g., data connection can be a UART or USB and so forth.",
                "value": 1,
                "macro_name": "MODEM_ON_BOARD_UART"
            }
        },
        "macros": ["TARGET_NEW"],
        "inherits": ["BaseTargetForAll"],
        "device_has": ["ETHERNET", "SPI"],
        "device_name": "NewDevice"
    }
```

In addition, you need to map onboard modem pin aliases to your target board pin names and polarity in `targets/TARGET_FAMILY/YOUR_TARGET/PinNames.h`. If any pin is not connected, mark it 'NC'. An example UART configuration is shown below:

```
typedef enum {

	MDMTXD = P0_15, // Transmit Data
	MDMRXD = P0_16, // Receive Data
	MDMCTS = P0_17, // Clear to Send
	MDMDCD = P0_18, // Data Carrier Detect
	MDMDSR = P0_19, // Data Set Ready
	MDMDTR = P0_20, // Data Terminal Ready
	MDMRI  = P0_21, // Ring Indicator
	MDMRTS = P0_22, // Ready to Receive

} PinName;

#define ACTIVE_HIGH_POLARITY    1
#define ACTIVE_LOW_POLARITY     0

#define MDM_PIN_POLARITY            ACTIVE_HIGH_POLARITY

```

If the board has an onboard modem, you need to implement `NetworkInterface::get_target_default_instance`, which instantiates the default cellular device driver for your modem with the default pin configurations and power up/down functionality. Typically, onboard drivers are named `ONBOARD_xxx.cpp` in the Mbed OS target folder, where `xxx` stands for a cellular device modem driver. You may need to create a new cellular device driver class for your modem in the `features/cellular/framework/targets/` folder.

## Adding a new cellular device driver

A generic cellular driver `features/cellular/framework/targets/GENERIC/GENERIC_AT3GPP/GENERIC_AT3GPP.cpp` class inheriting [AT_CellularDevice](https://os.mbed.com/docs/development/mbed-os-api-doxy/_a_t___cellular_device_8h_source.html) is the default driver for porting. It uses only the standard AT commands from 3GPP TS 27.007 to communicate with a modem. You need to copy the generic class and modify its `cellular_properties array` to define which features your modem supports. You may also need to override any nonstandard AT commands in AT_xxx classes implementing cellular APIs. Please view other drivers as examples to determine which methods to override.

In addition to the driver class, you need to copy and modify `features/cellular/framework/targets/GENERIC/GENERIC_AT3GPP/mbed_lib.json`, which defines correct pins and other setup for your modem.

## Socket adaptation

You can implement the socket API in two ways:

- Use the IP stack on the cellular module (AT mode).
- Use the LWIP stack on Mbed OS (PPP mode).

A modem can support both the AT and PPP modes, but an application developer needs to select at compile time which mode should be used. PPP and AT mode selection occur in the application's `mbed_app.json` configuration file using the `lwip.ppp-enabled` flag.

If the modem supports PPP mode, you can use the LWIP stack to handle sockets and IP connectivity for your modem. If your cellular module has an IP stack, you need to implement AT commands to control network sockets. For example implementations of a socket adaptation, look in `features/cellular/framework/targets`.

When the modem has AT and/or PPP mode support in place and the application developer has selected which mode to use, it's up to the cellular framework to instantiate the correct classes. For example, [mbed-os-example-cellular](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-cellular/) instantiates [CellularContext class](https://os.mbed.com/docs/development/mbed-os-api-doxy/_cellular_context_8h_source.html). CellularContext instantiates classes implementing [the AT command layer](https://os.mbed.com/docs/development/mbed-os-api-doxy/_a_t___cellular_device_8h_source.html) between the modem and the Mbed OS CPU. If an application developer has configured PPP mode in `mbed_app.json`, then [AT_CellularContext](https://os.mbed.com/docs/development/mbed-os-api-doxy/_a_t___cellular_context_8h_source.html) connects to a cellular network and calls `nsapi_ppp_connect()` to start the data call through the PPP pipe using LWIP sockets.

## Testing

Once you have implemented the cellular device drivers on the Mbed OS target, verify them by running `mbed-greentea` tests.

To run the tests:

1.  From the root of your application, enter this command:

    ```
    mbed test --compile-list
    ```

1.  Run Mbed OS Network interface tests. Please see the [Network Interface test plan](https://github.com/ARMmbed/mbed-os/blob/master/TESTS/network/interface/README.md) for more details.

1. Run Mbed OS Socket tests. Please see the [Network Socket test plan](https://github.com/ARMmbed/mbed-os/blob/master/TESTS/netsocket/README.md) for more details.

For more information on the `mbed-greentea` test suite, please visit [its documentation](../tools/greentea-testing-applications.html).

You may also find the [Mbed OS cellular example](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-cellular/) useful for testing.
