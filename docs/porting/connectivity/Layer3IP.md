<h1 id="l3-porting">IP Layer3 (L3IP) drivers</h1>

![L3IP API](https://raw.githubusercontent.com/ARMmbed/mbed-os-5-docs/development/docs/images/l3ip.png)

This document describes how to port and test a cellular IP Layer3 (L3IP) driver to Mbed OS.

The scope of this document is limited to advanced cellular modems, where the device presents an additional IP Layer3 interface to send and receive frames, and one of the onboard network stacks that runs on Mbed OS on the host processor uses this.

If the device has an off-board network stack, a driver needs to implement [NetworkStack](../porting/networkstack.html) directly instead of passing network calls to the offboard stack.
 
## Abstractions

![L3IP driver](https://raw.githubusercontent.com/ARMmbed/mbed-os-5-docs/development/docs/images/l3ip-driver.png)

The L3IP interface abstracts network stacks and drivers and easily permits multiple instances. The key API classes are:

- `NetworkInterface` - an Mbed OS network interface of any type.
- `NetworkStack` - an Mbed OS network stack of any type (may be off-board).
- `OnboardNetworkStack` - an onboard network stack.
- `L3IP` - an IP Layer3 cellular device driver.
- `NetStackMemoryManager` - a memory manager used to pass data between driver and stack.
- `L3IPInterface`- a `NetworkInterface` that uses an `L3IP` driver and an `OnboardNetworkStack`.

## L3IP driver core

The first step in the port is to create a driver class for the cellular device that you can instantiate to control your device. You must derive this class from the `L3IP` class. A network stack (or test framework) uses this API to control your driver.

Class L3IP is entirely abstract - you need to implement about a dozen calls to activate the driver, send and receive packets and perform other control and information functions.

There are also callback registration functions for upcalls from the driver - the stack can register callback functions for packet reception and link status changes.

### Initialization steps

The L3IP driver class is instantiated during the creation of the network interface. When the network interface is brought up, the network stack powers the L3IP driver.

Steps that the network stack uses to power the L3IP driver:

1. The network stack configures the IP Layer3 memory manager class reference for the driver.
1. The network stack sets the link input and state callbacks.
1. The network stack calls the driver's power up function.
1. The network stack reads the MTU size from the driver.

**Optional steps:**

1. The network stack might query the interface name from the driver.
1. The network stack might configure multicast filtering.
   1. The driver can either support multicast filtering or provide all frames.
1. The network stack might query for the memory buffer align preference from the driver.
   1. The network stack is not required to use the alignment for the memory buffers on link out.

## The IP Layer3 memory manager

The IP Layer3 memory manager class provides an abstracted memory interface toward memory modules used in different network stacks. For the send and receive paths, data is transferred in memory buffers controlled through a `NetStackMemoryManager` object. The network stack provides the L3IP driver with reference to the memory manager before the L3IP device powers up.

Memory buffer chains store the data on the memory interface. The data passed in either direction either may be contiguous (a single-buffer chain) or may consist of multiple buffers. You can chain the buffers using a singly linked list.

On the output call, the L3IP driver is given ownership of a buffer chain - it must free the chain when it has finished with the data. The data may or may not be contiguous. A driver can express alignment preferences for outgoing data, but the network stack is not required to meet these preferences, so a driver relying on alignment may need a slow path that copies data into an aligned (or contiguous) buffer.

For reception, the L3IP driver must allocate memory from the `NetStackMemoryManager` to store the received packets - this is then passed to the link input callback, which frees it. By preference, you should allocate this memory using the pool, but if contiguous memory is necessary, you can allocate it from the heap.

## IP Layer3 interface

All Mbed OS connectivity devices should provide an Mbed OS `NetworkInterface` implementation.

To create and use an IP Layer3 interface, you need the `L3IPInterface` and `L3IP` classes. Moreover, you need an L3IP derived driver class for the specific target device. Otherwise, the linker error `undefined reference to L3IP::get_default_instance()` stops the build process.

The user application code can create IP Layer3:

```
   	NetworkInterface *l3interface;
   	l3interface =new L3IPInterface(L3IP::get_default_instance(), OnboardNetworkStack::get_default_instance());
   	l3interface->connect();
```

This attaches the default network stack (usually LWIP - the other alternative is Nanostack) to the specified L3IP driver and provides all the `NetworkInterface` and `NetworkStack` APIs.
 
Below is an example of a target device driver class that needs to be implemented:

```
	class Cellular_driver_L3IP : public L3IP {... }

	Cellular_driver_L3IP &Cellular_driver_L3IP::get_instance()
	{
    	static Cellular_driver_L3IP l3ip_test_driver;
    	return l3ip_test_driver;
	}

	// Weak so a module can override
	MBED_WEAK L3IP &L3IP::get_default_instance()
	{
    	return Cellular_driver_L3IP::get_instance();
	}
```

You can find this driver class example in the `mbed-os/TESTS/network/l3ip` directory.

## Being the default interface 

In Mbed OS, targets may provide default network interfaces through an automated factory method. You can do this with the following call:

	NetworkInterface::get_default_instance()

This way, you can create an ethernet, Wi-Fi, mesh or cellular interface. The interface type depends on the `NETWORK_DEFAULT_INTERFACE_TYPE` value in the JSON configuration. Any interface you create this way is set as the default.
 
IP Layer3 Interface doesn't use `NetworkInterface::get_default_instance`, so it is not set as the default when you create it.
 
To set IP Layer3 as the default interface, you can use a new member of `set_as_default()`. This method is not limited to IP Layer3 and can set any network interface as default.

## Cellular interfaces

As a cellular interface, a little more work is necessary - at a minimum, you need to implement the extra configuration calls in `L3IPInterface`. This is because the network stacks and IP Layer3 APIs only relate to the basic data path - they have no knowledge of any other configuration mechanisms and assume they are already set up.

To do this, create a C++ class that inherits from both `L3IPInterface` and a base class for the new IP Layer3 cellular interface solution. The `L3IPInterface` is a helper class that implements all the core `NetworkInterface` functionality for you. You then need to implement the extra configuration methods.
 
You don't usually directly expose the `L3IP` driver class of a cellular  driver because it is not usually declared as `L3IP::get_default_instance`, but you would pass it to the constructor of your base `L3IPInterface`. This then makes it visible using the `getl3ip` method, which provides access to the L3IP device driver instance. The `getl3ip` method is a member of the `L3IPInterface` class.

## OnboardNetworkStack

You do not have to memorize the precise details of the `OnboardNetworkStack` API. It provides the mechanism to bind a driver to a stack and the APIs needed to implement a `NetworkInterface`, but `L3IPInterface` handles this.
 
## Tuning memory allocations

Depending on a driver's use of pool and heap memory and other factors, you might want to tune the configuration of particular network stack. You can do this using the `mbed_lib.json` of each network stack, using the `target_overrides` section.
 
## Testing

The Mbed OS tree contains Greentea-based tests that exercise the L3IP API directly, along with more general socket tests.

For Greentea information, please see the [Greentea](../tools/greentea-testing-applications.html) documentation.

Greentea L3IP tests are in the Mbed OS tree under the `TESTS/network/L3IP` directory.

The driver should also be tested with both network stacks available in Mbed OS because they use the driver somewhat differently. Do this with the JSON option `nsapi.default-stack` set to `LWIP` and `NANOSTACK`.

Please see the [Network Socket test plan](https://github.com/ARMmbed/mbed-os/blob/master/TESTS/netsocket/README.md) for instructions on how to run Mbed OS socket tests.
