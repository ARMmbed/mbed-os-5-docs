## EMAC

The Ethernet MAC device driver class provides an interface for a network stack to control the Etherner driver. 

### Default driver

If your EMAC driver is the default for the target, define the static get default instance function to return an instance of your EMAC.

### Usage

The EMAC driver class is instantiated during the creation of the network interface. When the network interface is brought up, the network stack powers the EMAC driver.

Steps that the network stack uses to power the EMAC driver:

1. The EMAC memory manager class reference is configured to the driver. 
1. The link input and state callbacks are set.
1. The driver powers up.
1. MTU and hardware address sizes are read from the driver.
1. Hardware address is read from the driver.
1. Hardware address is written to driver.
    1. If the driver does not provide address on the read call, the network stack chooses the address from the central system configuration and writes that to driver.

Optional steps:

1. Interface name is read from the driver.
1. Multicast filtering is configured.
    1. The driver can either support multicast filtering or provide all frames.
1. The memory buffer align preference is read from the driver.
    1. The network stack may or may not use the alignment for the memory buffers on link out.

### EMAC class reference

TBD:

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_emac.html)

### EMAC example

TBD: Add example here from teams repo.

### Related content

TBD:

- [EMAC memory manager](/docs/development/reference/contributing/connectivity/EMACMemoryManager.html)
