# Security overview

Security on Arm Mbed OS is divided into two parts:

- [Connection security through Arm Mbed TLS](tls.html).
- [Device security through Arm Mbed uVisor](uvisor.html).

<span class="warnings">**Warning**: uVisor is superseded by the Secure Partition Manager (SPM) defined in the ARM Platform Security Architecture (PSA). uVisor is deprecated as of Mbed OS 5.10, and being replaced by a native PSA-compliant implementation of SPM.</span>

The sections cover working with these modules in the context of Mbed OS. For generic documentation for both modules, see:

- [Mbed TLS full documentation](https://tls.mbed.org/).
- [Mbed uVisor full documentation](https://docs.mbed.com/docs/uvisor-and-uvisor-lib-documentation/en/latest/).
