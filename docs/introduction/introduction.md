# An introduction to Arm Mbed OS 6
<!--I don't like the structure here-->
Mbed OS is an open-source operating system for Internet of Things (IoT) Cortex-M boards: low-powered, constrained and connected. Mbed OS provides an abstraction layer for the microcontrollers it runs on, so that developers can write C/C++ applications that run on any Mbed-enabled board.<!--device is a problematic terms, because Keil uses it to mean something very specific, so going with "board"-->

## Profiles and RTOS<!--clumsy title--><!--maybe it doesn't even need a title?-->

The **full profile** of Mbed OS is an RTOS (it includes an RTX and all RTOS APIs), so it supports deterministic, multithreaded, real-time software execution. The RTOS primitives are always available, allowing drivers and applications to rely on threads, semaphores, mutexes and other RTOS features. It also includes all APIs by default, although you can remove unused ones at build time.

The **bare metal profile** doesn't include an RTX and is therefore not an RTOS - it is designed for applications that do not require complex thread management. It is also designed for constrained devices, and therefore focuses on minimising the size of the final application: by default, it includes only the smallest possible set of APIs, to which you can manually add APIs your application requires. The bare metal profile can use the small C libraries (which are not thread safe) to further minimise the size of the application.
<!--too many "designed" and "minimze" and the sentences are really long-->

## Licensing

We release Mbed OS under an Apache 2.0 license, so you can confidently use it in commercial and personal projects. For more information about licensing, please see [our licensing documentation](../contributing/license.html).


## Getting started

Our [quick start](../quick-start/index.html) guides show how to build an example application for both the full profile and bare metal profile, on Mbed CLI, Mbed Studio and the Mbed Online Compiler.

| [Build with Mbed Studio](https://os.mbed.com/docs/mbed-studio/current/getting-started/index.html) | [Build with Mbed Online Compiler](../quick-start/online-with-the-online-compiler.html) |  [Build with Mbed CLI](../quick-start/offline-with-mbed-cli.html) |
| --- | --- | --- |
| Download our dedicated desktop IDE, including all the necessary tools to work with Mbed OS. | Zero-installation web IDE to explore Mbed OS; great for rapid prototyping and education. | Command-line tool requiring manual setup of tools, but providing the greatest degree of flexibility. |

The Mbed OS source code is available on [GitHub](https://github.com/ARMmbed/mbed-os) and on our [release page](https://os.mbed.com/releases/).


## Recently updated documentation

<!--bare metal, list of deprecated APIs, new API structure, porting updates...-->

- New API references for [BufferedSerial](../apis/bufferedserial.html) and [UnbufferedSerial](../apis/unbufferedserial.html).
- New content about [using small C libraries in Mbed OS bare metal](../reference/using-small-c-libraries.html).
- A guide to [porting a custom board](../porting/porting-a-custom-board.html).
- A porting guide for the [static pin map extension](../porting/static-pinmap-port.html).
- The [UserAllocatedEvent](../apis/userallocatedevent.html) API reference.


## Hardware

Arm, its Partners and the Arm Mbed developer community work together to develop the Mbed OS project. This thriving ecosystem means that Mbed OS includes drivers for a lot of different hardware, so you can concentrate on clean and portable application code.

Broadly speaking, the hardware you can see on our site is of three types:

- **[Modules](https://os.mbed.com/modules/)**: include a microcontroller, IoT centric connectivity and required onboard memory. They are ideal for designing IoT products, from prototyping to mass production. Mbed Enabled Modules have full support for Mbed OS with all available connectivity drivers.
- **[Boards](https://os.mbed.com/platforms/)**: development boards are an inexpensive way to start developing with Mbed OS and other components.
- **[Components](https://os.mbed.com/components/)**: the Component Database hosts reusable libraries for different hardware, middleware and IoT services that you can use with Arm Microcontrollers. These components can be used as building blocks for quickly developing prototypes and products.

## Tools

The Mbed product suite includes the tools you need to work with Mbed OS, whatever your skill level.

For most users on Windows, macOS and Linux, we recommend Mbed Studio, which is our desktop IDE. Mbed Studio includes the dependencies and tools you need to work with Mbed OS, including access to Arm Compiler 6 to build your code and pyOCD to debug it. For experienced developers, we also include the Mbed command line tools (such as Mbed CLI) with the Mbed Studio installation.

If you prefer to work online, use the Mbed Online Compiler, which lets you write and build applications using a web browser with no additional setup.

If you are an experienced developer, you can also set up the command line tools manually by installing Mbed CLI, a compiler toolchain, a debugger and source control management.

You can use our debugging tools, DAPLink and pyOCD, to program and debug many devices. At the end of the development cycle, you can use the Mbed OS validation tools, Greentea and utest, to test your project.

Lastly, you can [export your work](../tools/exporting.html) from the Mbed tools to other IDEs.<!--should the intro have all the links, or none?-->
