# PSA initial attestation

The PSA initial attestation service enables an application to prove a device's identity to any server and application, as part of the authentication process.

The initial attestation service creates a token that contains a fixed set of device-specific data, upon request. To sign the token, the device must contain an attestation key pair, which is unique per device. The service uses the attestation private key to sign the token, and the caller uses the public key to verify the token's authenticity.

The PSA initial attestation service is based on the TF-M attestation service, which is available in the [TF-M repository]( https://git.trustedfirmware.org/trusted-firmware-m.git/).

## Specification

The initial attestation service exposes the following PSA interfaces:

```
enum psa_attest_err_t
psa_initial_attest_get_token(const uint8_t *challenge_obj,
                            uint32_t       challenge_size,
                            uint8_t       *token,
                            uint32_t      *token_size);
enum psa_attest_err_t
psa_initial_attest_get_token_size(uint32_t  challenge_size,
                                uint32_t *token_size);
psa_status_t
psa_attestation_inject_key(const uint8_t *key_data,
                        size_t key_data_length,
                        psa_key_type_t type,
                        uint8_t *public_key_data,
                        size_t public_key_data_size,
                        size_t *public_key_data_length);
```

To generate or import a key pair and export the public key in binary format, call the `psa_attestation_inject_key()` function. The function stores the attestation key as a persistent key with a specific `key-id`.

The size of the token that the service creates is highly dependent on the number of software components in the system and the provided attributes of these components. The calling server or device must allocate a sufficiently large buffer for the initial attestation service to create the token into.

To get the exact size of the created token, call the `psa_initial_attest_get_token_size()` function.

<span class="note"> **Note:** You must call the `psa_crypto_init()` API before calling the attestation API.</span>

## Claims in the initial attestation token

The initial attestation token consists of claims. A claim is a data item, which is represented as a key-value pair.

For the list of claims that are included in the token, see [the TF-M Initial Attestation Service Integration Guide](https://git.trustedfirmware.org/trusted-firmware-m.git/tree/docs/user_guides/services/tfm_attestation_integration_guide.md).

The token might also include data about the distinct software components on the device. The bootloader must provide this data encoded in TLV format.

In the current implementation, a bootloader does not exist in single and dual V7; therefore, we have provided temporary hardcoded boot status data claims in the `attestation_bootloader_data.c` file, including `HW version`, `Boot seed`, and some `Software components` entries. `Security lifecycle` should also be part of the boot status, but in the current implementation, it is provided by calling the `psa_security_lifecycle_state()` API directly.

## PSA initial attestation reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/group___p_s_a-_attestation.html)

## PSA initial attestation example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-attestation/blob/attestation_example)](https://github.com/ARMmbed/mbed-os-example-attestation/blob/mbed-os-5.14/main.cpp)

## Related content

- [PSA specification](https://pages.arm.com/PSA-APIs).
