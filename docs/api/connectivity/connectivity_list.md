# Connectivity APIs

## Network socket

- [Non-IP cellular socket](../apis/network-socket-apis.html): Send and receive 3GPP non-IP datagrams (NIDD) using the cellular IoT feature.
- [Socket](../apis/socket.html): The abstract base class for all of the protocol-specific socket types.
- [SocketAddress](../apis/socketaddress.html): Used to represent the IP address and port pair of a unique network endpoint.
- [SocketStats](../apis/socketstats.html): Read the network socket statistics for all sockets (both currently in use and closed).
- [TCPSocket](../apis/tcpsocket.html): Send a stream of data over TCP.
- [UDPSocket](../apis/udpsocket.html): Send packets of data over UDP.

## Network interface

- [Cellular](../apis/network-interface-apis.html): Connect to the internet over a Cellular device.
- [Ethernet](../apis/ethernet.html): Connect to the internet over Ethernet.
- [Mesh](../apis/mesh-api.html): Use the IPv6 mesh network topologies through the Nanostack networking stack to connect to a mesh network: Wi-Sun or 6LoWPAN-ND.
- [Network status](../apis/network-status.html): Trigger a callback each time the network interface's status changes.
- [Wi-Fi](../apis/wi-fi.html): Connect to the internet over a Wi-Fi device.

## Secure socket

- [DTLSSocket](../apis/secure-socket-apis.html): Implement a DTLS stream over the existing Socket transport.
- [TLSSocket](../apis/tlssocket.html): Implement a TLS stream over the existing Socket transport

## DNS

- [DNS Resolver](../apis/dns-apis.html): Perform DNS host name resolutions to convert resource names to IP addresses.

## Bluetooth (BLE)

- [BLE](../apis/bluetooth-apis.html): Interface with the BLE controller on the board.
- [GAP](../apis/gap.html): Handle connectivity tasks.
- [GattClient](../apis/gattclient.html): Initiate interactions with a GattServer to discover services, characteristics and descriptors and perform operations on them.
- [GattServer](../apis/gattserver.html): Respond to a GattClient.
- [SecurityManager](../apis/securitymanager.html): Use pairing and optional bonding processes to authenticate and encrypt BLE links.

## NFC

- [MessageBuilder](../apis/nfc-apis.html): Construct NDEF messages, the common data format exchange for NFC messages.
- [MessageParser](../apis/messageparser.html): An event-driven NDEF message parser for a data buffer.
- [NFCController](../apis/nfccontroller.html): Emulate NFC tags that a smartphone can read and generate NDEF messages on demand.
- [NFC EEPROM](../apis/nfc-eeprom.html): Store NDEF messages.
- [SimpleMessageParser](../apis/simplemessageparser.html): Similar to MessageParser, but includes subparsers for well-known NFC types records, such as Text, URI or Mime records, and produces usable objects out of the box.

## LoRaWAN

- [LoRaWANInterface](../apis/lorawan-apis.html): Connect to the internet over a LoRa network.
- [LoRaRadio](../apis/loraradio.html): A pure virtual class that defines APIs for a LoRa radio driver.
