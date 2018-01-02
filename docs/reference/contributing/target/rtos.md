### RTOS

CMSIS/RTX code is imported from <a href="https://github.com/ARM-software/CMSIS_5/" target="_blank">the upstream CMSIS repository (develop branch)</a> with the help of a Python script in the `mbed-os` repository `mbed-os\tools\importer\importer.py`.

#### Memory considerations

Please note that Arm Mbed OS doesn't use any of the RTX memory models, which are based on static carveouts (memory pools). This approach is not ideal for platform operating systems, such as Mbed OS, because calculating required numbers of RTOS objects is impossible. To avoid declaring arbitrary large buffers carved out at compile time, limiting the amount of available memory, Mbed OS shifts the responsibility of supplying the backing memory to CMSIS-RTOS2 users.

Developers need to use the Mbed OS RTOS C++ API or supply backing memory for RTX objects to `os*New` calls when using CMSIS-RTOS2 APIs directly. (Please consult CMSIS-RTOS2 documentation for API details.) The `mbed_rtos_storage.h` header provides wrappers that you can use to secure required memory without exposing the code to RTX implementation details.

#### Configuration

Mbed OS changes to RTX configuration all exist in a single file: `mbed-os/rtos/TARGET_CORTEX/mbed_rtx_conf.h`

Option | Value | Description |
-------|-------|-------------|
`OS_STACK_SIZE` | 4K | OS Stack size is set as `MBED_CONF_APP_THREAD_STACK_SIZE` which is 4096 as default. |
`OS_TIMER_THREAD_STACK_SIZE` | 768B | Timer thread stack set to 768B that's necessary to support the C++ wrappers (4 instances), but it may require changing to support larger number of active timers. |
`OS_IDLE_THREAD_STACK_SIZE` | 512B | Required to handle Mbed OS wrappers |
`OS_DYNAMIC_MEM_SIZE` | 0 | RTX dynamic memory is disabled. |
`OS_TICK_FREQ` | 1000 | OS Tickrate must be 1000 for system timing. |
`OS_STACK_WATERMARK` | 0 or 1 | Watermarking is enabled if `MBED_STACK_STATS_ENABLED` or `MBED_STACK_STATS_ENABLED` are set. |
`OS_PRIVILEGE_MODE` | 0 or 1 | We set it for 0 if uVisor is enabled, 1 otherwise. |

#### Code structure

Due to differences in the Mbed OS and CMSIS directory structure, you can't import the original code directly. You should use the `importer.py` and configuration file `cmsis_importer.json` to import upstream CMSIS code.

#### Modification

Due to different use cases between Mbed OS and CMSIS, we modified the source code. We upstream our changes to the CMSIS repository, but in cases when they aren't compatible with CMSIS requirements, we maintain a small set of changes. We maintain changes as separate commits in `mbed-os`, and SHAs are in the `commit_sha` section of the `cmsis_importer.json` file.
