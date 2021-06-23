# BLE

<span class="notes">**Note:** Some functions, variables or types have been deprecated. Please see the class reference linked below for details.</span>

Bluetooth low energy (BLE) is a low power wireless technology standard for building personal area networks. Typical applications of BLE are health care, fitness trackers, beacons, smart home, security, entertainment, proximity sensors, industrial and automotive.

Arm Mbed BLE, also called `BLE_API`, is the Bluetooth Low Energy software solution for Mbed. Many Mbed [targets and components](https://os.mbed.com/platforms/?mbed-enabled=15&connectivity=3) support Mbed BLE. Developers can use it to create new BLE enabled applications.

Mbed’s `BLE_API` interfaces with the BLE controller on the board. It hides the BLE stack’s complexity behind C++ abstractions and is compatible with all BLE-enabled Mbed board. The Mbed OS `BLE_API` automatically configuring the clocks, timers and other hardware peripherals to work at their lowest power consumption.

## `BLE_API`, bridges and stacks

<span class="images">![](../../../images/BLEDiagram.png)</span>

You can build a BLE application using Mbed OS, `BLE_API` and a controller-specific Bluetooth stack together with some bridge software to adapt it to `BLE_API`:

- `BLE_API` as described above.
- The bridge software is specific to each vendor’s board. It provides the instantiations for the interfaces `BLE_API` offers and helps drive the underlying controller and Bluetooth stack.
- The Bluetooth stack implements the Bluetooth protocol and is specific to the controller, so a vendor using different controllers may provide different stacks.

## Inside `BLE_API`

<span class="images">![](../../../images/Inside_API.png)</span>

`BLE_API` offers building blocks to help construct applications. These fall into two broad categories:

1. Interfaces under **`ble/`** to express BLE constructs, such as GAP, GATT, services and characteristics.

1. Classes under `ble/services` to offer reference implementations for many of the commonly used GATT profiles. The code under 'services/' isn't essential, but it’s a useful starting point for prototyping. We continue to implement the standard GATT profiles.

## The BLEDevice class and header

The entry point of Mbed's `BLE_API` is the BLE class accessible using the header `ble/BLE.h`. This class allows you to obtain a BLE object that includes the basic attributes of a spec-compatible BLE device and can work with any BLE radio:

```c TODO
#include "ble/BLE.h"

BLE& mydevicename = BLE::Instance();
```

The class's member functions can be divided by purpose:

1. Basic BLE operations, such as initializing the controller.

1. Accessor to Bluetooth Modules that manage GAP, GATT or the security.

## Usage

1. Set up advertising and connection modes.
1. Assign UUIDs to the service and its characteristic.
1. Create an input characteristic.
1. Construct a service class and add it to the BLE stack.
1. Push notifications when the characteristic's value changes.

## Tracing

To debug issues (or to understand what the stack is doing) it may be helpful to enable tracing.

Traces can be turned on by overriding configuration options in you mbed_app.json:

```
    "target_overrides": {
        "*": {
            "mbed-trace.enable": true,
            "mbed-trace.max-level": "TRACE_LEVEL_DEBUG",
            "cordio.trace-hci-packets": true,
            "cordio.trace-cordio-wsf-traces": true,
            "ble.trace-human-readable-enums": true
        }
    }
```

and compiling your application with `--profile debug`. Please note that with all options enabled your application may become too big - disable some options or lower the `mbed-trace.max-level`. Detailed documentation is available in the tracing [README.md](https://github.com/ARMmbed/mbed-os/blob/master/platform/mbed-trace/README.md).

All BLE modules contain tracing, each of the modules prefixed with a unique tag:
- `BLE ` - general BLE traces  
- `BLGP` - GAP
- `BLGS` - GATT Server
- `BLGC` - GATT Client
- `BLSM` - Security Manager
- `BLDB` - Security Database
- `BLHC` - HCI
- `BLCO` - Cordio stack
- `BLDM` - GAP pal
- `BLAT` - ATT client

Any contributions to BLE should include appropriate tracing code.

## BLE class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.12/mbed-os-api-doxy/classble_1_1_b_l_e.html)

## Related content

- Mbed Enabled [targets and components](https://os.mbed.com/platforms/?mbed-enabled=15&connectivity=3) that support BLE.
- [BLE example on GitHub](https://github.com/ARMmbed/mbed-os-example-ble/).
