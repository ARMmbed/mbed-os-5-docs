<h2 id="contributing-connectivity">Connectivity</h2>

### The network socket API

#### New device

The NetworkSocketAPI is designed to make porting new devices as easy as possible and only requires a handful of methods for a minimal implementation.

A new device must implement a <a href="https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/NetworkInterface.h" target="_blank">NetworkInterface</a>, with the naming convention of **DeviceInterface** - where **Device** is a unique name that represents the device or network processor.

The **DeviceInterface** should also inherit one of the following (unless it is an abstract device):

- <a href="https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/EthInterface.h" target="_blank">EthInterface</a>.
- <a href="https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/WiFiInterface.h" target="_blank">WiFiInterface</a>.
- <a href="https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/CellularInterface.h" target="_blank">CellularInterface</a>.
- <a href="https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/MeshInterface.h" target="_blank">MeshInterface</a>.

The **NetworkInterface** implementation provides the following methods:

```
    /** Get the internally stored IP address
    /return     IP address of the interface or null if not yet connected
     */
    virtual const char *get_ip_address() = 0;

    /** Get the stack this interface is bound to
    /return     The stack this interface is bound to or null if not yet connected
     */
    virtual NetworkStack * get_stack(void) = 0;

    /** Free NetworkInterface resources
     */
    virtual ~NetworkInterface() {};
```
