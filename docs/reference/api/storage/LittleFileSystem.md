## LittleFileSystem

The little filesystem is a fail-safe filesystem designed for embedded systems.

```
   | | |     .---._____
  .-----.   |          |
--|o    |---| littlefs |
--|     |---|          |
  '-----'   '----------'
   | | |
```

**Bounded RAM/ROM** - The littlefs is designed to work with a limited amount
of memory. Recursion is avoided, and dynamic memory is limited to configurable
buffers that can be provided statically.

**Power-loss resilient** - The littlefs is designed for systems that may have
random power failures. The littlefs has strong copy-on-write guarantees, and
storage on disk is always kept in a valid state.

**Wear leveling** - Because the most common form of embedded storage is erodible
flash memories, littlefs provides a form of dynamic wear leveling for systems
that cannot fit a full flash translation layer.

### LittleFileSystem class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_f_a_t_file_system.html)

### LittleFileSystem example

[Add example here.]
