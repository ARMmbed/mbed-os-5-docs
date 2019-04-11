# TLS

Arm Mbed TLS provides a comprehensive SSL/TLS solution and makes it easy for developers to include cryptographic and SSL/TLS capabilities in their software and embedded products. As an SSL library, it provides an intuitive API, readable source code and a minimal and highly configurable code footprint.

We have adapted and [preintegrated Mbed TLS with Mbed OS](https://github.com/ARMmbed/mbed-os/blob/master/features/mbedtls). You can import it from its standalone [release](https://github.com/ARMmbed/mbedtls). This edition of Mbed TLS does not include test code or the scripts used in the development of the library. You can find all of these in the standalone release.

<span class="notes">**Note:** Mbed TLS needs a secure source of random numbers; make sure that your target board has one and that it is fully ported to Arm Mbed OS. You can read more about this in our [porting guide](../contributing/index.html).</span>

## Mbed TLS examples

You can try the following examples:

1. [TLS client](https://github.com/ARMmbed/mbed-os-example-tls/blob/master/tls-client): Downloads a file from an HTTPS server (os.mbed.com) and looks for a specific string in that file.

1. [Benchmark](https://github.com/ARMmbed/mbed-os-example-tls/blob/master/benchmark): Measures the time taken to perform basic cryptographic functions used in the library.

1. [Hashing](https://github.com/ARMmbed/mbed-os-example-tls/blob/master/hashing): Demonstrates the various APIs for computing hashes of data (also known as message digests) with SHA-256.

1. [Authenticated encryption](https://github.com/ARMmbed/mbed-os-example-tls/blob/master/authcrypt): Demonstrates using the Cipher API for encrypting and authenticating data with AES-CCM.

Each of them comes with complete usage instructions as a readme file in the repository.

## Configuring Mbed TLS features

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

## Mbed TLS platform context

Some hardware accelerators require initialization, regardless of the specific cryptography engine. For this, we introduced `mbedtls_platform_setup()` and `mbedtls_platform_terminate()`.

As the [examples](#mbed-tls-examples) show, you *must* call the `mbedtls_platform_setup()` function before you call any Mbed TLS API. After using the Mbed TLS API, you *must* call `mbedtls_platform_teardown()` to terminate the platform hardware driver. For readability reasons, we suggest you set the platform context parameter for these functions as `NULL`, as it is not being used in Mbed OS.

```
    int ret = 0;

    if((ret = mbedtls_platform_setup(NULL)) != 0) {
        mbedtls_printf("Platform initialization failed with error %d\r\n", ret);
        return 1;
    }

    /* call Mbed TLS code here */

    mbedtls_platform_teardown(NULL);
    return 0;
```

## Other resources

The [Mbed TLS website](https://tls.mbed.org) contains many other useful resources for developers, such as [developer documentation](https://tls.mbed.org/dev-corner), [knowledge base articles](https://tls.mbed.org/kb) and a [support forum](https://forums.mbed.com/c/mbed-tls).
