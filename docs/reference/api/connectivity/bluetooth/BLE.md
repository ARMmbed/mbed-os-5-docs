## BLE

Bluetooth low energy (BLE) is a low power wireless technology standard for building personal area networks. Typical applications of BLE are health care, fitness trackers, beacons, smart home, security, entertainment, proximity sensors, industrial and automotive.

Arm Mbed BLE, also called `BLE_API`, is the Bluetooth Low Energy software solution for Mbed. Many Mbed <a href="https://os.mbed.com/platforms/?mbed-enabled=15&connectivity=3" target="_blank">targets and components</a> support Mbed BLE. Developers can use it to create new BLE enabled applications.

### BLE class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os-doc-builder.test.mbed.com/docs/v5.7/mbed-os-api-doxy/namespaceble.html)

### Usage

1. Set up advertising and connection modes.
1. Assign UUIDs to the service and its characteristic.
1. Create an input characteristic.
1. Construct a service class and add it to the BLE stack.
1. Push notifications when the characteristic's value changes.

### Example: BLE beacon

Here is an example demonstrating how you can create a BLE beacon.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-Beacon/)](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-Beacon/file/abc2d39dfdde/source/main.cpp)

### Example: BLE Heart Rate Monitor

Here is an example demonstrating how to build a heart rate sensor that can be connected and monitored by a BLE client such as your phone.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-HeartRate/)](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-HeartRate/file/b36aa157781d/source/main.cpp)

### Related content

- Mbed Enabled <a href="https://os.mbed.com/platforms/?mbed-enabled=15&connectivity=3" target="_blank">targets and components</a> that support BLE.
