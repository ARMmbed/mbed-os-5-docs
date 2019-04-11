<h1 id="mesh-tech">6LoWPAN-ND</h1>

This guide provides design guidelines for developing an application on top of the 6LoWPAN-ND mesh solution. The APIs and technologies are not discussed in detail here.

## Overview of the 6LoWPAN-ND network

![Node connected to server](https://github.com/ARMmbed/mbed-os-5-docs/blob/development/docs/images/node_to_server_2.jpg?raw=true)

Typically, the 6LoWPAN network consists of one border router on multiple low-powered nodes. The nodes are connected to a cloud service for feeding in the sensor or control data.

### Different device types in a 6LoWPAN network

In a 6LoWPAN network, devices can have different roles. The colors in the illustrations represent different device types and are used in the examples throughout this tutorial.

#### Border router (6LBR)

![Border router](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/br.png)

A border router is the coordinator of the 6LoWPAN network. It handles the translations between the 6LoWPAN and IPv6 networks. Arm does not provide translation to IPv4 network due the limited address space. We recommend using IPv6 tunnels over IPv4 network when operating in such environment.

The border router also authenticates the nodes joining the network and keeps track of the routing topology.

#### 6LoWPAN router (6LR)

![6LoWPAN router](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/6lr.png)

A 6LoWPAN router is a node that can route packets. This role is required to form a topological or mesh network. This configuration does not allow nodes to sleep because they route packets to their siblings.

#### 6LoWPAN host (6LH)

![6LoWPAN Host](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/6lh.png)

A 6LoWPAN host is a type of node that does not route any packets. It has only one parent routing the packets.

#### 6LoWPAN sleepy host

A 6LoWPAN sleepy host is a 6LoWPAN host that is periodically allowed to sleep and turn off its radio.

### Different types of mesh networks

6LoWPAN-based mesh networks cannot be described as a uniform standardized network type, such as Wi-Fi. Depending on the business requirements and use cases the network may have different setups and requirements.

#### Star network

![Start topology](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/star_topology.png)

Star topology is the simplest form of a mesh network. Actually, it is not mesh at all. Every node connects directly to the border router.

In a star network, nodes can be very low-power devices with least amount of RAM because they have no routing responsibilities. It also allows sleeping nodes.

#### Mesh/tree network

![Tree type mesh](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/mesh.png)

In a mesh/tree network, all nodes are configured as 6LoWPAN routers.

In a 6LoWPAN network, RPL protocol is used for forming the routing topology. Every node selects a primary parent for routing so the result looks like a tree.

This network type allows to cover large areas because each node extends the range of the network. However, the packet is retransmitted on every hop, which means that the transfer capacity of the network decreases as the size of the network increases.
