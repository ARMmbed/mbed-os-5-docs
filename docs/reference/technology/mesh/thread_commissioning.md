<h2 id="thread-commissioning">How to commission a Thread device in practice</h2>

### Requirements

Commissioning a Thread device requires:

- An Android device to run the commissioning app.
- A working IPv6 backhaul network with a Wi-Fi access point capable of handing out IPv6 addresses over its LAN.
- A border router running the nanostack-border-router application.
- A working IPv6 network with:
  - An Android device that can ping the border router.
  - A development machine (a PC) that can ping the border router.
  - A PC and border router with IPv6 addresses assigned to them from the Wi-Fi access point.
- A Thread-capable end device.

A model network setup could look like this:
<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/Thread_network_setup.PNG)<span>Sample network setup</span></span>

### Building the end node application

By default, the Mbed Thread applications/examples use the static network link configuration defined in the [mesh-api configuration file](https://github.com/ARMmbed/mbed-os/blob/master/features/nanostack/mbed-mesh-api/mbed_lib.json). If you want to use the Thread commissioning, add the following lines to your `.json` file. You can use the [mesh minimal](../apis/mesh-api.html#mesh-example) application as an example.

- `"mbed-mesh-api.thread-use-static-link-config": false` under `"target_overrides":`
- `"macros": ["MBEDTLS_USER_CONFIG_FILE=\"mbedtls_config.h\""]` in to the same level as `"config":` and `"target_overrides":`

Setting `thread-use-static-link-config` to `false` prevents the usage of the predefined link configuration values and allows the device to start network scanning.

Now build the application for your chosen target from Mbed CLI with:

`mbed compile -t <toolchain> -m <target> -c`

Once the binary is generated, flash the binary to the end device, and run the application. Do not power on the end device until the [border router](https://github.com/ARMmbed/nanostack-border-router) has obtained an IPv6 address from the Wi-Fi access point.

### QR code generation

You can use [a free online tool](http://www.qr-code-generator.com/) to generate a QR code.

In the online tool, fill in the URL field. The following is an example: `v=1&eui=000b57fffe07a8be&cc=ABCDEFGH`. Fill in the correct values for your device, and ensure `v=1` is always present. The other required parameters are:

- `cc` is the PSKd, which is configured in the `.json` file (see the mesh-api configuration). *PSKd must be uppercase characters (0-9, A-Y excluding I,O,Q and Z)*
- `eui` is equal to the EUI64 address.

You can get the EUI64 address for your end device by using the `device_eui64_get` method in your application. Please see the [mesh minimal example](../apis/mesh-api.html#mesh-example) for details.

There are four additional (optional) query parameters you can put into this field:

- `vn`    Vendor name.
- `vm`    Vendor model.
- `vv`    Product/Vendor version.
- `vs`    Product/Vendor serial number.

Once you have completed the details, proceed to generate the QR code for your end device.

### Using the Thread commissioning application

You can use the [Thread Android application](https://play.google.com/store/apps/details?id=org.threadgroup.commissioner) for commissioning. Download and install this on your Android device, turn on Wi-Fi and start the app. Then follow these steps after ensuring all the requirements listed above are satisfied:

1. Set up a connection to the Wi-Fi access point to which the Thread border router is connected. When connected, the application lists your Thread border router(s).
2. Select a border router from the list.
3. Enter the passphrase requested by the application. It is `Thread Network` (when using the default Mesh API Thread configuration). After successful connection to the border router, the application is ready to scan the QR code. NOTE: You may need to grant Android permissions in the app.
4. Power on your Thread device if it is not already on.
5. Scan the QR code. The Thread device joins the network. If you are using the mesh-minimal application, the IP address prints on the serial console: `connected. IP = ...`.
