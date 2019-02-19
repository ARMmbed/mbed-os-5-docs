<h2 id="device-management">Device Management for Mbed OS</h2>

This feature provides a way to add device management capabilities to Mbed OS devices using the Pelion Device Management service.

It:

- Enables applications to connect and perform firmware updates in a few lines of code.
- Runs separately from your main application; it does not take over your main loop.
- Provides LWM2M resources, variables that sync automatically through Device Management.
- Helps users avoid doing blocking network operations in interrupt contexts, by automatically deferring actions to a separate thread.
- Provides end-to-end Greentea tests for Device Management.

This library makes it trivial to expose sensors, actuators and other variables to a cloud service. For a complete Device Management Client API, please see our [documentation](https://cloud.mbed.com/docs/current/mbed-cloud-client/index.html). <!---This isn't a link to API references, though.--->

### Device Management for your Mbed OS application

Not every device (microcontroller, module or board) is capable of running device management features. Although you can add or extend some hardware capabilities, such as connectivity, storage and TRNG, others are impossible or inconvenient to extend (for example, RAM or flash).

The minimum requirements to add device management feature to your application are:

- RAM: 128K or more.
- Flash: 512K or more.
- Real Time Clock (RTC).
- (Optional but recommended) True Random Number Generator (TRNG).
- A storage device: SD card, SPI flash, QSPI flash or data flash.
- IP connectivity: Ethernet, Wi-Fi, cellular, 6LoWPAN or Thread.

Additionally, we recommend the latest version of Mbed OS support the device and any additional complementary hardware components, or that they have support for the APIs provided in the latest releases of Mbed OS.

Useful references:

- Check which Mbed OS platforms are supported in the [Device Management quick start guide](https://cloud.mbed.com/quick-start).
- Check the [storage options available](../reference/storage.html).
- Check the [network options available](../reference/network-socket.html).

#### Adding a device management feature to your application

1. Add this library to your Mbed OS project:

   ```
   $ mbed add https://github.com/ARMmbed/simple-mbed-cloud-client
   ```

   If you do not have an Mbed OS project to add, you can create one with `mbed new <your_application_name>` and then the `mbed add` step above.

1. Reference the library from the `main.cpp` file, and add network and storage drivers. Finally, initialize the SimpleMbedCloudClient library. This is the architecture of a device management application with Mbed OS:

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

1. Configure the API key for your Device Management account.

   If you don't have an API key available, then log in to [Device Management Portal](https://portal.mbedcloud.com/), navigate to `Access Management` and `API keys`, and create a new one. Then specify the API key as the global `mbed` configuration:

    ```
    $ mbed config -G CLOUD_SDK_API_KEY <your-api-key>
    ```

1. Install the Device Management certificate:

    ```
    $ mbed dm init -d "<your company name.com>" --model-name "<product model identifier>"
    ```

This creates your private and public key pair and also initialize various `.c` files with these credentials, so you can use Connect and (firmware) Update device management features.

#### Example applications

To help you start quickly, please refer to the following [application example](https://github.com/ARMmbed/pelion-ready-example). It demonstrates how to connect to the Pelion IoT Platform service, register resources and get ready to receive a firmware update.

Also, there are a number of board-specific applications that focus on providing more elaborate hardware features with Mbed OS and the Pelion IoT Platform. These are available in the Device Management [quick start](https://cloud.mbed.com/quick-start). Please see the reference table below, organized by vendor name, for details:

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
