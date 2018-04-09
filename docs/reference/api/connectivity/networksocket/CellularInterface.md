<h2 id="cellular-api">Cellular</h2>

<span class="images">![](https://os.mbed.com/docs/v5.8/mbed-os-api-doxy/class_cellular_base.png)<span>CellularBase class hierarchy</span></span>

The CellularBase provides a C++ API for connecting to the internet over a Cellular device.

Arm Mbed OS provides a [reference implementation of CellularBase](https://os.mbed.com/docs/v5.8/mbed-os-api-doxy/_easy_cellular_connection_8h_source.html), which has more information.

### CellularBase class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.8/mbed-os-api-doxy/class_cellular_base.html)

### Usage

To bring up the network interface:

1. Instantiate an implementation of the CellularBase class.
1. Call the `connect(pincode, apn)` function with a PIN code for your SIM card and an APN for your network.
1. Once connected, you can use Mbed OS [network sockets](/docs/v5.8/reference/network-socket.html) as usual.

### Cellular example: connection establishment

This example establishes connection with the cellular network using Mbed OS CellularInterface.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-cellular/)](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-cellular/file/0f644d6045cf/main.cpp)

### Related content

- [Network socket](/docs/v5.8/reference/network-socket.html) API reference overview.
