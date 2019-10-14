# BatteryService

It is often a requirement for devices operating on battery to report the battery charge level to the user.

The [Bluetooth Battery Service](https://www.bluetooth.org/docman/handlers/downloaddoc.ashx?doc_id=245138) defines how to expose a battery charge level through a BLE link. It allows a client - usually a smartphone application - of a device to read the current battery charge level and follow its evolution.

The BatteryService class implements the Bluetooth Battery Service as defined by the Bluetooth SIG. Makers of BLE devices operating on battery can use the API to expose interoperably the charge level of their products.

## BatteryService class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_battery_service.html)

## BatteryService example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-ble/blob/master/BLE_BatteryLevel/source)](https://github.com/ARMmbed/mbed-os-example-ble/blob/mbed-os-5.14/BLE_BatteryLevel/source/main.cpp)

## Related content

- [Bluetooth Battery Service](https://www.bluetooth.org/docman/handlers/downloaddoc.ashx?doc_id=245138) specification.
