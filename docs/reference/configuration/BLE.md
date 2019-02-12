<h2 id="configuration-ble">BLE</h2>

This page describes build-time configurable parameters for BLE. A resource constrained device can limit its functionality to decrease the memory and flash usage of the BLE module. 

To understand what each feature provides please refer to the API docs and the Bluetooth specification.

#### Build time configuration of the BLE feature

To minimise the size of the BLE stack, BLE defines a set of build options.

The configuration is contained in the `mbed_lib.json` configuration file. By default all the features are enabled.

Turning off individual features will remove the code and any memory allocations required by that feature. Some features depend on each other - see the comments in the configuration file. These dependencies will be enforced during compile time.

Trying to use a feature which has been disabled will result in a compile time error or an error reporting the feature as unimplemented at runtime.

#### Changing the configuration

An excerpt from the configuration file:

```
{
    "name": "ble",
    "config": {
        "ble-role-observer": {
            "help": "Include observer BLE role support, allows listening for and processing advertising packets.",
            "value": true,
            "macro_name": "BLE_ROLE_OBSERVER"
        },
    ...
```

By changing `"value": true,` to `false` you can disable each feature.

##### Configurable features

These are feature that can be deselected.

- observer (scanning)
- broadcaster (advertising)
- peripheral (a connectable broadcaster)
- central (an observer that can connect)
- gatt client
- gatt server
- security (link encryption, key management)
- secure connections
- signing
- whitelist (filtering based on a list of known devices)
- privacy (resolving random addresses based on keys)
- phy management (2M and Coded PHYs)
- extended advertising
- periodic advertising