## EMAC memory manager

The Ethernet MAC memory manager class provides abstracted memory interface toward memory modules used in different network stacks. The EMAC device driver uses the memory interface to handle memory related operations, such as allocation, free and data manipulation.

Memory buffer chains store the data on the memory interface. The data passed in either direction either may be contiguous (a single-buffer chain) or may consist of multiple buffers. You can chain the buffers using a singly linked list.

### Usage

On link output to EMAC driver, buffer chain ownership is given to the driver. Driver must free the buffer after it is no longer used. The driver can express alignment preferences for buffers sent to it, but the network stack is not required to meet these preferences. This means that the drivers relying on alignment, may need to copy the output data into an aligned (or contiguous) buffers.

EMAC driver can allocate memory either from a memory pool or from the heap (contiguous memory). By preference, link input memory should be allocated from the pool, but if contiguous memory is required it can be allocated from the heap. 

On link input to the network stack, buffer chain ownership is given to the stack. Stack frees the buffer after it no longer uses it.

### EMAC memory manager class reference

TBD:

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_emacmemorymanager.html)

### EMAC memory manager example

TBD:

Add link to example in teams repo here.

### Related content

TBD:

- [EMAC](/docs/development/reference/contributing/connectivity/EMAC.html)
