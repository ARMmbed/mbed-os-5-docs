## GattServer

A GattServer is a collection of GattServices. These services contain characteristics that a peer connected to the device may read or write. These characteristics may also emit updates to subscribed clients when their values change.

#### Server layout

Application code can add a GattService object to the server with the help of the function `addService()`. That function registers all the GattCharacteristics enclosed in the service, as well as all the characteristic descriptors (see GattAttribute) that these characteristics contain. Service registration assigns a unique handle to the various attributes that are part of the service. The user must use this handle to read or write these components.

There are no defined primitives that remove a single service; however, a call to the function `reset()` removes all services previously registered in the GattServer.

#### Characteristic and attributes access

You must access values of the characteristic and the characteristic descriptor present in the GattServer through the handle assigned to them when you registered the service. The GattServer class offers several types of `read()` and `write()` functions that retrieve or mutate an attribute value.

You can query the server by invoking the function `areUpdatesEnabled()` to find out if a client has subscribed to a given characteristic's value update.

#### Events

You can register several event handlers with the GattServer that it will call to notify you of client (remote application connected to the server) and server activities:

- `onDataSent`: Register an event handler with the GattServer that it will call to notify you when it sends a characteristic value update to a client.
- `onDataWriten`: Register an event handler with the GattServer that it will call to notify you when a client has written an attribute of the server.
- `onDataRead`: Register an event handler with the GattServer that it will call to notify you when a client has read an attribute of the server.
- `onUpdatesEnabled`: Register an event handler with the GattServer that it will call to notify you when a client subscribes to updates for a characteristic.
- `onUpdatesDisabled`: Register an event handler with the GattServer that it will call to notify you when a client unsubscribes from updates for a characteristic.
- `onConfimationReceived`: Register an event handler with the GattServer that it will call to notify you when a client acknowledges a characteristic value notification.

The term characteristic value update represents Characteristic Value Notification and Characteristic Value Indication when the nature of the server initiated is not relevant.

### GattServer class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.9/mbed-os-api-doxy/class_gatt_server.html)

### GattServer example

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-GattServer/)](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-GattServer/file/8fbed496a023/main.cpp)
