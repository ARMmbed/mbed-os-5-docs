<h1 id="wifi-port">Wi-Fi</h1>

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/wifi.png)<span>Wi-Fi driver</span></span>

This document describes how to port and test an IEEE 802.11 Wi-Fi driver to Mbed OS. There are two types of Wi-Fi drivers in Mbed OS, depending on which protocol layer it implements. Wi-Fi drivers are either a special case of Ethernet driver or external IP stacks. Wi-Fi drivers require configuration from an application and, therefore, implement both the low-level EMAC API or network stack API and the high-level controlling interface API called `WiFiInterface`.

## WifiInterface

The `WifiInterface` class is the controlling API from application to driver.
You can use this API for configuring security settings, network names and keys and also instantiating connection or disconnection phases from the network.

```
MyWiFiInterface wifi;

nsapi_error_t error = wifi.set_credentials("ssid", "password", NSAPI_SECURITY_WPA_WPA2);
if (error != NSAPI_ERROR_OK) {
    // Failed to set credentials
    ...
}

error = wifi.connect();
if (error != NSAPI_ERROR_OK) {
    // Failed to connect
    ...
}
```

Whether the driver is an AT-command driven external IP stack or an Ethernet device, this is the API to implement.

The driver takes care of the network joining process and presents Mbed OS only Ethernet layer interface, or IP stack. The driver and the device itself do all of the security handshakes.

For description of different driver layer, please read [the IP networking technology](../reference/ip-networking.html) section of this book.

## EMAC driver

If the device is implementing Ethernet MAC, the driver provides the EMAC interface for Mbed OS. In this case, please refer to the [Ethernet MAC (EMAC) drivers](ethernet-port.html) porting guide first.

## External IP stack

If the device is an eternal IP stack, for example an AT-command driven module, it needs to implement the full `NetworkStack` API. Please refer to the [networkStack porting guide](../porting/networkstack.html) for implementation details.

## Assumptions

### Defined behavior

- The driver either provides the EMAC interface for the network stack, or implements the full NetworkStack API.
- All functions in the Socket API are working as specified in API.
- The device can pass IPv4 and IPv6 packets.
- The device can handle IP packets sized 1500 bytes (MTU is 1500).

### Undefined behavior

- IP payloads larger than 1500 bytes may be fragmented but not guaranteed to work.

## Testing

For testing the `WifiInterface` implementation and network joining, we provide a set of Greentea tests in the Mbed OS tree under `TESTS/network/wifi`.

For testing the Ethernet MAC interface, please refer to the [Ethernet MAC (EMAC) drivers](ethernet-port.html) porting guide. For external IP stacks, these tests do not apply.

To test the stability of the driver or NetworkStack implementation, we provide a set of socket layer tests in the `TESTS/netsocket` tree. Please see the [Network Socket test plan](https://github.com/ARMmbed/mbed-os/blob/master/TESTS/netsocket/README.md) for instructions on how to run Mbed OS socket tests.
