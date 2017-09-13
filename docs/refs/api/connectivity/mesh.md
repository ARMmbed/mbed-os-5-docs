#### Mesh

The Arm Mbed mesh API allows the application to use the IPv6 mesh network topologies through the [nanostack](https://os.mbed.com/docs/v5.4/reference/mesh-1.html) networking stack.

**Tips:**
* The mesh API supports 6LoWPAN-ND (neighbor discovery) and Thread bootstrap modes.
* The applications do not use this module directly. The applications use `LoWPANNDInterface`, `ThreadInterface` or `NanostackEthernetInterface` directly.
* When using an Ethernet interface, there are no configuration options available. It is using the dynamic mode to learn the IPv6 prefix from the network.

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

The application below demonstrates a simple light control application, where devices can control the LED status of all devices in the network. You can build the application for the unsecure 6LoWPAN-ND or Thread network.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-mesh-minimal)](https://github.com/ARMmbed/mbed-os-example-mesh-minimal/blob/master/main.cpp)
