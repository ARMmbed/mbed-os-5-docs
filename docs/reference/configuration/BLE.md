<h1 id="configuration-ble">BLE</h1>

This page describes build-time configurable parameters for BLE. A resource constrained device can limit its functionality to decrease the memory and flash use of the BLE module. 

To understand what each feature provides, please refer to the API docs and the Bluetooth specification.

### Build time configuration of the BLE feature

To minimize the size of the BLE stack, BLE defines a set of build options.

The configuration is contained in the `mbed_lib.json` configuration file located in `mbed-os/features/FEATURE_BLE/`. By default, all the features are enabled.

Turning off individual features removes the code and any memory allocations required by that feature. Some features depend on one another - please see the comments in the configuration file for details. These dependencies are enforced during compile time.

Trying to use a disabled feature results in a compile time error or an error reporting the feature as unimplemented at run time.

### Changing the configuration

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

By changing `"value": true,` to `false`, you can disable each feature.

#### Configurable features

These are feature that you can disable:

```
Configuration parameters
------------------------

Name: ble.ble-role-observer
    Description: Include observer BLE role support (scanning for and processing advertising packets).
    Defined by: library:ble
    Value: true
    Macro name: BLE_ROLE_OBSERVER
    
Name: ble.ble-role-broadcaster
    Description: Include broadcaster BLE role support (sending advertising packets).
    Defined by: library:ble
    Value: true
    Macro name: BLE_ROLE_BROADCASTER

Name: ble.ble-role-central
    Description: Include central BLE role support (initiates connections), depends on observer role.
    Defined by: library:ble
    Value: true
    Macro name: BLE_ROLE_CENTRAL

Name: ble.ble-role-peripheral
    Description: Include peripheral BLE role support (accepts connections), depends on broadcaster role.
    Defined by: library:ble
    Value: true
    Macro name: BLE_ROLE_PERIPHERAL

Name: ble.ble-feature-gatt-client
    Description: Include Gatt Client BLE role support (requests remote operations on attributes), depends on peripheral and central role.
    Defined by: library:ble
    Value: true
    Macro name: BLE_FEATURE_GATT_CLIENT

Name: ble.ble-feature-gatt-server
    Description: Include Gatt Server BLE role support (executes operations on stored attributes), depends on peripheral or central role.
    Defined by: library:ble
    Value: true
    Macro name: BLE_FEATURE_GATT_SERVER

Name: ble.ble-feature-security
    Description: Include security support (key management), depends on peripheral or central role.
    Defined by: library:ble
    Value: true
    Macro name: BLE_FEATURE_SECURITY

Name: ble.ble-feature-secure-connections
    Description: Include secure connections support, depends on the security feature.
    Defined by: library:ble
    Value: true
    Macro name: BLE_FEATURE_SECURE_CONNECTIONS

Name: ble.ble-feature-signing
    Description: Include signing support (signed attribute writes), depends on the security feature.
    Defined by: library:ble
    Value: true
    Macro name: BLE_FEATURE_SIGNING

Name: ble.ble-feature-whitelist
    Description: Include whitelist support (peer filtering), depends on the security feature.
    Defined by: library:ble
    Value: true
    Macro name: BLE_FEATURE_WHITELIST

Name: ble.ble-feature-privacy
    Description: Include privacy support(random resolvable addresses), depends on the security feature.
    Defined by: library:ble
    Value: true
    Macro name: BLE_FEATURE_PRIVACY

Name: ble.ble-feature-phy-management
    Description: Additional PHY support (2M and Coded)
    Defined by: library:ble
    Value: true
    Macro name: BLE_FEATURE_PHY_MANAGEMENT

Name: ble.ble-feature-extended-advertising
    Description: Include extended advertising support(advertising sets, secondary channels), depends on the phy management feature.
    Defined by: library:ble
    Value: true
    Macro name: BLE_FEATURE_EXTENDED_ADVERTISING

Name: ble.ble-feature-periodic-advertising
    Description: Include periodic advertising support, depends on the extended advertising feature.
    Defined by: library:ble
    Value: true
    Macro name: BLE_FEATURE_PERIODIC_ADVERTISING
        
```
