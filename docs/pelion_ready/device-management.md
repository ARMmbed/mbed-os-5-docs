<h1 id="device-management">Device Management for Mbed OS</h1>

Pelion Client is an abstraction of the Device Management Client, and lets Mbed OS devices use the [Pelion Device Management Services](https://cloud.mbed.com/docs/latest/welcome/index.html). Pelion Client:

- Provides LwM2M resources - variables that sync automatically through Device Management. Pelion Client makes it trivial to expose sensors, actuators and other variables to a cloud service.
- Supports firmware updates with just a few lines of code.
- Runs separately from your main application; it does not take over your main loop.
- Helps avoid blocking network operations in interrupt contexts, by automatically deferring actions to a separate thread.
- Provides end-to-end Greentea tests for Device Management.

This guide builds on the [quick connect guide](https://os.mbed.com/guides/connect-device-to-pelion/), which creates a cloud-connected application for supported Mbed OS boards. The guide covers:

- [Hardware requirements](#requirements).
- [Adding the library to an application](#adding-device-management-connectivity-to-your-application).
- A list of [example applications for different boards](#example-applications).
- [Configuring the application and bootloader](../mbed-os-pelion/device-management-configuration.html).
- [Validation and testing](../mbed-os-pelion/device-management-test.html).
- [Troubleshooting](../mbed-os-pelion/device-management-test.html#troubleshooting).

<span class="tips">**Tip**: To learn more about Device Management Client, please see our [Device Management documentation](https://cloud.mbed.com/docs/latest/client-api-references/index.html).</span>

## Device Management for your Mbed OS application

### Requirements

Not every device (microcontroller, module or board) is capable of running device management features. Although you can add or extend some hardware capabilities, such as connectivity, storage and TRNG, others are impossible or inconvenient to extend (for example, RAM or flash).

The minimum requirements to add device management feature to your application are:

- RAM: 128K or more.
- Flash: 512K or more.
- Real Time Clock (RTC).
- (Optional but recommended) True Random Number Generator (TRNG).
- A storage device: SD card, SPI flash, QSPI flash or data flash.
- IP connectivity: Ethernet, Wi-Fi, cellular, Mesh (6LoWPAN-ND, Wi-SUN or Thread).

Additionally, we recommend the latest version of Mbed OS support the device and any additional complementary hardware components, or that they have support for the APIs provided in the latest releases of Mbed OS.

Useful references:

- Check which Mbed OS platforms are supported in the [Device Management quick start guide](https://cloud.mbed.com/quick-start).
- Check the [storage options available](../reference/storage.html).
- Check the [network options available](../reference/networking.html).

### Adding Device Management connectivity to your application

1. Add Pelion Client to your Mbed OS project:

    <span class="notes">**Note**: the library is called `simple-mbed-cloud-client`.</span>

   ```
   $ mbed add https://github.com/ARMmbed/simple-mbed-cloud-client
   ```

   If you do not have an Mbed OS project to add, you can create one with `mbed new <your_application_name>` and then the `mbed add` step above.

1. Reference the library from the `main.cpp` file, and add network and storage drivers.

1. Initialize the `simple-mbed-cloud-client` library:

    ```cpp NOCI
    #include "simple-mbed-cloud-client.h"
    #include <Block device>
    #include <Filesystem>
    #include <Network>

    int main() {

        /* Initialize connectivity */
        NetworkInterface *net = NetworkInterface::get_default_instance();
        net->connect();

        /* Initialize storage */
        BlockDevice *bd = BlockDevice::get_default_instance();
        <Filesystem> fs("fs", &bd);

        /* Initialize SimpleMbedCloudClient */
        SimpleMbedCloudClient client(net, &bd, &fs);
        client.init();

        /* Create resource */
        MbedCloudClientResource *variable;
        variable = client.create_resource("3201/0/5853", "variable");
        variable->set_value("assign new value");
        variable->methods(M2MMethod::GET | M2MMethod::PUT);

    }
    ```

1. Configure the API key for your Device Management account by specifying the API key as the global `mbed` configuration:

    ```
    $ mbed config -G CLOUD_SDK_API_KEY <your-api-key>
    ```

    <span class="tips">If you don't have an API key available, then log in to [Device Management Portal](https://portal.mbedcloud.com/), navigate to `Access Management` and `API keys`, and create a new one.</span>

1. Install the Device Management certificate:

    ```
    $ mbed dm init -d "<your company name.com>" --model-name "<product model identifier>"
    ```

This creates your private and public key pair and also initialize various `.c` files with these credentials, so you can use Connect and (firmware) Update device management features.

### Example applications

To help you start quickly, please refer to the following [application example](https://github.com/ARMmbed/pelion-ready-example). It demonstrates how to connect to the Device Management service, register resources and get ready to receive a firmware update.

Also, there are a number of board-specific applications that focus on providing more elaborate hardware features with Mbed OS and Device Management. These are available in the Device Management [quick start](https://cloud.mbed.com/quick-start). Please see the reference table below, organized by vendor name, for details:

Platform                        |  Connectivity      | Storage   | Example URL
--------------------------------| -------------------| --------- | --------------------
Nuvoton NUMAKER-IOT-M487        | Wi-Fi              | SD Card   | https://os.mbed.com/teams/Nuvoton/code/pelion-example-common/
Nuvoton NUMAKER-PFM-M487        | Ethernet           | SD Card   | https://os.mbed.com/teams/Nuvoton/code/pelion-example-common/
Nuvoton NUMAKER-PFM-NUC472      | Ethernet           | SD Card   |https://os.mbed.com/teams/Nuvoton/code/pelion-example-common/
NXP FRDM-K64F                   | Ethernet           | SD Card   | https://os.mbed.com/teams/NXP/code/mbed-cloud-connect-example-ethernet
NXP FRDM-K66F                   | Ethernet           | SD Card   | https://os.mbed.com/teams/NXP/code/mbed-cloud-connect-example-ethernet
Renesas GR-LCYHEE               | Wi-Fi              | SD Card   | https://os.mbed.com/teams/Renesas/code/pelion-example-common/
Sigma Delta Technologies SDT64B | Ethernet           | SD Card   | https://os.mbed.com/teams/Sigma-Delta-Technologies/code/pelion-example-common
ST DISCO_L475E_IOT01A           | Wi-Fi              | QSPI      | https://os.mbed.com/teams/ST/code/pelion-example-disco-iot01/
ST DISCO_F413H                  | Wi-Fi              | QSPI      | https://os.mbed.com/teams/ST/code/pelion-example-common/
ST DISCO_F746NG                 | Ethernet           | QSPI      | https://os.mbed.com/teams/ST/code/pelion-example-common/
ST NUCLEO_F429ZI                | Ethernet           | SD Card   | https://os.mbed.com/teams/ST/code/pelion-example-common/
ST NUCLEO_F767ZI                | Ethernet           | SD Card   | https://os.mbed.com/teams/ST/code/pelion-example-common/
ST NUCLEO_F746ZG                | Ethernet           | SD Card   | https://os.mbed.com/teams/ST/code/pelion-example-common/
ST NUCLEO_F207ZG                | Ethernet           | SD Card   | https://os.mbed.com/teams/ST/code/pelion-example-common/
UBlox EVK ODIN W2               | Wi-Fi              | SD Card   | https://os.mbed.com/teams/ublox/code/pelion-example-common/
UBlox C030 U201                 | Cellular           | SD Card   | https://os.mbed.com/teams/ublox/code/pelion-example-common/
