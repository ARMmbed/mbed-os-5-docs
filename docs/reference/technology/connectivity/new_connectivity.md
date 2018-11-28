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

Connected devices come in a wide variety<!--Amanda, help me!-->, and there is no globally correct connectivity method. Choose a method that fits your application needs, then choose a device that can support that method. If you're already committed to a device type, you may need to adjust your application to work within that device's connectivity constraints.

<!--Needs a bit more info to be useful-->

This table covers a number of options. Full details are in the following sections.

| Method | Memory requirements | Power consumption | Range | Bandwidth | Costs | Existing infrastructure | Indoors/outdoors |
| --- | --- | --- | --- | --- | --- | --- | --- |


### IP networking

Arm Mbed OS supports various IP-based connectivity options and IP stacks.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/ip-networking-simple.png)</span>

Our Socket API standardizes all of our connectivity options. It supports both IPv4 and IPv6. Applications are portable regardless of final connectivity option.

Mbed OS provides network drivers, such as Ethernet, Wi-Fi and cellular.

You can find descriptions of supported interfaces and protocols in the [IP networking](ip-networking.html) section.

#### Wi-Fi

Wi-Fi has a relatively high throughput of up to 1GB/s, which is suitable for data-heavy applications. That comes at the cost of a relatively high power consumption. Wi-Fi is not ideal for long-term deployments of battery-powered devices. It can also prove problematic where other devices compete for the same bandwidth.

It works for proof of concept devices because the infrastructure is in place in most offices, and its WPA2 security is familiar to developers.

End devices for Wi-Fi are not <!---cost-effictive? economical?---> because of hardware requirements. The network cost depends on whether the deployment location already includes a well maintained Wi-Fi infrastructure. Wi-Fi is ubiquitous indoors, and Wi-Fi devices enjoy a range of tens of meters, so for certain applications, like those for homes and offices, the infrastructure can be assumed to exist. <!---don't like this passive--->

#### Cellular

<!--Do I want to force all the methods into a single narrative structure for easier comparison, or is that covered by the table and I can be a bit more freeform in the text?-->

Cellular has a variable throughput, reaching 10mbp/s. Its coverage is extensive, and its range is 25-100km, so it is commonly used in transportation and logistics. It is also well suited for proof of concept, because - like Wi-Fi - it relies on an existing infrastructure.

Cellular coverage, load balancing and reliability are the responsibility of the providers, note the application. The downside is that access to the network is subscription based, so there is a direct correlation between usage and cost.

<!--Pasi, you say the variable throughput is great for applications that have changing needs. Does this mean that other protocols force a higher throughput, and that the device pays a price for that?-->

The new cellular technologies, NB-IoT and CAT-M1, are designed for IoT devices. They offer some advantages, but there are also risks and costs.

**NB-IoT** relies on a simple waveform and therefore requires the lowest power consumption of all the cellular methods. It also has fewer components and offers better wall penetration (thanks to lower bitrates and better link budgets)<!--I have no idea what I just wrote. Pasi, can I have more info, please?-->. On the other hand, because it's not part of the traditional LTE standard, it can be harder to deploy in some markets (like the USA), and its dual-chip base is more expensive to manufacture. It also needs a country-specific chip, because each country uses its own spectrum, which further complicates production. It also experiences problems with large transfers, because of its reduced bandwidth <!--how much?-->

**CAT-M1** has a higher data rate than NB-IoT (closer to existing cellular behaviour), but is not proven to be more power efficient. Any efficiency gains can be lost because of operator configurations.

It can be deployed on a single spectrum, reducing antenna configuration complexity, but it will not be deployed world-wide, and can take year to be deployed in countries using 3G. Its chips are expensive because of legacy licensing costs <!--more expensive than the dual chips of NB-IoT?-->

#### Bluetooth Low Energy (BLE)

BLE is optimised for cheap, battery-based devices and has a low memory footprint. It is widely adopted for connected spaces, but requires setting up an infrastructure. Its range is up to 100 meters, with 1 mb/s bandwidth. It supports floating mesh for large spaces.

Typical applications of BLE are health care, fitness trackers, beacons, smart homes, security, entertainment, proximity sensors, industrial applications, and automotives.

To learn how to use BLE on Mbed OS, please refer to the [Bluetooth](../apis/ble.html) user API reference.

####  IP-based mesh (Thread and Wi-SUN)

As a technology that was designed for deployment, mesh is optimized for long battery life and low cost.

**Thread** is designed for indoor use, with a range of only a few meters. **Wi-SUN** has a range of up to one kilometer, and is therefore better suited for external use. Both technologies have a low throughput of up to 200kb/s and experience delays.

Mesh networks are self-healing, with no single point of failure. The expense is in the infrastructure setup and maintenance, so they are therefore more suitable for limited spaces.

<!--"Additionally ARM mbed OS Thread stack is tested against pre-defined stability, reliability and performance test sets to ensure high quality production ready delivery for application and product creation."
Pre-defined by who? The Thread alliance?-->

#### 6LoWPAN Mesh networking

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/mesh.png)<span>Tree type mesh</span></span>

6LoWPAN is a compression method for IPv6 packets. Mbed OS supports 6LoWPAN-ND and Thread protocols for forming IPv6 based mesh networks. Both protocols use the same 6LoWPAN compression method but different routing protocols to achieve wireless mesh network.

Applications running on 6LoWPAN-based mesh networks use the same Mbed OS Socket API for connectivity. <!--same as what?-->

For descriptions of mesh networks, please see the [6LoWPAN Mesh](mesh-tech.html) section.

### Non-IP networking

#### LoRaWAN

LoRaWAN is optimized for low power consumption and a low memory footprint (allowing low-cost devices). The downside is a low throughput of no more than 50kb/s, as well as delays. It is a non-IP-based technology.

Because of its long range (up to 20km) and low power, it is suitable for low data rate, outdoors solutions.

<!--what's the infrastructure?-->

The [LoRa](lora-tech.html) section and [LoRa tutorial](../tutorials/LoRa-tutorial.html) describe LoRA networking.


#### NFC

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/n_mark.png)<span>NFC</span></span>

Near-field communication (NFC) is a short range (few centimeters) wireless technology standard for personal area networks. Typical uses of NFC are commissioning, easy sharing of small content and Bluetooth connection initiation/out-of-band pairing.

To learn how to use NFC with Mbed OS, please refer to the [NFC](../apis/nfc.html) user API reference.

#### Memory needs for Pelion-connected devices

Mbed OS's baseline memory footprint, without Pelion connectivity, is 2.8kb of RAM and 8.2kb of flash. When you add connectivity and full functionality, the footprint grows:

* For **Device Management Client Lite**, the smaller of the two connectivity libraries: a total of 20kb RAM, 210kb flash. This includes not just Ethernet connectivity, but also startup and runtime demands, the size of Client Lite itself and additional drivers. <!--which drivers?-->
* For **Device Management Client**: a total of 137kb RAM, 330kb flash. This adds FileSystem and the full Client to the functionality.

These two connectivity libraries give you the choice of a range of devices. Mbed OS with Client Lite can work on devices with only 64kb RAM and 256kb flash. Mbed OS with the full Client fits comfortably on devices with 128kb RAM and 1024kb flash.

#### Security

<!--Something about how we secure independently of the protocol, but are some methods still more secure than others?-->
