### How to commission a Thread device in practice

#### Requirements
Commissioning a Thread device requires the following conditions to be satisfied:

- An Android device to run the commissioning app.
- A working IPv6 backhaul network with a WiFi access point capable of handing out IPv6 addresses over it's LAN.
- A border router running the nanostack-border-router application.
- A working IPv6 network with the following:
  - The Android device able to ping the border router.
  - The development machine (a PC) able to ping the border router.
  - The PC, border router have IPv6 addressess assigned to them from the WiFi access point.
- A Thread capable end device.

#### Building the end node application

By default, the Mbed Thread applications/examples use the static network link configuration defined in the <a href="https://github.com/ARMmbed/mbed-os/blob/master/features/nanostack/FEATURE_NANOSTACK/mbed-mesh-api/mbed_lib.json" target="_blank">mesh-api configuration file</a>. If you want to use the Thread commissioning, add the following lines to your `.json` file. You can use the <a href="https://github.com/ARMmbed/mbed-os-example-mesh-minimal" target="_blank">mesh-minimal</a> application as an example.

- `"mbed-mesh-api.thread-use-static-link-config": false`
- `"macros": ["MBEDTLS_USER_CONFIG_FILE=\"mbedtls_config.h\""]`

Setting `thread-use-static-link-config` to `false` prevents the usage of the predefined link configuration values and allows the device to start network scanning.

Now build the application for your chosen target from mbed CLI with:
`mbed compile -t <toolchain> -m <target> -c`

Once the binary is generated, flash this to the end device and run the application. Do not power on the end device until the <a href="https://github.com/ARMmbed/nanostack-border-router">border router</a> has obtained a IPv6 address from the WiFi access point.

#### QR code generation

You can use <a href="http://www.qr-code-generator.com/" target="_blank">a free online tool</a> to generate a QR code.

In the online tool, fill in the URL field. The following is an example: `v=1&eui=000b57fffe07a8be&cc=PV7TUCB0`. Fill in the correct values for your device and make sure `v=1` is always present. The other required parameters are:

- `cc` is the PSKd, which is configured in the `.json` file (see the mesh-api configuration).
- `eui` is equal to the RF MAC address by default.

To get the MAC address for your end device, you need to connect the node to the Thread network with static configuration enabled i.e. `"mbed-mesh-api.thread-use-static-link-config": true`, unless you have your own configuration for the MAC address.

For example, in the **mesh-minimal** application, place this `printf("MAC address = %s\n", mesh.get_mac_address());` after `printf("connected. IP = %s\n", mesh.get_ip_address());`
There are four additional (optional) query parameters you can put into this field:

- `vn`    Vendor name
- `vm`    Vendor model
- `vv`    Product/Vendor version
- `vs`    Product/Vendor serial number

Once the details are filled, proceed to generate the QR code for your end device.

#### Using the Thread commissioning application

You can use the <a href="https://play.google.com/store/apps/details?id=org.threadgroup.commissioner" target="_blank">Thread Android application</a> for commissioning. Download and install this on your Android device, turn on WiFi and start the app. Then follow these steps after ensuring all the requirements listed above are satisfied:

1. Set up a connection to the Wi-Fi access point to which the Thread border router is connected. When connected, the application lists your Thread border routers(s).
2. Select a border router from the list.
3. Enter the passphrase requested by the application. It is `Thread Network` (when using the default mesh-api Thread configuration). After successful connection to the border router, the application is ready to scan the QR code. NOTE: You may need to grant android permissions in the app.
4. Power on your Thread device if it is not already on.
5. Scan the QR code. The Thread device should join the network. If you are using the mesh-minimal application you should see the IP address printed on the serial console: `connected. IP = ...`.
