# Writing applications with the mbed OS APIs

You can think of mbed OS as a collection of application programming interfaces (APIs). You use these APIs to control mbed OS, and mbed OS in turn controls the hardware.

mbed OS always exposes the same APIs, irrespective of the hardware on which you're working. The job of making these APIs work with different hardware is left to mbed OS itself, meaning you don't have to change your application code to have it run on any compatible hardware (this is known as "hardware agnosticism").

## APIs by feature

The APIs in this document are organized by the feature, or group of features, they enable.

* [Hardware inputs and outputs](../APIs/io/inputs_outputs.md): analog, digital, bus, port, PwmOut and interrupts.
* [Digital interfaces and USB](../APIs/interfaces/interfaces.md): serial, SPI, I2C, CAN and USB.
* [Networking and communication](../APIs/communication/communication.md): network stack, BLE, Ethernet, WiFi and radio. 
* [Device and networking security](../APIs/security/security.md): mbed uVisor and mbed TLS.
* [Task management](../APIs/tasks/tasks.md): timers and RTOS.
* [Memory and file system](...APIs/memory_files/memory_files.md): memory and file systems.
