<h1 id="wisun-tech">Wi-SUN</h1>

The Wi-SUN Field Area Network (FAN) is based on open standards from IEEE802, IETF, ANSI/TIA and ETSI.

Wi-SUN FAN operates on license-exempt sub-GHz RF band and uses frequency hopping to lower interference. Therefore, Wi-SUN is well suited for outdoor installations and dense urban neighborhoods.

The Mbed OS Wi-SUN stack is built on IPv6 over Low power Wireless Personal Area Networks (6LoWPAN), which itself builds on IEEE 802.15.4 to offer IP-based networking. Internet Protocol (IP) provides the core mechanism for relaying datagrams across IP networks, and its routing capabilities enable internetworking.

You can find more details about Wi-SUN at the [Wi-SUN Alliance site](https://www.wi-sun.org).

## Mbed Wi-SUN API

Mbed OS provides the [Mesh C++ API](../apis/mesh-api.html) for building Wi-SUN applications.

- To connect to the Wi-SUN network, use the [Wi-SUN interface API](https://github.com/ARMmbed/mbed-os/blob/master/features/nanostack/mbed-mesh-api/mbed-mesh-api/WisunInterface.h).
- For the socket communication over the Wi-SUN network, use the [Mbed sockets API](../apis/network-socket.html).

### Nanostack Wi-SUN API

Mbed Wi-SUN is implemented in the Nanostack library that provides a set of C API headers with more functionalities. The [nanostack folder](https://github.com/ARMmbed/mbed-os/tree/master/features/nanostack/sal-stack-nanostack/nanostack) has the following header files that can be used with Wi-SUN:

- `net_interface.h` for initializing, starting and stopping a Wi-SUN interface.
- `ws_management_api.h` for configuring device behavior.
- `ws_bbr_api.h` for Wi-SUN backbone border router application interface.

## Mbed Wi-SUN examples

Mbed Wi-SUN network consists of routers and border router(s). Mbed OS provides example applications to build Wi-SUN application.

### Router

You can find an example using the [Mesh C++ API](../apis/mesh-api.html) for building a Wi-SUN router device in the [mesh minimal example](https://github.com/ARMmbed/mbed-os-example-mesh-minimal).

### Border router

You can find an example using the [Nanostack API](https://github.com/ARMmbed/mbed-os/tree/master/features/nanostack/sal-stack-nanostack/nanostack) to build a Wi-SUN border router at [nanostack border router](https://github.com/ARMmbed/nanostack-border-router).
