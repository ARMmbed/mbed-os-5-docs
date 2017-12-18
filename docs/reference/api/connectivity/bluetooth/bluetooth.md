## Bluetooth overview

Bluetooth low energy (BLE) is a low power wireless technology standard for personal area networks. Typical applications of BLE are health care, fitness trackers, beacons, smart home, security, entertainment, proximity sensors, industrial and automotive.

Arm Mbed BLE, also called `BLE_API`, is the Bluetooth Low Energy software solution for Mbed. Many targets support Mbed BLE. Developers can use it to create new BLE applications.

#### Getting started

1. Choose an <a href="https://os.mbed.com/platforms/?mbed-enabled=15&connectivity=3" target="_blank">Arm Mbed board that supports BLE</a>, such as the <a href="https://os.mbed.com/platforms/Nordic-nRF51-DK/" target="_blank">NRF51-DK</a>.

	If your platform doesn't support BLE but is compatible with the Arduino UNO R3 connector, you can use an extension board such as the <a href="https://os.mbed.com/components/X-NUCLEO-IDB05A1-Bluetooth-Low-Energy/" target="_blank">X-NUCLEO-IDB05A1</a> to add BLE capabilities to your development board.

1. Install a BLE scanner on your phone. It allows you to track all BLE activities from your embedded application. This is a mandatory tool for BLE software development:

    - <a href="https://play.google.com/store/apps/details?id=no.nordicsemi.android.mcp" target="_blank">nRF Master Control Panel</a> for Android.

    - <a href="https://itunes.apple.com/gb/app/lightblue-bluetooth-low-energy/id557428110?mt=8" target="_blank">LightBlue</a> for iPhone.

1. Compile and run our BLE samples:

    - **Arm Mbed OS 5 samples** are available on <a href="https://os.mbed.com/teams/mbed-os-examples/" target="_blank">os.mbed.com</a> and <a href="https://github.com/ARMmbed/mbed-os-example-ble" target="_blank">Github</a>:
        - The <a href="https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-Beacon/" target="_blank">beacon</a> example is a good starting point; it demonstrates how you can create a BLE beacon with just a few lines of code.  
        - The <a href="https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-HeartRate/" target="_blank">heart rate monitor</a> example demonstrates how to build a heart rate sensor that can be connected and monitored by a BLE client such as your phone.
        - The <a href="https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-LED/" target="_blank">LED</a> and <a href="https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-LEDBlinker/" target="_blank">LED blinker</a> are a single example, which demonstrates how a client (LED) and a server (LED blinker) work together over BLE.

    <span>**Tip:** Despite the differences between the different Mbed OS versions, there is only **one** version of Mbed BLE, and it is easy to move code from one version of the OS to another. Choose the sample you use according to the version of Mbed OS supported by your development board.</span>

#### Going further

- The Mbed BLE <a href="/docs/v5.7/reference/ble.html" target="_blank">API reference</a> offers the full details of the API.

- The Mbed BLE <a href="https://os.mbed.com/teams/Bluetooth-Low-Energy/community/" target="_blank">online community</a> is also a great place to ask questions and share your knowledge.
