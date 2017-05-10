# CMSIS & RTX

CMSIS/RTX code is imported from the original CMSIS repository which can be found: https://github.com/ARM-software/CMSIS_5/

## Memory considerations

Please note that mbed OS doesn't use any of the RTX memory models, which are based on static carveouts (memory pools). This approach is not ideal for generic system like mbed OS as calculating required numbers of RTOS objects is impossible. To avoid declaring arbitrary large buffers, carved out on compile time, limiting amount of available memory, mbed OS shifts the responsibility of supplying the backing memory to CMSIS-RTOS2 users.

Therefore developers will need to use mbed OS RTOS C++ API or supply backing memory for RTX objects to `os*New` calls when using CMSIS-RTOS2 APIs directly (please consult CMSIS-RTOS2 documentation for API details). `mbed_rtos_storage.h` header provides handy wrappers that can be used to secure required memory without exposing the code to RTX implementation details.

## Configuration

mbed OS changes to RTX configuration are all maintained in a single file: `mbed-os/rtos/rtx2/mbed_rtx_conf.h`

Option | Value | Description |
-------|-------|-------------|
OS_STACK_SIZE | 4K or 2K | For normal target the thread stack size is set to 4K for constrained targets it's 2K |
OS_TIMER_THREAD_STACK_SIZE | 768B | Timer thread stack set to 768B that's necessary to support our C++ wrappers (4 instances), but may require changing to support larger number of active timers |
OS_IDLE_THREAD_STACK_SIZE | 256B | Required to handle mbed OS wrappers |
OS_DYNAMIC_MEM_SIZE | 0 | RTX dynamic memory is disabled |
OS_MUTEX_OBJ_MEM | 1 or 0 | For ARMC we use 1, for other toolchains it's 0. ARMC uses statically allocated mutexes internally. |
OS_MUTEX_NUM | 6 or 0 | For ARMC we use 6, for other toolchains it's 0. ARMC uses statically allocated mutexes internally. |
OS_STACK_WATERMARK | 0 or 1 | Watermarking enabled if MBED_STACK_STATS_ENABLED or MBED_STACK_STATS_ENABLED are set. |
OS_PRIVILEGE_MODE | 0 or 1 | We set it for 0 if uVisor is enabled, 1 otherwise. |


## Code structure

Due to differences in how mbed OS and CMSIS directory structures look like, we can't import the original code directly, some directory changes are necessary:

CMSIS5 | mbed OS | Explanation |
-------|---------|-------------|
CMSIS_5/CMSIS/Core/Include/core_*.h | mbed-os/cmsis/ | Core specific code |
CMSIS_5/CMSIS/Core/Include/tz_context.h | mbed-os/cmsis/ | TrustZone code |
CMSIS_5/CMSIS/Core/Include/cmsis_compiler.h | mbed-os/cmsis/ | Toolchain generic code |
CMSIS_5/CMSIS/Core/Include/cmsis_{armcc,armclang,gcc}.h | mbed-os/cmsis/TOOLCHAIN_{ARM,GCC}/ | Toolchain specific code |
CMSIS_5/CMSIS/RTOS2/Include/cmsis_os2.h | mbed-os/rtos/rtx2/TARGET_CORTEX_M/ | RTX main header |
CMSIS_5/CMSIS/RTOS2/RTX/Config/ | mbed-os/rtos/rtx2/TARGET_CORTEX_M/ | RTX configuration files |
CMSIS_5/CMSIS/RTOS2/RTX/Include1/ | mbed-os/rtos/rtx/ | RTOS1 compatibility layer |
CMSIS_5/CMSIS/RTOS2/RTX/Include/ | mbed-os/rtos/rtx2/TARGET_CORTEX_M/ | RTX definitions |
CMSIS_5/CMSIS/RTOS2/RTX/Source/rtx_* | mbed-os/rtos/rtx2/TARGET_CORTEX_M/ | RTX sources |
CMSIS_5/CMSIS/RTOS2/RTX/Source/svc_user.c | mbed-os/rtos/rtx2/TARGET_CORTEX_M/ | RTX SVC user table |
CMSIS_5/CMSIS/RTOS2/RTX/Source/{ARM,GCC,IAR}/| mbed-os/rtos/rtx2/TARGET_CORTEX_M/TARGET_{M0,M0P,M3,RTOS_M4_M7}/TOOLCHAIN_{ARM,GCC,IAR} | Toolchain and core specific exception handlers |

## Modification

Due to different use cases between mbed OS and CMSIS, we had to make some modifications to the source code. We've tried to upstream our changes to CMSIS repository, but in cases where they weren't compatible with CMSIS requirements we are forced to maintain small set of changes.

### CMSIS


Filename | Description |
---------|-------------|
cmsis_compiler.h | Added IAR missing __ALIGNED attribute for earlier (less than 7.8.4) versions |


### RTX

Filename | Description |
---------|-------------|
cmsis_os2.h | Doxygen added; added per-thread uVisor context |
cmsis_os1.h | Change `osThreadDef` to accept 3 parameters, rather than 4, and be not static as expected by mbed OS |
core_cm.h | Doxygen added; included headers changed to match mbed OS core selection; deferred priority setting of SVCall to uVisor, when uVisor is enabled |
RTX_Config.h | Doxygen added, mbed OS RTX config included |
rtx_evr.c | CMSIS component definition include removed |
rtx_evr.h | Doxygen added |
rtx_thread.c | Added per-thread uVisor context; notify uVisor of OS events  |
rtx_kernel.c | Added per-thread uVisor context; notify uVisor of OS events |
rtx_lib.h | Doxygen added; added per-thread uVisor context |
rtx_os.h | Doxygen added; added per-thread uVisor context |
irq_cm4.s | For all toolchains: added case for Cortex M4 cores without VFP |
svc_user.c | Removed as it's template file and should not be in our code base |
rt_OsEventObserver.{c,h} | Added an interface for uVisor to get notified about certain events from privileged code |

#### Other

* irq_cm0.s is used for both M0 and M0P cores in mbed OS for all toolchains
