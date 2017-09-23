<h2 id="cellular-api">Cellular</h2>

The [CellularBase](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.6/api/classCellularBase.html) provides a C++ API for connecting to the internet over a Cellular device.

Arm Mbed OS provides a reference implementation of CellularBase, which you can find [here](https://github.com/ARMmbed/mbed-os/tree/master/features/netsocket/cellular/generic_modem_driver).

### Cellular class reference

[![View code](https://www.mbed.com/embed/?type=library)](/docs/v5.4/mbed-os-api-doxy/class_cellular_base.html)

### Usage

To bring up the network interface:

1. Instantiate an implementation of the CellularBase class (for example, the [generic modem driver](https://github.com/hasnainvirk/mbed-os/blob/cellular_feature_br/features/cellular/TARGET_GENERIC_MODEM/generic_modem_driver/)).
1. Call the `connect(pincode, apn)` function with a PIN code for your SIM card and an APN for your network.
1. Once connected, you can use Mbed OS [network sockets](/docs/v5.4/reference/api-references.html#network-sockets) as usual.

### Cellular example: Connection establishment

This example establishes connection with the cellular network using Mbed OS CellularInterface.

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/cellular-example/)](https://developer.mbed.org/teams/mbed_example/code/cellular-example/file/fb873be06e31/main.cpp)
