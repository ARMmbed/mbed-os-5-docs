## Connectivity

 There are two different kinds of connectivity, IP and Non-IP. IP connected devices have an IP address, either IPV4 or IPV6. Non-IP devices must use a gateway in order to connect to the internet, the gateway translates the Non-IP protocol to IP. 

 1. IP 
 	- Device has an IPV4/V6 address, which makes it directly addressable from the internet
 	- Connectivity like Ethernet, WiFi, Cellular, Thread, NBIoT ... etc. 
 	- TCP/UDP capable
 	- Can run application level protocols like MQTT, WebSockets, HTML...etc
 1. Non-IP
 	- Device does not have an IP Address. 
 	- Connectivity like Bluetooth Low Energy, LoRa, and sub gigahertz.
 	- Gateways can translate between IP to Non-IP protocol to enable internet connectivity. 
 		- For example, LoRa has gateways to connect it to the application servers, the gateways are simple passthroughs for the data. BLE on the other hand does not have a gateway specification, so any implimentation is a custom mapping where the gateway translates and transcodes data between BLE and IP. 

### IP Connectivity

The [Network Socket API](https://os.mbed.com/docs/latest/reference/network-socket.html) is the API used for all IP based devices in Mbed OS. The TCP and UDP socket that are used as the basis for application level protocols liek HTTP and MQTT are based on the NSAPI level. 

The [Network Interfaces](https://os.mbed.com/docs/latest/reference/network-interfaces.html) are used to construct the NSAPI. Each IP connectivity method has its own Network Interface. When you want to change you connectivity method your application code stays the same, all you change is the network interface and the configurations associated with it.

	- Ethernet - `EthernetInterface eth` then `eth.connect()`
	- WiFi - 'WiFiInterface wifi', different wifi chips will have different interfaces. To connect use `wifi.connect('SSID','Password')`. You can modify the Security settings for WPA, WPA2, ...etc. 
	- Cellular - `CellularInterface cell` then `cell.connect(pincode,apn)`

#### Security with TLS
 // Coming Soon. In the september release there will be a TLSSocket, which will make security trivially easy to use. 

 You can secure your socket connections with [Mbed TLS](https://os.mbed.com/docs/latest/reference/tls.html)

### Non-IP

There are several different Non-IP connectivity options in Mbed OS, each has its own API. 

#### BLE

The [BLE API](https://os.mbed.com/docs/latest/reference/bluetooth.html) is an application level API that is compatible with several chip vendor stacks. The API stays the same no matter which BLE chip you use, so your application code is fully portable. 

The BLE API makes it really easy to access GATT and GAP, create Services and Profiles. In addition the Security Manager makes securing your connections trivially simple. 

BLE is designed to mostly be used device to device, typically from embedded device to phone. While gateways exist for BLE to connect them to the internet they are all non-standard and custom with some sort of application running on the gateway to cache data and then send it across BLE characteristics. 

#### LoRa

The [LoRa API](https://os.mbed.com/docs/v5.9/reference/lorawan.html) makes it easy to configure and use LoRa devices around the world. By the nature of how LoRa works the data is always secured from device through the gateway all the way to the cloud. The LoRa gateways are just simple passthroughs for the data. While you can do LoRa device to device, the majority of the use cases are device through gateway to the backend app in the cloud. Be advised though, the gateways can be expensive. 

We reccomend using [The Things Network](https://www.thethingsnetwork.org/) as it is a free LoRa network and application backhaul provider with global coverage that makes getting LoRa devices up and running super simple. 

For an in depth walkthrough of how to get started with LoRa I reccomend the [Getting Started with LoRa]() tutorial. 