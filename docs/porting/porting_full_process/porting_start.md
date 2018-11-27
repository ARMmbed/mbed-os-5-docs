## Porting guide

This document provides guidelines for adding a new MCU target to Mbed OS and Pelion.

### Scope and milestones
<!--I'm not sure I see how these milestones follow what's below, at least in numbering-->
The following milestones usually need to happen to port Mbed OS to a board or target:

1. Set up a development environment. Please choose:
   - Your primary development PC (Windows, Mac OS or Linux).

       You can port targets, connectivity and storage on Windows, macOS or Linux. Due to limitations in some development tools that Mbed OS uses, you need a Windows PC for DAPLink/FlashAlgo development.

  - An evaluation board with a target MCU, debug probe or an integrated interface chip.<!--I'm guessing the "or" is only for the last two things - debug probe or interface chip. In which case, this sentence requires rewriting.--> The hardware [is reviewed in greater details later in this document]().
  - A storage device (SD or external flash).

1. Locate reusable code to port to Mbed OS.
<!--Are the reusable code and SDK related? Are they the same thing?-->
    If there is an SDK available to speed up the porting process, we recommend reusing it (assuming copyright of the existing code is preserved).

1. Choose an IDE and debugger. The three commonly used IDEs are [Eclipse](https://www.eclipse.org/ide/), [IAR Embedded Workbench](https://www.iar.com/iar-embedded-workbench/) and [Keil MDK](http://www.keil.com/).

    Limitations:

    - Eclipse is license free, whereas both IAR and Keil IDE require licenses.
    - Currently, DAPLink development works only Keil MDK. You will have to use Keil for pyOCD and DAPLink development.

1. The [Mbed Enabled](https://www.mbed.com/en/about-mbed/mbed-enabled/introduction/) program requires pyOCD, so ultimately pyOCD needs to support the new target. To allow parallel development in porting targets, connectivity and storage while pyOCD is still under development, you can use other IDEs supported on the evaluation board in the beginning phase.

1. Implement and test CMSIS pack, bootstrap, linker script and startup code.

A basic framework is ready after this step. You can do the rest of the porting work in parallel:

1. Implement and test porting APIs. This includes all components described in the rest of this porting guide.

1. Test Mbed OS and Pelion example applications (as listed [in the final steps in this porting guide]()). This steps verifies that your new port is fully functional.
