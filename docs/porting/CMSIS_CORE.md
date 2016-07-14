# CMSIS Sources

Cortex Software Interface Standard (CMSIS) Core provides a consistent inteface for CPU intrisics and memory mapped devices. mbed OS 5.0 currently includes version 4.10 with support for the following families:

* Cortex-M0
* Cortex-M0plus
* Cortex-M3
* Cortex-M4 (extended with early preview for virtual NVIC from CMSIS 5)
* Cortex-M7
* Cortex-A9

The silicon vendor provides the files for the startup, system initialization and the devices memory mapped peripherals. For a given `TARGET` this typically looks like:

* ``startup_TARGET.S``
* ``system_TARGET.c``
* ``system_TARGET.h``
* ``TARGET.h``
* ``TARGET.sct``
* ``TARGET.ld``
* ``TARGET.icf``

mbed OS 5.0 has to provide additional files to dynamically set the vector table and to configure the memory model for the given C standard library:

* ``sys.cpp``
* ``cmsis.h``
* ``cmsis_nvic.c``
* ``cmsis_nvic.h``

``` c
void NVIC_SetVector(IRQn_Type IRQn, uint32_t vector) {
    uint32_t *vectors = (uint32_t*)SCB->VTOR;
    uint32_t i;

    // Copy and switch to dynamic vectors if the first time called
    if (SCB->VTOR < NVIC_RAM_VECTOR_ADDRESS) {
        uint32_t *old_vectors = vectors;
        vectors = (uint32_t*)NVIC_RAM_VECTOR_ADDRESS;
        for (i=0; i<NVIC_NUM_VECTORS; i++) {
            vectors[i] = old_vectors[i];
        }
        SCB->VTOR = (uint32_t)NVIC_RAM_VECTOR_ADDRESS;
    }
    vectors[IRQn + NVIC_USER_IRQ_OFFSET] = vector;
}

uint32_t NVIC_GetVector(IRQn_Type IRQn) {
    uint32_t *vectors = (uint32_t*)SCB->VTOR;
    return vectors[IRQn + NVIC_USER_IRQ_OFFSET];
}
```

**Info: CMSIS sources**

Usually, silicon vendors provide source packages containing both the CMSIS-CORE and the CMSIS device specific files.
