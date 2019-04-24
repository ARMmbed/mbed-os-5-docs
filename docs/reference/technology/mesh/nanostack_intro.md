<h1 id="nanostack-introduction-tech">Nanostack Introduction</h1>

Nanostack library implements 6LoWPAN-based wireless mesh protocols like:

 * [Wi-SUN](../reference/wisun-tech.html),
 * [Thread](../reference/thread-tech.html) and
 * [6LoWPAN-ND](../reference/6LoWPAN-ND-tech.html).
 
 Nanostack library requires the following Mbed OS components to operate:
 
  * IEEE 802.15.4 based radio driver.
  * mbedtls
  * mbed-trace.
  * nanostack-libservice.
  * mbed-coap.
 
This chapter introduces the Nanostack architecture. It contains the following sections:

- [Architecture](#architecture).
- [6LoWPAN stack](#6lowpan-stack).
- [Networking](#networking).

### Architecture

_IPv6 Low power Wireless Personal Area Network_ (6LoWPAN) is an adaptation layer that enables the use of IPv6 over low power wireless and supports IPv6 and _User Datagram Protocol_ (UDP) header compression. The Internet Protocol (IP) header compression allows 6LoWPAN packets to be compact, making it robust and, ideal for low power and lossy networks. It also handles fragmentation and reassembly of packets in scenarios where payloads larger than the _Maximum Transmission Unit_ (MTU) of the supported interface are transferred (a maximum of 1280 bytes).

The industry leading Arm 6LoWPAN stack is both highly scalable and reliable, but also provides an unrivaled feature set to include a compact source code base and optimal memory usage. Additionally, the 6LoWPAN stack can be supplied with optional software modules for security and Pelion Device Management. The modular structure of the design makes it possible for Arm to accommodate most requirements.

The combination of 6LoWPAN stack and 6LoWPAN border router _Access Point_ (AP) software enables developers to use the extremely flexible and multi-purpose mesh communication solution for most applications (see _Figure 1-1_).

**Figure 1-1 6LoWPAN network architecture**

![nw-arc](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/6lowpan_network_architecture.png)

### 6LoWPAN stack

The 6LoWPAN stack is modular in design and uses an extremely lightweight event environment internally. Additional benefits of the model are lower hardware requirements in the terms of flash and RAM usage. 

The stack architecture can be divided into four high-level components:

- [Event core](#event-core).
- [Protocol modules](#protocol-modules).
- [Security components (optional)](#optional-security-components).
- [Application modules](#application-modules).

These components are illustrated in _Figure 1-2_.

**Figure 1-2 The components that comprise the 6LoWPAN stack architecture**

![stack-arc](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/6lowpan_stack_architecture.png)

<span class="notes">**Note**: For simplicity, the event core is shown to be part of the same component, alongside the protocol modules.</span>

#### Event core

The event core is responsible for the low level events, scheduling and system timer functions. The core module provides all the basic functionality that the rest of the modules need (with the exception of the application modules) and is undertaken with a low resource requirement. The design objective has been to reserve and use minimal resources of the hardware platform and, instead, leave all unnecessary timers, for example, unused so that the developer has full control over these resources from the application layer.

The event system provides the application with the tools and functionality that it needs, for example, to post timed events to itself and create events with specific callback functions.

The event system relies on Platform API to provide portable set of functions that it needs. These platform drivers are then ported for each embedded platform you want to run the 6LoWPAN stack.

#### Protocol modules

The 6LoWPAN stack implements a wide range of protocols as individual modules, which is illustrated in _Figure 1-2_. These modules are designed to use an internal data structure that is used to exchange packets. The stack uses a no-copy design wherever possible because in some modules a packet may be copied to provide a re-transmission functionality, as mandated by related standards.

The modular design of the 6LoWPAN stack allows some modules to be omitted from the build, for example, excluding the _Transmission Control Protocol_ (TCP) module would disable the TCP transport mechanism.

At the upper-edge of the 6LoWPAN stack, the Socket _Application Programming Interface_ (API) is exposed (see _Figure 1-2_). This API is designed to provide a _Berkeley Software Distribution_ (BSD) socket-like interface for the application to receive and transmit packets using standard IPv6 address and port number definitions. The function names also roughly follow the BSD socket definitions with some minor modifications due to the nature of the event environment. The intention is to clearly indicate to the developer that minute differences exist between the embedded socket interface and a full BSD socket interface.

#### Optional security components

The 6LoWPAN stack can be delivered with optional security components. These components provide strong security mechanisms that offer data authentication, device authentication and authorization, and data encryption. The stack supports the following standards:

- PANA (requires EAP, TLS and SHA-256)
- EAP (requires TLS and SHA-256)
- TLS1.2 (requires SHA-256)
- SHA-256
- ECC (ECDSA and ECDHE) (requires X509.3)
- X509.3 (requires ECC)

The _Elliptic Curve Cryptography_ (ECC) component supports the EEC curve NIST-P256 as defined in the Smart Grid standards collection of the _National Institute of Standards and Technology_ (NIST); see [NIST](http://www.nist.gov/smartgrid/). The stack also provides full x509.3 certificate support along with certificate chaining.

The stack essentially allows the end device to be a part of a full _Public Key Infrastructure_ (PKI) security scheme.

<span class="notes">**Note**: The 6LoWPAN stack is dependent of the _Advanced Encryption Standard_ (AES)-_Counter Mode Cipher_* (CCM*) component that is part of the core stack.</span>

#### Application modules

The 6LoWPAN stack runs on a lightweight event-based system that allows low power consumption and minimal latency. Application logic is implemented in a specific event handler called tasklet. The 6LoWPAN stack allows the developer to define multiple tasklets to ease the task of application design. Each of these tasklets can then have full access to the network stack and its features. The system relies on events and does not attempt to provide real multi-thread services, so the developer does not need to be concerned about multiple access to resources.

One of the most important aspects of an application tasklet design is for the developer to understand how the event environment impacts it. The system does not support the capability for a multi-thread environment.

The application tasklet must be designed so that it cannot block the execution for an extended period of time. A simple design rule is that a tasklet needs to be implemented in a state machine fashion. The tasklet receives an event that it processes, performs an action, such as reading a sensor value, builds a packet and transmits it, sets up a new timed event, and eventually returns. When the tasklet returns, the event core system schedules the networking stack to take care of the actual transmission of the packet. The delay between the actual transmission of the packet and the `socket_sendto( )` function at the application layer depends on the overall loading of the device at that time. In an otherwise idle situation, the delay is subject to the performance of the processor, but is typically negligible.

_Figure 1-3_ shows the various protocol modules that make up the 6LoWPAN stack, which are placed alongside the Open Systems Interconnect (OSI) model.

**Figure 1-3 The 6LoWPAN stack placed alongside the OSI model**

![osi](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/6lowpan_stack_osi_model.png)

### Protocol layers and related standards

The related standards supported by the stack are:

- 6LoWPAN:
	- RFC4944.
	- RFC6282.
	- RFC6775.
- IPv6:
	- RFC2460.
	- RFC2464.
	- RFC3168 (parts).
	- RFC4291 (parts).
	- RFC6040.
	- RFC6437.
	- RFC6946.
- UDP:
	- RFC768.
- TCP:
	- RFC793 (parts).
- RPL:
	- RFC6550.
	- RFC6552.
	- RFC6553.
	- RFC6554.
	- RFC6719.
	- RFC2473 (parts).
- ICMPv6:
	- RFC4443 (parts).
	- RFC4861 (parts).
	- RFC4862 (parts).
- MLE:
	- IETF draft-kelsey-intarea-mesh-link-establishment-06.
	- IEEE802.15.4.
	- IEEE802.15.4-2006 (certified).
	- IEEE802.15.4g (parts).
- MPL:
	- IETF draft-ietf-roll-trickle-mcast-12 (parts).
- AES:
	- FIPS 197.
	- SP 800-38C.
- PANA:
	- RFC5191.
	- RFC6345.
	- RFC6786.
- EAP:
	- RFC3748.
	- RFC5216.
- TLS:
	- RFC4279.
	- RFC5216.
	- RFC5246.
	- RFC6655.
	- IETF draft-mcgrew-tls-aes-ccm-ecc-05.
- ECC:
	- RFC4492.
	- RFC5289.
	- IETF draft-mcgrew-tls-aes-ccm-ecc-05.

### Interfaces

The 6LoWPAN stack offers application developers programming interfaces for configuring the 6LoWPAN network, defining security levels and sending and receiving packets. The 6LoWPAN stack requires the developers to provide functions for platform specific tasks and network drivers for physical layer. For more information on programming interfaces, see [Mbed Mesh API](../apis/mesh-api.html).


## Networking

This chapter discusses the networking topology and the protocols used.

### Networking topology

The 6LoWPAN stack uses two types of networking topology, namely the star and tree topologies, as shown in _Figure 1-5_.

**Figure 1-5 Networking topologies supported by the 6LoWPAN stack ecosystem**

![nw-topologies](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/6lowpan_stack_networking_topologies.png)

### MAC

The _Media Access Control_ (MAC) implementation is based on the IEEE802.15.4-2006 standard and is used for MAC layer communication between nodes such as beacon scans and responses, and data requests and indications. The MAC implementation has already been certified on multiple platforms.

The MAC implements the non-beacon enabled modes of the standard. It does not implement _Guaranteed Time Slot_ (GTS).

### UDP

The 6LoWPAN stack supports the UDP transport protocol. Applications can use the Socket API to send and receive data using UDP sockets. UDP is typically used by applications to deliver short messages over IP. It is an unreliable, connectionless protocol, but can be used for broadcast and multicast messages. The advantage of UDP is that it does not require any kind of connection formation or handshake process to take place prior to communication. UDP is the classic fire-and-forget transport mechanism that combines inherent low reliability, requiring minimal overhead.

A disadvantage of UDP can easily be mitigated by using a simple application layer, end-to-end acknowledgment scheme. As an efficient and scalable example of such a solution, see the _Constrained Application Protocol_(CoAP) _Acknowledgement_ (ACK) mechanism as defined in [CoAP](http://tools.ietf.org/html/rfc7252).

### TCP

The 6LoWPAN stack supports the _Transmission Control Protocol_ (TCP) and applications can use the socket interface APIs of the stack to send and receive data using TCP sockets. Applications requiring a reliable, ordered transport for a stream of bytes can typically use TCP. However, TCP is not suitable for every application because it only supports unicast communication and reacts badly to packet loss. TCP is not suitable for very short transactions because the ratio of overhead to application data typically increases fairly quickly. Additionally, the use of TCP can have very adverse effects on the power consumption of a device because of the duration of the TCP handshake process.

### RPL routing

_Routing Protocol for Low power and Lossy networks_ (RPL) is a distance vector IPv6 routing protocol defined in the _Internet Engineering Task Force_ (IETF) for low power and lossy networks that specifies how to build a _Destination Oriented Directed Acyclic Graph_ (DODAG) using an objective function and a set of metrics and constraints. RPL is optimized for a many-to-one topology. Neighbors keep route records of the edge router as a final destination. The reverse route, or source route, is kept by the edge router and is used for sending data to any node in the network it has a route for. When a node sends a packet to another node, the packet travels up to a common ancestor in the DAG, at which point it is forwarded in the down direction to the destination.

### Automatic network healing process

It is fairly common for the RF channel to change even if the physical location of the actual mesh network has not. The network must then adapt to the new channel immediately and with ease.

The standards that the 6LoWPAN stack uses provide feedback from multiple protocol layers, such as the MAC, network and routing layers. This multiple layer approach provides the stack with numerous sources of information that can be used to make automatic decisions as to when network reconfiguration can be initiated. It can also be delivered to other devices in the IP network using standard _Internet Control Message Protocol_ (ICMP)v6 messages. More specifically, these messages can either be ICMPv6 Destination Unreachable or No Route To Host types.

#### MAC layer

When repeated notifications of _layer two_ (L2) ACKs are not passed up to the higher layers, a possible lost connection has occurred. If the ACK messages are lost from a parent device in the routing topology, this results in one of the following actions: 1) switch to a secondary parent, that is, an alternative parent that has been stored for backup; or 2) the stack should initiate a local network reconfiguration.

If the L2 ACKs are missing from a child node, the routing node typically transmits an ICMPv6 error message to the originator of the packet. If an application on the device itself is the originator, the application is notified of the error using a system event.

### Selecting Radio

6LoWPAN network uses IEEE 802.15.4 radios and therefore, operates on one of the following unlicensed frequency bands:

- 868.0–868.6 MHz: Europe, allows one communication channel (2003, 2006, 2011[4]).
- 902–928 MHz: North America, up to ten channels (2003), extended to thirty (2006).
- 2400–2483.5 MHz: worldwide use, up to sixteen channels (2003, 2006).

The data rate varies from 20 kbit/s to 250 kbit/s. Consider the data rate available per node when designing the application. Basically, the data rate is divided between all nodes in the network. Allocate roughly half of the channel capacity for signalling purposes. Each hop requires retransmisson of the packet.

![Datarate](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/bw.png)

<span class="tips">**Rule of thumb:** The bandwidth per node is divided by the number of nodes in the network and the number of hops.</span>
