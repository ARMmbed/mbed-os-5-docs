## Mbed statistics

Mbed OS provides a set of functions that you can use to capture the memory and thread statistics at runtime. `mbed_stats.h` declares these functions. To enable all Mbed OS statistics, you must build code with the `MBED_ALL_STATS_ENABLED` macro.

### Memory statistics

You can use memory statistics functions to capture heap usage, cumulative stack usage or stack usage per thread at runtime. To enable memory usage monitoring, you must build Mbed OS with the following macros:

- `MBED_HEAP_STATS_ENABLED`.
- `MBED_STACK_STATS_ENABLED`.

### Thread statistics

You can use the thread statistics function `mbed_stats_thread_get_each` to capture the thread ID, state, priority, name and stack information for all active threads at runtime. To enable thread monitoring, you must build Mbed OS with the `MBED_THREAD_STATS_ENABLED` macro.

### System information

You can use the `mbed_stats_sys_get` function to get the CPU ID and compiler information. You must build Mbed OS with the `MBED_SYS_STATS_ENABLED` macro to enable fetching of system information.

### CPU statistics

You can use the `mbed_stats_cpu_get` function to get the uptime, idle time, and sleep time information. Timing information available is cumulative since the system is up and running. You must build Mbed OS with the `MBED_CPU_STATS_ENABLED` macro to enable fetching of CPU information. Please note CPU statistics are dependent on availability of low power timer in HW.

### Mbed statistics functions reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/mbed__stats_8h_source.html)

### Memory statistics example

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/mbed-os-example-platform-utils/)](https://os.mbed.com/teams/mbed_example/code/mbed-os-example-platform-utils/file/92b97ba04fd3/main.cpp)

### Thread statistics example

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/thread_statistics/)](https://os.mbed.com/teams/mbed_example/code/thread_statistics/file/8cfc3eff0d78/main.cpp/)

### System information example

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/system_information/)](https://os.mbed.com/teams/mbed_example/code/system_information/file/8189a62cbb4e/main.cpp/)

### CPU statistics example

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/cpu_stats/)](https://os.mbed.com/teams/mbed_example/code/cpu_stats/file/de30f5166672/main.cpp/)

### CPU usage example

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/cpu_usage_calculation/)](https://os.mbed.com/teams/mbed_example/code/cpu_usage_calculation/file/358f7cf7196d/main.cpp/)
