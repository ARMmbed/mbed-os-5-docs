## LittleFileSystem

The little filesystem (littlefs) is a little fail-safe filesystem designed
for embedded systems, specifically microcontrollers using flash storage.

```
   | | |     .---._____
  .-----.   |          |
--|o    |---| littlefs |
--|     |---|          |
  '-----'   '----------'
   | | |
```

Microcontrollers and flash storage preset three big challenges for embedded
storage: [power-loss](#power-loss-resilient), [wear](#wear-leveling), and
[limited RAM and ROM](#bounded-ram-and-rom). The littlefs provides a solution
to all three of these problems.

### Power-loss resilient

Embedded systems are usually designed without a shutdown routine and the notable
lack of a user interface for recovery. With a filesystem that is not resilient
to power-loss, you rely on luck to not end up with a corrupted filesystem.
The combination of persistent storage and unpredictable power-loss creates
difficult to notice bugs that will ruin the user-experience of unlucky users.

The littlefs is built from the ground up with a power-loss resilient structure
that uses checksums to limit the assumptions of how the physical storage reacts
under power-loss. The littlefs provides strong copy-on-write guaruntees and
always keeps the storage on disk in a valid state.

### Wear leveling

Flash storage presents its own unique challenge: Wear. Flash is a
destructive form of storage, and continuously rewriting data to a block
will cause that block to wear out and become unwritable. Filesystems that
don't take wear into account can quickly burn through the blocks were
frequently updated metadata is stored and result in the premature death
of the system.

The littlefs is built with wear in mind and the underlying structure
of the filesystem reactively mutates as the underlying storage develops
errors over its lifetime. This results in a form of dynamic wear-leveling
that extends the lifetime of the physical storage proportionally to the
size of storage. With littlefs, the lifetime of storage can always be extended
by increasing the size of storage, which is a much cheaper than upgrading the
erase cycles on storage.

### Bounded RAM and ROM

The scale of resources available to microcontrollers is foreign to the types
of systems filesystems are normally targetting. A common trend of embedded
Linux filesystems is RAM usage that scales linearly with the size of storage,
which makes rationalizing RAM usage in a system difficult.

The littlefs is built to work with a very limited amount of memory. Recursion
is avoided and dynamic memory is limited to configurable buffers. At no point
during operation does littlefs store an entire storage block in RAM. The result
is small RAM usage that is completely independent of the geometry of the
underlying storage.

---

The little in littlefs comes from the focus on both keeping resource usage
low and keeping the scope self-contained. Aside from the three targeted issues
above, there is a heavy restriction against bloat in this software module.
Instead, additional features are pushed separate layers in the powerful
[block device API](TODO LINK ME) that drives the Mbed OS storage stack.
This gives Mbed OS a powerful tool for remaining flexible as technology
used by IoT devices develops.

### When should I use the littlefs?

The littlefs is intended for microcontrollers with external flash storage.
In this context, littlefs out-performs the other Mbed OS filesystems in
terms of RAM, ROM, wear, and runtime.

For storage on an SD card that is accessable from a PC, you would be better
off using the [FAT filesystem](TODO LINK ME) due to its portability.

For internal flash, littlefs is compatible with the
[flash IAP driver](https://github.com/ARMmbed/flashiap-driver) and has been
used successfully on several projects. However, in terms of size and erase
cycles, internal flash is much more expensive than external flash, and comes
with the cost of completely locking up the system during erase cycles. For
these reasons internal flash is discouraged for general storage use.

### How does littlefs work?

For a high-level view, the features of littlefs are baked into the structure
of the filesystem. At its core, littlefs is built around providing power-loss
resilience and wear leveling as a side-effect of the littlefs filesystem
structure. Because these features are baked into the structure of the
filesystem, they come with very little resource cost.

For a low-level view, the mechanics that makes littlefs tick can be found in
the [implementation details](https://github.com/ARMmbed/mbed-os/blob/master/features/filesystem/littlefs/littlefs/DESIGN.md)
in Mbed OS.

### How do we know littlefs works?

The gauruntees littlefs claims are bold. To back up these claims, littlefs is
checked by a series of different testing layers:

1. [Local, simulated functional tests](https://github.com/ARMmbed/mbed-os/tree/master/features/filesystem/littlefs/littlefs/tests)
1. [On device, functional filesystem tests](https://github.com/ARMmbed/mbed-os/tree/master/features/filesystem/littlefs/TESTS/filesystem)
1. [On device, functional retargeted filesystem tests](https://github.com/ARMmbed/mbed-os/tree/master/features/filesystem/littlefs/TESTS/filesystem_retarget)
1. [On device, simulated atomicity tests](https://github.com/ARMmbed/mbed-os/tree/master/features/filesystem/littlefs/TESTS/filesystem_recovery/resilience)
1. [On device, simulated wear leveling tests](https://github.com/ARMmbed/mbed-os/tree/master/features/filesystem/littlefs/TESTS/filesystem_recovery/wear_leveling)
1. [On device, power-loss tests](https://github.com/ARMmbed/mbed-os/tree/master/features/filesystem/littlefs/TESTS/filesystem_recovery/resilience_functional)
1. [On device, long-running SOAK tests](https://github.com/ARMmbed/mbed-littlefs-soaktest)

### How do I use littlefs?

If you have a project using a different Mbed OS filesystem, switching to
littlefs is as easy as changing the class name to `LittleFileSystem`.

The API presented by littlefs is the standard Mbed OS filesystem API with
few changes. Once declared, Mbed OS provides the retargeting layer for
the standard C library. See the [FileSystem docs](TODO LINK ME) for more
info on the filesystem API in Mbed OS.

### LittleFileSystem class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_f_a_t_file_system.html)

### LittleFileSystem config options

The littlefs provides several config options that can be overridden through
the [config system](TODO LINK ME) or the `LittleFileSystem` constructor:

- `littlefs.read_size`

  Minimum size of a block read. This determines the size of read buffers.
  This may be larger than the physical read size to improve performance by
  caching more of the block device.

  By default this is set to 64 bytes, which was determined expirementally.
  Note that littlefs will use the block device's read size if it is larger.

- `littlefs.prog_size`

  Minimum size of a block program. This determines the size of program buffers.
  This may be larger than the physical program size to improve performance by
  caching more of the block device.

  By default this is set to 64 bytes, which was determined expirementally.
  Note that littlefs will use the block device's program size if it is larger.

- `littlefs.block_size`

  Minimum size of an erasable block. This does not impact RAM consumption and
  may be larger than the physical erase size. However, this should be kept
  small as each file currently takes up an entire block.

  By default this is set to 512 bytes. Note that littlefs will use the block
  device's erase size if it is larger.

- `littlefs.lookahead_size`

  Number of blocks to lookahead during block allocation. A larger lookahead
  reduces the number of passes required to allocate a block. The lookahead
  buffer requires only 1 bit per block so it can be quite large with little
  RAM impact. Should be a multiple of 32.

  By default this is set to 512 blocks (which uses 64 bytes of RAM), which
  was determined expirementally.

- `littlefs.enable_info`

  Enables info logging, true = enabled, false = disabled, null = disabled
  only in release builds

  By default, info logging is disabled.

- `littlefs.enable_debug`

  Enables debug logging, true = enabled, false = disabled, null = disabled
  only in release builds

  By default, debug logging is enabled unless in a release build.

- `littlefs.enable_warn`

  Enables warn logging, true = enabled, false = disabled, null = disabled
  only in release builds

  By default, warn logging is enabled unless in a release build.

- `littlefs.enable_error`

  Enables error logging, true = enabled, false = disabled, null = disabled
  only in release builds

  By default, error logging is enabled unless in a release build.

### LittleFileSystem example

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-littlefs)
