## Porting WiFi driver

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/wifi.png)<span>Wi-Fi driver</span></span>

This document describes how to port and test an IEEE 802.11 WiFi driver to
mbed OS. There are two types of Wi-Fi drivers in Mbed OS, depending on which protocol layer it implements. Wi-Fi drivers are either a special case of Ethernet driver or external IP stacks. Wi-Fi drivers require configuration from an application and, therefore, implement both the low level EMAC API or Network stack API and the high level controlling interface API called `WiFiInterface`.

### WifiInterface

Class `WifiInterface` is the controlling API from application to driver.
It is the API that is used for configuring security settings, network names and keys.
The same API is also used for instantiating connection or disconnection phases from network.

Regradless of whether the driver is actually AT-command driven external IP stack, or actual
Ethernet device, this API will be implemented.

Driver should take care of network joining process and present Mbed OS only Ethernet layer
interface, or IP stack. All security handshakes are done by the driver or the device itself.

### EMAC driver

If the device is implementing Ethernet MAC, the driver provided EMAC interface for Mbed OS.
In that case, refer to [Ethernet MAC (EMAC) drivers](porting-ethernet-drivers.html) porting guide
first.

### External IP stack

If the device is actually eternal IP stack, for example AT-command driven module, it needs
to implement full `NetworkStack` API. Refer to [NetworkStack porting guide](networkstack.html)
for implementation details.

### Assumptions

#### Defined behavior

* Driver provides either EMAC interface for network stack, or implements the full NetworkStack API.
* All functions in Socket API are working as specified in API.
* Device is able to pass IPv4 and IPv6 packets
* Device is able to handle IP packets sized 1500 bytes (MTU is 1500).

#### Undefined behavior

* IP payloads larger than 1500 bytes may be fragmented, but not guaranteed to work.

### Testing

For testing the `WifiInterface` implementation and network joining, set of Greentea tests are
provided in Mbed OS tree under `TESTS/network/wifi`.

For testing the Ethernet MAC interface, refer to [Ethernet MAC (EMAC) drivers](porting-ethernet-drivers.html) porting guide. For External IP stacks these do not apply.

Finally testing the stability of driver, or NetworkStack implementation, set of Socket layer tests are provided in `TESTS/netsocket` tree.

