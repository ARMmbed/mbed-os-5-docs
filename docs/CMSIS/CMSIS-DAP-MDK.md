#CMSIS DAP MDK

##Current limitations 

For the purpose of this trial, it will not be possible to debug applications that use semi-hosting calls to the mbed interface. Examples of these calls are :

* Accessing the local file system

* Ethernet applications where the MAC address is provided by the interface (default)

* Accessing the power down functions of the interface 

This is because the MDK does not currently support the use of semihosting calls.

Getting started

To try the mbed CMSIS-DAP upgrade you will need :

* The firmware that supports CMSIS-DAP for your target.

* An offline tool that supports CMSIS-DAP - [Keil MDK v4.60](https://www.keil.com/demo/eval/arm.htm) for example.

* An example project you wish to debug.

##Upgrading your board

###Select your board

Select your board and follow the [firmware upgrade process](http://mbed.org/handbook/Firmware) for your board.

###Install the latest serial driver

Download and install the [serial driver](/Going_Further/Serial_Conf/).

###Results

There will now be three mbed USB devices in device manager :

* USB disk
* mbed Serial port
* mbed CMSIS-DAP

<span style="text-align:center; display:block;">
![](/Going_Further/Images/CMSIS/CMSIS1.png)
</span>

<span style="background-color:lightyellow; color:black; display:block; height:100%; padding:10px">
**Warning: Driver issue**
<br /><br />
If the serial is not recognised by the host:
<br />* Go into the device manager
<br />* Right click on "mbed composite"
<br />* Uninstall the driver
<br />* Disconnect and connect your mbed
<br />* Install the [serial driver](/Going_Further/Serial_Conf/)
</span>

##Install an offline tool

The recommended offline tool is [Keil MDK v4.60](https://www.keil.com/demo/eval/arm.htm). Follow the links and instructions to set up the evaluation copy.

##Export a project

[uVision](http://www.keil.com/uvision) is one of the external offline toolchains supported by the mbed platform.

For a complete overview of the export feature, please refer to our general: [Exporting to offline toolchains](/Going_Further/Export/).

To export your mbed program for use in uVision, right-click the program in your program workspace. From the dialog, you can select the "Export To" as "Keil uVision4", and the target microcontroller you wish to export for. 

When you choose export, a zip file containing all the files you need for uVision will be generated. Unzip it and open the uVision project file (In this case, "project.uvproj"):

<span style="text-align:center; display:block;">
![](/Going_Further/Images/CMSIS/CMSIS2.png)
</span>

##Compile, download, debug!

Once you have unzipped and opened the ".uvproj" file, your project should appear in the uVision IDE much in the same way it appeared in the online compiler. You can browse the project files by navigating in the left panel, and the code will appear in the main panel.

###Compile

When the project has successfully compiled, "fromelf" will automatically run, to extract a binary file. This could be drag and dropped onto the mbed flash disk.

<span style="text-align:center; display:block;">
![](/Going_Further/Images/CMSIS/CMSIS3.png)
</span>

###Download

With the CMSIS-DAP upgrade, clicking the download button within uVision will send the binary directly to the flash of the MCU

<span style="text-align:center; display:block;">
![](/Going_Further/Images/CMSIS/CMSIS4.png)
</span>

###4.3 Debug

Add break points (1) by clicking on the line of code you wish to stop at, and use the "run" button (2) to execute the program until the break point it hit.

<span style="text-align:center; display:block;">
![](/Going_Further/Images/CMSIS/CMSIS5.webp)
</span>

The tools enable you to step in various ways over/into/out of

Use the tool bar to add registers, memory, call stack, symbol and watch windows. This gives visibility on the system status when a breakpoint is reached.

<span style="text-align:center; display:block;">
![](/Going_Further/Images/CMSIS/CMSIS6.png)
</span>

###Conclusion

A simple firmware upgrade of your board enables the on-board programming interface to communicate with debugging tools over the new CMSIS-DAP protocol. Over time we hope this will mean mbed will become interoperable with a wide range of offline tools, proving professional debug capabilities when they are needed.