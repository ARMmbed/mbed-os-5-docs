<h2 id="contributing-connectivity">Connectivity</h2>

### The network socket API

#### New device

The NetworkSocketAPI is designed to make porting new devices as easy as possible and only requires a handful of methods for a minimal implementation.

A new device must implement a [NetworkInterface](https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/NetworkInterface.h), with the naming convention of **DeviceInterface** - where **Device** is a unique name that represents the device or network processor.

The **DeviceInterface** should also inherit one of the following (unless it is an abstract device):

* [EthInterface](https://github.com/ARMmbed/mbed-os/blob/master/features/NetworkSocketAPI/EthInterface.h)
* [WiFiInterface](https://github.com/ARMmbed/mbed-os/blob/master/features/NetworkSocketAPI/WiFiInterface.h)
* [CellularInterface](https://github.com/ARMmbed/mbed-os/blob/master/features/NetworkSocketAPI/CellularInterface.h)
* [MeshInterface](https://github.com/ARMmbed/mbed-os/blob/master/features/NetworkSocketAPI/MeshInterface.h)

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
