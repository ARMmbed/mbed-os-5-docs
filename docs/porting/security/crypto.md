<h1 id="crypto-port">Mbed Crypto</h1>

Mbed OS provides Mbed Crypto for targets that require support for entropy injection. For information about Mbed Crypto, please refer to [the Mbed Crypto repository](https://github.com/ARMmbed/mbed-crypto).

Both targets newly ported to Mbed OS and existing targets that use entropy injection require passing tests to validate Mbed Crypto functionality.

We run tests by default on several supported boards. To run the tests on a custom board, you can also run the tests manually by specifying additional compiler flags from the command-line.

## Testing

Mbed OS currently provides two tests for Mbed Crypto:

- A test for initialization of the Mbed Crypto module.
- A test for entropy injection feature.

To run these tests, make sure make sure your target configuration is set:

1.  `extra_labels` contains the label `PSA`.
1.  The `MBEDTLS_PSA_CRYPTO_C` macro is enabled for NSPE or SPE targets.

Additionally, if the device does not have a TRNG or if you'd like to run the entropy injection test, ensure the Mbed TLS configuration is set on the SPE:

1. The `MBEDTLS_ENTROPY_NV_SEED` and `MBEDTLS_PSA_INJECT_ENTROPY` macros are enabled.
1. The `MBEDTLS_PLATFORM_NV_SEED_READ_MACRO` macro is set to `mbed_default_seed_read`.
1. The `MBEDTLS_PLATFORM_NV_SEED_WRITE_MACRO` macro is set to `mbed_default_seed_write`.

## Compile and run

To compile and run the Mbed Crypto tests, run the following command:

```
mbed test -t <toolchain> -m <target> -n *entropy_inject,*crypto_init
```
