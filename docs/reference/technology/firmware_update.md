## Firmware update in Mbed OS

Mbed OS integrates the Pelion Device Management firmware update services, so if you have a Device Management account, you can send binaries to your remote device. The binary includes your full application and Mbed OS code, so you can update one or both of them.

Update support in Mbed OS relies on two modifications:

* Mbed OS now includes the bootloader that manages update verification and installation.
* Mbed CLI and the Mbed Online Compiler now support update actions, by wrapping around the Update Service and the Manifest Tool.<!--All of these will need links. Later.-->

### Updatable binaries

Mbed OS and any application running on top of it can be updated only if the binary installed on the device has:

1. A bootloader, as [reviewed below](#the-mbed-os-bootloader). The bootloader can load a new version of the firmware, or roll back to an old version if the new version is unstable.
1. Mbed OS with the Device Management Client (which includes the Update client). The clients allow your device to communicate with the Device Management Update service, receive update manifests and firmware, and verify the binary's validity. They are [reviewed in details in our Pelion Device Management documentation](https://cloud.mbed.com/docs/current/updating-firmware/index.html).

    Note: since some embedded devices don't require remote update capabilities, Mbed OS does not include the Device Management Client by default; you will need to explicitly import the client to your application.

1. Permission to access your Device Management account, as well as keys and certificates used to verify the firmware's source and validity.

### The Mbed OS bootloader

A bootloader is an intermediate stage during system startup responsible for selecting and forwarding control to the next stage in the boot sequence based on validation. Optionally, a bootloader can also install an alternate version of the next stage upon request (firmware update, for example) or when detecting a persistent failure in the next stage.

#### Background: boot sequences and fault tolerance

A boot sequence can have several stages of bootloaders, leading to an application. The different stages (including the application) may need to evolve over time, to add features or bug-fixes. Upgrades are possible for boot sequences with two or more stages: any active stage can replace the next stage in the sequence; when the system restarts, behaviour changes. Typically, however, the very first stage isn't replaced; because it takes control on startup, a faulty upgrade of this stage can make recovery impossible.

To protect against faults in the newly installed component, replaced components should be <!--why "should be"? do we or don't we save them?-->saved (up to a certain maximum number of versions). Recovery then relies on a stage being aware of the faulty state of the following stage, and rolling it back. For example, if stage 3 is unstable, needs additional functionality or is otherwise behaving incorrectly, stage 2 (during the *next* startup sequence) can roll stage 3 back to an earlier version before handing over control. This results in a boot-sequence tree that is traversed in a depth-first order as the system recovers from successive faults.

Most boot sequences are composed of only three stages:<!--And for Mbed OS?-->

1. Boot selector (also known as **root bootloader** or **boot selector**): does not get upgraded.
1. Bootloader: upgradable, with several versions stored on the device.
1. Application: upgradable, with several versions stored on the device.

Fault tolerance ultimately rests on the sanity of the first-stage bootloader. This bootloader is usually kept minimal to ensure dependable operation.<!--So what does Mbed OS do? Also, "minimal" is vague. What does it actually mean - that its functionality is limited to starting the sequence?-->

The Mbed bootloader is practically<!--as in "we did it because it's practical" or "you know, this basically is that"?--> a hybrid of the boot selector and a bootloader, but it fulfils the requirements of the boot selector: it is small enough to minimise the chance of bugs, but it is complex enough to handle installation of new images.<!---"Handle the installation" or just "install"? Is it an overseer, or does it do the work?--> <!--Therefore, the Mbed Bootloader is intended to be a reference implementation for constructing a bootloader.--><!--Not relevant for the Mbed OS one, right???-->


#### Managed bootloader tool integration


The Mbed tools (Mbed CLI, Online Compiler) can manage bootloaders where:

* The bootloader comes before the application in ROM.
* The application starts immediately after the bootloader.

If the Mbed tool finds a manageable bootloader, the image build process automatically merges the bootloader image with the application image.

#### Unmanaged bootloaders

If your bootloader does not meet the two requirements of a manageable bootloader, you will need an unmanaged bootloader. The Mbed tools will not automatically combine this bootloader with the application image; you will need to write your own scripts to build your full image.

#### Creating a bootloader

We have a full tutorial [for creating a bootloader](/docs/v5.10/tutorials/bootloader.html).

#### Porting a bootloader

If you're interested in porting the Update client and bootloader to new hardware, please [review the porting section](/docs/v5.10/porting/bootloader.html).

#### Security

Note two things about the Mbed OS bootloader's design:

1. It does not process encrypted off-chip candidate images.
1. It does not currently verify signatures of candidate images. To save code size and speed up boot time, we use a unique, per-device Message Authentication Code (MAC) to authenticate the firmware in the bootloader: firmware is distributed with a signature, and the Update client verifies the signature and replaces it with a MAC that the bootloader understands.

This means that the default bootloader does not implement secure boot; for high-security applications, further implementation is required. Please see [the full bootloader documentation](https://cloud.mbed.com/docs/current/updating-firmware/bootloaders.html) and the [porting section](https://cloud.mbed.com/docs/current/porting/porting-the-device-management-update-client.html) on the Pelion Device Management site.

<!--I don't think Product is going to like me calling this out.-->

### Managing updates with the bootloader

When a device downloads new firmware, it stores it locally (in the storage area) and reboots; the device's bootloader then:

1. Takes over after reboot.
1. Checks the integrity of the active firmware by calculating the hash of the active image and comparing it to the one in the metadata header (the bootloader metadata header is explained below).
1. Looks for available firmware on the system. There may be more than one image, depending on image sizes.
1. Chooses the firmware with the latest timestamp.
1. Checks the integrity of the image in the storage area by checking its hash against its internal metadata header.
1. Copies the image in the storage area to the active application region if it is applicable.
1. Forwards control to the start of the active firmware, which contains the Update client (part of Device Management client). The Update client runs the Pelion Device Management update process:
    1. Receives a notification from one of its update sources.
    1. Downloads the new manifest and parses it to obtain the firmware URI.
    1. Fetches the firmware from one of its update sources. Either the manifest or a cost-ranking algorithm specifies the update source to use.
    1. Writes the firmware into the storage region on the SD card (or external SPI Flash), as a candidate firmware image.
    1. Reboots, handing control back to the bootloader.


### Development pool integration with Pelion Device Management Update

Mbed CLI and the Online Compiler offer a wrap around the Pelion Device Management Update service and the manifest tool. For a device running an updatable application, this means an abstraction of many of the steps of setting up an update campaign.

<!--How secure is this? Is it only for development devices, or can I use this for deployment?-->

Your development tool needs to use your Device Management account's API key to call the Pelion Device Management APIs. Once it has access to the APIs, it can generate a manifest, upload the manifest and binary to the server, and deliver the manifest to a device or group of devices. For more information, see [the update API documentation](https://cloud.mbed.com/docs/current/service-api-references/update-service.html).
<!--Do we actually use one of the SDKs? Python, maybe? If so, link to https://cloud.mbed.com/docs/current/mbed-cloud-sdk-python/update.html-->

<!--Technically there are difference between CLI and IDE, and between a single device and device group flow. But I think that's something the tools should cover, not this section-->

<span class="notes">**Note**: The tools currently support the update flow for Device Management Client, not Device Management Client Lite.</span>

**Tutorials**:

* Try the firmware update flow on the Online Compiler.<!--No link yet; it's not live-->
* Review the [Mbed CLI update commands](https://os.mbed.com/docs/v5.10/tools/cli-update.html).
