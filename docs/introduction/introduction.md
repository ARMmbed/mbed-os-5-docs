# An introduction to Arm Mbed OS 6
<!--I don't like the structure here-->
Mbed OS is an open-source operating system for Internet of Things (IoT) Cortex-M boards: low-powered, constrained and connected. Mbed OS provides an abstraction layer for the microcontrollers it runs on, so that developers can write C/C++ applications that run on any Mbed-enabled board.<!--device is a problematic terms, because Keil uses it to mean something very specific, so going with "board"-->

The Mbed OS source code is available on [GitHub](https://github.com/ARMmbed/mbed-os) and on our [release page](https://os.mbed.com/releases/).

## Profiles and RTOS<!--clumsy title--><!--maybe it doesn't even need a title?-->

The **full profile** of Mbed OS is an RTOS (it includes an RTX and all RTOS APIs), so it supports deterministic, multithreaded, real-time software execution. The RTOS primitives are always available, allowing drivers and applications to rely on threads, semaphores, mutexes and other RTOS features. It also includes all APIs by default, although you can remove unused ones at build time.

The **bare metal profile** doesn't include an RTX and is therefore not an RTOS - it is designed for applications that do not require complex thread management. It is also designed for constrained devices, and therefore focuses on minimising the size of the final application: by default, it includes only the smallest possible set of APIs, to which you can manually add APIs your application requires. The bare metal profile can use the small C libraries (which are not thread safe) to further minimise the size of the application.
<!--too many "designed" and "minimze" and the sentences are really long-->

## Licensing

We release Mbed OS under an Apache 2.0 license, so you can confidently use it in commercial and personal projects. For more information about licensing, please see [our licensing documentation](../contributing/license.html).

## Getting started

Our [quick start](../quick-start/index.html) guides show how to build an example application for both the full profile and bare metal profile, on Mbed CLI, Mbed Studio and the Mbed Online Compiler.

| [Build with Mbed Studio](https://os.mbed.com/docs/mbed-studio/current/getting-started/index.html) | [Build with Mbed Online Compiler](../quick-start/build-and-debug-with-the-online-compiler.html) |  [Build with Mbed CLI](../quick-start/build-and-debug-with-mbed-cli.html) |
| --- | --- | --- |
| Download our dedicated desktop IDE, including all the necessary tools to work with Mbed OS. <br>This link will take you to the Mbed Studio documentation site. | Zero-installation web IDE to explore Mbed OS; great for rapid prototyping and education. | Command-line tool requiring manual setup of tools, but providing the greatest degree of flexibility. |


## Recently updated documentation

<!--bare metal, list of deprecated APIs, new API structure, porting updates...-->

- New API references for [BufferedSerial](../apis/bufferedserial.html) and [UnbufferedSerial](../apis/unbufferedserial.html).
- New content about [using small C libraries in Mbed OS bare metal](../reference/using-small-c-libraries.html).
- A guide to [porting a custom board](../porting/derivative-port.html).
- A porting guide for the [static pin map extension](../porting/static-pinmap-port.html).
- The [UserAllocatedEvent](../apis/userallocatedevent.html) API reference.
