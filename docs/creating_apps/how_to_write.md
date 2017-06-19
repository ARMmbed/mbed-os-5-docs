## Introduction to the mbed OS API 

mbed OS lets you write applications that run on embedded devices, by providing the layer that interprets your application's code in a way the hardware can understand.

Your application code is written in C++. It uses the application programing interfaces (APIs) that mbed OS provides. These APIs allow your code to work on different microcontrollers in a uniform way. This reduces a lot of the challenges in getting started with microcontrollers and integrating large amounts of software.

<span class="tips">**Tip:** You can explore the [code on GitHub](https://github.com/ARMmbed/mbed-os/tree/mbed-os-5.5).</span>

The APIs in this document are organized by the feature, or group of features, they enable.

* [Task management](APIs/tasks/tasks.md): handling tasks and events in mbed OS.
* [Inputs and outputs](APIs/io/inputs_outputs.md): analog, digital, bus, port, PwmOut and interrupts.
* [Digital interfaces](APIs/interfaces/interfaces.md): serial, SPI, I2C and CAN.
* [Communication](APIs/communication/communication_index.md): network sockets, Ethernet, Wi-Fi, mesh networking, BLE and Cellular.
* [Security](APIs/security/security.md): working with mbed uVisor and mbed TLS in the context of mbed OS.

We also provide guidelines [for using the API documentation in the mbed Online Compiler](APIs/API_Documentation.md).
