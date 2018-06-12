## Network interface overview

A socket requires a NetworkInterface instance when opened to indicate which NetworkInterface the socket should be created on. The NetworkInterface provides a network stack that implements the underlying socket operations.

Network interface is also the controlling API for application to specify network configuration.

Existing network interfaces:

- [Ethernet](/docs/v5.9/reference/ethernet.html): API for connecting to the internet over an Ethernet connection.
- [Wi-Fi](/docs/v5.9/reference/wi-fi.html): API for connecting to the internet with a Wi-Fi device.
- [Cellular](/docs/v5.9/reference/cellular-api.html): API for connecting to the internet using a cellular device.
- [Mesh networking interface](/docs/v5.9/reference/mesh-api.html): Mbed OS provides two kinds of IPv6-based mesh networks - 6LoWPAN_ND and Thread.

Optional functionality:

- [Network status](network-status.html): API for monitoring network status changes.
