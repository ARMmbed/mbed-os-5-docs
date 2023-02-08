# Keil uVision

This document explains how to build and debug Arm Mbed OS applications using Keil uVision 5. Due to the linker limits, this does not work in the free version of uVision. If you do not have a uVision license, you can use [Eclipse](../debug-test/third-party-tools.html), [Visual Studio Code](visual-studio-code.html) or any other IDE that supports debugging through GDB. For more info, please see [Setting up a local debug toolchain](../debug-test/setting-up-a-local-debug-toolchain.html).

## Exporting a project with Mbed CLI

To export your project to Keil uVision, you can use Mbed CLI.

<span class="notes">**Note:** Store the project on your local hard drive. Keil uVision does not support building from a network share.</span>

1. In your project folder, run:

    ```
    ## replace K64F with your target board
    $ mbed export -i uvision6 -m K64F
    ```

## Starting a debug session

The exported project contains a `.uvprojx` file. Double click on this file to open the project in Keil uVision. Keil uVision 5 does not support nested folders in the tree, so find your application source code by looking for a folder with the same name as your project.

<span class="images">![](../../images/uvision2.png)<span>Debugging an Mbed OS program in uVision 5</span></span>

To build your project and start a debug session:

1. Click *Project > Build Target*.
1. When building succeeds, click *Debug > Start/Stop Debug Session*.
1. If uVision does not connect to your development board, go to *Project > Options for Target > Debug*, and make sure 'CMSIS-DAP Debugger' is selected.

<span class="images">![](../../images/uvision3.png)<span>CMSIS-DAP Debugger options</span></span>

For more information on the CMSIS-DAP Debugger driver in uVision, see the [uVision documentation](http://www.keil.com/support/man/docs/dapdebug/dapdebug_drv_cfg.htm).
