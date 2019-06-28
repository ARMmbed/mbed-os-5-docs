# GattClient

GattClient defines procedures required for interacting with a remote GattServer.

### Discovery procedures

A GattServer hosts a fixed set of services. These services are a logical composition of characteristics that may be discovered, read or written and can broadcast their state to a connected client. These characteristics may also contain metainformation and named characteristic descriptors. A characteristic descriptor may indicate the unit used for a characteristic value, describe the characteristic purpose in a textual form or allow a client to register for update notifications for the characteristic value.

Prior to any interaction with a server characteristic, a GattClient discovers the layout of the services and characteristics present on the server.

The layout of the descriptors of a characteristic may also be issued as an extra discovery step.

### Attribute manipulation

As a result of the discovery process, the client can start interacting with the characteristic discovered. Depending on the characteristic properties (acquired during discovery), a client can read or write the value of a given characteristic.

Mbed BLE abstracts read and write operations to offer a single API that can be used to read or write characteristic values. The application code does not have to handle the necessary fragmentation or reassembly process if the attribute value to be transported can't fit in a single data packet.

### Server initiated events

When a server updates a characteristic value, it can forward the new value to any registered clients. Clients may register for these updates on a per-characteristic basis. The server sends the updates by using notifications (no confirmation from client) or indications (client confirms receipt). This mechanism minimizes the number of transactions between a client and a server by avoiding polling.

Clients register for these updates by setting the Client Characteristic Configuration Descriptor (CCCD) value. This is an attribute, and the client needs to discover its descriptor. It is present in the characteristic if its notify or indicate properties are set.

## GattClient class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.11/mbed-os-api-doxy/class_gatt_client.html)

## GattClient example

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-GattClient/)](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-GattClient/file/71d7cec222eb/main.cpp)
