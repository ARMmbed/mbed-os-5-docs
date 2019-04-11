# Hardware Accelerated Crypto

This document explains how to add hardware acceleration support for a development board in Arm Mbed OS and integrate it with [Arm Mbed TLS](https://github.com/ARMmbed/mbedtls).

## Introduction

### Why should I add hardware acceleration?

Whether the application developer uses Mbed TLS as a cryptographic library or as a TLS stack, cryptographic operations can be expensive in time and can impact the overall performance of application software. Hardware accelerators improve performance of cryptographic operations, which improves overall performance and response time as well.

You may want to add hardware acceleration in the following cases:

- Your processor has special instructions capable of accelerating cryptographic operations, and you can accelerate parts significantly with optimized assembly code.

- Your processor has access to a co-processor with cryptographic acceleration capabilities.

- Your platform has a dedicated crypto-module capable of executing cryptographic primitives, and possibly storing keys securely.

The Mbed TLS library was written in C and it has a small amount of hand-optimized assembly code, limited to arbitrary precision multiplication on some processors. You can find the list of supported platforms in the top comment in [bn_mul.h](https://github.com/ARMmbed/mbedtls/blob/development/include/mbedtls/bn_mul.h).

### What parts can I accelerate?

Mbed TLS has separate modules for the different cryptographic primitives. Hardware acceleration interface is available for the following modules and functions:

- Symmetric
    - [AES](https://tls.mbed.org/api/aes_8h.html): [`mbedtls_aes_setkey_enc()`](https://tls.mbed.org/api/aes_8h.html#acec17c6592b98876106d035c372b1efa), [`mbedtls_aes_setkey_dec()`](https://tls.mbed.org/api/aes_8h.html#a11580b789634605dd57e425eadb56617), [`mbedtls_internal_aes_encrypt()`](https://tls.mbed.org/api/aes_8h.html#a78da421a44bb3e01a3e2d2e98f989a28), [`mbedtls_internal_aes_decrypt()`](https://tls.mbed.org/api/aes_8h.html#ae3e7a68be582d306ab5d96fb4fc043a6).
    - [ARC4](https://tls.mbed.org/api/arc4_8h.html).
    - [BLOWFISH](https://tls.mbed.org/api/blowfish_8h.html).
    - [CAMELLIA](https://tls.mbed.org/api/camellia_8h.html).
    - [DES](https://tls.mbed.org/api/des_8h.html): [`mbedtls_des_setkey()`](https://tls.mbed.org/api/des_8h.html#a9ee690737bded4f7f6e12da86110a8e5), [`mbedtls_des_crypt_ecb()`](https://tls.mbed.org/api/des_8h.html#aa713501cc3e30c39a763b4568698f5c1), [`mbedtls_des3_crypt_ecb()`](https://tls.mbed.org/api/des_8h.html#a933b8f629cc201e06f5e89396d065204).
    - [XTEA](https://tls.mbed.org/api/xtea_8h.htmlm).
    - [MD2](https://tls.mbed.org/api/md2_8h.html): [`mbedtls_md2_process()`](https://tls.mbed.org/api/md2_8h.html#a490b39ec88fec878791c43b6460492a7).
    - [MD4](https://tls.mbed.org/api/md4_8h.html): [`mbedtls_md4_process()`](https://tls.mbed.org/api/md4_8h.html#aa199bb5f6a83d2075590c0144e3237db).
    - [MD5](https://tls.mbed.org/api/md5_8h.html): [`mbedtls_md5_process()`](https://tls.mbed.org/api/md5_8h.html#a4a896444a55569fffd338e7810a1e52b).
    - [RIPEMD160](https://tls.mbed.org/api/ripemd160_8h.html): [`mbedtls_ripemd160_process()`](https://tls.mbed.org/api/ripemd160_8h.html#a36256369d5d29e86e65ec5c46a6383d5).
    - [SHA1](https://tls.mbed.org/api/sha1_8h.html): [`mbedtls_sha1_process()`](https://tls.mbed.org/api/sha1_8h.html#a70417cbb2e95ce553501caef9bd6e076).
    - [SHA256](https://tls.mbed.org/api/sha256_8h.html): [`mbedtls_sha256_process()`](https://tls.mbed.org/api/sha256_8h.html#a1166c1d669de6fe668623612d936f402).
    - [SHA512](https://tls.mbed.org/api/sha512_8h.html): [`mbedtls_sha512_process()`](https://tls.mbed.org/api/sha512_8h.html#a297e591e713063151226993d52ad74a3).
- Asymmetric:
    - ECP: [`mbedtls_internal_ecp_randomize_jac()`](https://tls.mbed.org/api/ecp__internal_8h.html#aac10047640a6fcdd19bd1466371d896d), [`mbedtls_internal_ecp_add_mixed()`](https://tls.mbed.org/api/ecp__internal_8h.html#a3a3d7f9ac767f9007ad9c8d451394b08), [`mbedtls_internal_ecp_double_jac()`](https://tls.mbed.org/api/ecp__internal_8h.html#ae86c1581847bc201cd41b794647296ac), [`mbedtls_internal_ecp_normalize_jac_many()`](https://tls.mbed.org/api/ecp__internal_8h.html#a915f188f33640d90fa11eb13e99114d5), [`mbedtls_internal_ecp_normalize_jac()`](https://tls.mbed.org/api/ecp__internal_8h.html#a9f4a88693c277d48e2b98ce42c89965e), [`mbedtls_internal_ecp_double_add_mxz()`](https://tls.mbed.org/api/ecp__internal_8h.html#ae7b63bf0cfe62021e976b166fb422b54), [`mbedtls_internal_ecp_randomize_mxz()`](https://tls.mbed.org/api/ecp__internal_8h.html#a498b09b2a7c458847c9fd46b39808575), [`mbedtls_internal_ecp_normalize_mxz()`](https://tls.mbed.org/api/ecp__internal_8h.html#a45992cb245da01f5802ef6e544b9bac4).

### How can I make Mbed TLS use my hardware accelerator?

You have to provide an alternative implementation for the parts of Mbed TLS that you want to accelerate.

Mbed TLS has a variety of options to make use of your alternative implementation. These make it possible to easily replace functionality at various abstraction levels and to different extents. In other words, you can replace the least amount of code to reach the highest possible acceleration with the smallest amount of effort.

The easier and safer way to extend functionality is to [override some or all of the functions in a particular module](#adding-acceleration-by-replacing-functions). Sometimes this won't be enough, usually because of a need to change the data structures or the higher level algorithms. If this is the case, you'll need to [replace the whole module](#adding-acceleration-by-replacing-modules). Also, individual function replacement is only supported for function names [listed above under each module](#what-parts-can-i-accelerate); for modules listed without function names, Mbed TLS only supports replacing the whole module. Please note that in the case of ECP functions the override is only partial; Mbed TLS will fall back to the software implementation if the hardware cannot handle a particular group.

No matter which approach you choose, please note the [considerations below](#considerations-for-alternative-implementations).

## Adding acceleration by replacing functions

### Process overview

1. First, you should consider what kind of functionality your hardware provides. Does the processor have some accelerated cryptographic subroutines? Or does your board have a full hardware cryptography module, securely storing keys and providing the functionality of high level cryptographic primitives?

1. Identify the module or the functions you want to replace. For example, if you have a full hardware cryptography module, then you probably want to replace the whole Mbed TLS module. If you only have a couple of special instructions or a co-processor that accelerates some part of the cryptographic function, then you may want to replace only the relevant functions in the Mbed TLS module.

1. If you want to replace functions in the ECP module, you need to implement the mandatory utility functions:

    These are functions that do not have a counterpart in the standard Mbed TLS implementation and their only purpose is to facilitate the integration of the accelerated functions:
        - `mbedtls_internal_ecp_grp_capable`: Implement it to tell Mbed TLS if the cryptographic hardware can handle the group. If the answer is no, then Mbed TLS will fall back to the software implementation to continue the operation.
        - `mbedtls_internal_ecp_init` and `mbedtls_internal_ecp_free` are optional. Use them to optimize if you are replacing a function in the ECP module.
        - For more information about the utility functions read the subsection about the [ECP](#how-to-implement-ecp-module-functions) module.

1. Implement the selected functions with the help of your hardware accelerator.

1. Because Mbed TLS is implemented as a static link library in Arm Mbed OS, you also have to notify the compiler or linker that the alternative implementations are present. To do this, you have to set the macros corresponding to the selected functions. You can read more on this in the [subsection about setting macros](#how-to-set-the-macros).

### How to implement the functions

These functions have the same name as the ones they replace. There is a [doxygen documentation for the original functions](https://tls.mbed.org/api/). The exception to the naming conventions is the ECP module and parts of the AES module, where an internal API is exposed to enable hardware acceleration. These functions too have a doxygen documentation, and you can find them in the `ecp_internal.h` and `aes.h` header files. The function declarations have to remain unchanged; otherwise, Mbed TLS can't use them.

Clone the [Mbed OS repository](https://github.com/ARMmbed/mbed-os) and copy the source code of your function definitions to the `features/mbedtls/targets/TARGET_XXXX` directory specific to your target. Create a pull request when your code is finished and production ready. You may create a directory structure similar to the one you have for the HAL if you feel it appropriate.

### How to implement ECP module functions

Mbed TLS supports only curves over prime fields and uses mostly curves of short Weierstrass form. The function `mbedtls_internal_ecp_add_mixed` and the functions having `_jac_` in their names are related to point arithmetic on curves in short Weierstrass form. The only Montgomery curve supported is Curve25519. To accelerate operations on this curve, you have to replace the three functions with `_mxz_` in their name. For more information on elliptic curves in Mbed TLS, see the [corresponding Knowledge Base article](https://tls.mbed.org/kb/cryptography/elliptic-curve-performance-nist-vs-brainpool).

The method of accelerating the ECP module may support different kinds of elliptic curves. If that acceleration is a hardware accelerator, you may need to indicate what kind of curve operation the accelerator has to perform by setting a register or executing a special instruction. If performing this takes significant amount of time or power, then you may not want Mbed TLS to do this step unnecessarily. The replaceable functions in this module are relatively low level, and therefore it may not be necessary to do this initialization and release in each of them.

To resolve this, you can move the setup of the hardware to the `mbedtls_internal_ecp_init` and `mbedtls_internal_ecp_free` functions and let Mbed TLS call them whenever it is necessary. Please keep in mind that `mbedtls_internal_ecp_init` should return 0 upon a successful setup and `MBEDTLS_ERR_ECP_FEATURE_UNAVAILABLE` otherwise.

### How to set the macros

You will have to set some macros to notify Mbed TLS and the compiler or linker about the presence of your functions or module implementation.

The best way to do this is to supply a target-specific configuration file for your target. This configuration file won't replace the Mbed TLS configuration file - it is only an extension of it. Please note that the method described in this section is specific to hardware related macros - please don't use it for defining Mbed TLS macros.

First, you need to notify the build system that you to have a target-specific Mbed TLS configuration. In `targets.json`, add `MBEDTLS_CONFIG_HW_SUPPORT` to your target in the `macros` section:

```
"macros": ["MBEDTLS_CONFIG_HW_SUPPORT", etc.]
```

Now you can define your crypto hardware acceleration related macros in an `mbedtls_device.h` header, which is appended to the ordinary Mbed TLS configuration when compiling for your target.

<span class="notes">**Note:** Place this header in the `features/mbedtls/targets/TARGET_XXXX` directory specific to your target. You may create a directory structure similar to the one you have for the HAL if you feel it appropriate.</span>

Define the following macros in the header file:

1. When replacing an entire module: `<Module Name Allcaps>_ALT`.

1. When overriding a function: `<Function Name Allcaps>_ALT`.

For example, if you want to replace `mbedtls_sha512_process()` and the entire BLOWFISH module, then the contents of your `mbedtls_device.h` will look something like this:

```
#define MBEDTLS_SHA512_PROCESS_ALT
#define MBEDTLS_BLOWFISH_ALT
```

When overriding functions from the ECP module, please note:

- ECP function names don't contain the `_internal_` prefix. For example, to implement the `mbedtls_internal_ecp_normalize_mxz` function you need to define the `MBEDTLS_ECP_NORMALIZE_MXZ_ALT` macro.

- The ECP interface requires the implementation of some utility functions (`mbedtls_internal_ecp_grp_capable`, `mbedtls_internal_ecp_init` and `mbedtls_internal_ecp_free`), therefore you need to notify the compiler or linker about these functions by defining the `MBEDTLS_ECP_INTERNAL_ALT` macro.

## Adding acceleration by replacing modules

Replacing the whole module is the harder way, because it usually takes much more effort than providing alternatives for a handful of functions. It is also less safe, not just because taking this road can cause complications during the maintenance period, but also because it can lead to increased security risks. For example, if the alternative module implementation contains the duplicate of some Mbed TLS code, then keeping it up to date is an extra effort; not doing so may raise security risks.

To replace a module you have to:

- Implement the functionality of the whole module. Your implementation has to leave unchanged the function prototypes, and the names of any global type, variable or macro.

- Provide a header file for your implementation. The file name must be `<Module Name>_alt.h`.

- Set the macro `MBEDTLS_<Module Name>_ALT` to notify Mbed TLS and the compiler or linker about the replacement. You can read more on this in the [subsection about setting macros](#how-to-set-the-macros).

### Where to find the default implementations

The default implementation of the modules are usually in the file `feature/mbedtls/src/<Module Name>.c`. The ECP module is split to two files: `ecp.c` and `ecp_curves.c`.

## Mbed TLS platform context

Some hardware accelerators require initialization, regardless of the specific cryptography engine. For this, we introduced `mbedtls_platform_setup()` and `mbedtls_platform_terminate()`.

When your hardware accelerator driver requires initialization, do the following operations:

1. Define `MBEDTLS_PLATFORM_SETUP_TEARDOWN_ALT` in `mbedtls_device.h`
1. Implement `crypto_platform_setup(crypto_platform_ctx *ctx)` and `crypto_platform_terminate(crypto_platform_ctx *ctx)`, which initializes and terminates your hardware accelerator driver.
1. Define `crypto_platform_ctx` in `crypto_device_platform.h`.

## Considerations for alternative implementations

### Concurrency

Note that functions in Mbed TLS can be called from multiple threads and from multiple processes at the same time. Because hardware accelerators are usually a unique resource, it is important to protect all functions against concurrent access.

For short actions, disabling interrupts for the duration of the operation may be enough. When it is not desirable to prevent context switches during the execution of the operation, you must protect the operation with a mutual exclusion primitive such as a [mutex](../apis/mutex.html). Make sure to unlock the mutex or restore the interrupt status when returning from the function even if an error occurs.

### Power management

The current framework does not provide an interface to initialize and shut down accelerator hardware. One approach is to perform any necessary hardware initialization during system startup (outside of Mbed TLS); however this may not be desirable for power consumption reasons. At the other end of the spectrum, it is possible to initialize the hardware at the beginning of each function and shut it down after reading the results. This is a viable strategy if initialization is cheap enough.

If it is neither desirable to leave the hardware powered on permanently nor to initialize it each time, you need to determine a power management strategy according to the expected application usage. Note that unconditionally shutting down the hardware in `mbedtls_xxx_free` functions is usually not a particularly useful strategy because there may be other live contexts that require the hardware. A more useful strategy is to keep a global use counter: increment the counter as part of context allocation and decrement it as part of freeing each context. When the global counter drops to 0, the hardware is no longer in use.

In specialized applications, it may be best to provide a custom function to switch the hardware on and off and let the application developer decide when to call it.
