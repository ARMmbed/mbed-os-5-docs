# IP networking

IP Networking in Mbed OS is layered in three clearly defined API levels. The diagram below shows the layers next to the closest matching [OSI model](https://en.wikipedia.org/wiki/OSI_model) layers.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/ip-networking.png)<span>IP networking</span></span>

The following sections introduce the APIs and technologies implemented in each level.

## Socket API

The Socket API is the common API among all IP connectivity methods. All network stacks in Mbed OS provide the same Socket API, making applications portable among different connectivity methods or even stacks.

In the OSI model, the Socket API relates to layer 4, the Transport layer. In Mbed OS, the Socket API supports both TCP and UDP protocols.

Refer to [Socket API](../apis/network-socket.html) reference for usage instructions.

## IP stacks

Mbed OS has three options to select for the IP stack. The connectivity modules provides two built-in IP stacks or an external IP stack.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/networkstacks.png)<span>Network stack</span></span>

As the diagram above shows, all stacks implement the same Socket API. Therefore, the application developer rarely needs to know which stack is going to be used. Mbed OS chooses one at the build time, and usually it is LwIP.

Some external Wi-Fi modules and most cellular modules are in fact external IP stacks from the application point of view. In that case, the network driver implements the full Network stack API. These drivers usually drive the module through an AT-command type of interface. Using an external IP module saves RAM and Flash, but depending on the driver and AT-command interface, it might not properly match the full Socket API.

The following table summarizes different stacks, use cases and their limitations.

|Stack|Network protocols supported|Use cases|Limitations|
|-----|---------------------------|---------|-----------|
|LwIP|IPv4, IPv6, PPP|Ethernet, Wi-Fi, 2G/3G/4G Cellular|4 sockets, 1 interface, no routing|
|Nanostack|IPv6, 6LoWPAN, Thread|Mesh networking, Border Router|Only IPv6|
|External IP module|Depends on the module|(Save RAM/Flash)|Depends on the module. Usually poor match to Socket API|

### Configuring the IP stack interface

Depending on the Layer 3, Network layer, protocol used, there are different ways to configure the interface. It also depends on the stack used, which configurations are supported on each link layer.

|Stack|Data link layer|Network layer|Configurations supported|
|-----|---------------|-------------|------------------------|
|LwIP|Ethernet, WiFi|IPv4|DHCP, static|
|LwIP|Ethernet, WiFi|IPv6|[RFC 4862](https://tools.ietf.org/html/rfc4862) IPv6 Stateless Address Autoconfiguration. No DHCPv6 support|
|LwIP|PPP|IPv4,IPv6|automatic|
|Nanostack|Ethernet|IPv6|static or [RFC 4862](https://tools.ietf.org/html/rfc4862) IPv6 Stateless Address Autoconfiguration. No DHCPv6 support|
|Nanostack|IEEE 802.15.4|6LoWPAN|Thread or 6LoWPAN-ND+RPL|

## Network interfaces

Network interfaces are the application level APIs where users choose the driver, connectivity method and IP stack. Each connectivity methods requires different configuration, so these APIs are not interchangeable. The application developer must choose one. Choosing the interface also automatically pulls in the network stack as a dependency.

Please note that the interface API is not the same as the network driver. The interface API is the control interface for the application. The network driver implements the controlling API only if it requires configuration from application. From the application point of view, there is no difference, but the network driver developer needs to be aware of that.

Mbed OS implements the following network interface APIs:

- Ethernet.
- WiFi.
- Cellular (PPP).
- 6LoWPAN-ND mesh networking.
- Thread mesh networking.
- Wi-SUN mesh networking.

Refer to [Network Interface](../apis/network-interfaces.html) API reference for usage instructions.

## Network drivers

"Network driver" describes different APIs that connect a networking device to the IP stack or Socket API. Below is a description of each driver API.

### Ethernet driver

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/emac.png)<span>Emac API</span></span>

Ethernet drivers are implemented using the stack-independent EMAC API. Because the Ethernet driver requires no configuration, it does not implement any controlling interface for the application.

### Wi-Fi driver

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/wifi.png)<span>Wi-Fi driver</span></span>

There are two types of Wi-Fi drivers in Mbed OS, depending on which protocol layer it implements. Wi-Fi drivers are either a special case of Ethernet driver or external IP stacks. Wi-Fi drivers require configuration from an application and, therefore, implement both the low level EMAC API or Network stack API and the high level controlling interface API called `WiFiInterface`.

### Cellular modem driver

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/cellular.png)<span>Cellular driver</span></span>

Cellular drivers have the same two separate cases as Wi-Fi. If they use an external IP stack, the driver implements the Network stack API. If they use the internal IP stack, LwIP, then they implement the Serial PPP driver.

### Mesh (Wi-SUN, 6LoWPAN-ND, Thread) RF driver

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/rf-driver.png)<span>RF driver</span></span>

On Mesh networks, Nanostack uses IEEE 802.15.4 radios for transmitting and receiving packets. The RF driver implements the `NanostackRfPhy` API.

This driver type has no other use cases, so it is implemented in C using a Nanostack-specific API.

Please see the [Porting a new RF driver for the 6LoWPAN stack](../porting/lora-port.html) for more information.
