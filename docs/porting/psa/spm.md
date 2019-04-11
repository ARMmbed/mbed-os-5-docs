<h1 id="spm-port">PSA SPM</h1>

Secure Partition Manager (SPM) is a part of the PSA Firmware Framework that is responsible for isolating software in partitions, managing the execution of software within partitions and providing inter-process communication (IPC) between partitions.

For more information about SPM, please see the [SPM API page](../apis/security.html).

<span class="notes">This page gives guidelines for silicon partners adding SPM capabilities.</span>

## New target configuration

### Platform types

For information about the platform types supported by the Mbed implementation of PSA, see [Platform types](../apis/security.html).

### Defining a PSA-compliant target in targets.json

When adding a new target, add a new root target node to the `mbed-os/targets/targets.json` file. For PSA support, define specific PSA-related fields for this target:

- A secure target must inherit from the `SPE_Target` metatarget.
- A nonsecure target must inherit from `NSPE_Target`.
- Only for multicore architectures:
   - Both targets must add the `SPM_MAILBOX` component. You can read more about the mailbox mechanism in the [mailbox section](#mailbox).
   - Both targets must override the default configuration by specifying flash RAM and shared RAM regions. The [memory layout section](#memory-layout) explains this in more detail.
   - The secure target must declare its corresponding nonsecure target using the `deliver_to_target` field.

The example below demonstrates:

```json
"SPM_SECURE_CORE_PSA": {
        "inherits": ["SPE_Target"],
        "components_add": ["SPM_MAILBOX"],
        "deliver_to_target": "SPM_NONSECURE_CORE_PSA",
        "overrides": {
            "secure-rom-start": "0x10000000",
            "secure-rom-size": "0x78000",
            "non-secure-rom-start": "0x10080000",
            "non-secure-rom-size": "0x78000",
            "secure-ram-start": "0x08000000",
            "secure-ram-size": "0x10000",
            "non-secure-ram-start": "0x08011000",
            "non-secure-ram-size": "0x36800",
            "shared-ram-start": "0x08010000",
            "shared-ram-size": "0x1000"
        }
    },
    "SPM_NONSECURE_CORE_PSA": {
        "inherits": ["NSPE_Target"],
        "components_add": ["SPM_MAILBOX"],
        "overrides": {
            "secure-rom-start": "0x10000000",
            "secure-rom-size": "0x78000",
            "non-secure-rom-start": "0x10080000",
            "non-secure-rom-size": "0x78000",
            "secure-ram-start": "0x08000000",
            "secure-ram-size": "0x10000",
            "non-secure-ram-start": "0x08011000",
            "non-secure-ram-size": "0x36800",
            "shared-ram-start": "0x08010000",
            "shared-ram-size": "0x1000"
        }
    }
```

The following flags and labels must be added to each target type to add the relevant version of the source files to a compilation:

| Label/core                  | V7-single<br>(Target) | V7-dual NSPE<br>(NSPE_Target) | V7-dual SPE<br>(SPE_Target) | V8-NS<br>(NSPE_Target) | V8-S<br>(SPE_Target) |
| ----------------------        |:---------------------:|:-----------------------------:|:---------------------------:|:----------------------:|:--------------------:|
| `PSA_SRV_IMPL` (component)    | &#10003;                    |                               | &#10003;                           |                        | &#10003;                    |
| `PSA_SRV_EMUL` (component)     | &#10003;                     |                               |                             |                        |                      |
| `PSA_SRV_IPC` (component)       |                       | &#10003;                             | &#10003;                           | &#10003;                      | &#10003;                    |
| `SPE` (component)              |                       |                               | &#10003;                           |                        | &#10003;                    |
| `NSPE` (component)             | &#10003;                     | &#10003;                             |                             | &#10003;                      |                      |
| `SPM_MAILBOX` (component)      |                       | &#10003;                             | &#10003;                           |                        |                      |
| `MBED_SPM` (label)             |                       | &#10003;                             | &#10003;                           |                        |                      |
| `TFM` (label)                  |                       |                               |                             | &#10003;                      | &#10003;                    |


For more information about working with the `targets.json` file, please see [Adding and configuring targets](../reference/adding-and-configuring-targets.html).

### Memory layout

Typically, PSA platforms share the same RAM and flash between secure and nonsecure cores. To provide PSA isolation level 1 or higher, you need to partition both RAM and flash to secure and nonsecure parts, in a way the following image describes:

```text
                                 RAM
 +-----------+-------------+--------------------------------------------------+
 |   Secure  |  Shared     |     Nonsecure                                   |
 |    RAM    |   RAM       |        RAM                                       |
 +-----------+-------------+--------------------------------------------------+

                                 Flash
 +-----------------------+----------------------------------------------------+
 |   Secure              |     Nonsecure                                     |
 |    Flash              |       Flash                                        |
 +-----------------------+----------------------------------------------------+

```

To achieve RAM and flash partitioning, you must add start and size values to a target configuration in `targets.json` as in the example above.

<span class="notes">**Note:** For isolation levels higher than 1, on top of the partitioning between secure and nonsecure parts, secure flash and RAM must have an inner level of partitioning, creating sections per secure partition.</span>

## Linker script concepts

Linker scripts must include `MBED_ROM_START`, `MBED_ROM_SIZE`, `MBED_RAM_START` and `MBED_RAM_START` macros for defining memory regions. You can define a shared memory region by reserving RAM space for shared memory use. The shared memory location is target specific and depends on the memory protection scheme applied.

Typically, shared memory is located adjacent (before or after) to the nonsecure RAM, for saving MPU regions. The shared memory region is nonsecure memory that both cores use.

### Linker script example for GCC_ARM compiler

```
...
#if !defined(MBED_ROM_START)
  #define MBED_ROM_START    0x10000000
#endif

#if !defined(MBED_ROM_SIZE)
  #define MBED_ROM_SIZE     0x78000
#endif

#if !defined(MBED_RAM_START)
  #define MBED_RAM_START    0x08000000
#endif

#if !defined(MBED_RAM_SIZE)
  #define MBED_RAM_SIZE     0x10000
#endif

/* The MEMORY section below describes the location and size of blocks of memory in the target.
* Use this section to specify the memory regions available for allocation.
*/
MEMORY
{
    ram               (rwx)   : ORIGIN = MBED_RAM_START, LENGTH = MBED_RAM_SIZE
    flash             (rx)    : ORIGIN = MBED_ROM_START, LENGTH = MBED_ROM_SIZE
}
...
```

### Linker script example for ARM compiler

```
...
#if !defined(MBED_ROM_START)
  #define MBED_ROM_START    0x10000000
#endif

#if !defined(MBED_ROM_SIZE)
  #define MBED_ROM_SIZE     0x78000
#endif

#if !defined(MBED_RAM_START)
  #define MBED_RAM_START    0x08000000
#endif

#if !defined(MBED_RAM_SIZE)
  #define MBED_RAM_SIZE     0x10000
#endif

#define MBED_RAM0_START MBED_RAM_START
#define MBED_RAM0_SIZE  0x100
#define MBED_RAM1_START (MBED_RAM_START + MBED_RAM0_SIZE)
#define MBED_RAM1_SIZE  (MBED_RAM_SIZE - MBED_RAM0_SIZE)

LR_IROM1 MBED_ROM_START MBED_ROM_SIZE {
  ER_IROM1 MBED_ROM_START MBED_ROM_SIZE {
   *.o (RESET, +First)
   *(InRoot$$Sections)
   .ANY (+RO)
  }
  RW_IRAM0 MBED_RAM0_START UNINIT MBED_RAM0_SIZE { ;no init section
        *(*nvictable)
  }
  RW_IRAM1 MBED_RAM1_START MBED_RAM1_SIZE {
   .ANY (+RW +ZI)
  }
}
...
```

### Linker script example for IAR compiler

```
...
if (!isdefinedsymbol(MBED_ROM_START)) {
  define symbol MBED_ROM_START = 0x10000000;
}

if (!isdefinedsymbol(MBED_ROM_SIZE)) {
  define symbol MBED_ROM_SIZE = 0x78000;
}

if (!isdefinedsymbol(MBED_RAM_START)) {
  define symbol MBED_RAM_START = 0x08000000;
}

if (!isdefinedsymbol(MBED_RAM_SIZE)) {
  define symbol MBED_RAM_SIZE = 0x10000;
}

/* RAM */
define symbol __ICFEDIT_region_IRAM1_start__ = MBED_RAM_START;
define symbol __ICFEDIT_region_IRAM1_end__   = (MBED_RAM_START + MBED_RAM_SIZE);

/* Flash */
define symbol __ICFEDIT_region_IROM1_start__ = MBED_ROM_START;
define symbol __ICFEDIT_region_IROM1_end__   = (MBED_ROM_START + MBED_ROM_SIZE);
...
```

##  Porting SPM (asymmetric multiprocessing systems - multicore ARMv7-M)

These are the guidelines you should follow if you have multicore systems:

- For each core, initialize, configure and enable the mailbox event (usually an interrupt) at `SystemInit()`.
- For each core, implement the IPC event handler (usually interrupt handler):
  - The handler must call an Arm callback function. See the [HAL functions section](#hal-functions) for more details.
- For each core, implement the HAL function that notifies the peer processor about a mailbox event occurrence. This is a part of the HAL, and the section below explains this in more detail.
- For each core, add the `SPM_MAILBOX` component field for its target node in the `mbed-os/targets/targets.json` file.

### HAL functions

Target-specific code of silicon partners adding SPM capabilities must:

- Implement a list of functions which are being called by SPM code.
- Call Arm callback functions declared and documented in the HAL header files.

The HAL can be logically divided into two different fields:


#### Mailbox

Mailbox is the mechanism used to implement IPC and is **only relevant for multicore systems**. SPM uses mailbox to communicate with secure partitions from a nonsecure processing environment.

##### Concepts

The mailbox mechanism is based on message queues and dispatcher threads. Each core has a single dispatcher thread and a single message queue. The dispatcher thread waits on a mailbox event. Once this event occurs, the dispatcher thread reads and runs "tasks" accumulated on its local message queue.

##### Requirements

The SPM mailbox mechanism requires the platform to have the following capabilities:

- IPC capabilities - the ability to notify the peer processor about an event (usually implemented with interrupts).
- Ability to set a RAM section shared between the cores.


This part of HAL enables you to implement a thin, platform-specific layer of the mailbox mechanism.

#### Secure Processing Environment

This part of HAL allows you to apply your specific memory protection scheme. You can find a list of [these functions](https://os.mbed.com/docs/development/mbed-os-api-doxy/group___s_p_m.html).

## Memory protection

Target-specific code must implement the function `spm_hal_memory_protection_init()` called in SPM initialization. This function applies memory protection schemes to ensure secure memory can only be accessed from secure-state.

The implementation of this function must be aligned with the SPM general guidelines, as the table below describes. This table describes the allowed operations (Read, Write and Execute) on the secure and nonsecure RAM and Flash by each core:

- X means No access.
- &#10003; means Must be able to access.
- ? means it is up to the target.
- X? means it is up to the target, preferably No access.

Processor access    |Secure RAM        |Secure FLASH|Nonsecure RAM      |Nonsecure FLASH
--------------------|------------------|------------|-------------------|----------------
`Non Secure Read`   |   X              |    X       |        &#10003;          |    &#10003;
`Non Secure Write`  |   X              |    X       |        &#10003;          |    ?
`Non Secure Execute`|   X              |    X       |        X?         |    &#10003;
`Secure Read`       |   &#10003;              |    &#10003;       |        &#10003;          |    &#10003;
`Secure Write`      |   &#10003;              |    &#10003;       |        &#10003;          |    ?
`Secure Execute`    |   X?             |    &#10003;       |        X          |    ?


##  TF-M SPM porting (for ARMv8-M targets)

The `tfm_spm_hal.h` file defines TF-M HAL functions.

Mbed OS integrates TF-M sources from [trusted-firmware-m.git](https://git.trustedfirmware.org/trusted-firmware-m.git/about/).

For more information about Mbed OS builds and related concepts, please see [Mbed OS build rules](../reference/mbed-os-build-rules.html).


## System reset

According to the [Trusted Base System Architecture for M (TBSA-M)](https://pages.arm.com/psa-resources-tbsa-m.html) specification, the Secure Processing Environment (SPE) must manage the power state. To implement `NVIC_SystemReset` on the nonsecure side, Mbed OS provides the `mbed_psa_system_reset()` API. This API sends a request for a reset, and the SPE carries out a system reset after all critical tasks are complete.

## Testing

Arm provides a list of tests to check that the HAL functions are implemented according to requirements, and the porting is done correctly.

After finalizing the porting, execute the following tests:

- `tests-psa-spm_smoke`: This test checks that the porting of the mailbox mechanism (for dual core systems) is successful.
- `tests-mbed_hal-spm`: This test checks the porting of the memory protection (`spm_hal_memory_protection_init()` implementation) makes the correct partitioning between secure RAM/Flash and nonsecure RAM/Flash.

We recommended you leave the memory protection part (`spm_hal_memory_protection_init()` implementation) to the end of the porting. First, implement and test other HAL functions. After these tests pass, implement `spm_hal_memory_protection_init()`, and run the entire test suite again, including the memory protection related tests.

This example shows how to run SPM tests for a PSA target with a nonsecure core:

```
mbed test -t GCC_ARM -m SPM_NONSECURE_CORE_PSA -n mbed-os-tests-psa-spm_smoke -v

mbed test -t GCC_ARM -m SPM_NONSECURE_CORE_PSA -n mbed-os-tests-mbed_hal-spm -v
```
