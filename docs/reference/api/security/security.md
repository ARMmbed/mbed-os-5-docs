## Security overview

Security on Arm Mbed OS is divided into the following parts:

- Mbed TLS. For details, please see our [full documentation](https://tls.mbed.org/).
- Platform Security Architecture (PSA). For details, please see our [full documentation](https://developer.arm.com/products/architecture/security-architectures/platform-security-architecture).
- Mbed uVisor. For details, please see our [full documentation](https://docs.mbed.com/docs/uvisor-and-uvisor-lib-documentation/en/latest/).

<span class="warnings">**Warning**: uVisor is superseded by the Secure Partition Manager (SPM) defined in the ARM Platform Security Architecture (PSA). uVisor is deprecated as of Mbed OS 5.10, and being replaced by a native PSA-compliant implementation of SPM.</span>

For information about working with these modules in Mbed OS context, please refer to the following documents:

- [Connection security through Arm Mbed TLS](/docs/development/reference/tls.html).
- Platform Security Architecture - TBD - under development.
- [Device security through Arm Mbed uVisor](/docs/development/reference/uvisor.html).
