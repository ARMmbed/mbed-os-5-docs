### CellularInterface

This document provides guidelines and details for setting up a cellular device driver with Mbed OS. Please see the [working principles when working with a cellular C++ API](https://os.mbed.com/docs/latest/reference/network-socket.html) for more information.

#### Implementing CellularInterface

You can implement a cellular network interface in different ways depending on your requirements and physical setup. For example:

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/Cell_AT.png)<span>Figure 1</span></span>

**Case 1: An implementation using on-chip network stacks (AT only mode, refer to figure 1)**

-   Pros
    - Lighter RAM memory consumption and flash footprint.
    - More autonomous modem operation.

-   Cons
    - Needs chip-specific implementation of an abstraction layer over AT-sockets to glue them together with standard Mbed OS NSAPI sockets.
    - Subtle variations in different on-chip network stacks and NSAPI implementations make maintenance difficult and require more testing.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/Cell_PPP.png)<span>Figure 2</span></span>

**Case 2: An implementation using Mbed OS provided network stacks (PPP mode, refer to figure 2)**

-   Pros
    - A well-established network stack with full Mbed OS support.
    - The inherent network stack provides all socket APIs.

-   Cons
    - Heavier RAM memory consumption and bigger flash footprint.
    - All modems do not support PPP mode making AT only mode the only available choice.
    - Multiplexing command mode and data mode are not yet available.

##### Adding modem target support

For new targets, you may need to modify [targets.json](https://os.mbed.com/docs/v5.8/tools/adding-and-configuring-targets.html). `targets.json` defines all the target platforms that Mbed OS supports. If Mbed OS supports your specific target, an entry for your target is in this file. Define a global macro in your target description that tells the build system that your target has a modem, and the data connection type is attached with MCU.

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

Use standard pin names. A standard naming convention for pin names is required for standard modem pins in your target's **_'targets/TARGET_FAMILY/YOUR_TARGET/PinNames.h'_**. The example below shows the full UART capable modem. If any of these pins is not connected physically, mark it **_'NC'_**. Also indicate pin polarity.

```C
typedef enum {

	MDMTXD = P0_15, // Transmit Data
	MDMRXD = P0_16, // Receive Data
	MDMCTS = P0_17, // Clear to Send
	MDMDCD = P0_18, // Data Carrier Detect
	MDMDSR = P0_19, // Data Set Ready
	MDMDTR = P0_20, // Data Terminal Ready
	MDMRI  = P0_21, // Ring Indicator
	MDMRTS = P0_22, // Request to Send

} PinName;

#define ACTIVE_HIGH_POLARITY    1
#define ACTIVE_LOW_POLARITY     0

#define MDM_PIN_POLARITY            ACTIVE_HIGH_POLARITY

```

You must define all pins. Implement `onboard_modem_api.h`. The target board must provide an implementation of the [onboard_modem_API](https://os-doc-builder.test.mbed.com/docs/v5.8/mbed-os-api-doxy/onboard__modem__api_8h_source.html).

##### Modifying cellular targets

Setup for some predefined targets is available in [CellularTargets.h](https://os-doc-builder.test.mbed.com/docs/v5.8/mbed-os-api-doxy/_cellular_targets_8h_source.html). For a new target, you need to modify `CellularTargets.h`. In `CellularTargets.h`, you need to specify a cellular device in addition to UART pins connecting the Mbed OS CPU to the modem. For example, if the new device MY_NEW_TARGET defined above in the "Adding modem target support" chapter is connected with QUECTEL BG96, you would need the following changes marked in between `// !!!!` in `CellularTargets.h`:

```C
...
#elif TARGET_UBLOX_C027
#define CELLULAR_DEVICE UBLOX_C027
// !!!!
// cellular device to be connected with MY_NEW_TARGET is specified below:
#elif TARGET_MY_NEW_TARGET
#define CELLULAR_DEVICE QUECTEL_BG96
// !!!!
#else
#error Cellular target not defined, see cellular/targets.h
//#define CELLULAR_TARGET <target-modem>
//#define MDMTXD <pin-name>
//#define MDMRXD <pin-name>
#endif
#endif
// !!!!
// cellular target and UART pins connecting MY_NEW_TARGET with the modem are specified below:
#define CELLULAR_TARGET TARGET_MY_NEW_TARGET
#define MDMTXD PTC17
#define MDMRXD PTC16
// !!!!
...
```

If none of the existing modems is compatible with the new modem, then create new modem implementation under [features/cellular/framework/targets](https://github.com/ARMmbed/mbed-os/blob/master/features/cellular/framework/targets). A device class inheriting [AT_CellularDevice](https://os-doc-builder.test.mbed.com/docs/v5.8/mbed-os-api-doxy/_a_t___cellular_device_8h_source.html) is a minimum. [QUECTEL_BG96](https://github.com/ARMmbed/mbed-os/blob/master/features/cellular/framework/targets/QUECTEL/BG96/QUECTEL_BG96.h) is an example of the device class. You can create additional overlapping functionality for everything that is available in [features/cellular/framework/targets](https://github.com/ARMmbed/mbed-os/blob/master/features/cellular/framework/targets).

##### Providing an implementation using on-chip network stacks (AT only mode)

[QUECTEL_BG96_CellularStack](https://github.com/ARMmbed/mbed-os/blob/master/features/cellular/framework/targets/QUECTEL/BG96/QUECTEL_BG96_CellularStack.h) is an example of a modem specific AT command cellular stack implementation. For example, [mbed-os-example-cellular](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-cellular/) instantiates the [EasyCellularConnection class](https://os-doc-builder.test.mbed.com/docs/v5.8/mbed-os-api-doxy/_easy_cellular_connection_8h_source.html), which in turn instantiates the [CellularConnectionFSM class](https://os-doc-builder.test.mbed.com/docs/v5.8/mbed-os-api-doxy/_cellular_connection_f_s_m_8h_source.html). CellularConnectionFSM instantiates classes implementing [the AT command layer](https://os-doc-builder.test.mbed.com/docs/v5.8/mbed-os-api-doxy/_a_t___cellular_device_8h_source.html) between the modem and the Mbed OS CPU. For the [QUECTEL BG96](https://github.com/ARMmbed/mbed-os/tree/master/features/cellular/framework/targets/QUECTEL/BG96) classes [QUECTEL_BG96](https://github.com/ARMmbed/mbed-os/blob/master/features/cellular/framework/targets/QUECTEL/BG96/QUECTEL_BG96.h), [QUECTEL_BG96_CellularStack](https://github.com/ARMmbed/mbed-os/blob/master/features/cellular/framework/targets/QUECTEL/BG96/QUECTEL_BG96_CellularStack.h) and [QUECTEL_BG96_CellularNetwork](https://github.com/ARMmbed/mbed-os/blob/master/features/cellular/framework/targets/QUECTEL/BG96/QUECTEL_BG96_CellularNetwork.h) have been implemented for a modem specific functionality. QUECTEL_BG96_CellularStack implements QUECTEL BG96 specific AT command stack for socket data handling.

##### Providing an implementation using Mbed OS provided network stacks (PPP mode)

If the new modem supports PPP mode, then you can use the existing Mbed OS LWIP stack to control the modem when connecting to a network. To use the LWIP stack, set `lwip.ppp-enabled` to true in an application `mbed_app.json`. [UBLOX LISA](https://github.com/ARMmbed/mbed-os/tree/master/features/cellular/framework/targets/UBLOX/LISA_U) is an example of a modem implementation using PPP mode to connect to a network. For example, [mbed-os-example-cellular](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-cellular/) instantiates [EasyCellularConnection class](https://os-doc-builder.test.mbed.com/docs/v5.8/mbed-os-api-doxy/_easy_cellular_connection_8h_source.html), which in turn instantiates [CellularConnectionFSM class](https://os-doc-builder.test.mbed.com/docs/v5.8/mbed-os-api-doxy/_cellular_connection_f_s_m_8h_source.html). CellularConnectionFSM instantiates classes implementing [the AT command layer](https://os-doc-builder.test.mbed.com/docs/v5.8/mbed-os-api-doxy/_a_t___cellular_device_8h_source.html) between the modem and the Mbed OS CPU. For LISA classes [UBLOX_LISA_U](https://github.com/ARMmbed/mbed-os/blob/master/features/cellular/framework/targets/UBLOX/LISA_U/UBLOX_LISA_U.h), [UBLOX_LISA_U_CellularNetwork](https://github.com/ARMmbed/mbed-os/blob/master/features/cellular/framework/targets/UBLOX/LISA_U/UBLOX_LISA_U_CellularNetwork.h) and [UBLOX_LISA_U_CellularPower](https://github.com/ARMmbed/mbed-os/blob/master/features/cellular/framework/targets/UBLOX/LISA_U/UBLOX_LISA_U_CellularPower.h) have been implemented for a modem specific functionality. In the AT command layer, [AT_CellularNetwork](https://os-doc-builder.test.mbed.com/docs/v5.8/mbed-os-api-doxy/_a_t___cellular_network_8h_source.html) includes functionality calling [nsapi_ppp_connect()](https://os-doc-builder.test.mbed.com/docs/v5.8/mbed-os-api-doxy/netsocket_2nsapi__ppp_8h_source.html) to start the data call through the PPP pipe.

#### Testing

Once you have your target and driver port ready, you can verify your implementation by running port verification tests on your system. You must have `mbed-greentea` installed for this.

-   To run the tests:
 	1.  From the root of your application, enter this command:

 	```
 	mbed test --compile-list
 	```

 	1.  Look for the name of a test suite matching `mbed-os-features-cellular-tests-cellular-cellular_all`.
 	1.  Run tests with the command:

 	```
 	mbed test -n "mbed-os-features-cellular-tests-cellular-cellular_all" -m YOURMACHINE -t YOURCOMPILER --app-config YOURCONFIG.json
 	```

For more information on the  `mbed-greentea` test suite, please visit [its documentation](https://os.mbed.com/docs/v5.8/tools/greentea.html).

You can also run stand-alone tests. The [`UNITTESTS` folder](https://github.com/ARMmbed/mbed-os/tree/master/features/cellular/UNITTESTS) contains unit tests for cellular specific classes. Unit tests are based on the stubbing method.

You can run those tests locally by running `./run_tests` script under the [`UNITTESTS` folder](https://github.com/ARMmbed/mbed-os/tree/master/features/cellular/UNITTESTS).

You need the following applications: `cpputest`, `gcov` and `lcov` (`genhtml`) for running the tests by themselves.

After you have run the `run_tests` script, you can find test results in the [`UNITTESTS/results` folder](https://github.com/ARMmbed/mbed-os/tree/master/features/cellular/UNITTESTS) and line and function coverages in the [`UNITTESTS/coverages` folder](https://github.com/ARMmbed/mbed-os/tree/master/features/cellular/UNITTESTS).
