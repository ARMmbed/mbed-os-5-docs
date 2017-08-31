## Overview of the Arm Mbed OS References

Arm Mbed OS lets you write applications that run on embedded devices, by providing the layer that interprets your application's code in a way the hardware can understand.

Your application code is written in C++. It uses the application programing interfaces (APIs) that Mbed OS provides. These APIs allow your code to work on different microcontrollers in a uniform way. This reduces a lot of the challenges in getting started with microcontrollers and integrating large amounts of software.

<span class="tips">**Tip:** You can explore the [code on GitHub](https://github.com/ARMmbed/mbed-os/tree/mbed-os-5.5).</span>

## APIs References

The APIs in this document are organized by the feature, or group of features, they enable.

* [RTOS](APIs/tasks/tasks.md): handling tasks and events in Mbed OS.
* [Drivers](APIs/io/inputs_outputs.md): analog and digital input and outputs and digital interfaces.
* [Connectivity](APIs/communication/communication_index.md): network sockets, Ethernet, Wi-Fi, mesh networking, BLE and cellular.
* [Security](APIs/security/security.md): working with Arm Mbed uVisor and Arm Mbed TLS in the context of Mbed OS.
* [Storage](): working with the file system.

We also provide guidelines [for using the API documentation in the Arm Mbed Online Compiler](APIs/API_Documentation.md).
