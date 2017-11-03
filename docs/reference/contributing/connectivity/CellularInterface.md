### CellularInterface

This section guidelines and details porting a cellular device driver to Mbed OS. It first describes the building blocks of your new cellular interface and then gives step-by-step instructions on how to port.

#### Quick peek

You can implement a cellular network interface in different ways depending on your requirements and physical setup. For example:

**Case 1: An implementation using Mbed OS provided network stacks (PPP mode)**
   - Pros
		- A well-established network stack with full Mbed OS support.
		- Simple operation and implementation because the inherent network stack provides all socket APIs.
		- Needs less maintenance because the IP stack handles the bulk of the work in data mode. Command mode is turned off as soon as the device enters data mode.
   - Cons
		- Heavier memory consumption.
		- Bigger footprint on flash.
		- Multiplexing command mode and data mode is not yet available.

**Case 2: An implementation using on-chip network stacks (AT only mode)**
   - Pros
		- Lighter memory footprint.
		- Lighter flash footprint.
   - Cons
		- Needs to provide a chip-specific interface between AT-sockets and Mbed OS NSAPI sockets.
		- Subtle variations in different on-chip network stacks and NSAPI implementations make maintenance difficult and require more testing.
		- Limited capabilities in some instances.

**Case 3: Modem present on target board**
   - This refers to the case when the cellular modem is bundled with the target board.
   - Target board must provide an implementation of the <a href="https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/cellular/onboard_modem_api.h" target="_blank">onboard_modem_API</a>. For example, the target port for u-blox C027 Mbed Enabled IoT starter kit provides an <a href="https://github.com/ARMmbed/mbed-os/blob/master/targets/TARGET_NXP/TARGET_LPC176X/TARGET_UBLOX_C027/onboard_modem_api.c" target="_blank">implementation</a> of `onboard_modem_api`.
   - Following Mbed OS conventions, drivers for on-board modules may become part of the Mbed OS tree.
   - `OnboardCellularInterface` ties together `onboard_modem_api.h` with the generic `PPPCellularInterface` to provide a complete driver. At present, only UART connection type is handled.

**Case 4: Modem attached as a daughter board (Arduino shield)**
   - This refers to the case when the cellular modem comes as a plug-in module or an external shield (for example, with an Arduino form factor).
   - Following Mbed OS conventions, drivers for plug-in modules come as a library with an application. For example, they are not part of the Mbed OS tree.
   - If the port inherits from the generic modem driver that Arm Mbed OS, the structure might look like this:

   <span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/inherit_from_generic_modem.png)</span>

No matter your setup, Mbed OS provides ample framework. You can list common infrastructure shared between above-mentioned cases as:

**a) Onboard modem API**

> Only valid for onboard modem types. In other words, **Case 3** is applicable. A hardware abstraction layer is between a cellular modem and an Mbed OS cellular driver. This API provides basic framework for initializing and uninitializing hardware, as well as turning the modem on or off. For example:

```C
/** Sets the modem up for powering on
 *  modem_init() will be equivalent to plugging in the device, i.e.,
 *  attaching power or serial port.
 *  Layout of modem_t is implementation dependent
 */
void modem_init(modem_t *obj);
```

**b) A device type file handle**

> We have enhanced the existing `FileHandle` API to make it more usable for devices - it now supports nonblocking operation, SIGIO-style event notification and polling (see below). This makes a cellular interface implementation independent of underlying physical interface between the cellular modem and MCU, for example Serial UART, USB and so on.

``` CPP
FileHandle _fh;
```

> In case of a UART type of device, Mbed OS provides an implementation of serial device type `FileHandle` with software buffering.

```CPP
FileHandle * _fh = new UARTSerial(TX_PIN, RX_PIN, BAUDRATE);
```

> `UARTSerial` replaces Serial (which is a file handle not suitable for background use and which doesn't provide buffering) and BufferedSerial (an external library class which does not use the `FileHandle` abstraction).

**c) An AT command parser**

> An AT command parser that takes in a file handle and subsequently reads and writes to the user provided file handle.

```CPP
ATCmdParser *_at = new ATCmdParser(_fh);
```

**d) Polling mechanism for file handles**

> A mechanism to multiplex input and output over a set of file handles (file descriptors). `poll()` examines every file handle provided for any events registered for that particular file handle.

```CPP
/**
* Where fhs is an array of pollfh structs carrying FileHandle(s) and bit mask of events.
* nhfs is the number of file handles.
* timout is the amount of time to block poll, i.e., waiting for an event
*/
int poll(pollfh fhs[], unsigned nfhs, int timeout);
```

**e) PPP interface for network stacks**

> Only valid when **Case 1** is applicable. This provides an interface for cellular drivers to underlying framework provided by the network stack. This in effect means that the driver itself does not depend on a certain network stack. In other words, it talks to any network stack providing this standard PPP interface. For example:

```CPP
/** Connect to a PPP pipe
 *
 *  @param stream       Pointer to a device type file handle (descriptor)
 *  @param status_cb    Optional, user provided callback for connection status
 *  @param uname        Optional, username for the connection
 *  @param pwd          Optional, password for the connection
 *
 *  @return             0 on success, negative error code on failure
 */
nsapi_error_t nsapi_ppp_connect(FileHandle *stream, Callback<void(nsapi_error_t)> status_cb=0, const char *uname=0, const char *pwd=0);
```   

The application activating the appropriate network stack feature, and ensuring it has PPP enabled via JSON config, determines which network stack is used for PPP modems. As of Mbed OS 5.5, LWIP provides IPv4 over PPP, but not IPv6. Nanostack does not provide PPP.

#### Step-by-step porting process
##### Providing onboard modem API

Only valid when **Case 3** is applicable.

1. **Update `mbed-os/targets/targets.json`** This file defines all the target platforms that Mbed OS supports. If Mbed OS supports your specific target, an entry for your target is in this file. Define a global macro in your target description that tells the build system that your target has a modem and the data connection type is attached with MCU.

For example,

```json
    "MY_TARGET_007": {
        "supported_form_factors": ["ARDUINO"],
        "core": "Cortex-M3",
        "supported_toolchains": ["ARM", "uARM", "GCC_ARM", "GCC_CR", "IAR"],
        "extra_labels": ["LABEL", "ANOTHER_LABEL"],
        "config": {
            "modem_is_on_board": {
                "help": "Value: Tells the build system that the modem is on-board as oppose to a plug-in shield/module.",
                "value": 1,
                "macro_name": "MODEM_ON_BOARD"
            },
            "modem_data_connection_type": {
                "help": "Value: Defines how the modem is wired up to the MCU, e.g., data connection can be a UART or USB and so forth.",
                "value": 1,
                "macro_name": "MODEM_ON_BOARD_UART"
            }
        },
        "macros": ["TARGET_007"],
        "inherits": ["TargetBond"],
        "device_has": ["ETHERNET", "SPI"],
        "device_name": "JamesBond"
    },
```
2. **Use standard pin names**. A standard naming conventions for pin names is required for standard modem pins in your target's **_'targets/TARGET_FAMILY/YOUR_TARGET/PinNames.h'_**. An example is shown below for full UART capable modem. If any of these pins is not connected physically, mark it **_'NC'_**. Also indicate pin polarity.

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
The current implementation does not use all pins, but you must define all of them.

3. **Implement `onboard_modem_api.h`** Provide an implementation of `onboard_modem_api.h`. We provide an <a href="https://github.com/ARMmbed/mbed-os/blob/master/targets/TARGET_NXP/TARGET_LPC176X/TARGET_UBLOX_C027/onboard_modem_api.c" target="_blank">example implementation</a>.

###### Providing module modem API

Only valid when **Case 4** is applicable.

- If the modem is already ready to use via the UART, it may be possible to use `UARTCellularInterface` directly. Just pass its constructor the necessary pin information for the module connected to your board.

- If you require custom power and reset controls, create a custom class derived from `UARTCellularInterface`, which overrides the protected `modem_init()` methods.

- If using a different connection type, you must provide access to the connection by implementing the `FileHandle` API, and then you can pass your file handle for that connection to `PPPCellularInterface`. Either use it directly, or derive from it, and pass a file handle to its constructor in the same manner as `UARTCellularInterface`.

###### Providing an implementation using on-chip network stacks (AT only mode)

Only valid when **Case 1** is applicable.

- This is the most complex case - the bulk of the work is implementing the <a href="/docs/v5.6/reference/network-socket-overview.html" target="_blank">NSAPI socket and network interfaces</a>. The driver implementation derives from `CellularBase` to provide both the `NetworkInterface API` and the standard cellular API. Further layering to abstract connection type may be appropriate, as for the PPP case.

- Use a file handle, such as `UARTSerial`, to provide the raw data connection; then you can use `ATCmdParser` to handle connection logic and the data flow of the socket API, assuming that you use AT commands to control the sockets.

- An onboard implementation can use `onboard_modem_api.h` in the same manner as a PPP driver to access power controls - this could be shared with a PPP implementation.

###### Port verification testing

Once you have your target and driver port ready, you can verify your implementation by running port verification tests on your system. You must have `mbed-greentea` installed for this.

-	For onboard modem types:
	1. Copy contents of this <a href="https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/cellular/generic_modem_driver/TESTS/unit_tests/default/gmd_ut_config_header.h" target="_blank">folder</a> in your implementation directory. For example, `netsocket/cellular/YOUR_IMPLEMENTATION/TESTS/unit_tests/default/`.
 	1.  Rename `OnboardCellularInterface` everywhere in the `main.cpp` with your Class. (This could be a derived class from already provided APIs, as this [subsection](#providing-module-modem-api) mentions.)
 	1.  Make an empty test application with the fork of `mbed-os` where your implementation resides.
 	1.  Create a `.json` file in the root directory of your application, and copy the contents of `template_mbed_app.txt` into it.
 	1.  Now from the root of your application, enter this command:

 	 ```
 	$ mbed test --compile-list
 	```

 	1.  Look for the name of of your test suite matching to the directory path.
 	1.  Run tests with the command:

 	```
 	mbed test -n YOUR_TEST_SUITE_NAME
 	```

For more information on the  `mbed-greentea` testing suite, please visit <a href="/docs/v5.6/tools/greentea.html" target="_blank">its documentation</a>.
