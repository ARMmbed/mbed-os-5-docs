# Mbed Crypto

Arm Mbed Crypto is the reference implementation of the cryptography interface of the Arm Platform Security Architecture (PSA).

<span class="notes">**Note:** The version of Mbed Crypto shipping with Mbed OS implements PSA Crypto API v1.0b1.</span>

We have adapted and [integrated Mbed Crypto with Mbed OS](https://github.com/ARMmbed/mbed-os/blob/master/features/mbedtls/mbed-crypto). On PSA platforms that support it, Mbed Crypto comes integrated with Mbed OS to leverage the platform's segmented architecture and isolate cryptographic keys and operations from applications.

You can import Mbed Crypto from its standalone [release](https://github.com/ARMmbed/mbed-crypto). Mbed Crypto as integrated with Mbed OS does not include all test code or scripts used in the development of the library. You can find all of these in the standalone release.

<span class="notes">**Note:** Mbed Crypto, like Mbed TLS, needs a secure source of random numbers; make sure that your target board has one and that it is fully ported to Arm Mbed OS. You can read more about this in our [porting guide](../porting/entropy-sources.html).</span>

## Configuring Mbed Crypto features

The Mbed TLS configuration system configures Mbed Crypto. Please refer to [Mbed TLS documentation for how to configure Mbed TLS and Mbed Crypto](../apis/tls.html#configuring-mbed-tls-features).

## Mbed Crypto examples

This example covers some basic use of the PSA Crypto API, as well as factory entropy injection:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-mbed-crypto/)](https://github.com/ARMmbed/mbed-os-example-mbed-crypto/blob/mbed-os-5.14/getting-started/main.cpp)

For further information, please refer to the README file in [the example repository](https://github.com/ARMmbed/mbed-os-example-mbed-crypto).

## Other resources

The [Mbed Crypto project homepage on GitHub](https://github.com/ARMmbed/mbed-crypto) contains the following
resources:

 - [An overview of the PSA Crypto API](https://github.com/ARMmbed/mbed-crypto/blob/psa-api-1.0-beta/docs/PSA_Crypto_API_Overview.pdf).
 - [The PSA Crypto API reference](https://github.com/ARMmbed/mbed-crypto/blob/psa-api-1.0-beta/docs/PSA_Crypto_API_Reference.pdf).
 - [Other general developer documentation](https://github.com/ARMmbed/mbed-crypto/tree/development/docs).
