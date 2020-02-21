# Examples and Videos

## Blinky

- [Blinky](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-blinky/): our basic application, showing how to use the APIs to control the LED on the board.

## End to end projects

- [LoRa on Arm Mbed](https://docs.mbed.com/docs/lora-with-mbed/en/latest/)
- [Internet connected lighting system](https://docs.mbed.com/docs/building-an-internet-connected-lighting-system/en/latest/)

## Our YouTube channel

[https://www.youtube.com/armmbed/](https://www.youtube.com/armmbed/)

## BBC micro:bit

A few micro:bit How To videos:

- [Hello world](https://www.youtube.com/watch?v=Jctpi6aqrHQ)
- [Accelerometer](https://www.youtube.com/watch?v=_WGKBxSW_AE)
- [Proximity heart](https://www.youtube.com/watch?v=xKWQSjg6rX4)

## JavaScript on Arm Mbed OS 5

- [Building IoT devices with JavaScript](https://os.mbed.com/javascript-on-mbed/)
- [Blinky in JavaScript](https://github.com/ARMmbed/mbed-js-example)
- [Bluetooth Low Energy in JavaScript](https://github.com/ARMmbed/mbed-js-ble-example)
- [JavaScript REPL](https://github.com/janjongboom/mbed-js-repl-example)

## Component examples

### Security

#### Arm Mbed TLS

- [Cryptographic benchmark](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-tls-benchmark/): benchmarks the various cryptographic primitives offered by Arm Mbed TLS.
- [Authenticated encryption and decryption](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-tls-authcrypt/): performs authenticated encryption and authenticated decryption of a buffer. It serves as a tutorial for the basic authenticated encryption functions of Mbed TLS.
- [Hashing](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-tls-hashing/): performs hashing of a buffer with SHA-256 using various APIs. It serves as a tutorial for the basic hashing APIs of Mbed TLS.
- [TLS client](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-tls-tls-client/): downloads a file from an HTTPS server (os.mbed.com) and looks for a specific string in that file.

### Core features

#### File system

[Get the FAT file system working on an Mbed OS platform](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-fat-filesystem/).

#### Bootloader

- [Create a bootloader](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-bootloader/).
- [Use a blinky application with a prebuilt bootloader](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-bootloader-blinky/).

### mbed Client

[Getting started](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-client/): a basic example of mbed Client for Mbed OS. It demonstrates how to register a device with Mbed Device Connector, how to read and write values and how to deregister.

## Connectivity

- [HTTP](http://github.com/armmbed/mbed-os-example-http) and [HTTPS](https://github.com/ARMmbed/mbed-os-example-tls/blob/master/tls-client/main.cpp).
- [MQTT](https://os.mbed.com/teams/mqtt/code/HelloMQTT/).
- [CoAP](https://github.com/armmbed/mbed-os-example-coap).

### mesh

[Join a device to an insecure 6LoWPAN-ND or Thread network](https://os.mbed.com/teams/mbed-os-examples/code/nanostack-border-router). This is the simplest use of the mesh networking stack.

### Nanostack border router

[Use the generic Mbed border router and create a 6LoWPAN-ND or Thread network](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-mesh-minimal/). Your 6LoWPAN or Thread devices can access to internet using this gateway.

### Sockets

[Perform a transaction over TCP using the network-socket API](https://github.com/ARMmbed/mbed-os-example-sockets).

### Wi-Fi

[Perform simple HTTP operations using the Wi-Fi interface](https://github.com/ARMmbed/mbed-os-example-wifi).

### Bluetooth Low Energy (BLE)

- [Battery level](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-BatteryLevel/): use the Battery Level service to transmit a device's battery level.

- [BLE button](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-Button/): BLE service template for a read-only characteristic.

- [GAP button](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-GAPButton/): use GAP to transmit a value to a peer that's listening for advertisements.

- [Heart rate](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-HeartRate/): transmit a heart rate value using the SIG Heart Rate profile.

- [Thermometer](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-Thermometer/): send thermometer information using the Health Thermometer Profile.

- [Simple LED control](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-LED/): a client using a read/write characteristic to control an LED. This example goes with the [LED blinker](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-LEDBlinker/), a server that uses the GATT client API to control the BLE client device.

- Beacons send a small amount of information to a nearby device. Try:
    - [BLE beacon](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-Beacon/).
    - [Eddystone beacon](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-EddystoneService/). Try it with the [Eddystone observer](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-EddystoneObserver/), which scans for beacons.

### Peripherals

[On os.mbed.com](https://os.mbed.com/teams/mbed_example/)
