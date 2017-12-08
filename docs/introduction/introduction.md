## Mbed OS 5

Arm Mbed OS lets you write applications that run on embedded devices, by providing the layer that interprets your application's code in a way the hardware can understand.

Your application code is written in C and C++. It uses the *application programming interfaces* (APIs) that Mbed OS provides. These APIs allow your code to work on different microcontrollers in a uniform way. This reduces the challenges of getting started with Arm-based microcontrollers and integrating large software projects.

#### Where to start

<span class="tips">If you're working on Windows, you might need to <a href="/docs/v5.7/tutorials/windows-serial-driver.html" target="_blank">install a serial driver</a>.</span>

The easiest way to work with Mbed OS is using one of our development tools. We've set up an example, <a href="/docs/v5.7/tutorials/your-first-program.html" target="_blank">Blinky</a>, that you can try on each of the tools. Blinky teaches you to build and run an application on your board.

Once you know how to build an existing application, it's time to learn <a href="/docs/v5.7/reference/index.html" target="_blank">how to write your own applications</a>.

##### Development tools

- Our offline development tool is <a href="/docs/v5.7/tools/arm-mbed-cli.html" target="_blank">Arm Mbed CLI</a>, a command-line tool. This requires having a toolchain installed on your computer.
- The <a href="/docs/v5.7/tools/arm-online-compiler.html" target="_blank">Arm Mbed Online Compiler</a> lets you write and build applications using a web browser.
- If you're working with third party tools, look at <a href="/docs/v5.7/tools/exporting.html" target="_blank">exporting instructions for the most popular ones</a>.

##### Communicating with and monitoring your board

You can <a href="/docs/v5.7/tutorials/serial-comm.html" target="_blank">monitor and control an Mbed board</a> to help you debug and test your applications.

<span class="tips">**Tip:** Learn more about debugging in the <a href="/docs/v5.7/tutorials/debugging-applications.html" target="_blank">debugging applications section</a>.</span>

#### How to continue

When you've started writing applications using your selected development tool:

- Learn about <a href="/docs/v5.7/tools/collab-online-comp.html" target="_blank">collaborative work and version control</a>.
- Try one of the <a href="/docs/v5.7/tutorials/index.html" target="_blank">tutorials</a>, which cover concepts such as debugging and memory tracing.
- Ask questions and give advice on the <a href="https://os.mbed.com/forum/" target="_blank">forum</a>.

#### Contributing to Mbed OS

If you want to contribute to the `mbed-os` codebase, please see <a href="/docs/v5.7/reference/contributing-overview.html" target="_blank">the contribution section</a>.

You can find past releases and the current release on <a href="https://github.com/ARMmbed/mbed-os/releases/" target="_blank">GitHub</a>.

#### Porting to Mbed OS

Our full contributing guide is still being written. For now, we have:

- A guide to <a href="/docs/v5.7/reference/contributing-target.html" target="_blank">contributing targets</a>.
- Information about the <a href="/docs/v5.7/reference/contributing-tools.html" target="_blank">tools you need to contribute targets</a>.
- APIs about <a href="/docs/v5.7/reference/contributing-storage.html" target="_blank">storage</a> and <a href="/docs/v5.7/reference/contributing-connectivity.html" target="_blank">connectivity</a> in relation to porting.

## How Mbed works

The Arm Mbed hardware architecture is designed to make sure you have all the tools and utilities to be productive. Most boards have an integrated debug circuit that assists development by programming the device, logging program execution and giving access to the debug access port. Here is how it works.

#### Architecture diagram

This is the basic architecture of an Mbed board:

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/mbed_internal.png)<span>A sketch of a typical Mbed board's hardware architecture</span></span>

#### How programming works

There are two options:

1. When you plug an Mbed Enabled board to your PC using USB, it appears as a USB flash disk. The Mbed interface presents this small disk. It allows you to save Arm microcontroller binaries you want to run directly on to the board, without drivers.
2. The same USB connection exposes a debug protocol such as CMSIS-DAP. This enables lots of IDEs to program and debug the device.

##### How USB serial works

The Arm Mbed interface also presents a USB serial/com interface. This is basically a UART-USB bridge, and it connects to the interface's UART. So if you send characters out of the target board's UART, the Arm Mbed interface will read them and transfer them over the USB link. When you `printf()`, it is just sending characters to UART. This means that if you make your own PCB, these characters will still appear on UART.

##### Notes

The `.bin` files the Mbed microcontroller accepts are standard raw binaries. Use any compiler you like to generate them. As the separate interface manages programming over JTAG or SWD, you have unlimited control of the target microcontroller. You really are just loading on a raw binary; this means you can build your own PCB using the same target microcontroller, and the same program binary will run on that.

#### The Arm Mbed interface

You can find more information about the Mbed interface and the circuits on which it runs in the <a href="/docs/v5.7/reference/contributing-tools.html#arm-mbed-hdk" target="_blank">HDK reference manual</a> or on the <a href="https://github.com/ARMmbed/DAPLink/blob/master/README.md" target="_blank">DAPLink GitHub page</a>. The HDK includes reference circuits you can use to create your own boards, and DAPLink is the firmware that runs on these circuits.

#### Connectivity

The best representation of the connectivity of the Mbed interface is the same diagram we showed above.

The Mbed interface:

- Provides a USB connection to the host computer, which exposes a Mass Storage (flash disk) and a USB serial port.
- Has an SWD or JTAG connection to the target, so it can program the target flash. You can also use this for debugging.
- A physical UART connection exists between the target and the interface, which is relayed over the interface's USB serial port.
