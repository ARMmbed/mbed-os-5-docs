  
### Blinky

* [Blinky](https://developer.mbed.org/teams/mbed-os-examples/code/mbed-os-example-blinky/): our basic application, showing how to use the APIs to control the LED on the board.

### mbed TLS

* [Cryptographic benchmark](https://developer.mbed.org/teams/mbed-os-examples/code/mbed-os-example-tls-benchmark/): benchmarks the various cryptographic primitives offered by mbed TLS.

* [Authenticated encryption and decryption](https://developer.mbed.org/teams/mbed-os-examples/code/mbed-os-example-tls-authcrypt/): performs authenticated encryption and authenticated decryption of a buffer. It serves as a tutorial for the basic authenticated encryption functions of mbed TLS.

* [Hashing](https://developer.mbed.org/teams/mbed-os-examples/code/mbed-os-example-tls-hashing/):  performs hashing of a buffer with SHA-256 using various APIs. It serves as a tutorial for the basic hashing APIs of mbed TLS.

* [TLS client](https://developer.mbed.org/teams/mbed-os-examples/code/mbed-os-example-tls-tls-client/):  downloads a file from an HTTPS server (developer.mbed.org) and looks for a specific string in that file.

### mbed uVisor

The [uVisor sample](https://github.com/ARMmbed/mbed-os-example-uvisor) is for GCC only, so cannot be used in the mbed Online Compiler. 

### mbed Client

[Getting started](https://developer.mbed.org/teams/mbed-os-examples/code/mbed-os-example-client/): a basic example of mbed Client for mbed OS. It demonstrates how to register a device with mbed Device Connector, how to read and write values, and how to deregister.

### mesh 

[Join a device to an insecure 6LoWPAN-ND network](https://developer.mbed.org/teams/mbed-os-examples/code/mbed-os-example-mesh-minimal/). This is the simples use of the mesh networking sack.

### Bluetooth Low Energy (BLE)

* [Battery level](https://developer.mbed.org/teams/mbed-os-examples/code/mbed-os-example-ble-BatteryLevel/): use the Battery Level service to transmit a device's battery level.

* [BLE button](https://developer.mbed.org/teams/mbed-os-examples/code/mbed-os-example-ble-Button/): BLE service template for a read-only characteristic. 

* [GAP button](https://developer.mbed.org/teams/mbed-os-examples/code/mbed-os-example-ble-GAPButton/): use GAP to transmit a value to a peer that's listening for advertisements. 

* [Heart rate](https://developer.mbed.org/teams/mbed-os-examples/code/mbed-os-example-ble-HeartRate/): transmit a heart rate value using the SIG Heart Rate profile.

* [Thermometer](https://developer.mbed.org/teams/mbed-os-examples/code/mbed-os-example-ble-Thermometer/): send thermometer information using the Health Thermometer Profile.

* [Simple LED control](https://developer.mbed.org/teams/mbed-os-examples/code/mbed-os-example-ble-LED/): a client using a read/write characteristic to control an LED. This example goes with the [LED blinker](https://developer.mbed.org/teams/mbed-os-examples/code/mbed-os-example-ble-LEDBlinker/), a server that uses the GATT client API to control the BLE client device.

* Beacons send a small amount of information to a nearby device. Try:
    * [BLE beacon](https://developer.mbed.org/teams/mbed-os-examples/code/mbed-os-example-ble-Beacon/). 
    * [URI beacon](https://developer.mbed.org/teams/mbed-os-examples/code/mbed-os-example-ble-URIBeacon/).
    * [Eddystone beacon](https://developer.mbed.org/teams/mbed-os-examples/code/mbed-os-example-ble-EddystoneService/). Try it with the [Eddystone observer](https://developer.mbed.org/teams/mbed-os-examples/code/mbed-os-example-ble-EddystoneObserver/), which scans for beacons.
