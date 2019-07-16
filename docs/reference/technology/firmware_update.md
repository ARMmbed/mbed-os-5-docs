# Firmware update in Mbed OS

Mbed OS integrates Pelion Device Management firmware update services, so if you have a Device Management account, you can send binaries to your remote device.

Mbed OS now includes the boot loader that manages update verification and installation.

Mbed CLI and the Mbed Online Compiler now support update actions using the Update Service API and manifest tool. We have a quick start guide [for updating through the Online Compiler](https://cloud.mbed.com/guides/pelion-firmware-update), and a review [of the Mbed CLI flow and commands](../tools/cli-update.html).

## Updatable binaries

The active firmware, made up of Mbed OS and an application, can be updated only if the binary installed on the device has:

1. A boot loader, as [reviewed below](#the-mbed-os-bootloader). The boot loader can load a new version of the firmware. As a security feature, the default behavior of the boot loader is to refuse to roll back to old firmware versions once an update succeeds.
1. Mbed OS with Device Management Client (which includes the Update client). The clients allow your device to communicate with the Device Management Update service, receive update manifests and firmware, and verify the binary's validity. They are [reviewed in details in our Pelion Device Management documentation](https://www.pelion.com/docs/device-management/current/updating-firmware/index.html).

<span class="notes">**Note:** Because some embedded devices don't require remote update capabilities, Mbed OS does not include the Device Management Client by default. You must explicitly import the client to your application.</span>

1. Permission to access your Device Management account, as well as keys and certificates to verify the firmware's source and validity.

## The Mbed OS boot loader

During system startup, a boot loader is responsible for selecting and forwarding control to the next stage in the boot sequence. The Mbed OS boot loader also validates the next stage's sanity and signature before forwarding control to it; if validation fails, the boot loader can select an alternate version of the next stage. It can also install an alternative upon request (in other words, firmware update).

### Background: boot sequences and fault tolerance

A boot sequence can have several stages of boot loaders, leading to an application. The different stages (including the application) may need to evolve over time, to add features or bug-fixes. Upgrades are possible for boot sequences with two or more stages: any active stage can replace the next stage in the sequence; when the system restarts, it executes the updated components. Typically, however, the very first stage isn't replaced; because it takes control on startup, a faulty upgrade of this stage can make recovery impossible. This is known as stage 0 boot loader.

To protect against faults in the newly updated components, we store multiple versions (up to a certain maximum number of versions). Each stage is responsible for detecting faults in the following component and rolling it back if it discovers faults. For example, if the third stage is unstable, needs additional functionality or is otherwise behaving incorrectly, the second stage (during the *next* startup sequence) can roll the third stage back to an earlier version before handing over control. This results in a boot sequence tree traversed depth-first as the system recovers from successive faults.

Most boot sequences are composed of three stages:

1. Boot selector (also known as **root boot loader** or **stage zero boot loader**): does not get upgraded.
1. Boot loader: upgradable, with several versions stored on the device.
1. Application: upgradable, with several versions stored on the device.

Fault tolerance ultimately rests on the sanity of the first-stage boot loader. This boot loader is usually kept minimal to ensure dependable operation.

The Mbed OS boot loader is a hybrid of the boot selector and a boot loader, but it fulfills the requirements of the boot selector: It is small enough to minimize the chance of bugs, but advanced enough to install new images.

### Managed and unmanaged boot loader tool integration

Mbed tools (Mbed CLI, Online Compiler) can manage boot loaders where:

- The boot loader comes before the application in ROM.
- The application starts immediately after the boot loader.

If the Mbed tool finds a managed boot loader, the image build process automatically merges the boot loader image with the application image.

If your boot loader does not meet the two requirements of a manageable boot loader, you will need an unmanaged boot loader. The Mbed tools do not automatically combine this boot loader with the application image; you need to write your own scripts to build your full image.

For more information about [managed and unmanaged boot loaders, and how to create boot loaders, see the tutorial](../tutorials/bootloader.html).

### Porting a boot loader

If you're interested in porting the Update client and boot loader to new hardware, please [review the porting section](https://www.pelion.com/docs/device-management/current/porting/porting-the-device-management-update-client.html).
>Can this link just point to the DM-side porting docs?

### Security

Keep in mind that the Mbed OS boot loader:

* Does not process encrypted off-chip candidate images.
* Does not currently verify signatures of candidate images. To save code size and speed up boot time, we use a unique, per-device Message Authentication Code (MAC) to authenticate the firmware in the boot loader: firmware is distributed with a signature, and the Update client verifies the signature and replaces it with a MAC that the boot loader understands.

This means that the default boot loader does not implement secure boot; for high-security applications, further implementation is required. Please see [the full boot loader documentation](https://cloud.mbed.com/docs/latest/updating-firmware/bootloaders.html) and the [porting section](https://cloud.mbed.com/docs/latest/porting/porting-the-device-management-update-client.html) on the Device Management site.

## Development tool integration with Device Management Update

Mbed CLI and the Online Compiler implement the Device Management Update service by directly using the service APIs and the manifest tool. For a device running an updatable application, using Mbed CLI and the Online Compiler's built-in update features can reduce the steps needed to run an update campaign.

<span class="notes">**Note**: The development tool workflow is intended only for development and testing purposes. It is not secure for production.</span>

Your development tool needs to use your Device Management account API key to call the APIs. Once it has access to the APIs, it can generate a manifest, upload the manifest and binary to the server, and deliver the manifest to a device or group of devices. For more information, see [the update API documentation](https://cloud.mbed.com/docs/latest/service-api-references/update-service.html).

<span class="notes">**Note**: The tools currently support the update flow for Device Management Client, not Device Management Client Lite.</span>

**Tutorials**:

- Follow the Quick Connect guide, if you haven't already, to set up the original application](https://cloud.mbed.com/guides/connect-device-to-pelion).
  - Once your device is connected, try the firmware [update flow on the Online Compiler](https://cloud.mbed.com/guides/pelion-firmware-update). 
- Review the [Mbed CLI update commands](../tools/cli-update.html).
