## EMAC memory manager

The Ethernet MAC memory manager class provides abstracted memory interface toward memory modules used in different network stacks. The EMAC device driver uses the memory interface to handle memory related operations, such as allocation, free and data manipulation. The [EMAC](emac.html) drivers use this memory manager to reserve space for network packets.

Memory buffer chains store the data on the memory interface. The data passed in either direction either may be contiguous (a single-buffer chain) or may consist of multiple buffers. You can chain the buffers using a singly linked list.

### Usage

The EMAC driver can allocate memory either from a memory pool or from the heap (contiguous memory). By preference, link input memory should be allocated from the pool, but if contiguous memory is required by the hardware, it can be allocated from the heap.

The driver can express alignment preferences for buffers sent to it, but the network stack is not required to meet these preferences. This means that the drivers relying on alignment need to check the buffer address and may need to copy the output data into an aligned (or contiguous) buffer when its requirements are not met.

On link output to the EMAC driver, buffer chain ownership is given to the driver from network stack. The driver must free the buffer after it is no longer used.

On link input to the network stack, buffer chain ownership is given to the stack from driver. Stack frees the buffer after it no longer uses it.

### EMAC memory manager class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_emac_memory_manager.html)

### Related content

- [EMAC driver](EMAC.html) API
- [Ethernet MAC drivers porting](ethernet-port.html) guide.
