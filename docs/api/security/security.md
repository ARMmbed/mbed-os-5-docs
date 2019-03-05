## Security overview

Security on Arm Mbed OS is divided into the following parts:

- [Platform Security Architecture (PSA) Secure Partition Manager (SPM)](../apis/spm-apis.html) - Accesses secure services within a secure processing environment (on PSA targets only).

- [PSA Crypto](../apis/psa-crypto.html) - A reference implementation of the cryptography interface of PSA.

- [Mbed TLS](../apis/tls.html) - A comprehensive SSL/TLS solution. For full details, see the [Mbed TLS site](https://tls.mbed.org/).

- [PSA attestation](../apis/psa-attestation.html) - Enables an application to prove a device's identity to a caller during the authentication process.

- [PSA lifecycle](../apis/lifecycle/psa-lifecycle.html) - Enables fine-grained control of the target root of trust (RoT).

- [Device key](../apis/DeviceKey.html) - Implements key derivation from a root of trust key.
