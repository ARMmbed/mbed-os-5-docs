# How mbed works

The mbed hardware architecture is designed to make sure you have all the tools and utilities to be productive. Most boards have an integrated debug circuit that assists development by programming the device, logging program execution and giving access to the debug access port. Here is how it works.

## Architecture diagram

This is the basic architecture of an mbed board:

<span class="images">![](images/mbed_internals.jpg)<span>A sketch of a typical mbed board's hardware architecture</span></span>

## How programming works

There are two options:

1. When you plug an mbed Enabled board to your PC using USB, it appears as a USB flash disk. The mbed Interface presents this small disk. It allows you to save ARM microcontroller binaries you want to run directly on to the board, without drivers.
2. The same USB connection exposes a debug protocol such as CMSIS-DAP. This enables lots of IDEs to program and debug the device.

## How USB serial works

The mbed Interface also presents a USB serial/com interface. This is basically a UART-USB bridge, and it connects to the interface's UART. So if you send characters out of the target board's UART, the mbed Interface will read them and transfer them over the USB link. When you ``printf()``, it is just sending characters to UART. This means that if you make your own PCB, these characters will still appear on UART.

## Notes

The ``.bin`` files the mbed microcontroller accepts are standard raw ARM binaries. Use any compiler you like to generate them. As the separate interface manages programming over JTAG or SWD, you have unlimited control of the target microcontroller. You really are just loading on a raw binary; this means you can build your own PCB using the same target microcontroller, and the same program binary will run on that.


# The mbed Interface
You can find more information about the mbed Interface and the circuits on which it runs in the [HDK reference manual](https://docs.mbed.com/docs/mbed-hardware-development-kit/en/latest/) or on the [DAPLink GitHub page](https://github.com/ARMmbed/DAPLink/blob/master/README.md). The HDK includes reference circuits you can use to create your own boards, and DAPLink is the firmware that runs on these circuits.

## Connectivity

The best representation of the connectivity of the mbed Interface is the same diagram we showed above.

The mbed Interface:

- Provides a USB connection to the host computer, which exposes a Mass Storage (flash disk) and a USB serial port.

- Has an SWD or JTAG connection to the target, so it can program the target flash. You can also use this for debugging.

- A physical UART connection exists between the target and the interface, which is relayed over the interface's USB serial port.

