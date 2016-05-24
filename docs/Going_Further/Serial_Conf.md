#Windows Serial Configuration

The mbed serial port works by default on Mac and Linux, but Windows needs a driver. These instructions explain how to setup the mbed Microcontroller to use the USB serial port on Windows. 

##Download the mbed Windows serial port driver

[Download the installer](http://developer.mbed.org/media/downloads/drivers/mbedWinSerial_16466.exe) to your PC, e.g. your desktop.

##Run the installer

With your ``mbed plugged in``, and *no explorer drive windows open*, run the installer:

It will take some time (especially on Vista), and pop up a few 'unsigned driver' warnings, but after a while you should have a Serial port.

###Where Next

* [Serial PC](/Development/PC_Com/) - Communication with a PC
* [Terminals](/Going_Further/Terminals/) -  Guide to using terminal applications

<span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">
***Troubleshooting***
<br />
<br />
**If you have multiple mbed microcontrollers, but the serial port only appears for one of them:** Make sure you run the installer for every mbed; windows loads the driver based on the serial number, so it needs to be run for each mbed you use.
<br /><br />
**If the installer fails because "No mbed Microcontrollers were found":** Check your mbed Microcontroller is plugged in.
<br /><br />
**If the installer reports the message "mbedWinSerial_nnnnn.exe is not a valid Win32 application":**
<br /> * It is likely you are using Internet Explorer to download the installer file, which sometimes seems to only download part of the installer application for an unknown reason.
 <br />* To solve this, download the installer with a different browser (Firefox, Chrome), and try again; this should solve the issue.
<br /><br />
**If the Installer appears to hang:** Check if windows has popped-up a "unsigned driver/permission" window; these often get hidden behind other windows with nothing to indicate so in the taskbar! Windows may be waiting for you to click "OK"!
<br /><br />
**If you have any problems, or think this tutorial could be improved, please tell us in the [Forum](http://developer.mbed.org/forum).**
</span>