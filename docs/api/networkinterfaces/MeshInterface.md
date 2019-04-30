<h1 id="mesh-api">Mesh</h1>

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/class_mesh_interface.png)<span>MeshInterface class hierarchy</span></span>

The Arm Mbed Mesh API allows the application to use the IPv6 mesh network topologies through the [Nanostack](../reference/nanostack-introduction-tech.html) networking stack. 

Mbed OS provides three types of IPv6 based mesh networks:

- [Wi-SUN](../reference/wisun-tech.html), following the specification from Wi-SUN alliance.
- [Thread](../reference/thread-tech.html), following the specification from Thread Group.
- [6LoWPAN-ND](../reference/6LoWPAN-ND-tech.html), loosely following the Zigbee-IP specification.

The application can use the `LoWPANNDInterface`, `WisunInterface` or `ThreadInterface` object for connecting to the mesh network. When successfully connected, the application can use the Mbed [C++ socket APIs](network-socket.html) to create a socket to start communication with a remote peer. [Network status API](network-status.html) can be used for monitoring changes in the network status.

You can configure the mesh interface by providing values in `mbed_app.json`, as the [mesh configuration](../reference/configuration-mesh.html) section documents.

## Mesh class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/class_mesh_interface.html)

## Related content

 - [mesh tutorial](../tutorial/mesh-tutorial.html) for introduction to Mesh technology.
- [Thread](../reference/thread-tech.html) technology reference material.
- [Wi-SUN](../reference/wisun-tech.html) technology reference material.
- [6LowPAN-ND](../reference/6LoWPAN-ND-tech.html) technology reference material.
- [Mesh configuration](../reference/configuration-mesh.html) for configuring mesh.
- [Light control tutorial](../tutorials/light-control.html) for example light control application, where devices can control the LED status of all devices in the network.
 - [mbed-os-example-mesh-minimal](https://github.com/ARMmbed/mbed-os-example-mesh-minimal) example application using Mesh.
- [Nanostack](../reference/nanostack-introduction-tech.html) for information on the mesh stack internals.
