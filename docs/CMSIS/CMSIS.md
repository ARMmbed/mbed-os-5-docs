#CMSIS-DAP

The mbed HDK and mbed-enabled hardware support the CMSIS-DAP debug interface. It provides a standardised way to access the CoreSight Debug Access Port (DAP) of an ARM Cortex microcontroller via USB. CMSIS-DAP is generally implemented as an on-board interface chip, providing direct USB connection from a development board to a debugger running on a host computer on one side, and over Joint Test Action Group (JTAG) or Serial Wire Debug (SWD) to the target device to access the CoreSight DAP on the other.

You can access the documentation on the [ARM website](https://silver.arm.com/browse/CMSISDAP). You will need to register for an ARM silver account to access the documentation.

##Why the need for CMSIS-DAP?

There are several reasons for the introduction of CMSIS-DAP:

* Before the CMSIS-DAP standard, a lot of USB wigglers implemented their own protocols. With this configuration, the host debugger has to be aware of these different protocols and has to implement all of them, which produces a lot of fragmentation and re-inventing the wheel. At the same time, the protocols were usually defined at the JTAG level, meaning they were slow. CMSIS-DAP provides a standardised interface for debuggers that is defined at the CoreSight DAP level, allowing for a standard interface and fast driverless implementations.

* With the new CMSIS-DAP layer, the host debugger can debug targets over SWD or JTAG without the need to implement these two protocols.

* The USB connection uses the HID driver class. As HID drivers are bundled with all operating systems, there is no need to install a specific driver on the host computer.

##How can CMSIS-DAP be integrated?

As mentioned earlier, CMSIS-DAP has to be implemented on an Interface Chip. This chip provides the link between the host computer (over USB for instance) and the target that has to be debugged (over SWD or JTAG). 

On the mbed hardware, the CMSIS-DAP firmware has been implemented on the [mbed interface](/Introduction/mbed_Interface/) as part of the mbed HDK. In addition to the Mass Storage and the Virtual Serial Port interfaces, an HID endpoint is used to establish a CMSIS-DAP communication link with a debugger.

<span style="display:block; text-align:center; padding:20px;">
![Communication with a debugger](/Development/Images/CMSIS.png "CMSIS-DAP communication with a debugger across a USB connection")
<span>
<span style="background-color:lightblue; color:gray; display:block; height:100%; padding:10px;">*CMSIS-DAP communication with a debugger across a USB connection*</span>
##Overview of the CMSIS-DAP standard

Packets are exchanged between the host debugger and the interface chip: the host sends a command and the debug unit sends the response to the command. 

Different types of commands can be issued by the host:

* **General commands**: request information and control the debug unit. Also used to connect and disconnect the debug unit.
* **Common SWD/JTAG commands**: for example, set the clock speed.
* **SWD-specific commands**: configure the parameters for SWD mode.
* **JTAG-specific commands**: configure the JTAG device chain.
* **Transfer commands**: read/write [CoreSight](http://www.arm.com/products/system-ip/coresight/index.php) registers. These commands are independent of the transport protocol (SWD or JTAG).

##Example: read memory over CMSIS-DAP

Let's say that a debugger needs to read the value at a specific location in memory. The following commands have to be sent by the host:

* **Transfer Command**: write the ``CSW register`` (Control/Status Word Register). This will configure the transfer (32bits/16bits/8bits transfer).

* **Transfer Command**: write the ``TAR register`` (Transfer Address Register) with the address of the memory location.

* **Transfer Command**: read the ``DRW register`` (Data Read/Write register) to read the value at the location specified earlier.

##Conclusion

CMSIS-DAP provides a standardised interface for debuggers. It will probably become the de facto standard that debuggers and debug units will implement; this is why mbed chose to take advantage of this new standard to provide debug capabilities. For instance, Keil uVision, which combines an IDE, debugger and simulation environment already supports CMSIS-DAP. 

<span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">
**Tip:** If you have a project you want to debug, you can try the new [mbed interface with CMSIS-DAP](/CMSIS/CMSIS-DAP-MDK/).
</span>