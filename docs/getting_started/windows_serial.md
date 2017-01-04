# Windows serial driver

You can connect your board to your computer over USB. This should work out of the box on Linux and Mac OS X, but for Windows you will probably need to install a serial port driver:

1. Download the [mbed Windows serial port driver](http://developer.mbed.org/media/downloads/drivers/mbedWinSerial_16466.exe).
1. Plug in your mbed device over USB. It mounts as an mbed drive.
1. Close all Explorer windows showing the mbed drive.
1. Run the installer. This might take some time, or display a few "unsigned driver" warnings.

### Troubleshooting

**If you have multiple mbed devices, but the serial port only appears for one of them:** Make sure you run the installer for every device (plug in the device over USB and run the installer again); Windows loads the driver based on the serial number, so it needs to be run for each device individually.

**If the installer fails because "No mbed Microcontrollers were found":** Check your device is plugged in properly over USB.

**If the installer reports the message "mbedWinSerial_nnnnn.exe is not a valid Win32 application":** If you downloaded the installer using Internet Explorer, please try a different browser (Firefox, Chrome).

**If the installer appears to hang:** Check if Windows is displaying an "unsigned driver/permission" window; these often get hidden behind other windows with nothing to indicate so in the taskbar. The installer will continue to run as soon as you click OK.
