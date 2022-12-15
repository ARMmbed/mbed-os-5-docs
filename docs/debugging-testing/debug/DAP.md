# DAPLink

DAPlink is an open source project that implements the embedded firmware required for a Cortex debug probe. The project is hosted on GitHub and is published under an Apache 2.0 license, making it attractive for commercial developments.

The software project is complemented by a series of reference designs for creating the DAPLink debug probe hardware, which is available in the [HDK documentation](../../porting/porting-tools.html#arm-mbed-hdk).

## DAPLink features

A DAPLink debug probe connects to your host computer through USB and connects to your target system (the one to be programmed and debugged) through a standard Cortex debug connector. It provides three main features - all over a single USB connection.

### HID interface

The driver-less HID interface provides a channel over which the CMSIS-DAP debug protocol runs. This enables all the leading industry standard toolchains to program and debug the target system.

Supported tools include:

- Keil MDK.
- pyOCD.

### USB drag and drop programming

DAPLink debug probes appear on the host computer as a USB disk. Program files in binary (`.bin`) and hex (`.hex`) formats can be copied onto the USB disk, which then programs them into the memory of the target system.

<span class="notes">**Note:** The DAPLink probe needs to contain the programming algorithms specific to the target system. Therefore, the version of the DAPLink firmware you use must match the target system.</span>

## USB serial port

The DAPLink debug probe also provides a USB serial port, which can be bridged through to a TTL UART on the target system.
The USB serial port will appear on a Windows machine as a COM port, or on a Linux machine as a /dev/tty interface.

## Further reading

- [DAPLink firmware updates and FAQ page](https://armmbed.github.io/DAPLink/).
- [The DAPLink GitHub repo](https://github.com/ARMmbed/DAPLink/blob/master/README.md).
- [Debug probes built with DAPLink](https://os.mbed.com/platforms/SWDAP-LPC11U35).
