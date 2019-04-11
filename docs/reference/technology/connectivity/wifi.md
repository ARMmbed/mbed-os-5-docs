<h1 id="wlan-technology">Wireless LAN</h1>

One of the most popular connectivity technologies is Wireless LAN (Wireless Fidelity - Wi-Fi) as standardized in IEEE 802.11. It extends the Ethernet standards by making Ethernet wireless and adding required security.

To users, these networks behave exactly as Ethernet but without cables.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/wlan-segment.png)<span>WLAN networks</span></span>

A WLAN network typically consists of an access point (AP) connected to an Ethernet backbone and multiple stations (STA) connecting the same access point. You can identify networks by their name, which the standard refers to as *service set identifier* (SSID). Multiple access points can serve the same network, and you can identify each AP by its *basic service set identifier* (BSSID).

## Standards

The original version of the standard IEEE 802.11 was released in 1997. Updates and extended standards later made it obsolete.

| Standard   | Year | Speeds (Mb/s) | Frequency range |
|------------|------|---------------|-----------------|
| 802.11a | 1999 | 6, 9, 12, 18, 24, 36, 48, 54 | 5.16 - 5.35 Ghz |
| 802.11b | 1999 | 1, 2, 5.5, 11 | 2.401 - 2.495 Ghz |
| 802.11g | 2003 | 1, 2, 5.5, 6, 9, 11, 12, 18, 24, 36, 48, 54 | 2.401 - 2.495 Ghz |
| 802.11n | 2009 | 6.5 - 600 | Both 2.4 Ghz and 5 Ghz |
| 802.11ac | 2013 | 6.5 - 1000 | 5 Ghz |

Today, new access points and computers support all a/b/g/n/ac standards, and most embedded devices offer only a/b/g/n capability. The device and the access point negotiate speed and standard automatically without requiring user configuration.

## Wi-Fi in Mbed OS

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/wifi.png)<span>Wi-Fi driver</span></span>

In Mbed OS, wireless LAN devices are either external devices or integrated modules. The driver and hardware handle all the complexity of IEEE 802.11 family standards and integrate into Mbed OS by offering an emulated Ethernet interface or network stack API.

As with Ethernet, Wi-Fi networks are only used for carrying IP traffic in Mbed OS.

For more information, please see the following sections:

- [IP networking](ip-networking.html).
- [Ethernet](ethernet-technology.html).
- [Socket API](../apis/socket.html).
- [WifiInterface API](../apis/wi-fi.html).
