# Using PSA-enabled Mbed TLS (in Mbed OS 5.12)

### Building PSA-enabled Mbed TLS from git

The version of Mbed TLS that was shipped in Mbed OS 5.12 builds with PSA
enabled by default. However, should you need to build PSA-enabled version of
Mbed TLS from [our git repository](https://github.com/ARMmbed/mbedtls), here's
how to do it.

 1. Clone our repo, switch to the development-psa branch and initialize the submodule: `git checkout development-psa && git submodule update --init`
 1. Enable the `MBEDTLS_USE_PSA_CRYPTO` build-time configuration option in `include/mbedtls/config.h`, either by editing the file manually, or using the config script: `scripts/config.pl set MBEDTLS_USE_PSA_CRYPTO`
 1. Build normally, for example (with Gnu Make) make all test or (with CMake) `mkdir build && cd build && cmake .. && make all test`

### Switching from pre-PSA Mbed TLS to PSA-enabled Mbed TLS

So far, applications built with pre-PSA Mbed TLS can be used with PSA-enabled
Mbed TLS by just recompiling them against a PSA-enabled version of Mbed TLS.
(Note that relinking is not enough, though.) In other words, PSA-enabled Mbed
TLS is currently fully API-compatible with non-PSA-enabled Mbed TLS, but not
ABI compatible. All existing (pre-PSA) APIs are preserved and continue to exist
in parallel with new PSA-based APIs, in order to ease the transition for users
at this stage.

_Please note that this is likely to change at a later date though, as existing
interfaces are likely to be deprecated in favor of the new, PSA-based APIs -
if, when and how it happens is outside the scope of this document._

### Switching from PSA-enabled Mbed TLS in Mbed OS 5.11 to PSA-enabled Mbed TLS in Mbed OS 5.12

If your application is not using any of the new PSA-specific APIs described
below, then it can be used with the version in Mbed OS 5.12 by just recompiling
it. (Note that relinking is not enough, though.)

If you application is using one of the new PSA-specific APIs described below,
then you will need to change its source code as these APIs have been change in
an incompatible way between Mbed OS 5.11 and Mbed OS 5.12, to reflect changes
in PSA Crypto itself, whose API wasn't stable as of Mbed OS 5.11.

### New, PSA-based APIs in Mbed TLS

As mentioned in the previous section, old applications can still be built with
PSA-enabled Mbed TLS. Doing so is enough to benefit from PSA in some areas (for
example, some PSA-based hardware acceleration depending on platform support),
but in other areas changes in the application source code are necessary.
Currently, this mainly means replacing calls to pre-PSA APIs with calls to
their new PSA-based versions, as detailed in the following sections.

The new APIs allow using PSA-managed keys for a few purposes (TLS client
authentication, CSR generation, TLS PSK connections). Letting the key be
managed by PSA is good for security as PSA can isolate the keys from the rest
of the applications (referred to below as "opaque keys"). In order to use such
PSA-managed keys, you'll need to modify your code to use the new APIs as
described below.

### Using Opaque ECDSA Keys for TLS Client Authentication

This mainly involves using the new API function `mbedtls_pk_setup_opaque()` in
order to wrap a PSA-managed key into a PK context, then using that context with
the usual TLS APIs.

#### Application flow without PSA:

 1. At application startup, make sure `mbedtls_platform_setup()` is called if relevant.
 1. Declare (and allocate) an object of type `mbedtls_pk_context`
 1. Load a key into that PK context, presumably using `mbedtls_pk_parse_key()` (or `mbedtls_pk_parse_keyfile()`)
 1. Configure the key for use in client authentication with a matching certificate by calling `mbedtls_ssl_conf_own_cert()` on the PK context.
 1. Use the resulting SSL configuration for TLS connections as usual.
 1. When you're done using TLS connections based on that configuration, _and no longer want to use that key for anything else_, free the PK context using `mbedtls_pk_free()`.

#### Application flow with PSA in Mbed OS 5.11 (new/changed parts emphasized):

    1. At application startup, make sure `mbedtls_platform_setup()` is called if relevant, *and make sure `psa_crypto_init()` is called too*.
    1. Declare (and allocate) an object of type `mbedtls_pk_context` *and an object of type `psa_key_slot_t`*.
    1. *Point the key slot object to a slot configured and loaded with the key you want to use (this is achieved by using the relevant PSA Crypto APIs, and is outside the scope of this document, please refer to the PSA Crypto documentation) - and then set up the PK context to wrap that slot by calling `mbedtls_pk_setup_opaque()`*
    1. Configure the key for use in client authentication with a matching certificate by calling `mbedtls_ssl_conf_own_cert()` on the PK context.
    1. Use the resulting SSL configuration for TLS connections as usual.
    1. When you're done using TLS connections based on that configuration, free the PK context using `mbedtls_pk_free()`. *This will only free the PK context itself and leave the key slot untouched - you can either keep using the key slot or call `psa_destroy_key()` on it depending on your application flow (again, outside the scope of this document).*

#### Application flow with PSA in Mbed OS 5.12 (new/changed parts emphasized):

 1. At application startup, make sure `mbedtls_platform_setup()` is called if relevant, and make sure `psa_crypto_init()` is called too.
 1. Declare (and allocate) an object of type `mbedtls_pk_context` *and an object of type `psa_key_handle_t`*.
 1. Allocate and load the key you want to use via the handle object (this is achieved by using the relevant PSA Crypto APIs, and is outside the scope of this document, please refer to the PSA Crypto documentation) - and then set up the PK context to wrap that handle by calling `mbedtls_pk_setup_opaque()`
 1. Configure the key for use in client authentication with a matching certificate by calling `mbedtls_ssl_conf_own_cert()` on the PK context.
 1. Use the resulting SSL configuration for TLS connections as usual.
 1. When you're done using TLS connections based on that configuration, free the PK context using mbedtls_pk_free(). This will only free the PK context itself and leave the key handle untouched - you can either keep using the key handle or call psa_destroy_key() on it depending on your application flow (again, outside the scope of this document).

### Using Opaque ECDSA Keys to Generated Certificate Signing Requests (CSRs)

This mainly involves using the new API function `mbedtls_pk_setup_opaque()` in
order to wrap a PSA-managed key into a PK context, then using that context with
the usual TLS APIs.

#### Application flow without PSA:

 1. At application startup, make sure `mbedtls_platform_setup() is called if relevant.
 1. Declare (and allocate) an object of type `mbedtls_pk_context`
 1. Load a key into that PK context, presumably using `mbedtls_pk_parse_key()`, or by generating a fresh key.
 1. Configure the pending CSR object to use that key by calling `mbedtls_x509write_csr_set_key()` on that PK context.
 1. Call any other function that you need in order to configure and generate the CSR.
 1. When you're done generating the CSR, _and no longer want to use that key for anything else_, free the PK context using `mbedtls_pk_free()`.

#### Application flow with PSA in Mbed OS 5.11 (new/changed parts emphasized):

 1. At application startup, make sure `mbedtls_platform_setup()` is called if relevant, *and make sure `psa_crypto_init()` is called too.*
 1. Declare (and allocate) an object of type `mbedtls_pk_context` and and an object of type `psa_key_slot_t`.
 1. *Point the key slot object to a slot configured and loaded with the key you want to use (this is achieved by using the relevant PSA Crypto APIs, and is outside the scope of this document, please refer to the PSA Crypto documentation) - and then set up the PK context to wrap that slot by calling `mbedtls_pk_setup_opaque()`
 1. Configure the pending CSR object to use that key by calling `mbedtls_x509write_csr_set_key()` on that PK context.
 1. Call any other function that you need in order to configure and generate the CSR.
 1. When you're done generating the CSR, free the PK context using `mbedtls_pk_free()`. *This will only free the PK context itself and leave the key slot untouched - you can either keep using the key slot or call psa_destroy_key() on it depending on your application flow (again, outside the scope of this document).*

#### Application flow with PSA in Mbed OS 5.12 (new/changed parts emphasized):
 1. At application startup, make sure `mbedtls_platform_setup()` is called if relevant, and make sure `psa_crypto_init()` is called too.
 1. Declare (and allocate) an object of type `mbedtls_pk_context` and an object of type *`psa_key_handle_t`*.
 1. Allocate and load the key you want to use via the *handle* object (this is achieved by using the relevant PSA Crypto APIs, and is outside the scope of this document, please refer to the PSA Crypto documentation) - and then set up the PK context to wrap that handle by calling mbedtls_pk_setup_opaque()
 1. Configure the pending CSR object to use that key by calling mbedtls_x509write_csr_set_key() on that PK context.
 1. Call any other function that you need in order to configure and generate the CSR.
 1. When you're done generating the CSR, free the PK context using `mbedtls_pk_free()`. This will only free the PK context itself and leave the key *handle* untouched - you can either keep using the key *handle* or call `psa_destroy_key()` on it depending on your application flow (again, outside the scope of this document).

### Using Opaque Pre-Shared Keys with TLS PSK ciphersuites

This mainly involves using the new API function `mbedtls_ssl_conf_psk_opaque()`
in place of `mbedtls_ssl_conf_psk()` client-side or, server-side using
`mbedtls_ssl_set_hs_psk_opaque()` instead of `mbedtls_ssl_set_hs_psk()` in the
PSK callback.

#### Application flow without PSA (client-side for example):

    1. At application startup, make sure `mbedtls_platform_setup()` is called if relevant.
    1. Set up an `unsigned char *` to point to a memory area holding your pre-shared key.
    1. Call `mbedtls_ssl_conf_psk()` on the SSL configuration object.
    1. Use that configuration object in TLS connections.

#### Application flow with PSA in Mbed OS 5.11 (new/changed parts emphasized):

    1. At application startup, make sure `mbedtls_platform_setup()` is called if relevant, *and make sure `psa_crypto_init()` is called too.*
    1. *Set up a `psa_key_slot_t` to point to a configured slot holding your pre-shared key.*
    1. Call *`mbedtls_ssl_conf_psk_opaque()`* on the SSL configuration object.
    1. Use that configuration object in TLS connections.

#### Application flow with PSA in Mbed OS 5.12 (new/changed parts mphasized):

    1. At application startup, make sure `mbedtls_platform_setup()` is called if relevant, and make sure `psa_crypto_init()` is called too.
    1. Set up a *`psa_key_handle_t`* to point to a configured slot holding your pre-shared key.
    1. Call `mbedtls_ssl_conf_psk_opaque()` on the SSL configuration object.
    1. Use that configuration object in TLS connections.
