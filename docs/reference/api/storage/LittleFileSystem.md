## LittleFileSystem

The little filesystem (LittleFS) is a fail-safe filesystem designed for embedded systems, specifically for microcontrollers that use flash storage.

```
   | | |     .---._____
  .-----.   |          |
--|o    |---| LittleFS |
--|     |---|          |
  '-----'   '----------'
   | | |
```

Microcontrollers and flash storage present three challenges for embedded storage: [power loss](#power-loss-resilience), [wear](#wear-leveling) and [limited RAM and ROM](#bounded-ram-and-rom). The LittleFS provides a solution to all three of these problems.

- **Bounded RAM/ROM** - The LittleFS works with a limited amount of memory. The LittleFS avoids recursion and limits dynamic memory to configurable buffers that can be provided statically.

- **Power-loss resilient** - The LittleFS is designed for operating systems that may have random power failures. The LittleFS has strong copy-on-write guarantees and keeps storage on disk in a valid state.

- **Wear leveling** - Because the most common form of embedded storage is erodible flash memories, the LittleFS provides a form of dynamic wear leveling for systems that cannot fit a full flash translation layer.

### When to use the LittleFS

The LittleFS is intended for microcontrollers with external flash storage. In this context, the LittleFS outperforms the other Mbed OS file systems in terms of RAM, ROM, wear and runtime.

For storage on an SD card that is accessible from a PC, use the FATFileSystem due to its portability.

For internal flash, the LittleFS is compatible with the <a href="https://github.com/ARMmbed/flashiap-driver" target="_blank">flash IAP driver</a>, and developers have used it successfully in several projects. However, in size and erase cycles, internal flash is more expensive than external flash, and internal flash comes with the cost of locking up the system during erase cycles. For these reasons, we discourage internal flash for general storage use.

### How the LittleFS works

The features of the LittleFS affect the structure of the file system. At its core, the LittleFS provides resilience against power loss resilience and wear leveling. Because these features are part of the structure of the file system, they come with little resource cost.

You can find the low-level mechanics of the LittleFS in the <a href="https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/littlefs/littlefs/DESIGN.md" target="_blank">implementation details</a> in Mbed OS.

### How we know the LittleFS works

The guarantees the LittleFS claims are bold. To reinforce these claims, a series of different testing layers keep the LittleFS in check:

1. <a href="https://github.com/ARMmbed/mbed-os/tree/master/features/filesystem/littlefs/littlefs/tests" target="_blank">Local, simulated functional tests</a>.
1. <a href="https://github.com/ARMmbed/mbed-os/tree/master/features/filesystem/littlefs/TESTS/filesystem" target="_blank">On device, functional filesystem tests</a>.
1. <a href="https://github.com/ARMmbed/mbed-os/tree/master/features/filesystem/littlefs/TESTS/filesystem_retarget" target="_blank">On device, functional retargeted filesystem tests</a>.
1. <a href="https://github.com/ARMmbed/mbed-os/tree/master/features/filesystem/littlefs/TESTS/filesystem_recovery/resilience" target="_blank">On device, simulated atomicity tests</a>.
1. <a href="https://github.com/ARMmbed/mbed-os/tree/master/features/filesystem/littlefs/TESTS/filesystem_recovery/wear_leveling" target="_blank">On device, simulated wear leveling tests</a>.
1. <a href="https://github.com/ARMmbed/mbed-os/tree/master/features/filesystem/littlefs/TESTS/filesystem_recovery/resilience_functional" target="_blank">On device, power-loss tests</a>.
1. <a href="https://github.com/ARMmbed/mbed-littlefs-soaktest" target="_blank">On device, long-running SOAK tests</a>.

### How to use the LittleFS

If you have a project using a different Mbed OS file system, switching to the LittleFS is as easy as changing the class name to `LittleFileSystem`.

The API that the LittleFS presents is the standard Mbed OS file system API with few changes. Once declared, Mbed OS provides the retargeting layer for the standard C library.

### LittleFileSystem class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_f_a_t_file_system.html)

### LittleFileSystem example

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-littlefs)
