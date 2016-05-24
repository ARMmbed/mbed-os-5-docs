#The mbed Interface

Since the beginning of mbed, there has been a certain amount of interest and speculation around the "magic interface chip" on the underside of the mbed microcontroller.

There has been some information published surrounding this part, which is now collated on this page.

The full schematics of the mbed Microcontroller, including the mbed interface are now available in the handbook.

##Connectivity

The best representation of the connectivity of the mbed interface was in Simon's official unoffical diagram:

<span style="text-align:center; display:block;">
![](/Getting_Started/Images/mbed_Interface.webp)
</span>

The headlines are that it:

- Provides a USB connection to the host computer, which exposes a Mass Storage (flash disk) and a USB Serial Port

- Connects with the Serial Flash device, which implements the USB flash disk file storage

- Has a JTAG connection to the target, so that it can program the target flash. Semihosting of the USB flash drive (LocalFileSystem) is implemented over this JTAG connection

- A physical UART connection exists between the target and the interface which is relayed over interface USB Serial port

##Operation

There are a few facts and rules about how the interface interacts with the host computer and the target, the most significant ones are:

- The USB Drive is really a flash drive that can store multiple binary files. On power up/reset, the interface will always program the newest file into the target, unless the newest binary has already been programmed.

- When there is no binary file on the USB flash disk, the target is held in reset

- The reset button on the mbed Microcontroller doesn't directly resets the target. Instead it requests that the interface resets the target, checking first to see if there is a newer binary on the USB flash disk to be programmed.

- If a file is opened by the target using LocalFileSystem, the USB flash disk will disappear from the host computer until the file is closed, as the filesystem can not appear in two places at once. 

- Should the USB flash drive fail to appear when you plug in your mbed, it might be because your current program is using the local file system. Press and hold the reset button to keep the target in reset, and the flash drive will appear.

<span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">
See also:
<br /><br />
[How mbed Works](/Introduction/How_mbed_Works/)
</span>

