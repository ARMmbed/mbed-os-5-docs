#mbed HDK

The mbed Hardware Development Kit (HDK) provides full microcontroller sub-system design files and firmware for building development boards and custom products that benefit from the native support of the mbed SDK and free mbed Online Compiler and mbed Developer Platform.

The mbed HDK specifies all support components and circuits including the CMSIS-DAP Interface design that provides simple USB drag-n-drop programming and CMSIS-DAP debug interface for the target microcontroller.

Development boards that are already based on the mbed HDK are the quickest way to get started with the mbed platform. We manufacture official mbed Microcontroller modules that are specifically optimised for flexible rapid prototyping, and are available from distributors worldwide. Our partners are now also creating mbed-enabled hardware such as ultra low-cost ARM evaluation boards in the popular Arduino form-factor.

<span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">
**Creating your own mbed-enabled platforms** <br />
Are you are a hardware company that would like to create an mbed-enabled platform of your own that is supported within the mbed platforms database and tools? If so, then please email us at <mailto:support@mbed.org> and we can help you with your questions and support you through the process.
</span>

##Microcontroller Sub-systems 

Each of the subsystems designs include

  * Hardware design schematics (Eagle format)
  * Interface binary for the CMSIS-DAP interface

An example of how a microcontroller sub-system might be used to build an evaluation board:

<span style="display:block; text-align:center; padding:20px;">
![eveulation](/Development/Images/EvaluationBoard.png)
</span>

##CMSIS-DAP interface 

The CMSIS-DAP Interface is a microcontroller-based single chip solution that provides drag and drop programming, [CMSIS-DAP](/CMSIS/CMSIS/) debugger and USB serial interface to a range of Cortex-M based microcontrollers. The small footprint, low number of passive components and rich feature set provide a low cost, low overhead solution that can easily be integrated on a PCB.

The firmware required to turn the low cost microcontroller into a powerful programming, debug and communication interface is included with the HDK and can be used freely, even in commercial products.

<span style="display:block; text-align:center; padding:20px;">
![CMSIS](/Development/Images/CMSISDAPInterface.png)
</span>

The CMSIS-DAP interface provides three main functions over a single physical USB connection :

* USB Disk drag and drop programming - ideal for fast turnaround prototyping or in-field upgradable products.
* Debug interface using the [CMSIS-DAP](/CMSIS/CMSIS) - provides full debug capability with tools like [Keil MDK](/CMSIS/CMSIS-DAP-MDK/).
* USB Serial interface between the host computer and the target.


<span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">
For more information see the [CMSIS-DAP section](/CMSIS/CMSIS/).
</span>

##Benefits of the HDK 

There are various benefits to building a custom design onto of the mbed HDK. The ready made schematics are a great short cut, so you can get started on all the things that make your design, without worrying if you've correctly implemented all the "necessary bits" of the design. The mbed HDK incorporates the CMSIS-DAP interface. This provides USB drag and drop programming, [CMSIS-DAP](/CMSIS/CMSIS/) debugging and USB serial communication. The [mbed SDK](/Introduction/SDK/) supports each of the exact configurations of HDK designs, and libraries that have been written to the APIs in the mbed SDK are highly reusable. Lastly, the mbed community has developed a wealth of libraries, applications and code examples using the SDK/HDK, and this active community offers a lot of opportunities for support and even hiring in required skills.


##Sources

1. The mbed HDK, complete with PCB Layout files and schematics, can be downloaded from the repository [mbed-HDK](http://developer.mbed.org/teams/mbed/code/mbed-HDK/).

2. The sources of the [CMSIS-DAP Interface Firmware](http://developer.mbed.org/handbook/cmsis-dap-interface-firmware).

<span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">
For support, design review and other help making your platform, email <mailto:support@mbed.org>.
</span>

