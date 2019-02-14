<h2 id="configuration-ble">BLE</h2>

This page describes build-time configurable parameters for BLE. A resource constrained device can limit its functionality to decrease the memory and flash usage of the BLE module. 

To understand what each feature provides please refer to the API docs and the Bluetooth specification.

#### Build time configuration of the BLE feature

To minimise the size of the BLE stack, BLE defines a set of build options.

The configuration is contained in the `mbed_lib.json` configuration file located in `mbed-os/features/FEATURE_BLE/`. By default all the features are enabled.

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

These are feature that can be disabled:
```
|----------------------|------------------------------------|-------------------------------------------|-------------|
| Feature              | Config option name                 | Description                               | Dependency  |
|----------------------|------------------------------------|-------------------------------------------|-------------|
| Observer             | `ble-role-observer`                | Observer role, allows listening for       | None        |
|                                                           | and processing advertising packets         |             |
|----------------------|------------------------------------|-------------------------------------------|-------------|
| Broadcaster          | `ble-role-broadcaster`             | Broadcaster role, allows sending          | None        |
|                                                           | advertising packets.                      |             |
|----------------------|------------------------------------|-------------------------------------------|-------------|
| Central              | `ble-role-central`                 | Central role, initiates connections       | Observer    |
|----------------------|------------------------------------|-------------------------------------------|-------------|
| Peripheral           | `ble-role-peripheral`              | Peripheral role, accepts connections      | Broadcaster |
|----------------------|------------------------------------|-------------------------------------------|-------------|
| GATT Client          | `ble-feature-gatt-client`          | GATT Client support (requests remote      | Peripheral  | 
|                                                           | operations on attributes).                | or Central  |
|----------------------|------------------------------------|-------------------------------------------|-------------|
| GATT Server          | `ble-feature-gatt-server`          | GATT Server support (executes             | Peripheral  |
|                                                           | operations on stored attributes).         | or Central  |
|----------------------|------------------------------------|-------------------------------------------|-------------|
| Security             | `ble-feature-security`             | Security support (keys management).       | Peripheral  |
|                                                           |                                           | or Central  |
|----------------------|------------------------------------|-------------------------------------------|-------------|
| Secure Connections   | `ble-feature-secure-connections`   | Secure Connections support.               | Security    |
|----------------------|------------------------------------|-------------------------------------------|-------------|
| Signing              | `ble-feature-signing`              | Signing support (signed writes).          | Security    |
|----------------------|------------------------------------|-------------------------------------------|-------------|
| Whitelist            | `ble-feature-whitelist`            | whitelist support (peer filtering).       | Security    |
|----------------------|------------------------------------|-------------------------------------------|-------------|
| Privacy              | `ble-feature-privacy`              | Privacy support (random resolvable        | Security    |
|                                                           | addresses).                               |             |
|----------------------|------------------------------------|-------------------------------------------|-------------|
| Phy Management       | `ble-feature-phy-management`       | Additional PHY support (2M and Coded).    | None        |
|----------------------|------------------------------------|-------------------------------------------|-------------|
| Extended Advertising | `ble-feature-extended-advertising` | Extended advertising support (multiple    | Phy         |
|                                                           | advertising sets, secondary channels)     | Management  |
|----------------------|------------------------------------|-------------------------------------------|-------------|
| Periodic Advertising | `ble-feature-periodic-advertising` | Periodic advertising support.             | Extended    |
|                      |                                    |                                           | Advertising |
|----------------------|------------------------------------|-------------------------------------------|-------------|
```                                                                                                          Advertising |