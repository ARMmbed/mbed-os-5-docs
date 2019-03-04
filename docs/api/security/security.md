## Security overview

Security on Arm Mbed OS is divided into the following parts:

- [Platform Security Architecture (PSA) Secure Partition Manager (SPM)](../spm.html) - Accesses secure services within a secure processing environment (on PSA targets only).

- [PSA internal storage](../apis/psa_internal_storage.html) - Saves the PSA root of trust (RoT) state.

- [PSA protected storage](../apis/psa_protected_storage.html) - Saves data to and retrieves data from PSA protected storage.

- [PSA Crypto](../apis/psa_crypto.html) - A reference implementation of the cryptography interface of PSA.

- [Mbed TLS](../apis/tls.html) - A comprehensive SSL/TLS solution. For full details, see the [Mbed TLS site](https://tls.mbed.org/).

- [PSA attestation](../apis/psa_attestation.html) - Enables an application to prove a device's identity to a caller during the authentication process.

- [PSA lifecycle](../apis/lifecycle/psa_lifecycle.html) - Enables fine-grained control of the target root of trust (RoT).

- [Device key](../apis/DeviceKey.html) - Implements key derivation from a root of trust key.
