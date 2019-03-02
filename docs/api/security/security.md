## Security overview

Security on Arm Mbed OS is divided into the following parts:

- [PSA SPM](./spm.md) - used for accessing secure services within Secure Processing environment (on PSA targets only)

- [PSA internal storage](./psa_internal_storage.md) - used to save PSA RoT state

- [PSA protected storage](./psa_protected_storage.md)

- [PSA Crypto](psa_crypto.md) 

- Mbed TLS. For information about working with Mbed TLS in the context of Mbed OS, please see [Connection security through Arm Mbed TLS](../apis/tls.html).

    For full details, please see the [Mbed TLS site](https://tls.mbed.org/).

- [[PSA Attestation](psa_attestation.md)

- [PSA Lifecycle](./lifecycle/psa_lifecycle.md)

- [Device Key](./DeviceKey.md)
