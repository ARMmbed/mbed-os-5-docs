## Firmware update in Mbed OS

Mbed OS integrates the Pelion Device Management firmware update services, so if you have a Device Management account, you can send binaries to your remote device. The binary includes your full application and Mbed OS code, so you can update one or both of them.

Update support in Mbed OS relies on two modifications:

* Mbed OS now includes the bootloader that manages update verification and installation.
* Mbed CLI and the Mbed Online Compiler now support update actions, by wrapping around the Update Service and the Manifest Tool.<!--All of these will need links. Later.-->

<span class="tips">Since some embedded devices don't require remote update capabilities, Mbed OS does not include the Device Management Client by default. You will need to explicitly import the client to your application; this then includes the Update client, which manages firmware updates on the device.</span>

### The Mbed OS bootloader

A bootloader is an intermediate stage during system startup responsible for selecting and forwarding control to the next stage in the boot sequence based on validation. Optionally, a bootloader can also install an alternate version of the next stage upon request (firmware update, for example) or when detecting a persistent failure in the next stage.

A boot sequence can have several stages of bootloaders, leading to an application. The different stages (including the application) may need to evolve over time, to add features or bug-fixes. Upgrades are possible for boot sequences with two or more stages: any active stage can replace the next stage in the sequence; when the system restarts, behaviour changes. Typically, however, the very first stage isn't replaced; because it takes control on startup, a faulty upgrade of this stage can make recovery impossible.

To protect against faults in the newly installed component, replaced components should be <!--why "should be"? do we or don't we save them?-->saved (up to a certain maximum number of versions). Recovery then relies on a stage being aware of the faulty state of the following stage, and rolling it back. For example, if stage 3 is unstable, needs additional functionality or is otherwise behaving incorrectly, stage 2 (during the *next* startup sequence) can roll stage 3 back to an earlier version before handing over control. This results in a boot-sequence tree that is traversed in a depth-first order as the system recovers from successive faults.

Fault tolerance ultimately rests on the sanity of the first-stage bootloader (also referred to in this document as the **root bootloader** or the **boot selector**). This bootloader is usually kept minimal to ensure dependable operation.<!--So what does Mbed OS do? Also, "minimal" is vague. What does it actually mean - that its functionality is limited to starting the sequence?-->

Most boot sequences are usually composed of only three stages:<!--And for Mbed OS?-->

1. Boot selector: does not change.
1. Bootloader: upgradable, with several versions stored on the device.
1. Application: upgradable, with several versions stored on the device.

The Mbed bootloader is practically<!--as in "we did it because it's practical" or "you know, this basically is that"?--> a hybrid of the boot selector and a bootloader, but it fulfils the requirements of the boot selector: it is small enough to minimise the chance of bugs, but it is complex enough to handle installation of new images.<!---"Handle the installation" or just "install"? Is it an overseer, or does it do the work?--> <!--Therefore, the Mbed Bootloader is intended to be a reference implementation for constructing a bootloader.--><!--Not relevant for the Mbed OS one, right???-->



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

### Requirements and layout

The Mbed bootloader has three major requirements:

1. An external storage driver.
1. An internal storage driver.
1. A cryptographic engine.

The bootloader expects to have the following flash layout (if SOTP is used to provide the RoT):

```text
    +--------------------------+
    |                          |
    |                          |
    |                          |
    +--------------------------+
    |                          |
    |                          |
    |                          |
    |        Active App        |
    |                          |
    |                          |
    |                          |
    +--------------------------+ <-+ application-start-address
    |                          |
    |Active App Metadata Header|
    |                          |
    +--------------------------+ <-+ update-client.application-details
    |          SOTP_2          |
    +--------------------------+ <-+ sotp-section-2-address
    |          SOTP_1          |
    +--------------------------+ <-+ sotp-section-1-address
    |                          |
    |        Bootloader        |
    |                          |
    |                          |
    +--------------------------+ <-+ 0
```

### Security

Note two things about the bootloader's design:

1. It does not process encrypted off-chip candidate images.
1. It does not verify signatures of candidate images. This means that Mbed Bootloader does not implement secure boot.

This means that for high-security applications, further implementation is required. Please see [the full bootloader documentation on the Pelion Device Managment site]().

<!--
It means that it doesn’t do secure boot or encrypted off-chip storage and that’s a showstopper in many applications.
There’s no way to reliably lock the boot loader on most of these devices so secure boot doesn’t gain you much
If those things weren’t true, I would have yelled and screamed when they tried to ship it
We also aren’t encrypting firmware delivery yet

So encrypting it in storage gives very marginal security gains

However, transport encryption is a feature that can be added later whereas encrypted off-chip storage can’t because the bootloader isn’t upgradeable
The update client verified the signature. The update client then makes a Message Authentication Code for the firmware. The boot loader verifies that Message Authentication Code.

So you couch it in these terms: to save code size and speed up boot time, we use a unique, per-device MAC to authenticate the firmware in the boot loader. Because the firmware is distributed with a signature, the update client verifies the signature and replaces it with a MAC that the bootloader understands.
-->
### Tool integration

#### Mbed CLI
Mbed CLI
<!--Don't need the manifest tool, don't need to access the portal if I'm only updating one device-->
<!--ship a bin file to a server, pull down a developer certificate (not update????) and call the manifest tool-->
<!--CLI and IDE do not support Client Lite workflow-->

#### The Online Compiler
