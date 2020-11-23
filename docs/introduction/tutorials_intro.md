# Tutorials and official examples

This page is an index of all tutorials and official examples.

## API tutorials and official examples

| Topic | Tutorial | Official examples |
| --- | --- | --- |
| Data storage | | - [BlockDevice](https://github.com/ARMmbed/mbed-os-example-blockdevice) <br/> - [FileSystem](https://github.com/ARMmbed/mbed-os-example-filesystem) <br/> - [KVStore](https://github.com/ARMmbed/mbed-os-example-kvstore) <br/> - [SD driver](https://github.com/ARMmbed/mbed-os-example-sd-driver) |
| BLE | | - [Advertising](https://github.com/ARMmbed/mbed-os-example-ble/tree/master/BLE_Advertising) <br/> - [GAP](https://github.com/ARMmbed/mbed-os-example-ble/tree/master/BLE_GAP) <br/> - [Gatt Client - Characteristic Updates](https://github.com/ARMmbed/mbed-os-example-ble/tree/master/BLE_GattClient_CharacteristicUpdates) <br/> - [Gatt Client - Characteristic Write](https://github.com/ARMmbed/mbed-os-example-ble/tree/master/BLE_GattClient_CharacteristicWrite) <br/> - [Gatt Server - Add Service](https://github.com/ARMmbed/mbed-os-example-ble/tree/master/BLE_GattServer_AddService) <br/> - [Gatt Server - Characteristic Updates](https://github.com/ARMmbed/mbed-os-example-ble/tree/master/BLE_GattServer_CharacteristicUpdates) <br/> - [Gatt Server - Characteristic Write](https://github.com/ARMmbed/mbed-os-example-ble/tree/master/BLE_GattServer_CharacteristicWrite) <br/> - [Periodic advertising](https://github.com/ARMmbed/mbed-os-example-ble/tree/master/BLE_PeriodicAdvertising) <br/> - [Security & Privacy](https://github.com/ARMmbed/mbed-os-example-ble/tree/master/BLE_SecurityAndPrivacy) |
| Drivers | [Alarm](../apis/drivers-tutorials.html) | |
| Network interfaces | - [Mesh tutorial](../apis/connectivity-tutorials.html) <br/> - [LoRaWAN usage](../apis/lorawan-usage.html) <br/> - [Building a private loRa network](../apis/LoRa-tutorial.html) <br/> - [Nanostack border router](https://github.com/ARMmbed/nanostack-border-router) | - [Cellular](https://github.com/ARMmbed/mbed-os-example-cellular) <br/> - [LoRaWAN](https://github.com/ARMmbed/mbed-os-example-lorawan) <br/> - [Mesh minimal](https://github.com/ARMmbed/mbed-os-example-mesh-minimal) (also available in the [light control tutorial](../apis/light-control.html)) <br/> - [Wi-Fi ](https://github.com/ARMmbed/mbed-os-example-wifi) |
| Network socket | | - [Sockets](https://github.com/ARMmbed/mbed-os-example-sockets) <br/> - [Socket statistics](https://github.com/ARMmbed/mbed-os-example-socket-stats) |
| NFC | | - [Smart Poster](https://github.com/ARMmbed/mbed-os-example-nfc/blob/master/NFC_SmartPoster/README.md) <br/> - [EEPROM](https://github.com/ARMmbed/mbed-os-example-nfc/blob/master/NFC_EEPROM/README.md)|
| Network secure socket | | [TLS socket](https://github.com/ARMmbed/mbed-os-example-tls-socket) |
| Platform | - [Application flow control](../apis/platform-tutorials.html) <br/> - [Power optimization](../apis/power-optimization.html) | - [Thread statistics](https://github.com/ARMmbed/mbed-os-example-thread-statistics) <br/> - [CPU statistics](https://github.com/ARMmbed/mbed-os-example-cpu-stats) <br/> - [Error handling](https://github.com/ARMmbed/mbed-os-example-error-handling) <br/> - [System information](https://github.com/ARMmbed/mbed-os-example-sys-info) <br/> - [Link time optimization](../apis/link-time-optimization.html) |
| Scheduling | [EventQueue](../apis/scheduling-tutorials.html) | |
| Security | [Secure communication](../apis/tls-tutorial.html) | - [ATECC608A secure element](https://github.com/ARMmbed/mbed-os-example-atecc608a) <br/> - [DeviceKey](https://github.com/ARMmbed/mbed-os-example-devicekey) <br/> - [Mbed Crypto](https://github.com/ARMmbed/mbed-os-example-mbed-crypto) <br/> - [Mbed TLS: Authenticated encryption](https://github.com/ARMmbed/mbed-os-example-tls/blob/master/authcrypt) <br/> - [Mbed TLS: Benchmark](https://github.com/ARMmbed/mbed-os-example-tls/blob/master/benchmark) <br/> - [Mbed TLS: Hashing](https://github.com/ARMmbed/mbed-os-example-tls/blob/master/hashing) <br/> - [Mbed TLS: TLS client](https://github.com/ARMmbed/mbed-os-example-tls/blob/master/tls-client) <br/> - [PSA](https://github.com/ARMmbed/mbed-os-example-psa/) <br> - [PSA attestation](https://github.com/ARMmbed/mbed-os-example-attestation) |
| USB | [Audio player](../apis/usb-wav-audio-player.html) | |

## Serial communication

These tutorials teach you to communicate with your development board, an essential part of programming and debugging:

- [Windows serial driver tutorial](../program-setup/windows-serial-driver.html) (Windows 7 only)
- [Board to PC communication over USB tutorial](../program-setup/serial-communication.html)

## Debugging

These tutorials show you how to install, export a project to and start a debugging session with different IDEs.

### Methods

- [BBC micro:bit, pyOCD and GDB debugging tutorial](../debug-test/debug-microbit.html).
- [Troubleshooting common issues](../debug-test/troubleshooting-common-issues.html).
- [Analyzing Mbed OS crash dump tutorial](../debug-test/analyzing-mbed-os-crash-dump.html) and [crash reporting official example](https://github.com/ARMmbed/mbed-os-example-crash-reporting)
- [Compile time errors tutorial](../debug-test/compile-time-errors.html).
- [Debugging using `printf` statements](../debug-test/debugging-using-printf-statements.html).

### Debugging with third party tools

- [Eclipse](../debug-test/third-party-tools.html).
- [Keil uVision](../debug-test/keil-uvision.html).
- [Visual Studio](../debug-test/visual-studio-code.html).

## Testing

- [Test your applications or Mbed OS with Greentea](../debug-test/greentea-for-testing-applications.html).

## Bootloader

- [A tutorial for creating and using a bootloader](../program-setup/creating-and-using-a-bootloader.html).
- [An official example of bootloader implementation](https://github.com/ARMmbed/mbed-os-example-bootloader).

## Connecting to the cloud

- [Pelion Device Management](https://github.com/ARMmbed/mbed-os-example-pelion)
- [Mbed OS example for AWS IoT SDK](https://github.com/ARMmbed/mbed-os-example-for-aws)
- [Mbed OS example for Azure IoT Hub](https://github.com/ARMmbed/mbed-os-example-for-azure)
- [Mbed OS example for Google IoT Cloud](https://github.com/ARMmbed/mbed-os-example-for-google-iot-cloud)

## Migrating

If you are moving from Mbed OS 5 to Mbed OS 6, please see [the list of deprecated APIs](../apis/index.html#deprecated-apis).

If you are moving from Mbed 2 to Mbed OS 6 bare metal, [please see the bare metal documentation](../bare-metal/index.html).
