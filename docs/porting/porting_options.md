# mbed OS 5.0 Porting Guide

To port mbed OS 5.0 to your device, you need to:

1. [Port the OS core](Core_port.md). The easiest way to port is to [copy definitions from another device](#copying-from-an-existing-device). If you cannot find a suitable source to copy from, you'll have to do a [full port](#porting-from-scratch).
1. Port the [security modules](#security-releated-porting).
1. Port the [connectivity modules](#connectivity-related-porting) your hardware needs.

Please use the [mbed CLI](../Build_Tools/CLI.md) build system and [test as you work](../Testing/Porting.md).


## Porting option 1: copying from an existing device

The process for porting a new device from an existing one:

1. **Derivative target definitions:** your source device provides a set of definitions that form an mbed OS target. You may have to edit some of them to match your own device.
1. **Peripheral configuration:** edit definitions for pin names, external xtal and so on.
1. [Use Greentea to test](../Testing/Porting.md) your port.

## Porting option 2: from scratch

If there is no device to copy from, you'll have to do a [full port](Core_port.md):

1. Port [CMSIS-CORE](CMSIS_CORE.md).
1. Port [mbed HAL](HAL.md).
1. Port [mbed RTOS](RTOS.md) (based on CMSIS-RTOS standard).
1. [Use Greentea to test](../Testing/Porting.md) your CMSIS, HAL and RTOS ports.

The full process is [here](Core_port.md).

## Security related porting

When you have the mbed OS core working, port the security modules:

- [uVisor](../uVisor/Porting.md).
- [mbed TLS](../TLS/Porting.md).

## Connectivity related porting

Depending on what your hardware offers, port one or more of the connectivity modules:

- [BLE](../Connect/BLE.md).
- Ethernet and WiFi through the [Network Socket API](../Connect/Network_Socket.md).
- [15.4 for 6LoWPAN/Thread](../Connect/15_4.md).


## Testing your port

See the [Greentea page](../Testing/Porting.md) for more information.

## mbed OS concepts

### Targets

A target is mbed OS's abstraction for different hardware. When you build mbed OS you always build it for a specific target, using the target's defined toolchain and macros. You use the mbed Configuration System (below) to create a target.

For more information, see the [Targets page](Targets.md).

### Memory model

This is a basic overview of the memory model.

#### Threads

Each thread of execution in the RTOS has a separate stack. When you use the RTOS, before explicitly initializing any additional thread, you will have four separate stacks:

* The stack of the Main Thread (executing the main function).
* The Idle Thread executed each time all the other threads are waiting for external or scheduled events. This is particularly useful for implementing energy saving strategies (like sleep).
* The Timer Thread that executes all the time-scheduled tasks (periodic and non-periodic).
* The stack of OS Scheduler itself (also used by the ISRs).

Collisions between the main thread stack and heap can occur. Stack checking is turned on for application-defined threads and the kernel will error if an overflow condition is detected.

```
+-------------------+   Last Address of RAM
| Scheduler Stack   |
+-------------------+
| Main Thread Stack |
|         |         |
|         v         |
+---- GUARD WORD ---+
|                   |   RAM
|                   |
|         ^         |
|         |         |
|    Heap Cont..    |
+-------------------+
| app thread n      |
|-------------------|
| app thread 2      |
|-------------------|
| app thread 1      |
|-------------------|
|         ^         |
|         |         |
|       Heap        |
+-------------------+
| ZI                |
+-------------------+
| ZI: OS drv stack  |
+-------------------+
| ZI: app thread 3  |
+-------------------+
| ZI: Idle Stack    |
+-------------------+
| ZI: Timer Stack   |
+-------------------+
| RW                |  
+===================+   First Address of RAM
|                   |
|                   |   Flash

```

### Bootstrap Process

From a reset state the following hooks and conditions are expected.

* `ResetHandler` - vector table entry at start of Flash [main stack pointer].
* `SystemInit` - imported from CMSIS-CORE [main stack pointer].
* RW / ZI initialization [main stack pointer].
* `mbed_sdk_init` - used for HAL initialization [main stack pointer].
* `osKernelInitialize` - starts kernel and scheduler [main stack pointer].
* `pre_main` - C++ static initializers [process stack pointer].
* `mbed_main` - application hook before main [process stack pointer].
* `main` - application entry point [process stack pointer].

### Configuration system

The mbed configuration system customizes the compile time configuration of mbed components: targets, libraries and applications.

For more information, see the [Configuration System page](Config_sys.md).
