<h1 id="connectivity-tech">Network connectivity in Mbed OS</h1>

Mbed OS supports a wide range of connectivity options. This section helps you to understand how to connect Mbed OS based devices to the outside world.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/connectivity.png)<span>Connectivity options</span></span>

Below is a brief introduction of the different connectivity technologies that we support.

### Bluetooth low energy

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/bluetooth.png)<span>Bluetooth</span></span>

Bluetooth low energy (BLE) is a low power wireless technology standard for personal area networks. Typical applications of BLE are health care, fitness trackers, beacons, smart homes, security, entertainment, proximity sensors, industrial applications and automotives.

To learn how to use Bluetooth low energy on Mbed OS, please refer to the [Bluetooth](../apis/ble.html) user API reference.

### IP networking

Arm Mbed OS supports various IP based connectivity options and IP stacks.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/ip-networking-simple.png)</span>

Our Socket API is an API that standardizes all of our connectivity options. It supports both IPv4 and IPv6. Applications are therefore portable and easy to develop regardless of final connectivity option.

Mbed OS provides network drivers, such as Ethernet, Wi-Fi and cellular.

You can find descriptions of supported interfaces and protocols in the [IP networking](ip-networking.html) section.

### 6LoWPAN Mesh networking

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/mesh.png)<span>Tree type mesh</span></span>

6LoWPAN is a compression method for IPv6 packets. Mbed OS supports 6LoWPAN-ND and Thread protocols for forming IPv6 based mesh networks. Both protocols use the same 6LoWPAN compression method but different routing protocols to achieve wireless mesh network.

Applications running on 6LoWPAN based mesh networks use the same Mbed OS Socket API for connectivity.

For descriptions of mesh networks, please see the [6LoWPAN Mesh](mesh-tech.html) section.

### LoRa

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/lora.png)<span>LoRa</span></span>

[LoRaWAN](http://lora-alliance.org) is a long range wide-area network technology that combines long range with low power consumption. LoRaWAN is not IP based.

The [LoRa](lora-tech.html) section and [LoRa tutorial](../tutorials/LoRa-tutorial.html) describe LoRA networking.

### NFC

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/n_mark.png)<span>NFC</span></span>

Near-field communication (NFC) is a short range (few centimeters) wireless technology standard for personal area networks. Typical uses of NFC are commissioning, easy sharing of small content and Bluetooth connection initiation/out-of-band pairing.

To learn how to use NFC with Mbed OS, please refer to the [NFC](../apis/nfc.html) user API reference.
