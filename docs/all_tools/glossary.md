# Glossary

[TODO: This will need a massive edit, and additional info]


[TODO]: All below is not getting started. Maybe for porting but not handbook
## Bootstrap Process

From a reset state the following hooks and conditions are expected.

* `ResetHandler` - vector table entry at start of Flash (main stack pointer).
* `SystemInit` - imported from CMSIS-CORE (main stack pointer).
* RW/ZI initialization (main stack pointer).
* `mbed_sdk_init` - used for HAL initialization (main stack pointer).
* `osKernelInitialize` - starts kernel and scheduler (main stack pointer).
* `pre_main` - C++ static initializers (process stack pointer).
* `mbed_main` - application hook before main (process stack pointer).
* `main` - application entry point (process stack pointer).

## Configuration system

The mbed configuration system customizes the compile time configuration of mbed components: targets, libraries and applications.

For more information, see the [Configuration System page](../advanced/config_system.md).

## Memory model

This is a basic overview of the memory model.

## Targets

A target is mbed OS's abstraction for different hardware. When you build mbed OS you always build it for a specific target, using the target's defined toolchain and macros. You use the mbed Configuration System (below) to create a target.

For more information, see the [Targets page](../advanced/targets.md).

## Threads

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


