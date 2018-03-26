### IP Networking: WORK-IN-PROGRESS

IP Networking in Mbed OS is layered in three clearly defined API levels. In the diagram below,
the layers are shown next to closest matching [OSI model](https://en.wikipedia.org/wiki/OSI_model) layers.

![ip-networking](ip-networking.png)

Following sections introduce the APIs and technologies implemented in each level.

#### Socket API

Socket API is the common API between all IP connectivity methods. All network stacks in Mbed OS
provide the same Socket API, making applications portable between different connectivity methods
or even stacks.

In OSI model, Socket API relates to layer 4, Transport layer. In Mbed OS Socket API supports
both [TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol) and [UDP](https://en.wikipedia.org/wiki/User_Datagram_Protocol) protocols.

Refer to [TODO:Socket API](networksockets.md) reference for usage instructions.

#### IP Stacks

Mbed OS has three options to select for IP stack. Two build-in IP stack or external IP
stack provided by the connectivity module.

![Network stack](networkstacks.png)

As shown from the diagram above, all stacks implement the same Socket API and
therefore application developer rarely needs to know which stack is going to be used.
Mbed OS chooses one at the build time and usually it is LwIP.

Some external WiFi modules and most cellular modules are in fact external IP stacks from
application point of view. In that case the network driver implements actually the full Network
stack API. These drivers are usually driving the module through AT-command type of interface.
It saves RAM and Flash to use external IP module but depending on its driver and AT-command
interface, it might not properly match the full Socket API.

Following table summarises different stacks, usecases and their limitations.

|Stack|Network protocols supported|Use cases|Limitations|
|-----|---------------------------|---------|-----------|
|LwIP|IPv4, IPv6, PPP|Ethernet, WiFi, 2G/3G/4G Cellular|4 sockets, 1 interface, no routing|
|Nanostack|IPv6, 6LoWPAN, Thread|Mesh networking, Border Router|Only IPv6|
|External IP module|depends on the module|(Save RAM/Flash)|Depends on the module. Usually poor match to Socket API|


#### Network interfaces

Network inteface is the application level API where user chooses the driver, connectivity method
and IP stack. As each connectivity methods differ on how to configure them, these APIs are
noninterchangeable and requires application developer to choose one. Choosing the interface, also
automatically pulls in the network stack as a dependency.

Please note that Interface API is not the same as network driver.
Interface API is the control interface for application. Network driver implements the controlling
API only if it requires configuration from application. From application point of view, there
is no difference, but network driver developer needs to be aware of that.

Mbed OS implements following network interface APIs

* Ethernet
* WiFi
* Cellular (PPP)
* 6LoWPAN-ND mesh networking
* Thread mesh networking.

Refer to [TODO: sockets/interface API reference](TODO) for usage instructions.
