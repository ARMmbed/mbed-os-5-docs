## Cellular

Mbed OS cellular provides your IoT application with access to world-wide operator-maintained cellular networks, both IP and non-IP, as Figure 1 illustrates. Mbed OS cellular implementation is based on international 3GPP and OMA standards, and it has been verified to work with all cellular networks such as NB-IoT, CAT-M1, 4G LTE, 3G WCDMA and GPRS.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/api-cellular-overview.png)<span>Figure 1. Mbed OS cellular overview</span></span>

Please read about [Mbed OS connectivity technology](https://www.mbed.com/en/technologies/connectivity/) if you are not yet familiar with it.

### Key features

Key features of the Mbed OS cellular APIs include:

- Compatible with 3GPP TS 27.007 and 27.005.
- Implements core functionality for OMA Lightweight M2M Client.
- Out-of-the-box cellular modem support.

3GPP TS 27.007 and 27.005 are standards to provide consistent cellular network data connectivity and SMS over an AT command interface for cellular devices, regardless of the underlying cellular network.

OMA Lightweight M2M is a protocol from the Open Mobile Alliance for IoT device management. The Mbed OS cellular API provides core functionality to implement the LWM2M Client. For more information, please see _OMA LightweightM2M_ and _OMA LWM2M Object Connectivity Management_ at [OMA Specifications](http://openmobilealliance.org/wp/index.html).

Mbed OS already supports several Mbed Enabled boards with on-board cellular hosted modules out of the box. Because Mbed OS is an open source platform, developers can enable support for new cellular boards with our adaptation framework. Please see our [cellular porting guide](/docs/development/reference/contributing-connectivity.html#cellularinterface) for more information.

### Quick start

There are two phases to Mbed OS connectivity, in general:

1. Connect to a network.
1. Open a socket to send or receive data.

With cellular, the easiest way to connect your application to the internet over a cellular network is to use the `CellularConnectionFSM` class. It encapsulates most of the complexity of connecting to the cellular network and also reports any changes in connection status to your application. When connected to a cellular network, you can use Mbed OS network sockets as usual, as Figure 2 illustrates.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/api-cellular-quick-start.png)<span>Figure 2. Connect to cellular network and open a socket</span></span>

If you want to see code, you can go to our [cellular example](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-cellular/).

### Cellular hosted module

If you are using an Mbed OS target that has a supported on-board (mounted) cellular hosted module then cellular framework decides the correct cellular hosted module at compile-time. You can run `mbedls` to find out your current Mbed OS target and then match that to the supported targets in the `CellularTargets.h` file, where a CELLULAR_DEVICE macro is defined based on the Mbed OS target definition and can be used as a C++ class type to instantiate a driver class (inherited from `CellularDevice.h`).

You can browse `CellularTargets.h` file to find out if the hosted module you are using is already supported. In case the hosted module is not yet supported, you could adapt some existing driver for your needs.

Some Mbed OS target boards may have several different kind of cellular hosted modules on-board. In that case, the cellular hosted module driver detects at runtime the actual hosted module that is currently mounted and adapts to that specific cellular hosted module during runtime.

If you use an Mbed OS target and a separate cellular hosted module via a serial line (UART), you need to configure in your `mbed_app.json` configuration file which cellular hosted module to use and which UART pins are connected between the Mbed OS target board and the cellular hosted module:

    {
        "macros":
        [
            "CELLULAR_DEVICE=<manufacturer-module>",
            "MDMRXD=<rx-pin-name>",
            "MDMTXD=<tx-pin-name>"
        ]
    }    

You need to change the pin-names above to actual pins, such as D0 and D1, according to your Mbed target. You may also need to define MDMRTS and MDMCTS pins if you have RTS/CTS connected on UART.
    
### Cellular APIs

As an application developer, you should use and refer only to classes located under API folder. All the other classes have implementation details which are expected to change frequently.

Cellular APIs are structured based on main functionalities:

- `CellularNetwork` for cellular network features, such as preferred operator and APN.
- `CellularPower` for cellular hosted module power control, such as enabling power save.
- `CellularInformation` to read the cellular hosted module type and firmware version.
- `CellularSIM` to enter the PIN code and other SIM management functions.
- `CellularSMS` to read and write SMS messages.

The CellularDevice class encloses cellular APIs. Therefore, to use any cellular API, you need to get CellularDevice first. You can then use CellularDevice to open and close cellular APIs, as Figure 3 illustrates.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/api-cellular-device.png)<span>Figure 3. Use CellularDevice to open Cellular APIs</span></span>

When an application has opened a cellular API, you can use it to request API methods. For example:

    CellularNetwork *network  = cellularDevice->get_network();
    if (network) {
        printf("Local IP address is %s", network->get_ip_address());
    }

### UDP and TCP sockets

If you want to use UDP or TCP sockets, you need an IP stack. Mbed OS cellular has an option to use either the LWIP stack, which is part of Mbed OS, or to use the IP stack on the cellular hosted module. Figure 4 illustrates IP stack deployment.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/api-cellular-ip-stack.png)<span>Figure 4. IP stack can be used in PPP or AT mode</span></span>

#### PPP mode with the LWIP stack on Mbed OS

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/Cell_PPP.png)</span>

In PPP (Point-to-Point Protocol) mode, the LWIP stack is linked as a part of the Mbed OS application. Because LWIP stack implements sockets, the socket functionality is hardware-independent.

You can enable PPP mode and also configure LWIP features in the application configuration file:

    "lwip.ppp-enabled": true
    "lwip.ipv4-enabled": true
    "lwip.ipv6-enabled": true
    "lwip.tcp-enabled": true

#### AT mode with the IP stack on the modem

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/Cell_AT.png)</span>

In AT mode, the modem's internal IP stack is used over an AT link. Sockets are part of the IP stack, so AT commands are used to control sockets. Socket AT commands are modem specific, and need to be implemented on the Mbed OS side. You can browse `CellularStack` under the `cellular/targets` folder to find out how your hardware supports AT sockets.

The AT mode is enabled when the PPP mode is not enabled:

    "lwip.ppp-enabled": false

#### Should you use PPP or AT mode?

Consider the following points when selecting PPP or AT mode:

- Your cellular hosted module may support only AT or PPP mode.
- PPP mode supports both UDP and TCP sockets.
- PPP mode does not allow AT commands after connecting to data mode.
- PPP mode uses the LWIP stack, which uses memory from your Mbed OS application.
- AT mode typically supports only UDP sockets.
- AT mode is potentially better optimized for power consumption.

### Optimize for power consumption

The `CellularPower` class has methods to optimize power saving. The `set_powerl_level()` offers flexibility to control the reception and transmission power levels. In addition, 3GPP has specified advanced power optimizations that are useful for celluar IoT devices: Power Save Mode (PSM) and extended Discontinuous Reception (eDRX).

#### PSM - Power Save Mode

    opt_power_save_mode(int periodic_time, int active_time)

The new 4G modems implementing specifications release 13 and later include PSM. PSM allows the application to tell the modem and network that it does not expect any data in a given time interval, the `periodic_time`. The modem and network can optimize the sleep state and network resource reservations based on this information. During the PSM time, nothing can contact the device from the network side. The application can still send at any time. PSM time can be hours, days or weeks.

The `active_time` tells how many seconds the device waits to receive messages after it has sent data, or when the periodic time has lapsed. If the device sends a report to the management system, the device waits in listen state for the configured amount of time. Listening keeps the radio on in the modem, so it consumes more power than idle state.

This feature offers great power savings for periodically reporting devices. Between reports, the device is in PSM state with the modem in the deep sleep state. The latency of contacting the device is the PSM period.

PSM configuration is negotiated with the network, and the actual PSM time that network has accepted may differ from that requested.

#### eDRX - extended Discontinuous Reception

    opt_receive_period(int mode, EDRXAccessTechnology act_type, uint8_t edrx_value)

eDRX tells how long the device sleeps in continuous connection. The device needs to be able to receive data, but it can tell the network that it checks for incoming messages, for example only every 200 seconds. It can receive messages but only at the given times to allow battery saving sleep periods. These time values are greatly extended compared to normal 4G data transmission – hence the name.

This feature serves devices that need smaller latencies. A connection is kept open all the time, but the modem achieves a sleep state between the reception times. The data connection, if using IPv4, may need periodic keep alive messages to keep the network address translation mapping valid.

An application gives eDRX configuration to the modem which negotiates it with the network. The time accepted by the network may differ from the requested time. Availability of this optimization depends on the cellular network.

#### Sleep more, save energy

CellularConnectionFSM simplifies connecting to a cellular network. `CellularConnectionFSM` is a reliable way to connect, but you may want to optimize it further when implementing applications for constrained battery-operated devices. Figure 5 illustrates the `CellularConnectionFSM` operation.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/api-cellular-connect.png)<span>Figure 5. Cellular connection process in general</span></span>

### Considerations for UDP, TCP and non-IP use

Which networking protocol to use depends on multiple factors. Server communication model, power consumption, reliability need and operator support are the biggest factors. 

TCP is a reliable transmission protocol. For long-lived sessions, periodic keep alive messaging is necessary, which places demands on the main power source. For a long-lived TCP connection, the server application can contact the device. Connections can still have long latencies because the device's use of eDRX power optimization affects when it listens for incoming packets. Mbed TLS supports TLS transport security over TCP. Operators may, however, prevent using TCP over NB-IoT due to device deployment and network planning considerations.

UDP is unreliable, which places the retransmission mechanism burden on the application. UDP does not have a session; thus, the server application can contact the device only for a short while after it has received a UDP message from the device. 

Mbed TLS supports DTLS transport security over UDP.

Non-IP is a new option for communication over NB-IoT. The device sends messages to an operator messaging service. The server application communicates with the messaging service using a web API. The messaging service allows the device and server application to communicate regardless of their activity windows. The cellular network security services provide security inside the cellular network, from the messaging center to the web application with HTTPS. Because network support for non-IP may vary, the application depends on use case. For wider operation, it needs to support both non-IP and IP for a transition period.

For DTLS and TLS transport security, even if the device maintains its own IP address during power save periods, the address may be changed in the network due to Network Address Translation (NAT). NAT is a mechanism to share the few IPv4 addresses among more users. The NAT address change necessitates renegotiation of the (D)TLS security session. The TLS and DTLS protocols support session ID and session ticket mechanisms to optimize the renegotiation. Both device and (D)TLS server must support the used mechanism.

To read more about security, see [Arm Mbed TLS](https://os.mbed.com/docs/latest/reference/tls.html).

### Class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_cellular_device.html)
