<h2 id="blockdevice-port">PSA SPM</h2>

SPM (Secure Partition Manager) is a part of the PSA Firmware Framework that is responsible for isolating software in Partitions, managing the execution of software within Partitions, and providing IPC between Partitions.

For more information about SPM, refer to [TODO: WHEN READY, SPM OVERVIEW PAGE LINK]

**This page gives guidelines for silicon partners wishing to have Secure Partition Manager capabilities**


## Linker Scripts

Silicon partners must edit the secure and non-secure linker scripts to define sections for RAM, FLASH and SHARED_RAM.

Linker scripts guidelines:
- *__shared_memory_start* symbol is used in SPM code so it must be set with the start address of the shared memory
- *__shared_memory_start* must be 4 bytes aligned
- *__shared_memory_end* symbol is used in SPM code so it must be set with the end address of the shared memory
- SHARED_RAM must have Read/Write permissions from secure and non-secure cores
- SHARED_RAM address must be 4 bytes aligned
- SHARED_RAM must be given a minimum memory space of 256 bytes
- Secure RAM base address must be 4 bytes aligned and have Read/Write permissions only from secure core
- Secure FLASH base address must be 4 bytes aligned and have Read/Write/Execute permissions only from secure core
- Non-Secure RAM base address must be 4 bytes aligned and have Read/Write permissions from secure and non-secure cores
- Non-Secure FLASH base address must be 4 bytes aligned; must have Read permissions from secure and non-secure cores, and Execute permissions from non-secure core; May have Write permissions from secure and non-secure cores

This is an example of the relevant parts inside the linker scripts:

#### SECURE Core Linker Script

```
...
...
MEMORY
{
    /* The ram and flash regions control RAM and flash memory allocation for the SECURE core.
     * You can change the memory allocation by editing the 'ram' and 'flash' regions.
     * Your changes must be aligned with the corresponding memory regions for the NON-SECURE core in the 
     * NON-SECURE linker script.
     */
    ram               (rwx)   : ORIGIN = 0x08000000, LENGTH = 0x10000
    shared_ram        (rw)    : ORIGIN = 0x08010000, LENGTH = 0x1000
    flash             (rx)    : ORIGIN = 0x10000000, LENGTH = 0x78000
    
    ...
    ...
}

...
...

/* .shared_mem section contains memory shared between SECURE core and NON-SECURE core */
.shared_mem :
{
    __shared_memory_start = .;
    . += 0x1000;
    __shared_memory_end = .;

    /* Check if section is 4 bytes aligned */
    ASSERT (((__shared_memory_start % 4) == 0), "Error: shared_mem section is not 4 bytes aligned!!");
} > shared_ram

...
...
```

#### NON-SECURE Core Linker Script
```
...
...
MEMORY
{
    /* The ram and flash regions control RAM and flash memory allocation for the NON-SECURE core.
     * You can change the memory allocation by editing the 'ram' and 'flash' regions.
     * Your changes must be aligned with the corresponding memory regions for the SECURE core in the 
     * SECURE linker script.
     */
    ram               (rwx)   : ORIGIN = 0x08011000, LENGTH = 0x36800
    flash             (rx)    : ORIGIN = 0x10080000, LENGTH = 0x78000
    
    ...
    ...
}

...
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

The HAL can be logically divided into 3 different fields:

#### Addresses
This part of HAL allows the silicon partner to share the addresses set in the linker scripts with the SPM code. The SPM uses these addresses mostly to enforce access permissions.

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
