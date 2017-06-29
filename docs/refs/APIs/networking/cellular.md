### Cellular

The [CellularBase](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classCellularBase.html) provides a C++ API for connecting to the internet over a Cellular device.

ARM mbed OS provides a reference implementation of CellularBase, which you can find [here](https://github.com/ARMmbed/mbed-os/tree/master/features/netsocket/cellular/generic_modem_driver).

#### Getting started

1. Choose an [mbed board that supports cellular](https://developer.mbed.org/platforms/?mbed-enabled=15&connectivity=1), such as the [UBLOX-C027](https://developer.mbed.org/platforms/u-blox-C027/) or [MTS-DRAGONFLY](https://developer.mbed.org/platforms/MTS-Dragonfly/).

1. Clone [`mbed-os-example-cellular`](https://github.com/ARMmbed/mbed-os-example-cellular). Follow the instructions in the repository.

    1. Compile the code.
    1. Flash the board.

   You see output similar to the excerpt below:

```

mbed-os-example-cellular, Connecting...


Connection Established.
UDP: Sent 4 Bytes to echo.u-blox.com
Received from echo server 4 Bytes


Success. Exiting

```

#### Basic working principles

You can use and extend a cellular interface and extended in various different ways. For example,

- Using AT commands to control sockets in an IP stack built into the cellular modem.

<span class="images">![](Images/Cellular/Cell_AT.png)</span>

- Using a PPP pipe to pass IP packets between an mbed OS supported IP stack and cellular modem device.

<span class="images">![](Images/Cellular/Cell_PPP.png)</span>

[mbed-os-example-cellular](https://github.com/ARMmbed/mbed-os-example-cellular) uses [a generic modem driver](https://github.com/ARMmbed/mbed-os/tree/master/features/netsocket/cellular/generic_modem_driver). Figure 2 above shows the basic design that the driver is based on. In other words, CellularInterface uses PPP. We can summarize this particular basic design as follows:

* It uses An external IP stack (for example, LWIP) instead of on-chip network stacks.
* The generic modem driver uses standard 3GPP AT 27.007 AT commands to set up the cellular modem and registers to the network.
* After registration, the driver opens up a PPP (Point-to-Point Protocol) pipe using LWIP with the cellular modem and connects to the internet.

#### CellularBase API

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classCellularBase.html)

#### Usage summary

To bring up the network interface:

1. Instantiate an implementation of the CellularBase class (for example, the [generic modem driver](https://github.com/hasnainvirk/mbed-os/blob/cellular_feature_br/features/cellular/TARGET_GENERIC_MODEM/generic_modem_driver/)).
1. Call the `connect(pincode, apn)` function with a PIN code for your SIM card and an APN for your network.
1. Once connected, you can use mbed OS [network sockets](network_sockets.md) as usual.

#### Examples

##### Connection establishment

This example establishes connection with the cellular network using mbed OS CellularInterface.

```cpp
#include "mbed.h"
#include "OnboardCellularInterface.h"

/* SIM pin code goes here */
#define PIN_CODE    "1234"

/* Network credentials like APN go here, e.g.,
    "apn, username, password" */
#define CREDENTIALS "internet"

/* Number of retries */
#define RETRY_COUNT 3

OnboardCellularInterface iface;

nsapi_error_t do_connect()
{
    nsapi_error_t retcode;
    bool disconnected = false;
    uint8_t retry_counter = 0;

    while (!iface.is_connected()) {

        retcode = iface.connect();
        if (retcode == NSAPI_ERROR_AUTH_FAILURE) {
            printf("\n\nAuthentication Failure. Exiting application\n");
            return retcode;
        } else if (retcode != NSAPI_ERROR_OK) {
            printf("\n\nCouldn't connect: %d, will retry\n", retcode);
            retry_counter++;
            continue;
        } else if (retcode != NSAPI_ERROR_OK && retry_counter > RETRY_COUNT) {
            printf("\n\nFatal connection failure: %d\n", retcode);
            return retcode;
        }

        break;
    }

    printf("\n\nConnection Established.\n");

    return NSAPI_ERROR_OK;
}

int main()
{
    /* Set Pin code for SIM card */
    iface.set_sim_pin(PIN_CODE);

    /* Set network credentials here, e.g., APN*/
    iface.set_credentials(CREDENTIALS);

    printf("\n\nmbed-os-example-cellular, Connecting...\n");

    /* Attempt to connect to a cellular network */
    if (do_connect() == NSAPI_ERROR_OK) {
        printf("\n\nSuccess. Exiting \n\n");
        return 0;
    }

    printf("\n\nFailure. Exiting \n\n");
    return -1;
}
```

##### TCP socket example

This example opens a TCP socket with an echo server and undergoes a TCP transaction. Connection logic is the same as in the previous example.

```cpp
#include "mbed.h"
#include "UDPSocket.h"
#include "OnboardCellularInterface.h"

// SIM pin code goes here
#define PIN_CODE    "1234"

// Network credentials like APN go here, e.g.,
// "apn, username, password"
#define CREDENTIALS "internet"

// Number of retries /
#define RETRY_COUNT 3

// Cellular network interface object
OnboardCellularInterface iface;

// Echo server hostname
const char *host_name = "echo.u-blox.com";

// Echo server TCP port
const int port = 7;

/**
 * Connects to the Cellular Network
 */
nsapi_error_t do_connect()
{
    nsapi_error_t retcode;
    uint8_t retry_counter = 0;

    while (!iface.is_connected()) {

        retcode = iface.connect();
        if (retcode == NSAPI_ERROR_AUTH_FAILURE) {
            printf("\n\nAuthentication Failure. Exiting application\n");
            return retcode;
        } else if (retcode != NSAPI_ERROR_OK) {
            printf("\n\nCouldn't connect: %d, will retry\n", retcode);
            retry_counter++;
            continue;
        } else if (retcode != NSAPI_ERROR_OK && retry_counter > RETRY_COUNT) {
            printf("\n\nFatal connection failure: %d\n", retcode);
            return retcode;
        }

        break;
    }

    printf("\n\nConnection Established.\n");

    return NSAPI_ERROR_OK;
}

/**
 * Opens a TCP socket with the given echo server and undegoes an echo
 * transaction.
 */
nsapi_error_t test_send_recv()
{
    nsapi_size_or_error_t retcode;

    TCPSocket sock;

    retcode = sock.open(&iface);
    if (retcode != NSAPI_ERROR_OK) {
        printf("TCPSocket.open() fails, code: %d\n", retcode);
        return -1;
    }

    SocketAddress sock_addr;
    retcode = iface.gethostbyname(host_name, &sock_addr);
    if (retcode != NSAPI_ERROR_OK) {
        printf("Couldn't resolve remote host: %s, code: %d\n", host_name,
               retcode);
        return -1;
    }

    sock_addr.set_port(port);

    sock.set_timeout(15000);
    int n = 0;
    char *echo_string = "TEST";
    char recv_buf[4];

    retcode = sock.connect(sock_addr);
    if (retcode < 0) {
        printf("TCPSocket.connect() fails, code: %d\n", retcode);
        return -1;
    } else {
        printf("TCP: connected with %s server\n", host_name);
    }
    retcode = sock.send((void*) echo_string, sizeof(echo_string));
    if (retcode < 0) {
        printf("TCPSocket.send() fails, code: %d\n", retcode);
        return -1;
    } else {
        printf("TCP: Sent %d Bytes to %s\n", retcode, host_name);
    }

    n = sock.recv((void*) recv_buf, sizeof(recv_buf));

    sock.close();

    if (n > 0) {
        printf("Received from echo server %d Bytes\n", n);
        return 0;
    }

    return -1;

    return retcode;
}

int main()
{
    iface.modem_debug_on(MBED_CONF_APP_MODEM_TRACE);
    /* Set Pin code for SIM card */
    iface.set_sim_pin(PIN_CODE);

    /* Set network credentials here, e.g., APN*/
    iface.set_credentials(CREDENTIALS);

    printf("\n\nmbed-os-example-cellular, Connecting...\n");

    /* Attempt to connect to a cellular network */
    if (do_connect() == NSAPI_ERROR_OK) {
        nsapi_error_t retcode = test_send_recv();
        if (retcode == NSAPI_ERROR_OK) {
            printf("\n\nSuccess. Exiting \n\n");
            return 0;
        }
    }

    printf("\n\nFailure. Exiting \n\n");
    return -1;
}
// EOF
```

#### Porting guide

This section provides guidelines and details for porting a cellular device driver to mbed OS. It first provides view of the pieces that compose your new cellular interface and then gives step-by-step instructions on how to port.

##### Quick peek

You can implement a cellular network interface in different ways based on your requirements and physical setup. For example:

**Case 1: An implementation using mbed OS provided network stacks (PPP mode)**
   * Pros
		* A well-established network stack with full mbed OS support.
		* Simple operation and implementation because the inherent network stack provides all socket APIs.
		* Needs less maintenance because the IP stack handles the bulk of the work in data mode. Command mode is turned off as soon as the device enters data mode.
   * Cons
		* Heavier memory consumption.
		* Bigger footprint on flash.
		* Multiplexing command mode and data mode is not yet available.

**Case 2: An implementation using on-chip network stacks (AT only mode)**
   * Pros
		* Lighter memory footprint.
		* Lighter flash footprint.
   * Cons
		* Needs chip-specific implementation of an abstraction layer over AT-sockets to glue them together with standard mbed OS NSAPI sockets.
		* Subtle variations in different on-chip network stacks and NSAPI implementations make maintenance difficult and require more testing.
		* Limited capabilities in some instances.

**Case 3: Modem present on target board**
   * This refers to the case when the cellular modem is bundled with the target board.
   * Target board must provide an implementation of the [onboard_modem_API](https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/cellular/onboard_modem_api.h). For example, the target port for u-blox C027 mbed Enabled IoT starter kit provides an implementation of `onboard_modem_api` [here](https://github.com/ARMmbed/mbed-os/blob/master/targets/TARGET_NXP/TARGET_LPC176X/TARGET_UBLOX_C027/onboard_modem_api.c).
   * Following mbed OS conventions, drivers for on-board modules may become part of the mbed OS tree.
   * `OnboardCellularInterface` ties together `onboard_modem_api.h` with the generic `PPPCellularInterface` to provide a complete driver. At present, only UART connection type is handled.

**Case 4: Modem attached as a daughter board (Arduino shield)**
   * This refers to the case when the cellular modem comes as a plug-in module or an external shield (for example, with an Arduino form factor).
   * Following mbed OS conventions, drivers for plug-in modules come as a library with an application. For example, they are not part of the mbed OS tree.
   * If the port inherits from the generic modem driver that ARM mbed OS, the structure might look like this:

   <span class="images">![](Images/Cellular/inherit_from_generic_modem.png)</span>

No matter your setup, mbed OS provides ample framework. You can list common infrastructure shared between above-mentioned cases as:

**a) Onboard modem API**

> Only valid for onboard modem types. In other words, **Case 3** is applicable. A hardware abstraction layer is between a cellular modem and an mbed OS cellular driver. This API provides basic framework for initializing and uninitializing hardware, as well as turning the modem on or off. For example:

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

> In case of a UART type of device, mbed OS provides an implementation of serial device type `FileHandle` with software buffering.

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

**e) PPP abstraction layer for network stacks**

> Only valid when **Case 1** is applicable. This abstraction layer provides an entry point for cellular drivers to underlying PPP framework provided by the network stack. This in effect means that the driver itself does not depend on a certain network stack. In other words, it talks to any network stack providing this standard PPP interface. For example:

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

The application activating the appropriate network stack feature, and ensuring it has PPP enabled via JSON config, determines which network stack is used for PPP modems. As of mbed OS 5.5, LWIP provides IPv4 over PPP, but not IPv6. Nanostack does not provide PPP.

### Step-by-step porting process
#### Providing onboard modem API

Only valid when **Case 3** is applicable.

1. **Update _mbed-os/targets/targets.json_** This file defines all the target platforms that mbed OS supports. If mbed OS supports your specific target, an entry for your target is in this file. Define a global macro in your target description that tells the build system that your target has a modem and the data connection type is attached with MCU.

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

3. **Implement `onboard_modem_api.h`** Provide an implementation of `onboard_modem_api.h`. You can find an example implementation [here](https://github.com/ARMmbed/mbed-os/blob/master/targets/TARGET_NXP/TARGET_LPC176X/TARGET_UBLOX_C027/onboard_modem_api.c).

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/onboard_modem_api.html)

###### Providing module modem API

Only valid when **Case 4** is applicable.

* If the modem is already ready to use via the UART, it may be possible to use `UARTCellularInterface` directly. Just pass its constructor the necessary pin information for the module connected to your board.

* If you require custom power and reset controls, create a custom class derived from `UARTCellularInterface`, which overrides the protected `modem_init()` methods.

* If using a different connection type, you must provide access to the connection by implementing the `FileHandle` API, and then you can pass your file handle for that connection to `PPPCellularInterface`. Either use it directly, or derive from it, and pass a file handle to its constructor in the same manner as `UARTCellularInterface`.

###### Providing an implementation using on-chip network stacks (AT only mode)

Only valid when **Case 1** is applicable.

* This is the most complex case - the bulk of the work is implementing the [NSAPI socket and network interfaces](network_sockets.md). The driver implementation derives from `CellularBase` to provide both the `NetworkInterface API` and the standard cellular API. Further layering to abstract connection type may be appropriate, as for the PPP case.

* Use a file handle, such as `UARTSerial`, to provide the raw data connection; then you can use `ATCmdParser` to handle connection logic and the data flow of the socket API, assuming that you use AT commands to control the sockets.

* An onboard implementation can use `onboard_modem_api.h` in the same manner as a PPP driver to access power controls - this could be shared with a PPP implementation.

##### Port verification testing

Once you have your target and driver port ready, you can verify your implementation by running port verification tests on your system. You must have `mbed-greentea` installed for this.

*	For onboard modem types:
	1. Copy contents of this [folder](mbed-os/features/netsocket/cellular/generic_modem_driver/TESTS/unit_tests/default/gmd_ut_config_header.h) in your implementation directory. For example, netsocket/cellular/YOUR_IMPLEMENTATION/TESTS/unit_tests/default/
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

For more information onthe  `mbed-greentea` testing suite, please visit: https://docs.mbed.com/docs/mbed-os-handbook/en/latest/advanced/greentea/
