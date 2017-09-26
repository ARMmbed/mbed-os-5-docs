## TLS

Arm Mbed TLS provides a comprehensive SSL/TLS solution and makes it easy for developers to include cryptographic and SSL/TLS capabilities in their software and embedded products. As an SSL library, it provides an intuitive API, readable source code and a minimal and highly configurable code footprint.

<span class="notes">_**Note:** Mbed TLS needs a secure source of random numbers; make sure that your target board has one and that it is fully ported to Arm Mbed OS. You can read more about this in our [porting guide](https://os.mbed.com/docs/reference/contributing-overview)._</span>

### Mbed TLS examples

You can try the following examples:

1. [TLS client](https://github.com/ARMmbed/mbed-os-example-tls/tree/master/tls-client): Downloads a file from an HTTPS server (os.mbed.com) and looks for a specific string in that file.

1. [Benchmark](https://github.com/ARMmbed/mbed-os-example-tls/tree/master/benchmark): Measures the time taken to perform basic cryptographic functions used in the library.

1. [Hashing](https://github.com/ARMmbed/mbed-os-example-tls/tree/master/hashing): Demonstrates the various APIs for computing hashes of data (also known as message digests) with SHA-256.

1. [Authenticated encryption](https://github.com/ARMmbed/mbed-os-example-tls/tree/master/authcrypt): Demonstrates using the Cipher API for encrypting and authenticating data with AES-CCM.

Each of them comes with complete usage instructions as a readme file in the repository.

### Configuring Mbed TLS features

Mbed TLS simplifies enabling and disabling features to meet the needs of a particular project, through compilation options. The list of compilation flags is available in the fully documented configuration file, [config.h](https://github.com/ARMmbed/mbedtls/blob/development/include/mbedtls/config.h).

For example, in an application called `myapp`, if you want to enable the EC J-PAKE key exchange and disable the CBC cipher mode, you can create a file named  `mbedtls-config-changes.h` in the `myapp` directory containing the following lines:

```
#define MBEDTLS_ECJPAKE_C
#define MBEDTLS_KEY_EXCHANGE_ECJPAKE_ENABLED

#undef MBEDTLS_CIPHER_MODE_CBC
```

Then create a file named `mbed_app.json` at the root of your application with the following contents:

```
{
    "macros": ["MBEDTLS_USER_CONFIG_FILE=\"mbedtls-config-changes.h\""]
}
```

### Other resources

The [Mbed TLS website](https://tls.mbed.org) contains many other useful resources for developers, such as [developer documentation](https://tls.mbed.org/dev-corner), [knowledge base articles](https://tls.mbed.org/kb) and a [support forum](https://tls.mbed.org/discussions).
