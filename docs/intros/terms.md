## Glossary

[TODO: This will need a massive edit, and additional info]

Suggested ideas:

Abstraction layer

API - Application programming interface

Application - An executable module built out of libraries that acts as a final product.

Arm Mbed CLI - The name of the Arm Mbed [command-line tool](cli.md), packaged as `mbed-cli`.

Arm Mbed interface - The extra chip that sits on all Mbed Enabled development boards. It's what makes the target chip (for example, K64F) look like a USB drive. It usually runs a separate piece of software that generally doesn't change. That software is usually `DAPLink`, `CMSIS-DAP` or `STLink`.

Arm Mbed Online Compiler

Arm Mbed OS

Arm Mbed TLS - A [comprehensive SSL/TLS solution](/docs/v5.4/reference/api-references.html#arm-mbed-tls) that makes it easy for developers to include cryptographic and SSL/TLS capabilities in their software and embedded products. As an SSL library, it provides an intuitive API, readable source code and a minimal and highly configurable code footprint.

Arm Mbed uVisor

Bit - 

BLE - Bluetooth low energy.

Blinky - An [example application](/docs/v5.4/tutorials/your-first-arm-mbed-application.html) that you can use to get to know Arm Mbed OS and the development tools. It’s one of the simplest examples of Mbed OS.

Block Device - A file that represents a device, with data that can be read or written to it in blocks.

Board - An Mbed Enabled development board. You can see a complete list of these [here](https://developer.mbed.org/platforms/).

Boolean -

Bootloader - The program that loads Mbed OS when a board is turned on.

Build Profile

build script

Byte - 

Callback

CAN - Controller-area network.

Class - 

CI - Continuous integration.

CLI - Command-line interface. 

CMSIS-DAP - The precursor to DAPLink, this [project](https://github.com/mbedmicro/cmsis-dap) is deprecated due to known bugs. You should not use it in any new designs.

Command-line

DAPLink - An Arm maintained [project](https://github.com/mbedmicro/DAPLink) that is under active development.

Debugging - 

Deprecation - Marking a piece of code as out of date. You should not write new code that depends on deprecated APIs. We will remove deprecated APIs when our code no longer depends on them.

Dynamic Memory - 

Exporter -

Function - 

Git

GitHub

GPIO

Greentea - **G**eneric **re**gression **en**vironment for **te**st **a**utomation. [Greentea](/docs/v5.4/tools/testing-1.html#greentea---test-automation-for-arm-mbed) is the automated testing tool for Arm Mbed OS development.

`htrun`

I2C - Interintegrated circuit (short-distance, intraboard communication).

IDE - Integrated development environment

int - 

Library - A module that you can use to build applications.

LoRA - Long range (low power wireless platform)

Makefile

Mesh

Module - A self-contained unit of code containing classes and functions.

Nibble -

Platform - See `board`.

Porting

Program - See `application`.

Pull Request

REST - Representational State Transfer (API)

RTOS - Real time operating system

RTX

Serial

SPI - Serial peripheral interface

Static Memory

SSL - Secure sockets layer.

STLink - STMicro's [firmware](http://www.st.com/content/st_com/en/products/embedded-software/development-tool-software/stsw-link007.html) that performs the same tasks as DAPLink but uses a different [driver](http://www.st.com/content/st_com/en/products/embedded-software/development-tool-software/stsw-link009.html).

Target - See `board`.

Terminal Application

TLS - Transport layer security.

Toolchain

Travis -

utest -
