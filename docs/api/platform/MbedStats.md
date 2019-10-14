# Mbed statistics

Mbed OS provides a set of functions that you can use to capture the memory and thread statistics at runtime. `mbed_stats.h` declares these functions. To enable all Mbed OS platform statistics, you must enable the following Mbed OS configuration option:

```json
{
    "target_overrides": {
        "*": {
            "platform.all-stats-enabled": true
        }
    }
}
```

<span class="tips">**Tip:** See the documentation of the [Arm Mbed configuration system](../reference/configuration.html) for more details about `mbed_app.json`. </span>

## Memory statistics

You can use memory statistics functions to capture heap use, cumulative stack use or stack use for each thread at runtime. To enable memory use monitoring, you must enable the following Mbed OS configuration options:

```json
{
    "target_overrides": {
        "*": {
            "platform.heap-stats-enabled": true,
            "platform.stack-stats-enabled": true
        }
    }
}
```

<span class="notes">**Note:** Each `malloc` or `calloc` memory allocation call adds an overhead of 8 bytes when heap memory statistics are enabled.</span>

## Thread statistics

You can use the thread statistics function `mbed_stats_thread_get_each` to capture the thread ID, state, priority, name and stack information for all active threads at runtime. To enable thread monitoring, you must enable the following Mbed OS configuration options:

```json
{
    "target_overrides": {
        "*": {
            "platform.thread-stats-enabled": true
        }
    }
}
```

## System information

You can use the `mbed_stats_sys_get` function to get the CPU ID, compiler information and RAM and ROM memories on the target device. To enable system information fetching, you must enable the following Mbed OS configuration option:

```json
{
    "target_overrides": {
        "*": {
            "platform.sys-stats-enabled": true
        }
    }
}
```

## CPU statistics

You can use the `mbed_stats_cpu_get` function to get the uptime, idle time and sleep time information. Timing information available is cumulative because the system is on. Please note CPU statistics depend on the availability of the low power timer in the hardware. To enable fetching of CPU information, you must enable the following Mbed OS configuration option:

```json
{
    "target_overrides": {
        "*": {
            "platform.cpu-stats-enabled": true
        }
    }
}
```

## Mbed statistics function reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/mbed__stats_8h_source.html)

## Memory statistics example

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/mbed-os-example-platform-utils/)](https://os.mbed.com/teams/mbed_example/code/mbed-os-example-platform-utils/file/92b97ba04fd3/main.cpp)

## Thread statistics example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-thread-statistics)](https://github.com/ARMmbed/mbed-os-example-thread-statistics/blob/mbed-os-5.14/main.cpp)

## System information example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-sys-info)](https://github.com/ARMmbed/mbed-os-example-sys-info/blob/mbed-os-5.14/main.cpp)

## CPU statistics example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-cpu-stats)](https://github.com/ARMmbed/mbed-os-example-cpu-stats/blob/mbed-os-5.14/main.cpp)

## CPU usage example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-cpu-usage/)](https://github.com/ARMmbed/mbed-os-example-cpu-usage/blob/mbed-os-5.14/main.cpp)

## Related content

- [Platform configuration documentation](../apis/mbed-statistics.html).
- [Optimization tutorial](../tutorials/optimizing.html).
