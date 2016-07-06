# What you need

## User account

## Hardware

## Window serial driver

To use the mbed serial port over USB on Windows, you'll need a driver (it should work out of the box on Linux and Mac OS X). 

1. Download the [mbed Windows serial port driver](http://developer.mbed.org/media/downloads/drivers/mbedWinSerial_16466.exe).
2. Run the installer with your **mbed device plugged in**, and **no explorer windows showing the mbed drive**. This might take some time, or display a few "unsigned driver" warnings.

### Troubleshooting

**If you have multiple mbed devices, but the serial port only appears for one of them:** Make sure you run the installer for every device; Windows loads the driver based on the serial number, so it needs to be run for each device individually.

**If the installer fails because "No mbed Microcontrollers were found":** Check your device is plugged in over USB.

**If the installer reports the message "mbedWinSerial_nnnnn.exe is not a valid Win32 application":** It is likely you are using Internet Explorer to download the installer file, which sometimes seems to only download part of the installer application for an unknown reason. To solve this, try downloading the installer with a different browser (Firefox, Chrome).

**If the installer appears to hang:** Check if Windows is displaying an "unsigned driver/permission" window; these often get hidden behind other windows with nothing to indicate so in the taskbar. The installer will continue to run as soon as you click OK.
