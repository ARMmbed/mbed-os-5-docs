# Arm Mbed HDK

The Arm Mbed Hardware Development Kit (Mbed HDK) is a collection of hardware design resources that we have gathered to assist the development of custom hardware benefiting from the Arm Mbed ecosystem and associated technologies, like Arm Mbed OS and DAPLink. Working with development boards that are based on the Mbed HDK is the most efficient way to get started with the Arm Mbed platform.

## HDK content per project

- Eagle schematic and board files.
- PDF schematic and board copies.
- CAM Job GERBERS for manufacture (including pick/place and drill).
- Bill of Materials (BOM).
- An online BOM for easy purchasing (eBOM).

## Repository content and projects

The [`mbed-hdk`](https://github.com/ARMmbed/mbed-hdk) repository offers:

- CAD resources in Eagle 7.3.0 format:
    - Mbed HDK component library.
    - Design rules.
    - CAM jobs.
    - User Language Program (ULP) scripts for Eagle 7.3.0.
- Production Design Projects:
    - Arm Mbed Application Shield.
    - Arm Mbed 6LoWPAN border router HAT.
    - Arm Mbed USB border router.
    - Arm Mbed xDOT shield.
    - Arm Mbed LPC1768.
    - CI Test Shield.
    - DAPLink:
       - SWDAP LPC11U35.
       - DAPLink LPC11U35.

Production Design Projects include projects of the Mbed HDK that have been manufactured and that fulfill a specific use case. Each Production Design Project is referenced by its most up-to-date version v`x.x.x`. If you want to find an older project version, navigate to that release or check out a previous commit.

Please keep in mind that the resources are provided "as is". Though we have made the best effort to ensure the highest possible quality, we can offer no support or guarantees. The latest versions of Production Designs contained in the Mbed HDK have been successfully manufactured by a third-party manufacturer and proven to work.
