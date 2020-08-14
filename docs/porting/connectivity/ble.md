# Bluetooth Low Energy (BLE)

Mbed OS uses the Cordio stack for its BLE host. We recommend porting the Cordio platform<!--is that what they call it?--> to your board, or porting at the HCI level<!--what's the distinction between porting the platform and porting the HCI level? If one is ported to the board, where is the other ported to? The chip? What's the difference between porting to a whole board v porting to a chip?--> as described in the HCI documentation.
<!--we need a decision from Andy about the Cordio docs before we start linking. Ours are 18 months old!-->

## Replacing the Cordio stack

You can replace the Cordio stack by porting a complete alternative stack. You must do this at the API level<!--as opposed to which level?--> by:

1. Disabling the Cordio compilation.
1. Implementing all the user interfaces (Gap, GattServer, GattClient, SecurityManager).
1. Providing a BLEInstaceBase that `createBLEInstance()` returns.

### Disabling Cordio

All the source files for Cordio are part of a library and are currently required by the BLE feature. Remove this requirement so that none of the Cordio implementations are compiled, otherwise they will conflict with your implementation.

### Implementing the user interface APIs and BLEInstanceBase

There are four user API files in`include/ble/`:

- Gap.h
- GattClient.h
- GattServer.h
- SecurityManager.h

And `BLEInstanceBase` is in `ble/internal/BLEInstanceBase.h`.

Each API contains a class in a namespace `ble::interface`. Your implementation must inherit from this class and have the same class name, but be directly in the `ble` interface. Your implementation classes must implement all interface functions.

Place your `include`<!--adding the bunny ears just helps parse the sentence--> files in a path ending with `ble/internal/`, and add the suffix `Impl`: `GapImpl.h`, `GattClientImpl.h`, `GattServerImpl.h`, `SecurityManagerImpl.h`, `BLEInstanceBaseImpl.h`.

### Providing BLEInstanceBase

The global function `createBLEInstance()` must provide your implementation of `BLEInstanceBase`.

`BLEInstanceBase` must instantiate all the user interfaces and provide BLE event handling (see the BLEInstanceBase documentation for details<!--where is that?-->). `BLEInstanceBase` can also instantiate the PAL interfaces provided in `ble/internal`, depending on your implementation. They<!--who is they?--> may be used as the user interfaces, but are not required for user API level porting.
