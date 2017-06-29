### Bluetooth Low Energy (BLE)

Bluetooth low energy (BLE) is a very low power wireless technology standard for personal area networks. Typical applications of BLE are health care, fitness trackers, beacons, smart home, security, entertainment, proximity sensors, industrial and automotive.

mbed BLE, also called `BLE_API`, is the Bluetooth Low Energy software solution for mbed. Many targets support mbed BLE. Developers can use it to create new BLE applications.

#### Getting started

1. Choose an [mbed board that supports BLE](https://developer.mbed.org/platforms/?mbed-enabled=15&connectivity=3), such as the [NRF51-DK](https://developer.mbed.org/platforms/Nordic-nRF51-DK/).

	If your platform doesn't support BLE but is compatible with the Arduino UNO R3 connector, you can use an extension board such as the [X-NUCLEO-IDB05A1](https://developer.mbed.org/components/X-NUCLEO-IDB05A1-Bluetooth-Low-Energy/) to add BLE capabilities to your development board.

1. Install a BLE scanner on your phone. It allows you to track all BLE activities from your embedded application. This is a mandatory tool for BLE software development:

    * [nRF Master Control Panel](https://play.google.com/store/apps/details?id=no.nordicsemi.android.mcp) for Android.

    * [LightBlue](https://itunes.apple.com/gb/app/lightblue-bluetooth-low-energy/id557428110?mt=8) for iPhone.

1. Compile and run our BLE samples:

    * **mbed OS 5 samples** are available on [developer.mbed.org](https://developer.mbed.org/teams/mbed-os-examples/) and [Github](https://github.com/ARMmbed/mbed-os-example-ble):
        * The [beacon](https://developer.mbed.org/teams/mbed-os-examples/code/mbed-os-example-ble-Beacon/) example is a good starting point; it demonstrates how you can create a BLE beacon with just a few lines of code.  
        * The [heart rate monitor](https://developer.mbed.org/teams/mbed-os-examples/code/mbed-os-example-ble-HeartRate/) example demonstrates how to build a heart rate sensor that can be connected and monitored by a BLE client such as your phone.
        * The [LED](https://developer.mbed.org/teams/mbed-os-examples/code/mbed-os-example-ble-LED/) and [LED blinker](https://developer.mbed.org/teams/mbed-os-examples/code/mbed-os-example-ble-LEDBlinker/) are a single example, which demonstrates how a client (LED) and a server (LED blinker) work together over BLE.

    <span>**Tip:** Despite the differences between the different mbed OS versions, there is only **one** version of mbed BLE, and it is easy to move code from one version of the OS to another. Choose the sample you use according to the version of mbed OS supported by your development board.</span>

#### Going further

* [Introduction to mbed BLE](https://docs.mbed.com/docs/ble-intros/en/latest/) is a resource for developers new to BLE and mbed BLE. It covers how to build BLE embedded applications with mbed.

* The Bluetooth Low Energy main [page](https://developer.mbed.org/teams/Bluetooth-Low-Energy/) on developer.mbed.org also provide samples and resources around BLE.

* The mbed BLE [API reference](https://docs.mbed.com/docs/ble-api/en/master/api/index.html) offer the full details of the API.

* The mbed BLE [online community](https://developer.mbed.org/teams/Bluetooth-Low-Energy/community/) is also a great place to ask questions and share your knowledge.

#### API reference

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classBLE.html)
