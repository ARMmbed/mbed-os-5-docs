# Firmware update in Mbed OS

Mbed OS integrates Pelion Device Management Update services, so if you have a Device Management account, you can send firmware images to your devices remotely.

Mbed OS includes a bootloader that manages update verification and installation for Device Management Client.

Mbed CLI and the Mbed Online Compiler support update actions using the Update Service API and manifest tool. We have a quick start guide [for updating through the Online Compiler](https://os.mbed.com/guides/pelion-firmware-update), and a review [of the Mbed CLI flow and commands](../tools/cli-update.html).

## Updatable binaries

An updatable binary includes:

- The user application.
- A bootloader, as [explained below](#the-pelion-bootloader). The bootloader can load a new version of the firmware. As a security feature, the default behavior of the bootloader is to refuse to roll back to old firmware versions after an update succeeds.
- Mbed OS or another operating system.
- Device Management Client (which includes the Update client). The client allows your device to communicate with the Update service, receive update manifests and firmware and verify firmware validity. Please see our [Device Management documentation](https://www.pelion.com/docs/device-management/latest/updating-firmware/index.html) for more details.

  <span class="notes">**Note:** Because some embedded devices don't require remote update capabilities, Mbed OS does not include Device Management Client by default. You must explicitly import the client to your application.</span>

- Permission to access your Device Management account, as well as keys and certificates to verify the firmware source and validity.

## The Pelion bootloader

During system startup, a [bootloader](https://www.pelion.com/docs/device-management/latest/updating-firmware/bootloaders.html) is responsible for selecting and forwarding control to the next stage in the boot sequence. The Pelion bootloader validates the next stage's sanity and signature before forwarding control to it; if validation fails, the bootloader can select an alternate version of the next stage. It can also install an alternative upon request (in other words, firmware update).

### Porting a bootloader

If you're interested in porting the Update client and bootloader to new hardware, please [review the porting section](https://www.pelion.com/docs/device-management/latest/porting/porting-the-device-management-update-client.html).

### Security

Keep in mind that the Pelion bootloader:

- Does not process encrypted off-chip candidate images.
- Does not currently verify signatures of candidate images. To save code size and speed up boot time, we use a unique, per-device Message Authentication Code (MAC) to authenticate the firmware in the bootloader: firmware is distributed with a signature, and the Update client verifies the signature and replaces it with a MAC that the bootloader understands.

This means that the default bootloader does not implement secure boot; for high-security applications, further implementation is required. Please see [the full bootloader documentation](https://www.pelion.com/docs/device-management/latest/updating-firmware/bootloaders.html) and the [porting section](https://www.pelion.com/docs/device-management/current/porting/porting-the-device-management-update-client.html) on the Device Management site.

## Development tool integration with Device Management Update

Mbed CLI and the Online Compiler implement the Device Management Update service by directly using the service APIs and the manifest tool. For a device running an updatable application, using Mbed CLI and the Online Compiler's built-in update features can reduce the steps needed to run an update campaign.

<span class="notes">**Note**: The development tool workflow is intended only for development and testing purposes. It is not secure for production.</span>

Your development tool needs to use your Device Management account API key to call the APIs. After it has access to the APIs, it can generate a manifest, upload the manifest and binary to the server and deliver the manifest to a device or group of devices. For more information, see [the update API documentation](https://cloud.mbed.com/docs/latest/service-api-references/update-service.html).

<span class="notes">**Note**: The tools currently support the update flow for Device Management Client, not Device Management Client Lite.</span>

**Tutorials**:

- Follow the [Quick Connect guide](https://os.mbed.com/guides/connect-device-to-pelion/) to set up the original application.
  - After your device is connected, try the firmware [update flow on the Online Compiler](https://os.mbed.com/guides/pelion-firmware-update).
- Review the [Mbed CLI update commands](../tools/cli-update.html).
