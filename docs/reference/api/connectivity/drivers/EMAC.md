## EMAC

The Ethernet MAC device driver class provides an interface for a network stack to control the Etherner driver.

### Default driver

If your EMAC driver is the default for the target, you should provide implementation of the `EMAC::get_default_instance()`

```
static EMAC EMAC::get_default_instance() {
    static MyEMACdriver driver_instance;
    return driver_instance;
}
```

### Usage

The EMAC driver class is instantiated during the creation of the network interface. When the network interface is brought up, the network stack powers the EMAC driver.

Steps that the network stack uses to power the EMAC driver:

1. The network stack configures the EMAC memory manager class reference for the driver.
1. The network stack sets the link input and state callbacks.
1. The network stack calls the driver's power up function.
1. The network stack reads the MTU and hardware MAC address sizes from the driver.
1. The network stack queries the hardware MAC address from the driver. The driver is allowed to respond a failure.
1. The hardware MAC address is written to the driver from the network stack.
    1. If the driver does not provide an address on the read call, the network stack chooses the address from the central system configuration and writes that to driver.

**Optional steps:**

1. The network stack might query the interface name from the driver.
1. The network stack might configure multicast filtering.
    1. The driver can either support multicast filtering or provide all frames.
1. The network stack might query for the memory buffer align preference from the driver.
    1. The network stack is not required to use the alignment for the memory buffers on link out.

### EMAC class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_emac.html)

### Related content

- [EMAC memory manager](emac-memory-manager.html)
- [Ethernet MAC drivers porting](ethernet-port.html) guide.
