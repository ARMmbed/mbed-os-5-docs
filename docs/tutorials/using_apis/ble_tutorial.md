<h1 id="ble-tutorial">BLE</h1>

## Getting started

1. Choose an [Arm Mbed board that supports BLE](https://os.mbed.com/platforms/?mbed-enabled=15&connectivity=3), such as the [NRF51-DK](https://os.mbed.com/platforms/Nordic-nRF51-DK/).

	If your platform doesn't support BLE but is compatible with the Arduino UNO R3 connector, you can use an extension board such as the [X-NUCLEO-IDB05A1](https://os.mbed.com/components/X-NUCLEO-IDB05A1-Bluetooth-Low-Energy/) to add BLE capabilities to your development board.

1. Install a BLE scanner on your phone. It allows you to track all BLE activities from your embedded application. This is a mandatory tool for BLE software development:

    - [nRF Connect](https://play.google.com/store/apps/details?id=no.nordicsemi.android.mcp) for Android.

    - [LightBlue](https://itunes.apple.com/gb/app/lightblue-bluetooth-low-energy/id557428110?mt=8) for iPhone.

1. Compile and run our BLE samples:

    - **Arm Mbed OS 5 samples** are available on [os.mbed.com](https://os.mbed.com/teams/mbed-os-examples/) and [GitHub](https://github.com/ARMmbed/mbed-os-example-ble):
        - The [beacon](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-Beacon/) example is a good starting point; it demonstrates how you can create a BLE beacon with just a few lines of code.  
        - The [heart rate monitor](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-HeartRate/) example demonstrates how to build a heart rate sensor that can be connected and monitored by a BLE client such as your phone.
        - The [LED](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-LED/) and [LED blinker](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-LEDBlinker/) are a single example, which demonstrates how a client (LED) and a server (LED blinker) work together over BLE.

    <span>**Tip:** Despite the differences between the different Mbed OS versions, there is only **one** version of Mbed BLE, and it is easy to move code from one version of the OS to another. Choose the sample you use according to the version of Mbed OS supported by your development board.</span>

## Going further

- The Mbed BLE [API reference](../apis/ble.html) offers the full details of the API.

- The Mbed BLE [online community](https://os.mbed.com/teams/Bluetooth-Low-Energy/community/) is also a great place to ask questions and share your knowledge.
