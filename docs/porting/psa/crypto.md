<h1 id="crypto-port">Mbed Crypto</h1>

Mbed OS provides Mbed Crypto for targets that require support for entropy injection. For information about Mbed Crypto, please refer to [the Mbed Crypto repository](https://github.com/ARMmbed/mbed-crypto).

Both targets newly ported to Mbed OS and existing targets that use entropy injection require passing tests to validate Mbed Crypto functionality.

We run tests by default on several supported boards. To run the tests on a custom board, you can also run the tests manually by specifying additional compiler flags from the command-line.

## Testing

Mbed OS currently provides two tests for Mbed Crypto:

- A test for initialization of the Mbed Crypto module.
- A test for entropy injection feature.

To run these tests, make sure make sure your target configuration is set:

1.  `extra_labels` contains the label `PSA`. Please see an example using the [K64F](https://github.com/ARMmbed/mbed-os/blob/master/targets/targets.json#L1451) or [Future Sequana](https://github.com/ARMmbed/mbed-os/blob/master/targets/targets.json#L7694).
1.  `MBEDTLS_PSA_CRYPTO_C` macro is enabled. Please see an example using the [K64F](https://github.com/ARMmbed/mbed-os/blob/master/targets/targets.json#L1454) or [Future Sequana](https://github.com/ARMmbed/mbed-os/blob/master/targets/targets.json#L7697).
1. `MBEDTLS_ENTROPY_NV_SEED` macro is enabled in the SPE if the device does not have TRNG or if you want the entropy injection test. Please see an example using the [Future Sequana](https://github.com/ARMmbed/mbed-os/blob/master/targets/targets.json#L7673).
1. `MBEDTLS_PLATFORM_NV_SEED_READ_MACRO` macro is set to `mbed_default_seed_read` in the SPE if the device does not have TRNG or if you want the entropy injection test. Please see an example using the [Future Sequana](https://github.com/ARMmbed/mbed-os/blob/master/targets/targets.json#L7674).
1. `MBEDTLS_PLATFORM_NV_SEED_WRITE_MACRO` macro is set to `mbed_default_seed_write` in the SPE if the device does not have TRNG or if you want the entropy injection test. Please see an example using the [Future Sequana](https://github.com/ARMmbed/mbed-os/blob/master/targets/targets.json#L7674).

## Compile and run

To compile and run the Mbed Crypto tests, run the following command:

```
mbed test -t <toolchain> -m <target> -n *entropy_inject,*crypto_init
```
