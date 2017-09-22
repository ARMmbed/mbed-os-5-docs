## Glossary

API - [Application programming interface](/docs/v5.6/reference/api.html).

Application - An executable module built out of libraries that acts as a final product.

Arm Mbed CLI - The name of the Arm Mbed [command-line tool](/docs/v5.6/tools/mbed-cli.html), packaged as `mbed-cli`.

Arm Mbed interface - The extra chip that sits on all [Mbed Enabled development boards](/docs/v5.6/introduction/how-mbed-works.html#architecture-diagram). It's what makes the target chip (for example, K64F) look like a USB drive. It usually runs a separate piece of software that generally doesn't change. That software is usually `DAPLink`, `CMSIS-DAP` or `STLink`.

Arm Mbed Online Compiler - [Arm’s online tool](/docs/v5.6/tools/online.html), which you can use to create and compile your code.

Arm Mbed OS - Arm's [platform operating system](https://docs.mbed.com/) for the Internet of Things.

Arm Mbed TLS - A [comprehensive SSL/TLS solution](/docs/v5.6/reference/security.html#tlss) that makes it easy for developers to include cryptographic and SSL/TLS capabilities in their software and embedded products. As an SSL library, it provides an intuitive API, readable source code and a minimal and highly configurable code footprint.

Arm Mbed uVisor - A self-contained [software hypervisor](/docs/v5.6/reference/security.html#uvisor) that creates independent secure domains on ARM Cortex-M3 and M4 micro-controllers. 

Bit - A basic unit of digital information that can be one of two values: `0` (`false`) or `1` (`true`).

BLE - [Bluetooth Low Energy](/docs/v5.6/reference/ble.html).

Blinky - An [example application](/docs/v5.6/tutorials/your-first-arm-mbed-application.html) that you can use to get to know Arm Mbed OS and the development tools. It’s one of the simplest examples of Mbed OS.

Block Device - A [file](/docs/v5.6/reference/contributing-storage.html#block-devices) that represents a device, with data that can be read or written to it in blocks.

Board - An Mbed Enabled development board. You can see a complete list of these [here](https://developer.mbed.org/platforms/).

Boolean - A binary variable, having two possible values called `true` and `false`.

Bootloader - [The program](/docs/v5.6/tutorials/creating-and-using-a-bootloader.html) that loads Mbed OS when a board is turned on.

Build Profile - Mbed OS 5 supports three primary [build profiles](/docs/v5.6/tools/mbed-cli.html#build-profiles): develop, debug and release.

Build Script - A build automation and generation utility.

Byte - A unit of digital information that consists of 8 bits (see `Bit`).

Callback - Any [executable code](/docs/v5.6/reference/api-references.html#callback) that is passed as an argument to other code, which is expected to call back (execute) the argument at a given time.

CAN - [Controller-area network](/docs/v5.6/reference/api-references.html#can).

Class - An extensible program-code-template for creating objects, providing initial values for state and implementations of behavior.

CI - Continuous integration.

CLI - Command-line interface. 

CMSIS-DAP - The precursor to DAPLink, this [project](https://github.com/mbedmicro/cmsis-dap) is deprecated due to known bugs. You should not use it in any new designs.

DAPLink - An Arm maintained [project](https://github.com/mbedmicro/DAPLink) that is under active development.

Debugging - The [process](/docs/v5.6/tools/debugging.html) of finding and solving problems in code.

Deprecation - Marking a piece of code as out of date. You should not write new code that depends on deprecated APIs. We will remove deprecated APIs when our code no longer depends on them.

Dynamic Memory - 

Exporter - Use the Arm Mbed [exporters](/docs/v5.6/tools/exporting.html#about-the-exporters) to export your code to various third party tools and IDEs.

GitHub - A web-based [Git development platform](https://github.com/armmbed/mbed-os) for version-controlled repositories.

GPIO - General-purpose input/output, a generic pin that is controllable by the user at run-time.

Greentea - **G**eneric **re**gression **en**vironment for **te**st **a**utomation. [Greentea](/docs/v5.6/tools/tools-testing.html#greentea) is the automated testing tool for Arm Mbed OS development.

`htrun` - An Mbed OS command used to drive test binary flashing, device reset and test execution.

I2C - [Interintegrated Circuit](/docs/v5.6/reference/api-references.html#i2c) (short-distance, intraboard communication).

IDE - Integrated Development Environment.

int - Short for "integer", it is a variable type that can be used to define numeric variables holding whole numbers.

Library - A module that you can use to build applications.

LoRA - Long range (low power wireless platform).

Makefile - A file containing a set of directives used with the make build automation tool. 

Mesh - A network topology in which each node relays data for the network.

Module - A self-contained unit of code containing classes and functions.

Nibble - A unit of digital information that consists of 4 bits (see `Bit`).

Platform - See `board`.

Porting - A process to add target support to Mbed OS.

Program - See `application`.

Pull Request - Used by version-controlled repositories to propose and collaborate on changes.

REST - Representational State Transfer (API).

RTOS - [Real-Time Operating System](/docs/v5.6/reference/rtos.html).

Serial - A [protocol](/docs/v5.6/reference/api-references.html#serial) used in data transmission for the transfer of individual bits of information.

SPI - [Serial Peripheral Interface](/docs/v5.6/reference/api-references.html#spi).

Static Memory - The allocation of memory at compile time, before the program is executed.

SSL - Secure sockets layer.

STLink - STMicro's [firmware](http://www.st.com/content/st_com/en/products/embedded-software/development-tool-software/stsw-link007.html) that performs the same tasks as DAPLink but uses a different [driver](http://www.st.com/content/st_com/en/products/embedded-software/development-tool-software/stsw-link009.html).

Target - See [`board`](/docs/v5.6/introduction/glossary.html#board).

Terminal Application - [Applications](/docs/v5.6/tutorials/serial-communication.html#terminal-applications) that run on your host PC that provide a window where your Mbed board can print and where you can type characters back to your board.

TLS - Transport Layer Security.

Toolchain - A [group of programming tools](/docs/v5.6/tools/exporting.html#setting-up-a-local-debug-toolchain).

Travis CI - a continuous integration service used to build and test software projects hosted at GitHub (see `GitHub`).

utest - A [test harness](/docs/v5.6/tools/tools-testing.html#utest-asynchronous-c-test-harness) you can use to execute a specified series of (asynchronous) C++ test cases.
