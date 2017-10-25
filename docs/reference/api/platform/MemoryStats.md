## MemoryStats

Mbed-OS provides a set of functions which can be used to capture the memory stats at runtime. These functions are declared in mbed_stats.h. Memory stats functions can be used capture heap usage, cumulative stack usage or stack usage per thread at runtime. In order to enable memory usage monitoring Mbed-OS must be built with following macros.

MBED_MEM_TRACING_ENABLED
MBED_HEAP_STATS_ENABLED
MBED_STACK_STATS_ENABLED

### MemoryStats functions reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/group__platform__stats.html)

### MemoryStats example

[![View Example](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-platform-utils)](https://github.com/ARMmbed/mbed-os-example-platform-utils) 
