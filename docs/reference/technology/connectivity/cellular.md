# MBED OS CELLULAR

Mbed OS cellular provides your IoT application with an access to world-wide operator-maintained cellular networks, both IP and non-IP as illustrated in Figure 1. Mbed OS cellular implementation is based on international 3GPP and OMA standards and it has been verified to work with all cellular networks such as NB-IoT, CAT-M1, 4G LTE, 3G WCDMA and GPRS.

![Cellular overview](/images/api-cellular-overview.png)

Figure 1. Mbed OS cellular overview

If you are not yet familiar with Mbed OS Connectivity Technology, you may want to read first about [Mbed OS Connectivity Technology](https://www.mbed.com/en/technologies/).

## Key features

Mbed OS cellular is your preferred choice of building applications for [Mbed Cloud](https://cloud.mbed.com/docs/) and cellular IoT solutions.

- Compatible with 3GPP TS 27.007 and 27.005
- OMA Lightweight M2M Client enabler
- Out-of-the-box cellular modem support

3GPP TS 27.007 and 27.005 are standards to provide consistent cellular network data connectivity and SMS over AT command interface for cellular devices regardless of underlaying cellular network.

OMA Lightweight M2M is a protocol from the Open Mobile Alliance for IoT device management. Mbed OS cellular API provides core functionality to implement LWM2M Client, see [OMA LWM2M](https://en.wikipedia.org/wiki/OMA_LWM2M) and [OMA LwM2M ConnMgmt](http://www.openmobilealliance.org/release/LWM2M_CONNMGMT/V1_0-20170314-A/OMA-TS-LWM2M_ConnMgmt-V1_0-20170314-A.pdf).

Several Mbed OS boards with on-board cellular module are already supported out-of-the-box. Because Mbed OS is an open source platform the developers can enable support for new cellular boards with our easy to use adaptation framework, see [porting guide](https://os.mbed.com/docs/v5.8/reference/contributing-connectivity.html#cellularinterface).


## Quick start

Mbed OS connectivity is divided to two phases:

1. Connect to a network
1. Open a socket to send/receive data

The easiest way for connecting your application to Internet over a cellular network is to use the ``CellularConnectionFSM`` class. It encapsulates most of the complexity to connect to the cellular network and also reports any changes in connection status to your application. When connected to a cellular network, you can use Mbed OS network sockets as usual, see Figure 2.

![Quick start](/images/api-cellular-quick-start.png)

Figure 2. Connect to cellular network and open a socket

If you want to see code, you can go to [basic example](https://github.com/ARMmbed/mbed-os-example-cellular) or 
[advanced example](https://github.com/ARMmbed/mbed-os-example-cellular-advanced).

## Cellular connection management

Application can use Cellular APIs to fine-control cellular connection. Cellular APIs are structured based on main-functionalities:

- ``CellularNetwork`` for cellular network features, such as preferred operator, APN, …
- ``CellularPower`` for cellular module power control, such as enabling power save
- ``CellularInformation`` to read cellular module type, firmware version, …
- ``CellularSIM`` to enter PIN code and other SIM management functions
- ``CellularSMS`` to read and write SMS messages

Cellular APIs are enclosed within the CellularDevice class, and thus, to use any cellular API you need to get CellularDevice first. CellularDevice can then be used to open/close Cellular APIs, as illustrated in Figure 3.

![Cellular API](/images/api-cellular-device.png)

Figure 3. Use CellularDevice to open Cellular APIs

When application has opened a Cellular API that can be used to request API methods, for example:

    CellularNetwork *network  = cellularDevice->get_network();
    if (network) {
        printf("Local IP address is %s", network->get_ip_address());
    }

## UDP and TCP sockets

If you want to use UDP or TCP sockets you need an IP stack. Mbed OS cellular has an option to use either 1) lwIP stack which is part of Mbed OS or to use 2) IP stack on cellular module. IP stack deployment is illustrated in Figure 4.

![IP stack](/images/api-cellular-ip-stack.png)

Figure 4. IP stack can be used in PPP or AT mode

### PPP mode with lwIP stack on Mbed OS

In PPP mode, lwIP stack is linked as a part of Mbed OS application. Sockets are implemented on lwIP stack and modem is used over a PPP (Point-to-Point Protocol) link as a plain data-pipe.

PPP mode can be enabled in application configuration file:

    "lwip.ppp-enabled": true

### AT mode with IP stack on modem

In AT mode, modem's internal IP stack is used over an AT link. Sockets are part of IP stack so AT commands are used to control sockets. Socket AT commands are modem specific and need to be implemented on Mbed OS side within a ``CellularStack`` class. You can browse ``CellularStack`` under cellular/targets folder to find out how AT sockets are supported on your cellular module.

AT mode is enabled when PPP mode is not enabled:

    "lwip.ppp-enabled": false

### Should you use PPP or AT mode

Here are some points to consider when selecting PPP or AT mode:

- Your cellular module may support only AT or PPP mode
- PPP mode supports both UDP and TCP sockets
- PPP mode does not allow AT commands after connected to data-mode
- PPP mode uses lwIP stack which takes memory from your Mbed OS application
- AT mode typically supports only UDP sockets
- AT mode is potentially better optimized for power consumption

## Non-IP optimizations

Mbed OS cellular API has also been planned to **support for non-IP communication in the near future**. You need to make two changes when using non-IP in your application:

1. Request a non-IP context from network
1. Open a non-IP socket type

A non-IP stack type need to be requested via CellularNetwork before issuing connect:

    nsapi_error_t set_stack_type(nsapi_ip_stack_t stack_type)

Non-IP communication uses DatagramSocket that is similar to UDPSocket, but without IP addressing and UDP port functionality:

    class DatagramSocket

An application can also request for control-plane optimizations when connecting to a cellular network. The application needs to advertise it’s capability to support control-plane optimizations, and it’s preference to use it. The non-IP optimization options can be selected via CellularNetwork:

    set_ciot_optimization_config(Supported_UE_Opt supported_opt,
                                 Preferred_UE_Opt preferred_opt)

## Optimize for power consumption

The ``CellularPower`` class has methods to optimize power saving. The ``set_powerl_level()`` offers flexibility to control the reception and transmission power levels. In addition 3GPP has specified advanced power optimizations that are especially useful for celluar IoT devices: PSM (Power Save Mode) and eDRX (extended Discontinuous Reception).

### PSM - Power Save Mode

    opt_power_save_mode(int periodic_time, int active_time)

The new 4G modems, implementing specifications release 13 and later, includes PSM. PSM allows the application to tell the modem, and network, that it does not expect any data in given time-interval, the periodic_time. Modem and network can optimize sleep state and network resource reservations based on this information. During the PSM time, the device cannot be contacted from the network side. Application can still start sending at any time. PSM time can be hours, days and weeks even.

The active_time tells how many seconds the device waits to receive messages after it has sent data, or when the periodic time has lapsed. So if the device sends a report to management system, it will wait in listen state for configured amount of time. Listening keeps the radio on in the modem, so it consumes more power then idle state.
This feature offers great power savings for periodically reporting devices. Between reports the device is in PSM state, with modem in deep sleep state. The latency of contacting the device is the PSM period.

PSM configuration is negotiated with the network, and actual PSM time that network has accepted may differ from the requested.

### eDRX - extended Discontinuous Reception

    opt_receive_period(int mode, EDRXAccessTechnology act_type, uint8_t edrx_value)

eDRX tells how long the device sleeps in continuous connection. The device needs to be able to receive data, but it can tell the network that it checks for incoming messages for example only every 200 seconds. It can receive messages, but only at the given times to allow battery saving sleep periods. These time values have been greatly extended compared to normal 4G data transmission – hence the name.

This feature serves devices that need smaller latencies. A connection is kept open all the time, but the modem achieves a sleep state between the reception times. The data connection, if using IPv4, may need periodic keep-alive messages to keep the network address translation mapping valid.

eDRX configuration is given to the modem. It is negotiated with the network, and the time accepted by the network may differ from requested time. Availability of this optimization depends on the cellular network.

### Sleep more, save energy

CellularConnectionFSM is made to simplify connecting to a cellular network. ``CellularConnectionFSM`` is an easy to use and reliable way to connect, but you may want to optimize it further when implementing applications for very constrained battery-operated devices. ``CellularConnectionFSM`` operation is illustrated in Figure 5 for a reference.

![Cellular connect](/images/api-cellular-connect.png)

Figure 5. Cellular connection process in general

## Considerations for UDP, TCP and non-IP use

Which networking protocol to use depends on multiple factors. Server communication model, power consumption, reliability need and operator support are biggest factors. 

TCP is reliable transmission protocol. For long lived sessions periodic keep alive messaging is needed, placing demands on mains power source. For a long lived TCP connection, the server application can contact the device when needed. Connections can still have long latencies as the device usage of eDRX power optimization impacts when it will listen for incoming packets. The mbedTLS supports TLS transport security over TCP. Operators may however prevent using TCP over NB-IoT due to their device deployment and network planning considerations. 

UDP is unreliable, placing re-transmission mechanism burden on application. UDP does not have a session, thus the server application can contact the device only for a short while after it has received a UDP message from the device. 
The mbedTLS supports DTLS transport security over UDP. 

Non-IP is a new option for communication over NB-IoT. Device sends messages to a operator messaging service. Server application communicates with the messaging service using a web API. The messaging service allows device and server application to communicate regardless of each others activity windows. Security inside cellular network is provided by the cellular network security services, and from messaging centre to web application with HTTPS. Because network support for non-IP may vary, the application should depending on use case, for wider operation, support both non-IP and IP for a transition period.

For DTLS and TLS transport security even if the device maintains it’s own IP address during power save periods, the address may be changed in the network due to Network Address Translation. NAT is a mechanism to share the few IPv4 addresses among more users. The NAT address change necessitates re-negotiation of (D)TLS security session. The TLS and DTLS protocols support session ID and session ticket mechanisms to optimise the re-negotiation. Both device and (D)TLS server must support the used mechanism.

## Browse class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_cellular_device.html)
