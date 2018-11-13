<h2 id="blockdevice-port">PSA SPM</h2>

SPM (Secure Partition Manager) is a part of the PSA Firmware Framework that is responsible for isolating software in Partitions, managing the execution of software within Partitions, and providing IPC between Partitions.

For more information about SPM, refer to [TODO: WHEN READY, SPM OVERVIEW PAGE LINK]

**This page gives guidelines for silicon partners wishing to have Secure Partition Manager capabilities**


## Memory layout

Typically PSA platforms will share same RAM and flash between secure and non secure cores.
In order to provide PSA isolation level 1 or higher we need to partition both RAM and flash
in a way described by following drawing:

```text
                                 RAM
 +-----------+-------------+--------------------------------------------------+
 |   Secure  |  Shared     |     Non-Secure                                   |
 |      RAM  |     RAM     |            RAM                                   |
 +-----------+-------------+--------------------------------------------------+

                                 Flash
 +-----------------------+----------------------------------------------------+
 |   Secure              |     Non-Secure                                     |
 |      Flash            |            Flash                                   |
 +-----------------------+----------------------------------------------------+

```
In order to achieve RAM and Flash partitioning start and size values must be added to target a configuration in `targets.json`.
The process of defining can be described in the following steps:
1. secure target must inherit from `SPE_Target` meta-target
2. non-secure target must inherit from `NSPE_Target`
3. both targets must override default configuration by specifying flash RAM and shared RAM regions.

```json
"FUTURE_SEQUANA_M0_PSA": {
        "inherits": ["SPE_Target", "FUTURE_SEQUANA_M0"],
        "extra_labels_add": ["PSOC6_PSA"],
        "components_add": ["SPM_MAILBOX"],
        "macros_add": ["PSOC6_DYNSRM_DISABLE=1"],
        "deliver_to_target": "FUTURE_SEQUANA_PSA",
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
    "FUTURE_SEQUANA_PSA": {
        "inherits": ["NSPE_Target", "FUTURE_SEQUANA"],
        "sub_target": "FUTURE_SEQUANA_M0_PSA",
        "extra_labels_remove": ["CORDIO"],
        "extra_labels_add": ["PSOC6_PSA"],
        "components_add": ["SPM_MAILBOX"],
        "macros_add": ["PSOC6_DYNSRM_DISABLE=1"],
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

> Note: shared memory region is required only for multi core architectures.

## Linker Scripts

Linker scripts mast include `MBED_ROM_START`, `MBED_ROM_SIZE`, `MBED_RAM_START` and `MBED_RAM_START` macros for defining memory regions.
Shared memory region is defined by reserving RAM space for shared memory usage. Shared memory location is target specific and depends on the memory protection scheme applied.
Typically shared memory will be located before/after non-secure RAM, for saving MPU regions. Shared memory region is considered non-secure memory used by both cores.

### Linker Script example GCC_ARM
```
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
### Linker Script example ARM

```
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
```
### Linker Script example IAR

```
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

## Mailbox

Mailbox is the SPM mechanism in charge of Inter Processor Communication, and is **relevant for multi-core systems only**.

#### Concepts
The mailbox mechanism is based on message queues and dispatcher threads.
Each core has a single dispatcher thread, and a single message queue.
The dispatcher thread waits on a mailbox event. Once this event occurs, the dispatcher thread reads and runs "tasks" accumulated on its local message queue. 

#### Requirements
The SPM mailbox mechanism requires that the platform should have the following capabilities:
* Inter Processor Communication capabilities - The ability to notify the peer processor about an event (usually implemented with interrupts)
* Ability to set a RAM section which is shared between the cores

#### Porting
These are the guidelines which should be followed by silicon partners with multi-core systems:
- For each core, initialize, configure and enable the a mailbox event (usually an interrupt) at SystemInit()
- For each core, implement the mailbox event handler (usually interrupt handler):
  - This handler must call an ARM callback function. This is explained in more details in the [HAL Functions section](#hal-functions)
  - It is the silicon partner's responsibility to clear the mailbox event. This can be done in the event handler.
- For each core, implement the HAL function which notifies the peer processor about a mailbox event occurrence. This is a part of the HAL, and explained in more details in the [HAL Functions section](#hal-functions)


## HAL Functions

Target specific code of silicon partners who wish to have SPM capabilities must:
- Implement a list of functions which are being called by SPM code
- Call other functions supplied by ARM

The HAL can be logically divided into 2 different fields:

#### Mailbox
This part of HAL allows the silicon partner to implement a thin layer of the mailbox mechanism which is specific to their platform.
It must be implemented only by silicon partners with multi-core systems.

#### Secure Processing Environment
This part of HAL allows the silicon partner to apply their specific memory protection scheme.

A list of these functions can be found here [TODO: WHEN READY, ADD LINK TO DOXYGEN FILES OF HAL FUNCTIONS]


## Memory Protection

As explained in the [HAL Functions section](#hal-functions), target specific code must implement the function *spm_hal_memory_protection_init()* called on SPM initialization.
This function should apply memory protection schemes to ensure secure memory can only be accessed from secure-state.

The implementation of this function, must be aligned with the SPM general guidelines as described in the table below.

This table describes the allowed operations (Read / Write / Execute) on the Secure and Non-Secure RAM and FLASH by each core:

- X means No Access
- V means Must Be Able to Access
- ? means it is up to the target
- X? means it is up to the target, preferably No Access

Processor Access    |Secure RAM        |Secure FLASH|Non Secure RAM     |Non Secure FLASH
--------------------|------------------|------------|-------------------|----------------
`Non Secure Read`   |   X              |    X       |        V          |    V
`Non Secure Write`  |   X              |    X       |        V          |    ?
`Non Secure Execute`|   X              |    X       |        X?         |    V
`Secure Read`       |   V              |    V       |        V          |    V
`Secure Write`      |   V              |    V       |        V          |    ?
`Secure Execute`    |   X?             |    V       |        X          |    ?


## Testing

ARM provides a list of tests to make sure the HAL functions are implemented according to requirements, and the porting is done correctly.

After finalizing the porting, the following tests should be executed:
- [TODO: WHEN READY, ADD TEST NAME]
- [TODO: WHEN READY, ADD TEST NAME]
- ...

It is recommended to leave the memory protection part [*spm_hal_memory_protection_init()* implementation] to the end of the porting.
First implement and test other HAL functions, and after these tests pass, implement *spm_hal_memory_protection_init()* and run the entire test suite again, including the memory protection related tests.
