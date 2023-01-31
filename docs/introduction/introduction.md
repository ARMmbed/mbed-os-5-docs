# An introduction to Arm Mbed OS 6

Mbed OS is an open-source operating system for Internet of Things (IoT) Cortex-M boards: low-powered, constrained and connected. Mbed OS provides an abstraction layer for the microcontrollers it runs on, so that developers can write C/C++ applications that run on any Mbed-enabled board.

The Mbed OS source code is available on [GitHub](https://github.com/ARMmbed/mbed-os) and on our [release page](https://os.mbed.com/releases/).

## Profiles and RTOS

The **full profile** of Mbed OS is an RTOS (it includes [Keil RTX](https://www2.keil.com/mdk5/cmsis/rtx) and all RTOS APIs), so it supports deterministic, multithreaded, real-time software execution. The RTOS primitives are always available, allowing drivers and applications to rely on threads, semaphores, mutexes and other RTOS features. It also includes all APIs by default, although you can remove unused ones at build time.

The **bare metal profile** doesn't include Keil RTX and is therefore not an RTOS - it is designed for applications that do not require complex thread management. It is also designed for constrained devices, and therefore focuses on minimizing the size of the final application: by default, it includes only the smallest possible set of APIs, to which you can manually add APIs that your application requires. The bare metal profile can use the small C libraries (which are not thread safe) to further minimize the size of the application. Mbed 2 users who want to move to Mbed OS 6 should use the bare metal profile.

## Licensing

We release Mbed OS under an Apache 2.0 license, so you can confidently use it in commercial and personal projects. For more information about licensing, please see [our licensing documentation](../contributing/license.html).

## Getting started

Our [quick start](../quick-start/index.html) guides show how to build an example application for both the full profile and bare metal profile, with Mbed Studio, Keil Studio and Mbed CLI.

| [Build with Mbed Studio](https://os.mbed.com/docs/mbed-studio/current/getting-started/index.html) | [Build with Keil Studio](https://developer.arm.com/documentation/102497/1-5/Tutorials/Get-started-with-an-Mbed-OS-Blinky-example) | [Build with Mbed CLI 1](../quick-start/build-with-mbed-cli.html) |
| --- | --- | --- |
| Download our dedicated desktop IDE, including all the necessary tools to work with Mbed OS. <br>This link will take you to the Mbed Studio documentation site. | Replaces the Mbed Online Compiler. Our zero-installation web IDE to explore Mbed OS and CMSIS; great for rapid prototyping and education. <br>This link will take you to Arm Developer | Command-line tool requiring manual setup of tools, but providing the greatest degree of flexibility. |

## Recently updated documentation

- Mbed Online Compiler replaced by Keil Studio.
