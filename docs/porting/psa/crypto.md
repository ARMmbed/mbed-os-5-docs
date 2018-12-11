<h2 id="crypto-port">Mbed Crypto</h2>

For information about Mbed Crypto, please refer to [the Mbed Crypto repository](https://github.com/ARMmbed/mbed-crypto).

## Testing
Mbed OS currently provide two test for Mbed Crypto
* Test for initialisation of the Mbed Crypto module
* Test for entropy injection feature

In order to run these tests make sure the following configuration is set in your target:
1.  "extra_labels" contains the label "PSA". For example in [K64F](https://github.com/ARMmbed/mbed-os/blob/master/targets/targets.json#L1451) and [Sequana](https://github.com/ARMmbed/mbed-os/blob/master/targets/targets.json#L7694) 
2.  "MBEDTLS_PSA_CRYPTO_C" macro is enabled. For example in [K64F](https://github.com/ARMmbed/mbed-os/blob/master/targets/targets.json#L1454) and [Sequana](https://github.com/ARMmbed/mbed-os/blob/master/targets/targets.json#L7697)
3. "MBEDTLS_ENTROPY_NV_SEED" macro is enabled in the SPE. If the device does not have TRNG or if entropy injection test is wanted. For example in [Sequana](https://github.com/ARMmbed/mbed-os/blob/master/targets/targets.json#L7673)
4. "MBEDTLS_PLATFORM_NV_SEED_READ_MACRO" macro is set to "mbed_default_seed_read" in the SPE. If the device does not have TRNG or if entropy injection test is wanted. For example in [Sequana](https://github.com/ARMmbed/mbed-os/blob/master/targets/targets.json#L7674)
5. "MBEDTLS_PLATFORM_NV_SEED_WRITE_MACRO" macro is set to mbed_default_seed_write" in the SPE. If the device does not have TRNG or if entropy injection test is wanted. For example in [Sequana](https://github.com/ARMmbed/mbed-os/blob/master/targets/targets.json#L7674)

### Compile and run
In order to compile and run the Mbed Crypto Test run the following command:
```
mbed test -t <toolchain> -m <target> -n *entropy_inject,*crypto_init
```