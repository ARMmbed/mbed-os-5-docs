# Cellular networking

Mbed OS cellular provides your IoT application with access to world-wide operator-maintained cellular networks, both IP and non-IP, as Figure 1 illustrates. Mbed OS cellular implementation is based on international 3GPP and OMA standards, and it has been verified to work with all cellular networks such as NB-IoT, CAT-M1, 4G LTE, 3G WCDMA and GPRS.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/api-cellular-overview.png)<span>Figure 1. Mbed OS cellular overview</span></span>

Please read about [Mbed OS connectivity technology](https://www.mbed.com/en/technologies/connectivity/) if you are not yet familiar with it.

## Key features

Key features of the Mbed OS cellular APIs include:

- Compatible with 3GPP TS 27.007 and 27.005.
- Implements core functionality for OMA Lightweight M2M Client.
- Supports many Mbed Enabled cellular boards.

3GPP TS 27.007 and 27.005 are standards to provide consistent cellular network data connectivity and SMS over an AT command interface for cellular devices, regardless of the underlying cellular network.

OMA Lightweight M2M is a protocol from the Open Mobile Alliance for IoT device management. The Mbed OS cellular API provides core functionality to implement the LWM2M Client. For more information, please see _OMA LightweightM2M_ and _OMA LWM2M Object Connectivity Management_ at [OMA Specifications](http://openmobilealliance.org/wp/index.html).

Many Mbed Enabled boards already support cellular connectivity. Because Mbed OS is an open source platform, developers can enable support for new cellular boards with our adaptation framework. Please see our [cellular porting guide](../porting/cellular-device-porting.html) for more information.

## Quick start

To use cellular data connection:

1. Connect to a network.
1. Open a socket to send or receive data.

With cellular, the easiest way to connect your application to the internet over a cellular network is to use the `CellularContext` class and `get_default_instance`. It encapsulates most of the complexity of connecting to the cellular network and also reports any changes in connection status to your application. When connected to a cellular network, you can use Mbed OS network sockets as usual.

A network interface instantiated directly or using calls such as `CellularInterface::get_default_instance()` or `CellularContext::get_default_instance()` is initially unconfigured. You can call `NetworkInterface::set_default_parameters()` to set the default parameters that would have been set if the interface had been requested using `NetworkInterface::get_default_instance()`.

If you want to see code, you can go to our [cellular example](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-cellular/).

## Cellular device selection

If an Mbed OS target board has an on-board cellular device then the cellular framework uses that by default when calling `get_default_instance()`. The default cellular device instance can be overridden in the cellular driver `mbed_lib.json` files or an application can override  `NetworkInterface::get_default_instance()`.

## Cellular APIs

As an application developer, you should use and refer only to classes located under API folder. All the other classes have implementation details that are expected to change frequently.

Cellular APIs are structured based on main functionalities:

- `CellularContext` is the main interface for the application. You can use it to connect to the operator's Access Point Name (APN).
- `CellularNetwork` for cellular network features, such as registering and attaching to a network.
- `CellularInformation` to read the cellular device and SIM information.
- `CellularSMS` to read and write SMS messages.

You can instantiate the CellularContext class with `CellularContext::get_default_instance()`, which opens `CellularDevice` and, through the device, opens `CellularContext`. Opening `CellularContext` through `get_default_instance` uses values from `mbed_app.json`.
These values are not defined by default, and you must override them in `mbed_app.json` if you need them:
```
"target_overrides": {
        "*": {
            "nsapi.default-cellular-plmn": "\"12346\"",
            "nsapi.default-cellular-sim-pin": "\"1234\"",
            "nsapi.default-cellular-apn": "\"internet\"",
            "nsapi.default-cellular-username": 0,
            "nsapi.default-cellular-password": 0
        }
    }
```
The CellularDevice class encloses cellular APIs. Therefore, to use a cellular API, you need to get CellularDevice first. You can then use CellularDevice to open and close cellular APIs.

When an application has opened a cellular API, you can use it to request API methods. For example:
```
    CellularContext *ctx  = cellularDevice->create_context();
    if (ctx) {
    		if (ctx->connect() == NSAPI_ERROR_OK) {
      			printf("Local IP address is %s", ctx->get_ip_address());
    		}
    }
```
## UDP and TCP sockets

If you want to use UDP or TCP sockets, you need an IP stack. Mbed OS cellular has an option to use either the LWIP stack (PPP mode), which is part of Mbed OS, or to use the IP stack on the cellular device (AT mode).

### PPP mode with the LWIP stack on Mbed OS

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/Cell_PPP.png)</span>

In PPP (Point-to-Point Protocol) mode, the LWIP stack is linked as a part of the Mbed OS application. Because LWIP stack implements sockets, the socket functionality is hardware-independent.

You can enable PPP mode and also configure LWIP features in the application configuration file:

    "lwip.ppp-enabled": true
    "lwip.ipv4-enabled": true
    "lwip.ipv6-enabled": true
    "lwip.tcp-enabled": true

### AT mode with the IP stack on the modem

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/Cell_AT.png)</span>

In AT mode, the modem's internal IP stack is used over an AT link. Sockets are part of the IP stack, so AT commands are used to control sockets. Socket AT commands are modem specific, and need to be implemented on the Mbed OS side. You can browse `CellularStack` under the `cellular/targets` folder to find out how your hardware supports AT sockets.

The AT mode is enabled when the PPP mode is not enabled:

    "lwip.ppp-enabled": false

### Should you use PPP or AT mode?

Consider the following points when selecting PPP or AT mode:

- A cellular device may support only AT or PPP mode.
- PPP mode supports both UDP and TCP sockets.
- PPP mode does not allow AT commands after connecting to data mode.
- PPP mode uses the LWIP stack, which uses memory from your Mbed OS application.
- AT mode typically supports only UDP sockets.
- AT mode is potentially better optimized for power consumption.

## Optimize for power consumption

The cellular API has methods to optimize power saving: Power Save Mode (PSM) and extended Discontinuous Reception (eDRX).

### PSM - Power Save Mode

    set_power_save_mode(int periodic_time, int active_time)

The new 4G modems implementing specifications release 13 and later include PSM. PSM allows the application to tell the modem and network that it does not expect any data in a given time interval, the `periodic_time`. The modem and network can optimize the sleep state and network resource reservations based on this information. During the PSM time, nothing can contact the device from the network side. The application can still send at any time. PSM time can be hours, days or weeks.

The `active_time` tells how many seconds the device waits to receive messages after it has sent data, or when the periodic time has lapsed. If the device sends a report to the management system, the device waits in listen state for the configured amount of time. Listening keeps the radio on in the modem, so it consumes more power than idle state.

This feature offers great power savings for periodically reporting devices. Between reports, the device is in PSM state with the modem in the deep sleep state. The latency of contacting the device is the PSM period.

PSM configuration is negotiated with the network, and the actual PSM time that network has accepted may differ from that requested.

### eDRX - extended Discontinuous Reception

    set_receive_period(int mode, EDRXAccessTechnology act_type, uint8_t edrx_value)

eDRX tells how long the device sleeps in continuous connection. The device needs to be able to receive data, but it can tell the network that it checks for incoming messages, for example only every 200 seconds. It can receive messages but only at the given times to allow battery saving sleep periods. These time values are greatly extended compared to normal 4G data transmission – hence the name.

This feature serves devices that need smaller latencies. A connection is kept open all the time, but the modem achieves a sleep state between the reception times. The data connection, if using IPv4, may need periodic keep alive messages to keep the network address translation mapping valid.

An application gives eDRX configuration to the modem which negotiates it with the network. The time accepted by the network may differ from the requested time. Availability of this optimization depends on the cellular network.

## Considerations for UDP, TCP and non-IP use

Which networking protocol to use depends on multiple factors. Server communication model, power consumption, reliability need and operator support are the biggest factors.

TCP is a reliable transmission protocol. For long-lived sessions, periodic keep alive messaging is necessary, which places demands on the main power source. For a long-lived TCP connection, the server application can contact the device. Connections can still have long latencies because the device's use of eDRX power optimization affects when it listens for incoming packets. Mbed TLS supports TLS transport security over TCP. Operators may, however, prevent using TCP over NB-IoT due to device deployment and network planning considerations.

UDP is unreliable, which places the retransmission mechanism burden on the application. UDP does not have a session; thus, the server application can contact the device only for a short while after it has received a UDP message from the device.

Mbed TLS supports DTLS transport security over UDP.

Non-IP is a new option for communication over NB-IoT. The device sends messages to an operator messaging service. The server application communicates with the messaging service using a web API. The messaging service allows the device and server application to communicate regardless of their activity windows. The cellular network security services provide security inside the cellular network, from the messaging center to the web application with HTTPS. Because network support for non-IP may vary, the application depends on use case. For wider operation, it needs to support both non-IP and IP for a transition period.

For DTLS and TLS transport security, even if the device maintains its own IP address during power save periods, the address may be changed in the network due to Network Address Translation (NAT). NAT is a mechanism to share the few IPv4 addresses among more users. The NAT address change necessitates renegotiation of the (D)TLS security session. The TLS and DTLS protocols support session ID and session ticket mechanisms to optimize the renegotiation. Both device and (D)TLS server must support the used mechanism.

To read more about security, see [Arm Mbed TLS](../apis/tls.html).
