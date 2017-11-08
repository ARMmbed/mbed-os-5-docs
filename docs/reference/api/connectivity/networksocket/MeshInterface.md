## Mesh

The Arm Mbed mesh API allows the application to use the IPv6 mesh network topologies through the <a href="/docs/v5.6/tutorials/mesh.html#nanostack" target="_blank">nanostack</a> networking stack.

**Tips:**
* The mesh API supports 6LoWPAN-ND (neighbor discovery) and Thread bootstrap modes.
* The applications do not use this module directly. The applications use `LoWPANNDInterface`, `ThreadInterface` or `NanostackEthernetInterface` directly.
* When using an Ethernet interface, there are no configuration options available. It is using the dynamic mode to learn the IPv6 prefix from the network.

### Mesh class reference

**LoWPANNDInterface**

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_lo_w_p_a_n_n_d_interface.html)

**ThreadInterface**

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_thread_interface.html)

**NanostackEthernetInterface**

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_nanostack_ethernet_interface.html)

### Usage

1. Create a network interface and driver objects.
1. Initialize the interface with given PHY driver.
1. Connect to network.

### Mesh example

The application below demonstrates a simple light control application, where devices can control the LED status of all devices in the network. You can build the application for the unsecure 6LoWPAN-ND or Thread network.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-mesh-minimal)](https://github.com/ARMmbed/mbed-os-example-mesh-minimal/blob/master/main.cpp)

### Related content

- <a href="/docs/v5.6/tutorials/mesh.html#nanostack" target="_blank">Nanostack</a> tutorial.
