## Mbed PSA

Mbed [PSA](/docs/development/introduction/glossary.html) provides root of trust services and infrastructure for developing IoT applications.

When Mbed OS is running on a PSA Security Model compliant target, Mbed PSA helps to protect cryptographic assets, credentials and critical code sections by providing an isolation between a [Secure Processing Environment (SPE)](/docs/development/introduction/glossary.html) and a [Non-Secure Processing Environment (NSPE)](/docs/development/introduction/glossary.html). The [Secure Partition Manager (SPM)](/docs/development/introduction/glossary.html), which uses the target's hardware features, manages the isolation. The SPM provides standardized [IPC](/docs/development/introduction/glossary.html) APIs that you can use regardless of system architecture (v8M, TEE on Cortex-A) or inside another chip.

Mbed PSA bridges the differences between PSA platforms and non-PSA platforms for application developers, allowing them to use the same standard PSA APIs on both platform types.

Mbed PSA allows you to choose the platform type at later phase according to the final application threat model.

<span class="images">![diagram](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/PSA-standardized-Interfaces-diagram.png)<span>PSA diagram</span></span>

### SPM

The SPM is a PSA-compliant software hypervisor that creates and manages independent secure partitions on Arm Cortex&reg;-M microcontrollers. It increases resilience against malware and protects secrets from leaking between different modules in the same application. The SPM complements other important security features, such as safe firmware updates and secure crypto libraries.

The SPM provides hardware-enforced partitions for individual code blocks by limiting access to memories and peripherals using the existing hardware security features of the Cortex&reg;-M microcontrollers. It isolates software in partitions, managing the execution of software within those partitions and providing IPC between the partitions. Correct use of SPM prevents malware from becoming resident on the device and enables protection of device secrets, such as cryptographic keys.

#### Isolating partitions in the SPE

The SPM and the secure partitions are located in the SPE, isolating them from the NSPE, which contains the application firmware, OS kernel and libraries and other nonsecure hardware resources.

A secure partition is a container for one or more root of trust services, and a platform may have multiple secure partitions. Secure partitions provide the execution environment for security functionality.

Platform hardware, such as the [Security Attribution Unit (SAU)](/docs/development/introduction/glossary.html) and Memory Protection Unit (MPU) in the ARMv8-M platforms, enforces the separation of partitions. Other platforms may use different mechanisms to provide equivalent isolation for the partitions.

### Platform types

Mbed PSA supports the following platform types:

- Non-PSA platform: These are single core ARMv7-M targets. On these targets, Mbed PSA provides the same PSA services exposing PSA APIs as it would on PSA targets. The PSA emulation layer allows seamless software portability to more security-oriented targets.

- Asymmetric Multiprocessing (AMP) systems: Multicore ARMv7-M targets (for example, PSoC6 featuring CM4 and CM0+ cores). On these targets, one of the cores is dedicated to PSA use only and implements SPE. Mbed PSA provides PSA API proxy implementation on a nonsecure core, which redirects execution to the SPE.

- ARMv8-M: Generation of ARM processors featuring TrustZone-M architecture. PSA support for this platforms is in final stages of development and will be added to the list of Mbed PSA supported platforms shortly.

### Mbed PSA RoT services

Mbed PSA provides the following services:

- PSA [RoT](/docs/development/introduction/glossary.html) internal storage.
- PSA Crypto APIs.
