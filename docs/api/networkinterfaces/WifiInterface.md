# Wi-Fi

<span class="images">![](http://os.mbed.com/docs/development/mbed-os-api-doxy/class_wi_fi_interface.png)<span>WiFiInterface class hierarchy</span></span>

The WifiInterface provides a simple C++ API for connecting to the internet over a Wi-Fi device.

## Wi-Fi class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/development/mbed-os-api-doxy/class_wi_fi_interface.html)

## Usage

To bring up the network interface of an external Wi-Fi device (for example, the ESP8266Interface):

1. Instantiate an implementation of the WiFiInterface class.
    1. Initialize the AT command parser.
1. Call the `connect()` function with an SSID and password for the Wi-Fi network.
    1. Command the Wi-Fi device to connect to network.
1. Once connected, you can use the WiFiInterface as a target for opening [network sockets](network-socket.html).

To bring up the network interface of an Ethernet-like driver (for example, the OdinWiFiInterface):

1. Instantiate an implementation of the WiFiInterface class.
    1. Initialize the Wi-Fi driver for the target.
    1. Initialize network stack (LWIP).
1. Call the `connect()` function with an SSID and password for the Wi-Fi network.
    1. Connect the Wi-Fi driver to the Wi-Fi network.
    2. Ensure the network stack acquires the IP address and DNS server address.
1. Once connected, you can use the WiFiInterface as a target for opening [network sockets](network-socket.html).

## Troubleshooting information

Network interface `connect()` and `set_credential()` might return following errors:

| Error code | Possible reason |
|------------|-----------------|
| `NSAPI_ERROR_UNSUPPORTED` | Security mode is unsupported. |
| `NSAPI_ERROR_PARAMETER` | Wrong parameters supplied for the given security mode, for example, no password. |
| `NSAPI_ERROR_NO_SSID` | The device did not find the given Wi-Fi network. |
| `NSAPI_ERROR_AUTH_FAILURE` | Wrong password given. |
| `NSAPI_ERROR_DEVICE_ERROR` | Unknown failure happened in the device. The device may not be capable of reporting more descriptive error codes. |

## Security

For specifying security settings, both `connect()` and `set_credential()` have optional parameter `nsapi_security_t security`, which defines the security mode the device uses. WifiInterface supports the following security modes:

| `nsapi_security_t`        | Security mode |
|---------------------------|---------------|
| `NSAPI_SECURITY_NONE`     | Not secure. Require no password or encryption. |
| `NSAPI_SECURITY_WEP`      | WEP security. Outdated. |
| `NSAPI_SECURITY_WPA`      | WPA security mode. Obsolete by WPA2; do not use. |
| `NSAPI_SECURITY_WPA2`     | WPA2 security. Mostly used security mode. |
| `NSAPI_SECURITY_WPA_WPA2` | Allows either WPA or WPA2 security. |

Please note that settings should match the security mode from the access point. Also, not all drivers support every mode. For most compatible settings, use `NSAPI_SECURITY_WPA_WPA2`, and set the Wi-Fi access point to allow only WPA2 mode.

## Wi-Fi example

This program scans for Wi-Fi access points in the area. There are multiple [Wi-Fi components](https://os.mbed.com/components/cat/wifi/) that implement the WiFiInterface class. The example below uses the [ESP8266Interface](https://github.com/armmbed/esp8266-driver) and [OdinWiFiInterface](https://github.com/u-blox/ublox-odin-w2-drivers-docs-mbed-5).

The ESP8266Interface uses AT commands over serial interface to connect to an external Wi-Fi device. The OdinWiFiInterface provides an Ethernet-like driver to the Mbed OS network stack. The network stack uses the driver to connect to Wi-Fi:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-wifi)](https://github.com/ARMmbed/mbed-os-example-wifi/blob/mbed-os-5.14/main.cpp)

## Related content

- [Wi-Fi components](https://os.mbed.com/components/cat/wifi/).
- [Network socket](network-socket.html) API overview.
- [Wi-Fi architecture](../reference/wlan-technology.html).
