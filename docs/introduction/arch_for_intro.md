# Architecture

This is the basic architecture of an Mbed board running Mbed OS:

<span class="images">![](../images/Mbed_OS_diagram_for_intro.png)</span>

## Mbed OS foundations

Mbed OS uses a hardware abstraction layer (HAL) to support the most common parts of a microcontroller, such as timers. This foundation facilitates writing applications against a common set of application programming interfaces (APIs); your device automatically includes necessary libraries and driver support for standard MCU peripherals, such as I2C, Bus and SPI.

The HAL also serves as the starting point when adding support for new targets or features to existing targets. We work closely with our silicon Partners to port these new features to Mbed Enabled development boards.

The structure of Mbed OS enables matching applications and storage systems. In other words, where the block level storage options vary and are application dependent, you can choose the file system that best fits your IoT device. The FAT file system - backed by an SD card - provides compatibility with other operating systems, such as Windows, Mac OS or Linux. When high reliability and recovery from power failure are important, it makes sense to use our embedded file system, backed with a (Q)SPI NOR flash chip.

Finally, Mbed OS implements the retargeting layer and boot process integration of each supported toolchain for you, so application development feels similar to C or C++ development for any other operating system.

## Connectivity

Arm works with its Partners to enable Bluetooth Low Energy, NFC, RFID, <!--LoRa?-->, 6LoWPAN-ND, Thread, Wi-SUN, Ethernet, Wi-Fi, cellular and mobile IoT (LPWA) across devices and system architectures running Mbed OS. Mbed OS offers a stable core of existing connectivity technologies. At the same time, it adds modern ones in quarterly feature releases, keeping you informed of industry trends so you can transition to new, innovative solutions that generate business value.

The networking and connectivity stacks are flexible enough to meet the needs of the most demanding IoT device designs, whether a combination of a single chip microcontroller and radio, or multiple chips connected across serial buses. System designers can have confidence in our certified connectivity stacks, such as our certified Thread stack, because of their maturity, interoperability and validated components.

## Security

The Pelion IoT Platform has built-in security at all levels, stressing both protection against violations and mitigation of their consequences. Alongside hardened cloud services, robust communication stacks and safe firmware updates, Mbed offers two security-specific embedded building blocks: [Arm Mbed TLS](https://www.mbed.com/en/technologies/security/mbed-tls/) and a Secure Partition Manager (SPM) that meets industry best practices as part of Arm’s Platform Security Architecture. Mbed TLS secures communication channels between a device and gateway or server, and the use of a secure partition manager and isolated security domains for trusted system services reduces the attack surface. All together, this provides a unique chip-to-cloud security model, relying on the low-level capabilities the Arm ecosystem silicon Partners provide to secure the data and identity of cloud-connected devices.

Our approach to security is to leverage state-of-the-art industry standard protocols, ciphers and encryption suites following the recommendations from NIST and other related organizations. This gives us access to the latest work by the global security research community, rather than a limited in-house resource.  We regularly verify the results of these efforts with code reviews, penetration exercises and other methods.
