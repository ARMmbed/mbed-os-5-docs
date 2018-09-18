## Connectivity in Mbed OS

### Supported connectivity technologies

Mbed OS offers a strong, integrated stack of standards-based technologies:

For IP devices:

* Arm Mbed Thread.
* 6LoWPAN.
* Cellular.
* NB-IoT.
* Bluetooth Low Energy (BLE).

Non-IP devices require a gateway:

* LoRaWAN.

<!--Edge?-->

### Choosing your connectivity method

Connected devices come in all shapes and sizes <!--Amanda, help me!-->, and there is no globally correct connectivity method choice; you will need to choose a method that fits your application needs, then choose a device that can support that method. If you're already committed a device type, you may need to adjust your application to work within that device's connectivity constraints.

<!--Needs a bit more info to be useful-->

This table should help you narrow down your options. Full details are in the following sections.

| Method | Memory requirements | Power consumption | Range | Bandwidth | Costs | Existing infrastructure | Indoors/outdoors |
| --- | --- | --- | --- | --- | --- | --- | --- |


### IP networking

Arm Mbed OS supports various IP based connectivity options and IP stacks.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/ip-networking-simple.png)</span>

Our Socket API is an API that standardizes all of our connectivity options. It supports both IPv4 and IPv6. Applications are therefore portable and easy to develop regardless of final connectivity option.

Mbed OS provides network drivers, such as Ethernet, Wi-Fi and cellular.

You can find descriptions of supported interfaces and protocols in the [IP networking](ip-networking.html) section.

#### WiFi

WiFi has relatively high throughput - up to 1GB/s - perfect for data-heavy applications. That comes at the cost of a relatively high power consumption; it is not ideal for long-term deployments of battery-powered devices. It can also prove problematic where a lot of other devices may compete for the same bandwidth.

It's a great method for proof of concept devices, because the infrastructure is in place in any modern office, and its WPA2 security is familiar to developers.

End devices for WiFi are not the cheapest, because of the hardware requirements WiFi entails. The network cost depends on whether the deployment location already includes a well maintained WiFi infrastructure. WiFi is ubiquitous - indoors - and WiFi devices enjoy a range of tens of meters, so for certain applications, like those for homes and offices, the infrastructure can be assumed to exist.

#### Cellular

<!--Do I want to force all the methods into a single narrative structure for easier comparison, or is that covered by the table and I can be a bit more freeform in the text?-->

Cellular has a variable throughput, reaching 10mbp/s. Its coverage is extensive, and its range is 25-100km, so it is commonly used in transportation and logistics. It is also well suited for proof of concept, because - like WiFi - it relies on an existing infrastructure.

Cellular coverage, load balancing and reliability are the responsibility of the providers, note the application. The downside is that access to the network is subscription based, so there is a direct correlation between usage and cost.

<!--Pasi, you say the variable throughput is great for applications that have changing needs. Does this mean that other protocols force a higher throughput, and that the device pays a price for that?-->

The new cellular technologies, NB-IoT and CAT-M1, are designed for IoT devices. They offer some advantages, but there are also risks and costs.

**NB-IoT** relies on a simple waveform and therefore requires the lowest power consumption of all the cellular methods. It also has fewer components and offers better wall penetration (thanks to lower bitrates and better link budgets)<!--I have no idea what I just wrote. Pasi, can I have more info, please?-->. On the other hand, because it's not part of the traditional LTE standard, it can be harder to deploy in some markets (like the USA), and its dual-chip base is more expensive to manufacture. It also needs a country-specific chip, because each country uses its own spectrum, which further complicates production. It also experiences problems with large transfers, because of its reduced bandwidth <!--how much?-->

**CAT-M1** has a higher data rate than NB-IoT (closer to existing cellular behaviour), but is not proven to be more power efficient - and any efficiency gains can be lost because of operator configurations.

It can be deployed on a single spectrum, reducing antenna configuration complexity, but it will not be deployed world-wide, and can take year to be deployed in countries using 3G. Its chips are expensive because of legacy licensing costs <!--more expensive than the dual chips of NB-IoT?-->

#### Bluetooth Low Energy (BLE)

BLE is optimised for cheap, battery-based devices and has a low memory footprint. It is widely adopted for connected spaces, but requires setting up an infrastructure. Its range is up to 100 meters, with a 1mb/s bandwidth, and it support floating mesh for large spaces.

Typical applications of BLE are health care, fitness trackers, beacons, smart homes, security, entertainment, proximity sensors, industrial applications and automotives.

To learn how to use Bluetooth low energy on Mbed OS, please refer to the [Bluetooth](/docs/development/apis/ble.html) user API reference.

####  IP-based mesh (Thread and Wi-SUN)

As a technology that was designed for deployment, it's not surprising to find that mesh is optimised for a long battery life and low costs.

**Thread** is designed for indoor use, with a range of only a few meters. **Wi-SUN** has a range of up to one kilometer, and is therefore better suited for external use. Both technologies have a low throughput - up to 200kb/s - and experience delays.

Mesh networks are self-healing - they have no single point of failure. The expense is in the infrastructure setup and maintenance, and they are therefore more suitable for limited spaces.

<!--"Additionally ARM mbed OS Thread stack is tested against pre-defined stability, reliability and performance test sets to ensure high quality production ready delivery for application and product creation."
Pre-defined by who? The Thread alliance?-->


#### 6LoWPAN Mesh networking

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/mesh.png)<span>Tree type mesh</span></span>

6LoWPAN is a compression method for IPv6 packets. Mbed OS supports 6LoWPAN-ND and Thread protocols for forming IPv6 based mesh networks. Both protocols use the same 6LoWPAN compression method but different routing protocols to achieve wireless mesh network.

Applications running on 6LoWPAN-based mesh networks use the same Mbed OS Socket API for connectivity. <!--same as what?-->

For descriptions of mesh networks, please see the [6LoWPAN Mesh](mesh-tech.html) section.


### Non-IP networking

#### LoRaWAN

LoRaWAN is optimised for low power consumption and a low memory footprint (allowing low-cost devices). The downside is that it has a very low throughput - no more than 50kb/s - and suffers delays. It is a non-IP based technology.

Because of its long range - up to 20km - and low power, it is suitable for low data rate, outdoors solutions.

<!--what's the infrastructure?-->

The [LoRa](lora-tech.html) section and [LoRa tutorial](/docs/development/tutorials/LoRa-tutorial.html) describe LoRA networking.


#### NFC

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/n_mark.png)<span>NFC</span></span>

Near-field communication (NFC) is a short range (few centimeters) wireless technology standard for personal area networks. Typical uses of NFC are commissioning, easy sharing of small content and Bluetooth connection initiation/out-of-band pairing.

To learn how to use NFC with Mbed OS, please refer to the [NFC](/docs/development/apis/nfc.html) user API reference.


#### Memory needs for Pelion-connected devices

Mbed OS's baseline memory footprint, without Pelion connectivity, is 2.8kb of RAM and 8.2kb of flash. When you add Pelion connectivity and full functionality, the footprint grows:

* For **Pelion Client Lite**, the smaller of the two Pelion connectivity libraries: a total of 20kb RAM, 210kb flash. This includes not just Ethernet connectivity, but also startup and runtime demands, the size of Pelion Client Lite itself and additional driver <!--which drivers?-->
* For **Pelion Client**: a total of 137kb RAM, 330kb flash. This adds FileSystem and the full Pelion Client to the functionality.

The two Pelion connectivity libraries give you the choice of a huge range of devices. Mbed OS with Pelion Client Lite can work on devices with only 64kb RAM and 256kb flash. Mbed OS with the full Pelion Client fits comfortably on devices with 128kb RAM and 1024kb flash.

#### Security

<!--Something about how we secure independently of the protocol, but are some methods still more secure than others?

-->
