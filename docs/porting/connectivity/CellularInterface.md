## Cellular module porting

This document provides guidelines how to make a cellular modem adaptation for Mbed OS. Please see [Cellular API usage](/docs/development/apis/cellular-api.html) about how to use cellular modules from an application point of view.

### Adding modem target support

For new targets, you may need to modify [targets.json](/docs/development/tools/adding-and-configuring-targets.html), which defines all the target platforms that Mbed OS supports. If Mbed OS supports your specific target, an entry for your target is in this file. To tell the Mbed OS build configuration that your target board has an onboard cellular module, you need to define `modem_is_on_board` and `modem_data_connection_type`.

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
    },
```

In addition you need to map onboard modem pin aliases to your target board pin names and polarity in `targets/TARGET_FAMILY/YOUR_TARGET/PinNames.h`. If any of the pins are not connected, mark it 'NC'. An example UART configuration:

```C
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

### Adding a new cellular target

You need to specify in [CellularTargets.h](https://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/_cellular_targets_8h_source.html) the `<manufacturer-module>` that is mounted on your board.

```target

#elif <your target>
#define CELLULAR_DEVICE <manufacturer-module>

```

You can browse the existing `manufacturer-modules` under `features/cellular/framework/targets`. If none of those are compatible with your module then you need to make a new cellular module adaptation.

### Adding a new cellular module

You can probably reuse an existing adaptation because most cellular modules are similar to one another.

You need to create a new folder as _MANUFACTURER/MODULE/_ for your new cellular module in `features/cellular/framework/targets/`. A device class inheriting [AT_CellularDevice](https://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/_a_t___cellular_device_8h_source.html) is a minimum, and you may need to extend other cellular APIs as well if the default implementation is not sufficient for your cellular module.

### Socket adaptation

You can implement the socket API in two ways:

- Use the IP stack on the cellular module (AT mode).
- Use the LWIP stack on Mbed OS (PPP mode).

If your cellular module has an IP stack, you need to implement the AT commands to connect to a network and to control network sockets. If the modem supports PPP mode, you can use the LWIP stack to handle sockets and IP connectivity for your modem after it connects to a network. A modem can support both the AT and PPP modes, but an application developer needs to select at compile time which mode should be used. This selection is made in the application's `mbed_app.json` configuration file using the `lwip.ppp-enabled` flag.

For example implementations of a socket adaptation, look in `features/cellular/framework/targets`.

When the modem has AT and/or PPP mode support in place and the application developer has selected which mode to use, it's up to the cellular framework to instantiate the correct classes. For example, [mbed-os-example-cellular](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-cellular/) instantiates [EasyCellularConnection class](https://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/_easy_cellular_connection_8h_source.html), which in turn instantiates [CellularConnectionFSM class](https://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/_cellular_connection_f_s_m_8h_source.html). CellularConnectionFSM instantiates classes implementing [the AT command layer](https://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/_a_t___cellular_device_8h_source.html) between the modem and the Mbed OS CPU. If an application developer has configured PPP mode in `mbed_app.json` then [AT_CellularNetwork](https://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/_a_t___cellular_network_8h_source.html) connects to a cellular network and calls `nsapi_ppp_connect()` to start the data call through the PPP pipe using LWIP sockets.

### Testing

Once you have your target and driver port ready, you can verify your implementation by running port verification tests on your system. You must have `mbed-greentea` installed for this.

To run the tests:

1.  From the root of your application, enter this command:

    ```
    mbed test --compile-list
    ```

1.  Look for the name of a test suite matching `features-cellular-tests-*`.
1.  Run tests with the command:

    ```
    mbed test -n "mbed-os-features-cellular-tests-*" -m TARGET -t TOOLCHAIN --app-config YOURCONFIG.json
    ```

For more information on the  `mbed-greentea` test suite, please visit [its documentation](/docs/development/tools/greentea-testing-applications.html).
