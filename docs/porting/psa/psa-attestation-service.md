<h2 id="initial-attest-port">PSA Initial Attestation Service</h2>

PSA Initial Attestation Service allows the application to prove the device
identity during an authentication process to a verification entity.

The initial attestation service can create a token on request, which contains a fix set of device specific data. Device must contain an attestation key pair, which is unique per device. The token is signed with the private part of attestation key pair. The public key is used to verify the token authenticity. Attestation key injection by an existing private key that pass by user or by generate a key pair. Attestation key stored as a persistent key with specific key-id.

`PSA Initial Attestation Service based on TF-M Attestation Service.`

TF-M latest attestation version is: c43181daf54f69f53de58593a50dd6a9c233eecd and can be taken from: [TF-M repository]( https://git.trustedfirmware.org/trusted-firmware-m.git/).

### Initial Attestation Service interface

Initial Attestation Service exposes the following PSA interface:
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
The caller must allocate a large enough buffer, where the token is going to be created by Initial Attestation Service. The size of the created token is highly dependent on the number of software components in the system and the provided attributes of these.
The `psa_initial_attest_get_token_size()` function can be called to get the
exact size of the created token.
The ` psa_attestation_inject_key()` function called to generate or import a given key pair and export the public part in a binary format.

Before calling Attestation API `psa_crypto_init()` API need to be called.

### Claims in the initial attestation token
The initial attestation token is formed of claims. A claim is a data item,
which is represented in a key - value structure. The following fixed set of
claims are included in the token:
-	`Challenge:` Input object from caller. Can be a single nonce from server or hash of nonce and attested data. It is intended to provide freshness to reports and the caller has responsibility to arrange this
-	`Instance ID:` It represents the unique identifier of the instance. In the PSA definition it is a hash of the public attestation key of the instance.
-	`Verification service indicator:` Optional claim. It is used by a Relying Party to locate a validation service for the token. The value is atext string that can be used to locate the service or a URL specifying the address of the service. 
-	`Profile definition:` Optional claim. It contains the name of a document that describes the 'profile' of the token, being a full description of the claims, their usage, verification and token signing. 
-	`Implementation ID:` It represents the original implementation signer of the attestation key and identifies the contract between the report and verification. A verification service will use this claim to locate the details of the verification process. 
-	`Security lifecycle:` It represents the current lifecycle state of the instance.
-	`Client ID:` The partition ID of that secure partition or non-secure thread who called the initial attestation API
-	`HW version:` Optional claim. Globally unique number in EAN-13 format identifying the GDSII that went to fabrication, HW and ROM. It can be used to reference the security level of the PSA-ROT via a certification website.
-	`Boot seed:` It represents a random value created at system boot time that will allow differentiation of reports from different system sessions.
-	`Software components:` Optional claim. It represents the software state of the system. The value of the claim is an array of CBOR map entries, with one entry per software component within the device. Each map contains multiple claims that describe evidence about the details of the software component.

For information and list of claims are included in the, please refer to [Claims in PSA IAT report]( https://confluence.arm.com/display/IoTBU/Claims+in+PSA+IAT+report).



In current implementation only temporary claims are given by a hardcoded data: caller ID, instance ID, implementation ID, verification service indicator, profile definition and boot status data.
The attestation service might include data in the token about the distinct software components in the device. This data is provided by the boot loader and must be encoded in the TLV format.
In current implementation no bootloader exists in single & dual V7.
Hardcoded temporary bootloader status data (attestation_bootloader_data.c) contains: HW version, Boot seed and some Software components. Security lifecycle should be part of boot status but in current implementation it is given by call directly to `psa_security_lifecycle_state()` API.

### Crypto interface
Device must contain an asymmetric key pair. The private part of it is used
to sign the initial attestation token. Current implementation supports only the ECDSA P256 signature over SHA256. The public part of the key pair is used to create the key identifier (kid) in the unprotected part of the COSE header. The kid is used by verification entity to look up the corresponding public key to verify the signature in the token.
Attestation service uses crypto operation: hash, asymmetric sign, inject attestation key.
