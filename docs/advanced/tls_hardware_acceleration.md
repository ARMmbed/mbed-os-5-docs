# mbed TLS Hardware Acceleration

This document explains how to use hardware acceleration for various cryptographic primitives with [mbed TLS](https://github.com/ARMmbed/mbedtls) running on an embedded device.


## Introduction

### Why should I add hardware acceleration?

Whether the application developer uses mbed TLS as a cryptographic library or uses it as a TLS stack, cryptographic operations can be expensive in time and can impact the overall performance of application software. To improve performance of cryptographic operations, hardware accelerators can be used. Clearly, this improves overall performance and response time as well.

You may want to add hardware acceleration in the following cases:

- Your processor has special instructions capable of accelerating cryptographic operations, and you can accelerate parts significantly with optimised assembly code.


- Your processor has access to a co-processor with cryptographic acceleration capabilities.


- Your platform has a dedicated crypto-module capable of executing cryptographic primitives, and possibly storing keys securely.

The mbed TLS library was written in C and it has a small amount of hand-optimised assembly code, limited to arbitrary precision multiplication on some processors. You can find the list of supported platforms in the top comment in [bn_mul.h](https://github.com/ARMmbed/mbedtls/blob/development/include/mbedtls/bn_mul.h).

### What parts can I accelerate?

mbed TLS has separate modules for the different cryptographic primitives. Hardware acceleration interface is available for the following modules and functions:

- Symmetric
    - AES: `mbedtls_aes_setkey_enc()`, `mbedtls_aes_setkey_dec()`, `mbedtls_aes_encrypt()`, `mbedtls_aes_decrypt()`
    - ARC4
    - BLOWFISH
    - CAMELLIA
    - DES: `mbedtls_des_setkey()`, `mbedtls_des_crypt_ecb()`, `mbedtls_des3_crypt_ecb()`
    - XTEA
    - MD2: `mbedtls_md2_process()`
    - MD4: `mbedtls_md4_process()`
    - MD5: `mbedtls_md5_process()`
    - RIPEMD160: `mbedtls_ripemd160_process()`
    - SHA1: `mbedtls_sha1_process()`
    - SHA256: `mbedtls_sha256_process()`
    - SHA512: `mbedtls_sha512_process()`
- Asymmetric:
    - ECP: `mbedtls_internal_ecp_randomize_jac()`, `mbedtls_internal_ecp_add_mixed()`, `mbedtls_internal_ecp_double_jac()`, `mbedtls_internal_ecp_normalize_jac_many()`, `mbedtls_internal_ecp_normalize_jac()`, `mbedtls_internal_ecp_double_add_mxz()`, `mbedtls_internal_ecp_randomize_mxz()`, `mbedtls_internal_ecp_normalize_mxz()`

<span class="notes">**Note:** Hardware acceleration of asymmetric cryptographic functions, is provided only for evaluation in the 5.3 release of mbed OS, in the feature branch [feature\_hw\_crypto](https://github.com/ARMmbed/mbed-os/tree/feature_hw_crypto).</span>

You can extend functionality by either overriding certain functions or replacing the whole module. The easier and safer way of doing this is to override some or all of the functions in a particular module. Sometimes this won't be enough, usually because of a need to change the data structures or the higher level algorithms. If this is the case, you'll need to replace the whole module. Please note that in the case of ECP functions the override is only partial, mbed TLS will fall back to the software implementation if the hardware cannot handle a particular group.

### How can I make mbed TLS use my hardware accelerator?

You have to provide an alternative implementation for the parts of mbed TLS that you want to accelerate.

mbed TLS has a variety of options to make use of your alternative implementation. These make it possible to easily replace functionality at various abstraction levels and to different extents. In other words, you can replace the least amount of code to reach the highest possible acceleration with the smallest amount of effort.

## Adding acceleration by replacing functions

First, you should consider what kind of functionality your hardware provides. Does the processor have some accelerated cryptographic subroutines? Or does your board have a full cryptographic module, securely storing keys and providing the functionality of high level cryptographic primitives?

### Process overview

1. Identify the module or the functions you want to replace. For example, if you have a full cryptographic module, then you probably want to replace functions in the modules. If you only have a couple of special instructions or a co-processor that accelerates some part of the cryptographic function, then you may want to replace only the relevant functions in the module.

1. If you want to replace functions in the ECP module, you need to implement the mandatory utility functions:
    - these are functions that do not have a counterpart in the standard mbed TLS implementation and their only purpose is to facilitate the integration of the accelerated functions.
    - `mbedtls_internal_ecp_grp_capable`: implement it to tell mbed TLS if the cryptographic hardware can handle the group. If the answer is no, then mbed TLS will fall back to the software implementation to continue the operation.
    - `mbedtls_internal_ecp_init` and `mbedtls_internal_ecp_free` are optional. Use them to optimise if you are replacing a function in the ECP module.
    - For more information about the utility functions read the subsection about the [ECP](#How-to-implement-ECP-module-functions) module.

1. Implement the selected functions with the help of your hardware accelerator and copy the source code to the `features/mbedtls/targets/TARGET_XXXX` directory specific to your target. You may create a directory structure similar to the one you have for the HAL if you feel it appropriate. These functions have the same name as the ones they replace. There is a [doxygen documentation for the original functions](https://tls.mbed.org/api/). The exception to the naming conventions is the ECP module, where an internal API is exposed to enable hardware acceleration. These functions too have a doxygen documentation and you can find them in the `ecp_internal.h` header file.

1. Since mbed TLS is implemented as a static link library in mbed OS, you also have to somehow notify the compiler/linker that the alternative implementations are present. To do this, you have to set the macros corresponding to the selected functions. You can read more on this in the [subsection about setting macros](#How-to-set-the-macros?) section.

### How to implement ECP module functions

mbed TLS supports only curves over prime fields and uses mostly curves of short Weierstrass form. The function `ecp_add_mixed_alt` and the functions having `_jac_` in their names are related to point arithmetic on curves in short Weierstrass form. The only Montgomery curve supported is Curve25519. To accelerate operations on this curve you have to replace the three functions with `_mxz_` in their name.

The method of accelerating the ECP module may support different kinds of elliptic curves. If that acceleration is a hardware accelerator, you may need to indicate what kind of curve operation the accelerator has to perform by setting a registers or executing a special instruction. If performing this takes significant amount of time or power, then you may not want mbed TLS to do this step unnecessarily. Unfortunately the replaceable functions in this module are relatively low level, and it may not be necessary to do this initialisation and de-initialisation in each of them.

To resolve this, you can move the setup of the hardware to the `mbedtls_internal_ecp_init` and `mbedtls_internal_ecp_free` functions and let mbed TLS call them whenever it is necessary. Please keep in mind that `mbedtls_internal_ecp_init` should return 0 upon a successful setup and `MBEDTLS_ERR_ECP_FEATURE_UNAVAILABLE` otherwise.

### How to set the macros

You will have to set some macros to notify mbed TLS and the compiler/linker about the presence of your functions or module implementation. The best way to do this is, to supply a target specific mbed TLS configuration file for your target.

First you need to notify the build system that you to have a target specific mbed TLS configuration, by adding `MBEDTLS_CONFIG_HW_SUPPORT` to your target in `targets.json` to the `macros` section:

```
"macros": ["MBEDTLS_CONFIG_HW_SUPPORT", etc.]
```

Now you can define your crypto hardware acceleration related macros in an `mbedtls_device.h` header (this entire file will be appended to the ordinary mbed TLS configuration when compiling for your target). Place this header into the `features/mbedtls/targets/TARGET_XXXX` directory specific to your target. You may create a directory structure similar to the one you have for the HAL if you feel it appropriate.

In this header file you need to define the following macros:

1. When replacing an entire module: You have to set the macro `<Module Name Allcaps>_ALT`.

1. When overriding a function: You have to set the macro `<Function Name Allcaps>_ALT`.

For example, if you want to replace `mbedtls_sha512_process()` and the entire BLOWFISH module, then the contents of your `mbedtls_device.h` will look something like this:

```
#define MBEDTLS_SHA512_PROCESS_ALT
#define MBEDTLS_BLOWFISH_ALT
```

When overriding functions from the ECP module please note, that

- The naming conventions for the ECP module functions are slightly different and the macro names don't contain the `_internal_` prefix. For example, to implement the `mbedtls_internal_ecp_normalize_mxz` function you need to define the `MBEDTLS_ECP_NORMALIZE_MXZ_ALT` macro.

- The ECP interface requires the implementation of some utility functions, therefore you need to notify the compiler/linker about these functions by defining the `MBEDTLS_ECP_INTERNAL_ALT` macro.

## Adding acceleration by replacing modules

Replacing the whole module is the harder way, because it usually takes much more effort than providing alternatives for a handful of functions. It is also less safe, not just because taking this road can cause complications during the maintenance period, but also because it can lead to increased security risks (For example, if the alternative module implementation contains the duplicate of some mbed TLS code, then keeping it up to date is an extra effort; not doing so may raise security risks).

To replace a module you have to:

- Implement the functionality of the whole module. Your implementation has to leave the function prototypes, and the name of any global type, variable or macro, unchanged.

- Provide a header file for your implementation. The file name must be `<Module Name>_alt.h`.

- Set the macro `MBEDTLS_<Module Name>_ALT` to notify mbed TLS and the compiler/linker about the replacement. You can read more on this in the [subsection about setting macros](#How-to-set-the-macros).


### Where to find the default implementations

The default implementation of the modules are usually in the file `feature/mbedtls/src/<Module Name>.c`. The ECP module is split to two files: `ecp.c` and `ecp_curves.c`.
