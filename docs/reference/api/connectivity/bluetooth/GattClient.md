## GattClient

GattClient defines procedures required for interacting with a remote GattServer.

#### Discovery procedures

A GattServer hosts a fixed set of services. These services are a logical composition of characteristics that may be discovered, read, or written, and can broadcast their state to a connected client. These characteristics may also contain metainformation and named characteristic descriptors. A characteristic descriptor may indicate the unit used for a characteristic value, describe the characteristic purpose in a textual form or allow a client to register for update notifications for the characteristic value.

Prior to any interaction with server characteristic, a GattClient discovers the layout of the services and characteristics present on the server.

The layout of the descriptors of a characteristic may also be issued to as an extra discovery step.

#### Attribute manipulation

As a result of the discovery process, the client can start interacting with the characteristic discovered. Depending on the characteristic properties (acquired during discovery), a client can read or write the value of a given characteristic.

Mbed BLE abstracts most read and write operations to offer a single API that can be used to read or write characteristics values. Application code does not have to handle the fragmentation/reassembly process necessary if the attribute value to transported cannot fit in a single data packet.

#### Server Initiated events

If a characteristic has to notify or indicate a property set; then, a client may register to a notification or indication from the characteristic. When the server updates the characteristic value, the server can forward the new value to the registered clients. The notification/indication mechanism prevents polling from the client and therefore minimise the transactions involved between a client and a server.

Registration is made by writing the Client Characteristic Configuration Descriptor, which is present in the characteristic if the notify or indicate properties are set. The client discovers that descriptor if it intends to register to server initiated events.

### GattClient class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_gatt_client.html)

### GattClient example

[Add example here.]
