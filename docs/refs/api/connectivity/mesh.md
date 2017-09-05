#### Arm Mbed Mesh

Mbed Mesh API allows the application to use the IPv6 mesh network topologies through the [nanostack](docs/tutorials/mesh/02_N_arch.md) netowrking stack.

Note: Currently, 6LoWPAN-ND (neighbour discovery) and Thread bootstrap modes are supported.

##### Usage

1. Create a network interface and driver objects:
1. Initialize the interface with given PHY driver.
1. Connect to network:

Note: This module should not be used directly by the applications. The applications should use the `LoWPANNDInterface`, `ThreadInterface` or `NanostackEthernetInterface` directly.

Note: When using an Ethernet interface, there are no configuration options available. It is using the dynamic mode to learn the IPv6 prefix from the network. No static configuration is supported.

##### Example: 6LoWPAN ND mode

```
// Create a network interface and driver objects:
LoWPANNDInterface mesh;
NanostackRfPhyNcs36510 rf_phy;

int main() {
    // Initialize the interface with given PHY driver.
    mesh.initialize(&rf_phy);
    
    // Connect to network:
    if (mesh.connect()) {
        printf("Connection failed!\r\n");
        return -1;
    }
    
    printf("connected. IP = %s\r\n", mesh.get_ip_address());
}
```

##### Usage example for 6LoWPAN Thread mode

Basically, the same as for ND, but the network interface uses a different class:

```
// Create a network interface and driver objects:
ThreadInterface mesh;
NanostackRfPhyNcs36510 rf_phy;

int main() {
    // Initialize the interface with given PHY driver.
    mesh.initialize(&rf_phy);
    
    // Connect to network:
    if (mesh.connect()) {
        printf("Connection failed!\r\n");
        return -1;
    }
    
    printf("connected. IP = %s\r\n", mesh.get_ip_address());
}
```

##### Usage example with Ethernet

The API is still the same, you just need to provide a driver that implements the `NanostackEthernetPhy` API:

```
// Create a network interface and driver objects:
NanostackEthernetInterface eth;
NanostackEthernetPhyK64F phy;

int main() {
    // Initialize the interface with given PHY driver.
    eth.initialize(&phy);

    // Connect to network:
    if (eth.connect()) {
        printf("Connection failed!\r\n");
        return -1;
    }

    printf("connected. IP = %s\r\n", eth.get_ip_address());
}
```
