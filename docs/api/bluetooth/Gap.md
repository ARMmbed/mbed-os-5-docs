# GAP

The Generic Access Profile is the layer of the stack that handles connectivity tasks. This includes link establishment and termination, advertising and scanning.

Devices with data to publish can use GAP to advertise. They can include the data in the advertisement itself, inside the scan response, or leave a peer device to query it after the connection has been established.

The other side of the process is the act of scanning, which listens for advertisements, allows you to query the advertisers for more data through a scan request or connect in order to query the peer device for the data you want.

Advertising, scanning and connection all have parameters that let you find a compromise between desired power consumption levels, latency and efficiency of these processes.

### Advertising

Advertising consists of broadcasting at a regular interval a small amount of data containing valuable information about the device. Peer devices listening on BLE advertising channels may scan these packets.

Scanners may also request additional information from device advertising by sending a scan request. If the broadcaster accepts scan requests, it can reply with a scan response packet containing additional information.

### Scanning

Scanning consists of listening for peer advertising packets. From a scan, a device can identify devices available in its environment.

If the device scans actively, it sends scan request to scannable advertisers and collects their scan responses.
 
### Privacy

Privacy is a feature that allows a device to avoid being tracked by other (untrusted) devices. The device achieves it by periodically generating a new random address. The random address may be a resolvable random address, enabling trusted devices to recognize it as belonging to the same device. These trusted devices receive an Identity Resolution Key (IRK) during pairing. The SecurityManager handles this and relies on the other device accepting and storing the IRK.

You need to enable privacy by calling `enablePrivacy()` after initializing the SecurityManager because privacy requires SecurityManager to handle IRKs. Set the behavior of privacy enabled devices by using `setCentralPrivacyConfiguration()`, which specifies what the device should be with devices using random addresses, and `setPeripheralPrivacyConfiguration`. Random addresses that privacy enabled devices generate can be of two types: resolvable (by devices who have the IRK) and unresolvable. You can't use unresolvable addresses for connecting and connectable advertising; therefore, use a resolvable one for these, regardless of the privacy configuration.

### Modulation schemes

When supported by the host and controller, you can select different modulation schemes:

 - LE 1M PHY.
 - LE 2M PHY.
 - LE coded PHY.
 
These provide different compromises between bandwidth, power usage and error resiliency (see BLUETOOTH SPECIFICATION Version 5.0 Vol 1, Part A - 1.2).

You may set preferred PHYs (separately for RX and TX) using `setPreferredPhys()`. You may also set the currently used PHYs on a selected connection using `setPhy()`. Both of these settings are only advisory. The controller is allowed to make its own decision on the best PHY to use based on your request, the peer's supported features and the connection's physical conditions.

You may query the currently used PHY using `readPhy()`, which returns the result through a call to the registered event handler. You may register the handler with `setEventHandler()`. The events inform about the currently used PHY and of any changes to PHYs, which the controller or the peer may trigger autonomously.

## GAP class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.10/mbed-os-api-doxy/class_gap.html)

## GAP example

Here is an example demonstrating how to use the GAP API to advertise, scan, connect and disconnect and how parameters influence efficiency of these actions.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-GAP/)](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-GAP/file/37872bf83624/source/main.cpp)
