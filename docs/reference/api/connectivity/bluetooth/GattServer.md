## GattServer

A GattServer is a collection of GattServices; these services contain characteristics that a peer connected to the device may read or write. These characteristics may also emit updates to subscribed clients when their values change.

#### Server Layout

Application code can add a GattService object to the server with the help of the function `addService()`. That function registers all the GattCharacteristic enclosed in the service, as well as all the characteristics descriptors (see GattAttribute) these characteristics contain. Service registration assigns a unique handle to the various attributes being part of the service; this handle should be used for subsequent read or write of these components.

There are no primitives defined to remove a single service; however, a call to the function `reset()` removes all services previously registered in the GattServer.

#### Characteristic and attributes access

Values of the characteristic and the characteristic descriptor present in the GattServer must be accessed through the handle assigned to them when the service has been registered; the GattServer class offers several flavours of `read()` and `write()` functions that retrieve or mutate an attribute value.

Application code can query if a client has subscribed to a given characteristic's value update by invoking the function `areUpdatesEnabled()`.

#### Events

The GattServer allows application code to register several event handlers that can be used to monitor client and server activities:
- `onDataSent`: Register an event handler that is called when a characteristic value update has been sent to a client.
- `onDataWriten`: Register an event handler that is called when a client has written an attribute of the server.
- `onDataRead`: Register an event handler that is called when a client has read an attribute of the server.
- `onUpdatesEnabled`: Register an event handler that is called when a client subscribes to updates of a characteristic.
- `onUpdatesDisabled`: Register an event handler that is called when a client unsubscribes from updates of a characteristic.
- `onConfimationReceived`: Register an event handler that is called when a client acknowledges a characteristic value notification.

The term characteristic value update is used to represent Characteristic Value Notification and Characteristic Value Indication when the nature of the server initiated is not relevant.

### GattServer class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_gatt_server.html)

### GattServer example

[Add example here.]
