## Mbed Stats

Mbed OS provides a set of functions that you can use to capture the memory and thread statistics at runtime. `mbed_stats.h` declares these functions. To enable all Mbed OS statistics, you must build code with `MBED_ALL_STATS_ENABLED` macro.

### Memory Stats
You can use memory statistics functions to capture heap usage, cumulative stack usage or stack usage per thread at runtime. To enable memory usage monitoring, you must build Mbed OS with the following macros.

- `MBED_HEAP_STATS_ENABLED`.
- `MBED_STACK_STATS_ENABLED`.

### Thread Stats
You can use thread statistics function `mbed_stats_thread_get_each` to capture thread ID, state, priority, name and stack information for all active threads at runtime. To enable thread monitoring, you must build Mbed OS with `MBED_THREAD_STATS_ENABLED` macro.

### Mbed Stats functions reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/mbed__stats_8h_source.html)

### Memory Stats example

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/mbed-os-example-platform-utils/)](https://os.mbed.com/teams/mbed_example/code/mbed-os-example-platform-utils/file/92b97ba04fd3/main.cpp)

### Thread Stats example

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/thread_statistics/)](https://os.mbed.com/teams/mbed_example/code/thread_statistics/file/8cfc3eff0d78/main.cpp/)
