<h2 id="mesh-api">6LoWPAN Mesh Interfaces</h2>

<span class="images">![](https://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_mesh_interface.png)<span>MeshInterface class hierarchy</span></span>

The Arm Mbed Mesh API allows the application to use the IPv6 mesh network topologies through the [Nanostack](/docs/v5.7/tutorials/mesh.html#nanostack) networking stack.

Mbed OS provides two types of IPv6 based mesh networks:

- 6LoWPAN_ND, loosely following the Zigbee-IP specification.
- Thread, following the specification from Thread Group.

Nanostack is the networking stack that provides both of these protocols. For more information on the stack internals, please refer to the [6LoWPAN mesh technology](mesh-tech.html) section. Application developers use Nanostack through the Mbed Mesh API.

The application can use the `LoWPANNDInterface` or `ThreadInterface` object for connecting to the mesh network. When successfully connected, the application can use the Mbed C++ socket APIs to create a socket to start communication with a remote peer.

You can configure the mesh interface by providing values in `mbed_app.json`, as the [mesh configuration](mesh-configuration.html) section documents.

### Usage

1. Create a network interface and driver objects.
1. Initialize the interface with given PHY driver.
1. Connect to network.

### Supported mesh networking modes

Currently, 6LoWPAN-ND (neighbor discovery) and Thread bootstrap modes are supported.


### Network connection states

After the initialization, the network state is `MESH_DISCONNECTED`. After a successful connection, the state changes to `MESH_CONNECTED` and when disconnected from the network the state is changed back to `MESH_DISCONNECTED`.

In case of connection errors, the state is changed to some of the connection error states. In an error state, there is no need to make a `disconnect` request and the application is allowed to attempt connecting again.

### Getting started

See the example application [mbed-os-example-mesh-minimal](https://github.com/ARMmbed/mbed-os-example-mesh-minimal) for usage.


### Mesh class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_mesh_interface.html)


### Mesh example

The application below demonstrates a simple light control application, where devices can control the LED status of all devices in the network. You can build the application for the unsecure 6LoWPAN-ND or Thread network.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-mesh-minimal/)](https://github.com/ARMmbed/mbed-os-example-mesh-minimal/blob/master/main.cpp)

### Related content

- [Nanostack](/docs/development/reference/technology.html#nanostack) technology reference material.
