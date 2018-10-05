## Firmware update in Mbed OS

Mbed OS integrates the Pelion Device Management firmware update services, so if you have a Device Management account, you can send binaries to your remote device. The binary includes your full application and Mbed OS code, so you can update one or both of them.

Update support in Mbed OS relies on two modifications:

* Mbed OS now includes the bootloader that manages update verification and installation.
* Mbed CLI and the Mbed Online Compiler now support update actions, by wrapping around the Update Service and the Manifest Tool.<!--All of these will need links. Later.-->


<!--This doesn't mean you don't need to explicitly include Device Management Client, by the way. DMC includes the update client.-->
### Background: the Mbed OS bootloader

A bootloader is an intermediate stage during system startup responsible for selecting and forwarding control to the 'next stage' in the boot sequence based on validation. Optionally, a bootloader can also install an alternate version of the next stage upon request (firmware update, for example) or when detecting a persistent failure in the next stage.

Boot sequences usually have only three stages:

1. **Boot selector (or root bootloader)**: usually kept minimal to ensure dependable operation, and does not get updated (since there is no way to remotely recover from updating to a faulty boot selector).
1. **Bootloader**: a device can store multiple versions. The boot selector will attempt to hand control to the newest bootloader. If that bootloader is not stable or does not operate at all, the boot selector will hand control to an older version. This protects the device from being bricked by a faulty bootloader.
1. **Application**: follows the exact same logic as the bootloader.

To allow remote updates, Mbed OS now has a built-in bootloader that meets the following requirements:

* A minimal feature set, to increase the likelihood of correct operation.
* Chaining: Each stage of the boot sequence (except the boot selector) uses a metadata header to expose data such as its version, size and hash. Each stage use's the *next* stage's header to verify that stage's integrity before forwarding control. Specifically, the firmware version metadata orders the firmware, so each boot stage can select the best among the next stage's available versions.

    An example of the header:<!--Is that the Mbed OS structure?-->

    ```
    typedef struct FirmwareHeader {
        uint32_t magic;                         /** Metadata-header specific magic code */
        uint32_t version;                       /** Revision number for this generic metadata header. */
        uint32_t checksum;                      /** A checksum of this header. This field should be considered to be zeroed out for
                                                 *  the sake of computing the checksum. */
        uint32_t totalSize;                     /** Total space (in bytes) occupied by the firmware BLOB, including headers and any padding. */
        uint64_t firmwareVersion;               /** Version number for the accompanying firmware. Larger numbers imply more preferred (recent)
                                                 *  versions. This defines the selection order when multiple versions are available. */
        uint8_t  firmwareSHA256[SIZEOF_SHA256]; /** A SHA-2 using a block-size of 256-bits of the firmware, including any firmware-padding. */
    } FirmwareHeader_t;
    ```
* A bootloader can change its behaviour based on where in the bootloader chain it is called. That means a bootloader can be reused in different ways in different systems, depending on its index position (where the boot selector is always 0, and each subsequent bootloader is an increasing index number). The bootloader therefore needs to receive its index as a dynamic parameter when receiving control from the previous stage, for example from a reserved space in SRAM. <!--But what mechanism does Mbed OS use?-->
*

Because Mbed OS runs on M-class devices, there was an additional requirement: not to use virtual memory to manage different offset addresses. In Mbed OS, there, software always executes from the same offset; the bootloader copies the candidate image into the active image slot on startup. This makes the bootloader more complex, but it also allows for off-chip image storage, making larger images possible.

### Using the bootloader to manage updates

Mbed OS uses the bootloader to manage firmware updates. The bootloader:

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


### Security

### Tool integration

#### Mbed CLI
Mbed CLI
<!--Don't need the manifest tool, don't need to access the portal if I'm only updating one device-->
<!--ship a bin file to a server, pull down a developer certificate (not update????) and call the manifest tool-->

#### The Online Compiler
