## Mbed PSA

### Terms and Abbreviations

| Term         | Meaning                             |
|--------------|-------------------------------------|
| IPC          | Inter Process Communication         |
| NSPE         | Non-Secure Processing Environment   |
| PSA          | Platform Security Architecture      |
| RoT          | Root Of Trust                       |
| SAU          | Security Attribution Unit           |
| SPE          | Secure Processing Environment       |
| SPM          | Secure Partition Manager            |


### Overview
Mbed PSA provides essential root of trust services and infrastructure for developing robust IoT applications.

When Mbed OS is running on PSA Security Model compliant target, Mbed PSA helps to protect cryptographic assets, credentials, and critical code sections by providing an isolation between a Secure Processing Environment (SPE) and a Non-Secure Processing Environment (NSPE). The isolation is managed by the Secure Partition Manager (SPM) which utilizes unique hardware features available on the target. The SPM provides standardized IPC APIs which abstract the fact that partitions could be living inside a virtualized environment (v8M, TEE on Cortex-A), or inside another chip.

Mbed PSA bridges the differences between PSA platforms and Non-PSA platforms for application developers, allowing them to use the same standard PSA APIs on both platform types.
Mbed PSA provides PSA API compliance for developing robust IoT applications and 
allows to choose platform type at later phase according to final application threat model.

![diagram](png/PSA-standardized-Interfaces-diagram.png)

### Secure Partition Manager (SPM)

The **Secure Partition Manager (SPM)** is a PSA compliant software hypervisor that creates and manages independent Secure Partitions on Arm Cortex&reg;-M microcontrollers. It increases resilience against malware and protects secrets from leaking between different modules in the same application. The SPM complements other important security features, such as safe firmware updates and secure crypto libraries.

The SPM provides hardware-enforced partitions for individual code blocks by limiting access to memories and peripherals using the existing hardware security features of the Cortex&reg;-M microcontrollers. It isolates software in partitions, managing the execution of software within those partitions and providing IPC between the partitions. Correct use of SPM prevents malware from becoming resident on the device and enables protection of device secrets, such as cryptographic keys.

#### Isolating partitions in the Secure Processing Environment

The SPM and the secure partitions are located in the Secure Processing Environment (SPE), isolating them from the Non-Secure Processing Environment (NSPE), which contains the application firmware, OS kernel and libraries, and other nonsecure hardware resources.

A secure partition is a container for one or more root of trust services, and a platform may have multiple secure partitions. Secure partitions provide the execution environment for security functionality.

Platform hardware, such as the Security Attribution Unit (SAU) and Memory Protection Unit (MPU) in the new ARMv8-M platforms, enforces the separation of partitions. Other platforms may use different mechanisms to provide equivalent isolation for the partitions.

### Platform types
Mbed PSA supports the following platform types:
- Non PSA platform: These are single core ARMv7-M targets.
On these targets Mbed PSA provides the same PSA services exposing PSA APIs as it would on PSA targets.
PSA emulation layer allows seamless software portability to more security oriented targets.
- Asymmetric Multiprocessing (AMP) systems: Multi core ARMv7-M targets (for example, PSoC6 featuring CM4 and CM0+ cores).
On these targets one of the cores is dedicated to PSA usage only and implements SPE.
Mbed PSA provides PSA APIs proxy implementation on non-secure core, which redirects execution to the SPE.
- ARMv8-M: New generation of ARM processors featuring TrustZone-M architecture.
PSA support for this platforms is in final stages of development and will be added to the list of Mbed PSA supported platforms shortly.

### Mbed PSA RoT Services

Mbed PSA provides the following services:
- PSA RoT internal storage
- PSA Crypto APIs
