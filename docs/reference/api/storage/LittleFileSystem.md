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

Microcontrollers and flash storage present three challenges for embedded storage: [power loss](#power-loss-resilience), [wear](#wear-leveling) and [limited RAM and ROM](#bounded-ram-and-rom). LittleFS provides a solution to all three of these problems.

#### Power loss resilience

Microcontroller-scale embedded systems are usually without a shutdown routine and notably lack a user interface for recovery. With a file system that is not resilient to power loss, you rely on luck to not end up with a corrupted file system. The combination of persistent storage and unpredictable power loss creates bugs that are difficult to notice and ruin the experience of unlucky users.

We built LittleFS with a structure that is resilient to power loss. It uses checksums to limit the assumptions of how the physical storage reacts to power loss. LittleFS provides copy-on-write guarantees and keeps the storage on disk in a valid state.

#### Wear leveling

Flash storage presents its own challenge: wear. Flash is a destructive form of storage, and continuously rewriting data to a block causes that block to wear out and become unwritable. File systems that don't account for wear can quickly burn through the blocks that store frequently updated metadata and result in the premature death of the system.

We accounted for wear when we built LittleFS, and the underlying structure of the file system reactively mutates as the underlying storage develops errors throughout its lifetime. This results in a form of dynamic wear-leveling that extends the lifetime of the physical storage proportionally to the size of storage. With LittleFS, you can extend the lifetime of storage by increasing the size of storage, which is cheaper than upgrading the storage's erase cycles.

#### Bounded RAM and ROM

File systems normally target operating systems where the scale of resources available is foreign to a microcontroller. A common trend of embedded Linux file systems is RAM usage that scales linearly with the size of storage, which makes rationalizing RAM usage in a system difficult.

We optimized LittleFS to work with a limited amount of RAM and ROM. LittleFS avoids recursion and limits dynamic memory to configurable buffers. At no point during operation does LittleFS store an entire storage block in RAM. The result is small RAM usage that is independent of the geometry of the underlying storage.

---

The "little" in the little file system comes from the focus on both keeping resource usage low and keeping the scope self-contained. Aside from the three targeted issues above, there is a heavy restriction against bloat in this software module. Instead, additional features are pushed separate layers in the powerful [BlockDevice API](TODO LINK ME) that drives the Mbed OS storage stack. This gives Mbed OS a tool for remaining flexible as technology used by IoT devices develops.

### When to use LittleFS

LittleFS is intended for microcontrollers with external flash storage. In this context, LittleFS outperforms the other Mbed OS file systems in terms of RAM, ROM, wear and runtime.

For storage on an SD card that is accessable from a PC, use the [FATFileSystem](TODO LINK ME) due to its portability.

For internal flash, LittleFS is compatible with the [flash IAP driver](https://github.com/ARMmbed/flashiap-driver), and developers have used it successfully in several projects. However, in size and erase cycles, internal flash is more expensive than external flash, and internal flash comes with the cost of locking up the system during erase cycles. For these reasons, we discourage internal flash for general storage use.

### How LittleFS works

The features of LittleFS affect the structure of the file system. At its core, LittleFS provides resilience against power loss resilience and wear leveling. Because these features are part of the structure of the file system, they come with little resource cost.

You can find the low-level mechanics of LittleFS in the [implementation details](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/littlefs/littlefs/DESIGN.md) in Mbed OS.

### How we know LittleFS works

The guarantees LittleFS claims are bold. To reinforce these claims, a series of different testing layers keep LittleFS in check:

1. [Local, simulated functional tests](https://github.com/ARMmbed/mbed-os/tree/master/features/filesystem/littlefs/littlefs/tests).
1. [On device, functional filesystem tests](https://github.com/ARMmbed/mbed-os/tree/master/features/filesystem/littlefs/TESTS/filesystem).
1. [On device, functional retargeted filesystem tests](https://github.com/ARMmbed/mbed-os/tree/master/features/filesystem/littlefs/TESTS/filesystem_retarget).
1. [On device, simulated atomicity tests](https://github.com/ARMmbed/mbed-os/tree/master/features/filesystem/littlefs/TESTS/filesystem_recovery/resilience).
1. [On device, simulated wear leveling tests](https://github.com/ARMmbed/mbed-os/tree/master/features/filesystem/littlefs/TESTS/filesystem_recovery/wear_leveling).
1. [On device, power-loss tests](https://github.com/ARMmbed/mbed-os/tree/master/features/filesystem/littlefs/TESTS/filesystem_recovery/resilience_functional).
1. [On device, long-running SOAK tests](https://github.com/ARMmbed/mbed-littlefs-soaktest).

### How to use LittleFS

If you have a project using a different Mbed OS file system, switching to LittleFS is as easy as changing the class name to `LittleFileSystem`.

The API that LittleFS presents is the standard Mbed OS file system API with few changes. Once declared, Mbed OS provides the retargeting layer for the standard C library.

### LittleFileSystem class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_f_a_t_file_system.html)

### LittleFileSystem configuration options

LittleFS provides several configuration options that the configuration system or the `LittleFileSystem` constructor can override:

- `littlefs.read_size`

  Minimum size of a block read. This determines the size of read buffers. This may be larger than the physical read size to improve performance by caching more of the block device.

  By default, this is set to 64 bytes, which we determined experimentally. Note that LittleFS uses the block device's read size if it is larger.

- `littlefs.prog_size`

  Minimum size of a block program. This determines the size of the program buffers. This may be larger than the physical program size to improve performance by caching more of the block device.

  By default, this is set to 64 bytes, which we determined experimentally. Note that LittleFS uses the block device's program size if it is larger.

- `littlefs.block_size`

  Minimum size of an erasable block. This does not affect RAM consumption and may be larger than the physical erase size. However, this needs to be small because each file takes up an entire block.

  By default, this is set to 512 bytes. Note that LittleFS uses the block device's erase size if it is larger.

- `littlefs.lookahead_size`

  Number of blocks to lookahead during block allocation. A larger lookahead reduces the number of passes required to allocate a block. The lookahead buffer requires only 1 bit per block, so it can be large with little effect on RAM. This is a multiple of 32.

  By default, this is set to 512 blocks (which use 64 bytes of RAM), which we determined experimentally.

- `littlefs.enable_info`

  Enables information logging (true = enabled, false = disabled, null = disabled) in release builds.

  By default, information logging is disabled.

- `littlefs.enable_debug`

  Enables debug logging (true = enabled, false = disabled, null = disabled) in release builds.

  By default, debug logging is enabled unless you are using a release build.

- `littlefs.enable_warn`

  Enables warn logging (true = enabled, false = disabled, null = disabled) in release builds.

  By default, warn logging is enabled unless you are using a release build.

- `littlefs.enable_error`

  Enables error logging, true = enabled, false = disabled, null = disabled
  only in release builds

  By default, error logging is enabled unless in a release build.

### LittleFileSystem example

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-littlefs)
