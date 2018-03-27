## LittleFileSystem

The little file system (LittleFS) is a fail-safe file system designed for embedded systems, specifically for microcontrollers that use external flash storage.

```
   | | |     .---._____
  .-----.   |          |
--|o    |---| LittleFS |
--|     |---|          |
  '-----'   '----------'
   | | |
```

Microcontrollers and flash storage present three challenges for embedded storage: power loss, wear and limited RAM and ROM. This file system provides a solution to all three of these problems.

- **Bounded RAM/ROM** - This file system works with a limited amount of memory. It avoids recursion and limits dynamic memory to configurable buffers that can be provided statically.

- **Power-loss resilient** - We have designed this for operating systems that may have random power failures. It has strong copy-on-write guarantees and keeps storage on disk in a valid state.

- **Wear leveling** - Because the most common form of embedded storage is erodible flash memories, the file system provides a form of dynamic wear leveling for systems that cannot fit a full flash translation layer.

For additional information, please see the [storage overview page](/docs/v5.8/reference/storage.html#declaring-a-file-system).

### Use cases

We built this for microcontrollers with external flash storage. In this context, it outperforms the other Mbed OS file systems in terms of RAM, ROM, wear and runtime.

For storage on an SD card that is accessible from a PC, use the FATFileSystem due to its portability.

### Usage

Instantiate the `LittleFileSystem` class with a block device and file path.

The API that this presents is the standard Mbed OS file system API. Once declared, Mbed OS provides the retargeting layer for the standard C library.

### LittleFileSystem class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/v5.8/mbed-os-api-doxy/class_little_file_system.html)

### LittleFileSystem example

[![View code](https://www.mbed.com/embed/?url=https://github.com/armmbed/mbed-os-example-filesystem)](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-filesystem/file/8e251d9511b8/main.cpp)
