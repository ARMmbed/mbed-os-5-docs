# HeartRateService

People practicing physical activities use heart rate monitors to track their pulse in real time and improve their physical performances.

The [Bluetooth Heart Rate Service](https://www.bluetooth.org/docman/handlers/downloaddoc.ashx?doc_id=239866) defines how data from a heart rate sensor should be exposed through a BLE link. The standard nature of the service allows seamless operations between collectors - usually smartphone applications - and heart rate monitors conforming to the service.

The HeartRateService class implements the Bluetooth Heart Rate service as defined by the Bluetooth body. Makers of BLE enabled fitness devices can use it to expose interoperably heart rate sensor data.

<span class="note"> **Note:** The Bluetooth Heart Rate Service is part of the [Bluetooth Heart Rate Profile](https://www.bluetooth.org/docman/handlers/downloaddoc.ashx?doc_id=239865), which defines behaviors that a Bluetooth heart rate sensor expects. You must ensure that your application conforms to the heart rate profile to guarantee interoperability of your heart rate sensors.</span>

## HeartRateService class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_heart_rate_service.html)

## HeartRateService example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-ble/blob/master/BLE_HeartRate/source)](https://github.com/ARMmbed/mbed-os-example-ble/blob/mbed-os-5.14/BLE_HeartRate/source/main.cpp)

## Related content

- [Bluetooth Heart Rate Service](https://www.bluetooth.org/docman/handlers/downloaddoc.ashx?doc_id=239866) specification.
- [Bluetooth Heart Rate Profile](https://www.bluetooth.org/docman/handlers/downloaddoc.ashx?doc_id=239865) specification.
