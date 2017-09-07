#### Arm Mbed Mesh

Mbed Mesh API allows the application to use the IPv6 mesh network topologies through the [nanostack](docs/tutorials/mesh/02_N_arch.md) netoworking stack.

**Tips:**
* Currently, 6LoWPAN-ND (neighbour discovery) and Thread bootstrap modes are supported.
* This module should not be used directly by the applications. The applications should use the `LoWPANNDInterface`, `ThreadInterface` or `NanostackEthernetInterface` directly.
* When using an Ethernet interface, there are no configuration options available. It is using the dynamic mode to learn the IPv6 prefix from the network. No static configuration is supported.

##### API

**LoWPANNDInterface**

[![View code](https://www.mbed.com/embed/?type=library)](https://github.com/ARMmbed/mbed-os/blob/master/features/nanostack/FEATURE_NANOSTACK/mbed-mesh-api/mbed-mesh-api/LoWPANNDInterface.h)

**ThreadInterface**

[![View code](https://www.mbed.com/embed/?type=library)](https://github.com/ARMmbed/mbed-os/blob/master/features/nanostack/FEATURE_NANOSTACK/mbed-mesh-api/mbed-mesh-api/ThreadInterface.h)

**NanostackEthernetInterface**

[![View code](https://www.mbed.com/embed/?type=library)](https://github.com/ARMmbed/mbed-os/blob/master/features/nanostack/FEATURE_NANOSTACK/mbed-mesh-api/mbed-mesh-api/NanostackEthernetInterface.h)

##### Usage

1. Create a network interface and driver objects.
1. Initialize the interface with given PHY driver.
1. Connect to network.

##### Example

The application below demonstrates a simple light control application, where devices can control the LED status of all devices in the network. The application can be built for the unsecure 6LoWPAN-ND or Thread network.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-mesh-minimal)](https://github.com/ARMmbed/mbed-os-example-mesh-minimal/blob/master/main.cpp)
