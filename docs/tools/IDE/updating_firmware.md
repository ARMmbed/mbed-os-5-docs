<h1 id="ide-update">Updating devices</h1>

The Online Compiler integrates with Pelion Device Management's remote firmware update services.

<span class="tips">**Tip**: The fastest way to learn about firmware updates in the Online Compiler is to try the [Quick Connect guide](https://cloud.mbed.com/guides/connect-device-to-pelion) to create the original application, and the [Quick Update guide](https://cloud.mbed.com/guides/pelion-firmware-update) to perform a firmware update.</span>

<span class="notes">You need a [Pelion Device Management](https://portal.mbedcloud.com/login) account to use the update workflow.</span>

## Creating an application you can update

To be able to receive updates, an application must have:

- A **connect certificate** to access a Pelion Device Management account. When you run the application on your device, the bootstrap server will use this connect certificate to authenticate your application with your Pelion Device Management account.
- An **update certificate** to verify that incoming updates come from a trusted source.
- A **bootloader** to verify and install update images.
- The Device Management Client, [normally imported as part of the example application](https://github.com/ARMmbed/mbed-cloud-client-example). You can also import it using the [Quick Connect guide we mentioned above](https://cloud.mbed.com/guides/connect-device-to-pelion).

You need:

- A **private key** so you can sign the firmware update manifest file.
- A **manifest file**, which defines the update, including the location of the new firmware image and the type of device the update applies to. The manifest file is signed with the private key to assure the device that the image is from a trusted source and has not been tampered with.

For development use cases only, you can use the Online Compiler to generate the certificates and the manifest file. For production use cases, you would use offline tools to generate and store them securely. Learn more [about the developer workflow below](#notes-about-the-developer-workflow).

## Creating an update image

Once the initial, updatable application is on the device, the device is considered updatable. Subsequent images do not include the certificates, keys and bootloader of the original application; they contain only the application code. These images can be sent to the device without a physical connection, using Device Management Update.

## Actions in the Online Compiler

In the **Pelion Device Management** dropdown menu, you can:

- Create the initial application:

   - **Manage Connect Certificates**: create a developer connect certificate, and see existing ones. Note: this process uses your Device Management API key. If the key is not found, you will be prompted to enter it manually. You can create an API key in the [Pelion Device Management portal](https://portal.mbedcloud.com/access/keys).
   - **Apply Update Certificate**: create an update certificate and generate a private key for manifest signing. Note: you need to download the private key and store it securely.

   When you build your application, the Online Compiler will combine the bootloader with your certificates and your application code.

- Create an update image:

   - **Publish Firmware Update**: build your program and upload it to your Pelion Device Management account so you can use it as a firmware update. This build does not include the certificates or the bootloader.

   This stage also creates a manifest for the update, and will ask for your private key to sign the manifest.

## Notes about the developer workflow

The Device Management workflow in the Online Compiler is intended only for development devices; it does not support production requirements:

- The Online Compiler uses web crypto to generate the update public certificate and private key and is not available in Internet Explorer or Microsoft Edge.
- The developer update certificate and key are not suitable for production use cases.
- The developer connect certificate file contains multiple certificates and a private key. It is not suitable for production and you must keep it safe so as not to expose the private key.
