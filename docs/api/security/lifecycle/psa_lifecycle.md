## PSA lifecycle


### Description

PSA Lifecycle allows fine grained control over target RoT without compromising on developer experience.
PSA Lifecycle can be described by following state machine:

![lifecycle](./psa_lifecycle.png)

<span class="notes"> **Note:**
PSA Lifectcle is not a standalone feature as it depends on a PSA bootloader support, which is not yet introduced to mbed-os.
The only supported lifecycle change available at the moment is `PSA_LIFECYCLE_ASSEMBLY_AND_TEST` to `PSA_LIFECYCLE_ASSEMBLY_AND_TEST`, which can be used for tests to reset device RoT state.
All the dashed edges are not implemented.
</span>

Lifecycle can be specified during build time by `MBED_CONF_LIFECYCLE_STATE` macro. Default value is `PSA_LIFECYCLE_ASSEMBLY_AND_TEST`.

In mbed-os PSA Lifecycle is implemented as part of [platform service](../platform_servcie.md)

### Specification

More details can be found in [Platform Security Architecture - Firmware Framework ](https://pages.arm.com/psa-resources-ff.html)


###Doxygen:

[![View code](https://www.mbed.com/embed/?type=library)](../mbed-os-api-doxy/lifecycle_8h.html)
