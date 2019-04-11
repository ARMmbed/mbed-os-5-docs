<h1 id="mesh-api">Mesh</h1>

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/class_mesh_interface.png)<span>MeshInterface class hierarchy</span></span>

The Arm Mbed Mesh API allows the application to use the IPv6 mesh network topologies through the Nanostack networking stack.

Mbed OS provides three types of IPv6 based mesh networks:

- 6LoWPAN_ND, loosely following the Zigbee-IP specification.
- Wi-SUN, following the specification from Wi-SUN alliance.
- Thread, following the specification from Thread Group.

Nanostack is the networking stack that provides these protocols. For more information on the stack internals, please refer to the [Thread](../reference/thread-tech.html), [Wi-SUN](../reference/wisun-tech.html) and [6LowPAN](../reference/mesh-tech.html) sections. Application developers use Nanostack through the Mbed Mesh API.

The application can use the `LoWPANNDInterface`, `WisunInterface` or `ThreadInterface` object for connecting to the mesh network. When successfully connected, the application can use the Mbed [C++ socket APIs](network-socket.html) to create a socket to start communication with a remote peer.

You can configure the mesh interface by providing values in `mbed_app.json`, as the [mesh configuration](../reference/configuration-mesh.html) section documents.

## Usage

1. Create a network interface and driver objects.
1. Initialize the interface with given PHY driver.
1. Connect to network.

## Supported mesh networking modes

Currently, 6LoWPAN-ND (neighbor discovery), Wi-SUN FAN and Thread bootstrap modes are supported.

## Network connection states

After the initialization, the network state is `MESH_DISCONNECTED`. After a successful connection, the state changes to `MESH_CONNECTED` and when disconnected from the network the state is changed back to `MESH_DISCONNECTED`.

In case of connection errors, the state is changed to some of the connection error states. In an error state, there is no need to make a `disconnect` request and the application is allowed to attempt connecting again.

## Getting started

See the example application [mbed-os-example-mesh-minimal](https://github.com/ARMmbed/mbed-os-example-mesh-minimal) for usage.

## Mesh class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/class_mesh_interface.html)

## Mesh example

To learn how to use mesh, please see our [light control tutorial](../tutorials/light-control.html), which demonstrates a light control application, where devices can control the LED status of all devices in the network. You can build the application for the unsecure 6LoWPAN-ND, Wi-SUN or Thread network.

## Related content

- [Thread](../reference/thread-tech.html) technology reference material.
- [Wi-SUN](../reference/wisun-tech.html) technology reference material.
- [6LowPAN](../reference/mesh-tech.html) technology reference material.
- [6LoWPAN, Wi-SUN and Thread Mesh configuration documentation](../reference/configuration-mesh.html).
- [Light control tutorial](../tutorials/light-control.html).
