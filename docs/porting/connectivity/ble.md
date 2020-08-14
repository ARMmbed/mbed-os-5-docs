# Bluetooth Low Energy (BLE)

Mbed OS uses the Cordio stack for its BLE host. We recommend porting either the full Cordio stack, or the Host Controller Interface (HCI), as explained in the Cordio documentation. If you want to port your own BLE stack to replace the Cordio stack, follow the instructions on this page. 

<!--we need a decision from Andy about the Cordio docs before we start linking. Ours are 18 months old!-->

## Replacing the Cordio stack

You can replace the Cordio stack by porting a complete alternative stack. You must port the full API by:

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

`BLEInstanceBase` must instantiate all the user interfaces and provide BLE event handling (see the [BLEInstanceBase documentation for details](../mbed-os-api-doxy/_b_l_e_instance_base_8h_source.html)). `BLEInstanceBase` can also instantiate the PAL interfaces provided in `ble/internal`, depending on your implementation. You can use the PAL classes by inheriting from the interface classes (like the user interfaces above), but they are not required for user API level porting.
