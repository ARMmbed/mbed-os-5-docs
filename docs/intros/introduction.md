## Introduction to mbed OS 5

Welcome to the mbed OS 5 handbook.

If you’re an experienced mbed applications developer, you might want to dive straight into the [API References](https://docs.mbed.com/docs/mbed-os-api-reference/en/) or look at our [development tools documentation](dev_tools/options.md).

If you're new to all this, continue reading.

### Developing applications on top of mbed OS

mbed OS lets you write applications that run on embedded devices, by providing the layer that interprets your application's code in a way the hardware can understand.

Your application code is written in C++. It uses the *application programming interfaces* (APIs) that mbed OS provides. These APIs allow your code to work on different microcontrollers in a uniform way. This reduces a lot of the challenges in getting started with microcontrollers and integrating large amounts of software.

#### Where to start

<span class="tips">If you're working on Windows, you might need to [install a serial driver](getting_started/what_need.md#windows-serial-driver).</span>

The easiest way to work with mbed OS is using one of our development tools. We've set up an example, [Blinky](getting_started/first_program.md), that you can try on each of the tools. It will teach you to build and run an application on your board.

When you know how to build an existing application, it's time to learn [how to write your own applications](APIs/intro.md).

#### Development tools

* Our offline development tool is the [mbed CLI](dev_tools/cli.md), a command-line tool. This requires having a toolchain installed on your computer.
* The [mbed Online Compiler](dev_tools/online_comp.md) lets you write and build applications using just a web browser and USB connection.
* If you're working with third party tools, look at [exporting instructions for the most popular ones](dev_tools/third_party.md).

#### Communicating with and monitoring your board

You can monitor and control an mbed board [to help you debug and test your applications](getting_started/mbed_interface.md).

<span class="tips">**Tip:** You can learn more about debugging [here](advanced/debugging.md).</span>

#### How to continue

When you've started writing applications using your selected development tool:

* Learn about [collaborative work and version control](collab/collab_intro.md).

* Try one of the [advanced tutorials](advanced/intro.md), which cover concepts such as debugging and memory trace.

* We have a [forum](https://forums.mbed.com/) for questions and advice.

### Contributing to mbed OS

If you want to contribute to the mbed OS codebase, please see [the contribution section](cont/contributing.md).

The current version of mbed OS 5 is 5.5.0. It is available on [GitHub](https://github.com/ARMmbed/mbed-os/releases/tag/mbed-os-5.5.0).

### Porting to mbed OS

Our full porting guide is still being written. For now, we have:

* A high-level [porting guide](advanced/porting_guide.md).
* Porting [from mbed OS 3 to mbed OS 5](advanced/MINAR_migration.md) (focusing on MINAR).
* Porting [mbed TLS](advanced/tls_porting.md).


## How mbed works

The mbed hardware architecture is designed to make sure you have all the tools and utilities to be productive. Most boards have an integrated debug circuit that assists development by programming the device, logging program execution and giving access to the debug access port. Here is how it works.

### Architecture diagram

This is the basic architecture of an mbed board:

<span class="images">![](images/mbed_internals.jpg)<span>A sketch of a typical mbed board's hardware architecture</span></span>

### How programming works

There are two options:

1. When you plug an mbed Enabled board to your PC using USB, it appears as a USB flash disk. The mbed Interface presents this small disk. It allows you to save ARM microcontroller binaries you want to run directly on to the board, without drivers.
2. The same USB connection exposes a debug protocol such as CMSIS-DAP. This enables lots of IDEs to program and debug the device.

### How USB serial works

The mbed Interface also presents a USB serial/com interface. This is basically a UART-USB bridge, and it connects to the interface's UART. So if you send characters out of the target board's UART, the mbed Interface will read them and transfer them over the USB link. When you ``printf()``, it is just sending characters to UART. This means that if you make your own PCB, these characters will still appear on UART.

### Notes

The ``.bin`` files the mbed microcontroller accepts are standard raw ARM binaries. Use any compiler you like to generate them. As the separate interface manages programming over JTAG or SWD, you have unlimited control of the target microcontroller. You really are just loading on a raw binary; this means you can build your own PCB using the same target microcontroller, and the same program binary will run on that.

### The mbed Interface

You can find more information about the mbed Interface and the circuits on which it runs in the [HDK reference manual](https://docs.mbed.com/docs/mbed-hardware-development-kit/en/latest/) or on the [DAPLink GitHub page](https://github.com/ARMmbed/DAPLink/blob/master/README.md). The HDK includes reference circuits you can use to create your own boards, and DAPLink is the firmware that runs on these circuits.

### Connectivity

The best representation of the connectivity of the mbed Interface is the same diagram we showed above.

The mbed Interface:

- Provides a USB connection to the host computer, which exposes a Mass Storage (flash disk) and a USB serial port.

- Has an SWD or JTAG connection to the target, so it can program the target flash. You can also use this for debugging.

- A physical UART connection exists between the target and the interface, which is relayed over the interface's USB serial port.
