### Connectivity

The main connectivity APIs in Arm Mbed OS are:

* [Network sockets](network_sockets.md): provide a common interface for using sockets on network devices.
* [Ethernet](ethernet.md): API for connecting to the internet over an Ethernet connection.
* [Wi-Fi](wifi.md): API for connecting to the internet with a Wi-Fi device.
* [Mesh networking](mesh.md): Mbed OS provides two kinds of IPv6-based mesh networks - 6LoWPAN_ND and Thread.
* [Bluetooth Low Energy (BLE)](ble.md): designed for small, energy-efficient BLE applications.
* [Cellular](cellular.md): API for connecting to the internet using a cellular device.


#### Cellular

The [CellularBase](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classCellularBase.html) provides a C++ API for connecting to the internet over a Cellular device.

Arm Mbed OS provides a reference implementation of CellularBase, which you can find [here](https://github.com/ARMmbed/mbed-os/tree/master/features/netsocket/cellular/generic_modem_driver).

##### Getting started

1. Choose an [Mbed board that supports cellular](https://developer.mbed.org/platforms/?mbed-enabled=15&connectivity=1), such as the [UBLOX-C027](https://developer.mbed.org/platforms/u-blox-C027/) or [MTS-DRAGONFLY](https://developer.mbed.org/platforms/MTS-Dragonfly/).

1. Clone [`mbed-os-example-cellular`](https://github.com/ARMmbed/mbed-os-example-cellular). Follow the instructions in the repository.

    1. Compile the code.
    1. Flash the board.

   You see output similar to the excerpt below:

```

mbed-os-example-cellular, Connecting...


Connection Established.
UDP: Sent 4 Bytes to echo.u-blox.com
Received from echo server 4 Bytes


Success. Exiting

```

##### Basic working principles

You can use and extend a cellular interface in various different ways. For example,

- Using AT commands to control sockets in an existing IP stack built into the cellular modem.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/Cell_AT.png)</span>

- Using a PPP (Point-to-Point Protocol) pipe to pass IP packets between an Mbed OS supported IP stack and cellular modem device.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/Cell_PPP.png)</span>

[`mbed-os-example-cellular`](https://github.com/ARMmbed/mbed-os-example-cellular) uses [a generic modem driver](https://github.com/ARMmbed/mbed-os/tree/master/features/netsocket/cellular/generic_modem_driver). In other words, CellularInterface uses PPP. We can summarize this particular design as follows:

* It uses an external IP stack (for example, LWIP) instead of on-chip network stacks.
* The generic modem driver uses standard 3GPP AT 27.007 AT commands to set up the cellular modem and registers to the network.
* After registration, the driver opens up a PPP (Point-to-Point Protocol) pipe using LWIP with the cellular modem and connects to the internet.

