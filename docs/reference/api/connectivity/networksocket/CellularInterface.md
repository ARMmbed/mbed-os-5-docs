<h2 id="cellular-api">Cellular</h2>

The CellularBase provides a C++ API for connecting to the internet over a Cellular device.

Arm Mbed OS provides a [reference implementation of CellularBase](https://github.com/ARMmbed/mbed-os/tree/master/features/netsocket/cellular/generic_modem_driver), which has more information.

### CellularBase class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_cellular_base.html)

### Usage

To bring up the network interface:

1. Instantiate an implementation of the CellularBase class.
1. Call the `connect(pincode, apn)` function with a PIN code for your SIM card and an APN for your network.
1. Once connected, you can use Mbed OS [network sockets](/docs/development/reference/network-socket.html) as usual.

### Cellular example: connection establishment

This example establishes connection with the cellular network using Mbed OS CellularInterface.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/cellular-example/)](https://os.mbed.com/teams/mbed_example/code/cellular-example/file/fb873be06e31/main.cpp)

### Related content

- [Network socket](/docs/development/reference/network-socket.html) API reference overview.
