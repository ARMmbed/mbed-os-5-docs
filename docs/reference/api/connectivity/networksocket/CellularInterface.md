<h2 id="cellular-api">Cellular</h2>

<span class="images">![](https://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_cellular_base.png)<span>CellularBase class hierarchy</span></span>

The CellularBase provides a C++ API for connecting to the internet over a Cellular device.

Arm Mbed OS provides a [reference implementation of CellularBase](https://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/_easy_cellular_connection_8h_source.html), which has more information.

#### Cellular

The [CellularBase](https://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/_cellular_base_8h_source.html) provides a C++ API for connecting to the internet over a Cellular device.

Arm Mbed OS provides a [reference implementation of CellularBase](https://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/_easy_cellular_connection_8h_source.html).

##### Getting started

1. Choose an [Mbed board that supports cellular](https://os.mbed.com/platforms/?mbed-enabled=15&connectivity=1), such as the [UBLOX-C027](https://os.mbed.com/platforms/u-blox-C027/) or [MTS-DRAGONFLY](https://os.mbed.com/platforms/MTS-Dragonfly/).

1. Clone [`mbed-os-example-cellular`](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-cellular/). Follow the instructions in the repository.

    1. Compile the code.
    1. Flash the board.

   You see output similar to the excerpt below:

```
mbed-os-example-cellular
Establishing connection ......

Connection Established.
TCP: connected with echo.mbedcloudtesting.com server
TCP: Sent 4 Bytes to echo.mbedcloudtesting.com
Received from echo server 4 Bytes


Success. Exiting
```

##### Basic working principles

You can use and extend a cellular interface in various different ways. For example,

- Using AT commands to control sockets in an existing IP stack built into the cellular modem.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/Cell_AT.png)</span>

- Using a PPP (Point-to-Point Protocol) pipe to pass IP packets between an Mbed OS supported IP stack and cellular modem device.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/Cell_PPP.png)</span>

[`mbed-os-example-cellular`](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-cellular/) uses [an easy cellular connection](https://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/_easy_cellular_connection_8h_source.html). It depends on the modem whether the application uses PPP or AT mode. We can summarize this particular design as follows:

- It uses an external IP stack, such as LWIP, or on-chip network stacks such as when the modem does not support PPP.
- The easy cellular connection uses standard 3GPP AT 27.007 AT commands to set up the cellular modem and to register to the network.
- After registration, the driver opens a PPP pipe using LWIP with the cellular modem and connects to the internet. If AT only mode is in use, then modem-specific AT commands are used for socket data control.

### CellularBase class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_cellular_base.html)

### Usage

To bring up the network interface:

1. Instantiate an implementation of the CellularBase class.
1. Call the `connect(pincode, apn)` function with a PIN code for your SIM card and an APN for your network.
1. Once connected, you can use Mbed OS [network sockets](/docs/development/reference/network-socket.html) as usual.

### Cellular example: connection establishment

This example establishes connection with the cellular network using Mbed OS CellularInterface.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-cellular/)](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-cellular/file/0f644d6045cf/main.cpp)

### Related content

- [Network socket](/docs/development/reference/network-socket.html) API reference overview.
