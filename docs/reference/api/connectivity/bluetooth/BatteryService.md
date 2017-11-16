## BatteryService

It is often a requirement for devices operating on battery to report the battery charge level to the user.

The <a href="https://www.bluetooth.org/docman/handlers/downloaddoc.ashx?doc_id=245138" target="_blank">Bluetooth Battery Service</a> defines how a battery charge level should be exposed through a BLE link. It allows clients - usually smartphone application - of a device to read the current battery charge level and follow its evolution.

The BatteryService class implements the Bluetooth Battery Service as defined by the Bluetooth body. Makers of BLE devices operating on Battery can use it to expose interoperably the charge level of their products.

### BatteryService class reference

[![View code](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_battery_service.html)

### BatteryService example

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-BatteryLevel/)](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-BatteryLevel/file/5d8484f69181/source/main.cpp/)

### Related content

- [Bluetooth Battery Service](https://www.bluetooth.org/docman/handlers/downloaddoc.ashx?doc_id=245138) specification.