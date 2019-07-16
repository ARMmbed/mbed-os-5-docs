# Firmware update in Mbed OS

Mbed OS integrates Pelion Device Management firmware update services, so if you have a Device Management account, you can send binaries to your remote device.

Mbed OS now includes the boot loader that manages update verification and installation.

Mbed CLI and the Mbed Online Compiler now support update actions using the Update Service API and manifest tool. We have a quick start guide [for updating through the Online Compiler](https://cloud.mbed.com/guides/pelion-firmware-update), and a review [of the Mbed CLI flow and commands](../tools/cli-update.html).

## Updatable binaries

The active firmware, made up of Mbed OS and an application, can be updated only if the binary installed on the device has:

1. A bootloader, as [reviewed below](#the-mbed-os-bootloader). The boot loader can load a new version of the firmware. As a security feature, the default behavior of the boot loader is to refuse to roll back to old firmware versions once an update succeeds.
1. Mbed OS with Device Management Client (which includes the Update client). The clients allow your device to communicate with the Device Management Update service, receive update manifests and firmware, and verify the binary's validity. They are [reviewed in details in our Pelion Device Management documentation](https://www.pelion.com/docs/device-management/current/updating-firmware/index.html).

<span class="notes">**Note:** Because some embedded devices don't require remote update capabilities, Mbed OS does not include the Device Management Client by default. You must explicitly import the client to your application.</span>

1. Permission to access your Device Management account, as well as keys and certificates to verify the firmware's source and validity.

## The Mbed OS bootloader

During system startup, a boot loader is responsible for selecting and forwarding control to the next stage in the boot sequence. The Mbed OS boot loader also validates the next stage's sanity and signature before forwarding control to it; if validation fails, the boot loader can select an alternate version of the next stage. It can also install an alternative upon request (in other words, firmware update).
>This is much more detail than the DM boot loader docs go into. Who wants to own it? I'd say it makes more sense to store it in the DM docs, and link out. Is the boot loader related to anything besides Update client?

### Background: boot sequences and fault tolerance

A boot sequence can have several stages of bootloaders, leading to an application. The different stages (including the application) may need to evolve over time, to add features or bug-fixes. Upgrades are possible for boot sequences with two or more stages: any active stage can replace the next stage in the sequence; when the system restarts, it executes the updated components. Typically, however, the very first stage isn't replaced; because it takes control on startup, a faulty upgrade of this stage can make recovery impossible. This is known as stage 0 bootloader.

To protect against faults in the newly updated components, we store multiple versions (up to a certain maximum number of versions). <!---What is that number?---> Each stage is responsible for detecting faults in the following component and rolling it back if it discovers faults. For example, if the third stage is unstable, needs additional functionality or is otherwise behaving incorrectly, the second stage (during the *next* startup sequence) can roll the third stage back to an earlier version before handing over control. This results in a boot sequence tree that is traversed in a depth-first order as the system recovers from successive faults.

>That is traversed?

Most boot sequences are composed of three stages:

1. Boot selector (also known as **root bootloader** or **stage zero bootloader**): does not get upgraded.
1. Bootloader: upgradable, with several versions stored on the device.
1. Application: upgradable, with several versions stored on the device.

Fault tolerance ultimately rests on the sanity of the first-stage bootloader. This boot loader is usually kept minimal to ensure dependable operation.

The Mbed OS boot loader is a hybrid of the boot selector and a bootloader, but it fulfills the requirements of the boot selector: It is small enough to minimize the chance of bugs, but advanced enough to install new images.

### Managed and unmanaged boot loader tool integration

Mbed tools (Mbed CLI, Online Compiler) can manage bootloaders where:

- The boot loader comes before the application in ROM.
- The application starts immediately after the bootloader.

If the Mbed tool finds a manageable bootloader, the image build process automatically merges the boot loader image with the application image.
>We say managed and manageable--which one should we go with?

If your boot loader does not meet the two requirements of a manageable bootloader, you will need an unmanaged bootloader. The Mbed tools do not automatically combine this boot loader with the application image; you need to write your own scripts to build your full image.

For more information about [managed and unmanaged bootloaders, and how to create bootloaders, see the tutorial](../tutorials/bootloader.html).

### Porting a bootloader

If you're interested in porting the Update client and boot loader to new hardware, please [review the porting section](https://www.pelion.com/docs/device-management/current/porting/porting-the-device-management-update-client.html).
>Can this link just point to the DM-side porting docs?

### Security

Keep in mind that the Mbed OS bootloader:

* Does not process encrypted off-chip candidate images.
* Does not currently verify signatures of candidate images. To save code size and speed up boot time, we use a unique, per-device Message Authentication Code (MAC) to authenticate the firmware in the bootloader: firmware is distributed with a signature, and the Update client verifies the signature and replaces it with a MAC that the boot loader understands.

This means that the default boot loader does not implement secure boot; for high-security applications, further implementation is required. Please see [the full boot loader documentation](https://cloud.mbed.com/docs/latest/updating-firmware/bootloaders.html) and the [porting section](https://cloud.mbed.com/docs/latest/porting/porting-the-device-management-update-client.html) on the Pelion Device Management site.

## Managing updates with the bootloader

<!---this should go in the information on DM bootloader--->

When a device downloads new firmware, it stores it locally (in the storage area) and reboots. The boot loader then:

1. Checks the integrity of the active firmware by calculating the hash of the active image and comparing it to the one in the metadata header (the boot loader metadata header is explained below).
1. Looks for available firmware on the system. There may be more than one image, depending on image sizes.
1. Chooses the firmware with the latest timestamp.
1. Checks the integrity of the image in the storage area by checking its hash against its internal metadata header.
1. Copies the image in the storage area to the active application region if it is applicable.
1. Forwards control to the start of the active firmware, which contains the Update client (part of Device Management Client). The Update client runs the Pelion Device Management update process:
    1. Receives a notification from one of its update sources.
    1. Downloads the new manifest and parses it to obtain the firmware URI.
    1. Fetches the firmware from one of its update sources. Either the manifest or a cost-ranking algorithm specifies the update source to use.
    1. Writes the firmware into the storage region on the SD card (or external SPI Flash), as a candidate firmware image.
    1. Reboots, handing control back to the bootloader.

## Development tool integration with Device Management Update

Mbed CLI and the Online Compiler implement the Device Management Update service by directly using the service APIs and the manifest tool. For a device running an updatable application, using Mbed CLI and the Online Compiler's built-in update features can reduce the steps needed to run an update campaign.

<span class="notes">**Note**: The development tool workflow is intended only for development and testing purposes. It is not secure for production.</span>

Your development tool needs to use your Device Management account API key to call the APIs. Once it has access to the APIs, it can generate a manifest, upload the manifest and binary to the server, and deliver the manifest to a device or group of devices. For more information, see [the update API documentation](https://cloud.mbed.com/docs/latest/service-api-references/update-service.html).

<span class="notes">**Note**: The tools currently support the update flow for Device Management Client, not Device Management Client Lite.</span>

**Tutorials**:

- Follow the Quick Connect guide, if you hvaen't already, to set up the original application]     (https://cloud.mbed.com/guides/connect-device-to-pelion).
  - Then try the firmware [update flow on the Online Compiler](https://cloud.mbed.com/guides/pelion-firmware-update). 
- Review the [Mbed CLI update commands](../tools/cli-update.html).
