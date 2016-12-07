# mbed TLS Hardware Acceleration

This document explains how to use hardware acceleration for various cryptographic primitives with [mbed TLS](https://github.com/ARMmbed/mbedtls) running on an embedded device.

## Introduction

### Why should I add hardware acceleration?

Whether the application developer uses mbed TLS as a cryptographic library or uses it as a TLS stack, they will end up with time-consuming cryptographic routines in their application that will heavily impact response time. The platform that reduces this adverse effect will have an edge over platforms that do not (or do so to a lesser extent).

You may want to add hardware acceleration in the following cases:


- You can accelerate parts significantly with optimised assembly code.


- Your processor has special instructions capable of accelerating cryptographic operations.


- Your processor has access to a coprocessor with cryptographic acceleration capabilities.


- Your platform has a dedicated crypto-module capable of executing cryptographic primitives, and possibly storing keys securely.

The mbed TLS library was written in C and it doesn’t use any optimised assembly code. The only exception is the arbitrary precision multiplication on selected processors. You can find the list of supported platforms in the top comment in [bn_mul.h](https://github.com/ARMmbed/mbedtls/blob/development/include/mbedtls/bn_mul.h).

### What parts can I accelerate?

mbed TLS has separate modules for the different cryptographic primitives. Hardware acceleration interface is avaliable for the following modules:

- Asymmetric:
    - Elliptic Curve Point (module name: ECP) arithmetic.

You can extend functionality by either overriding certain functions or replacing the whole module. The easier and safer way of doing this is to override some or all of the functions in a particular module. Sometimes this won't be enough, usually because of a need to change the data structures or the higher level algorithms. If this is the case, you'll need to replace the whole module.

### How can I make mbed TLS use my hardware accelerator?

You have to provide an alternative implementation for the parts of mbed TLS that you want to accelerate.

mbed TLS has a variety of options to make use of your alternative implementation. These make it possible to easily replace functionality at various abstraction levels and to different extents. In other words, you can replace the least amount of code to reach the highest possible acceleration with the smallest amount of effort.

## Adding acceleration by replacing functions

First, you should consider what kind of functionality your hardware provides. Does the processor have some modular arithmetic capabilities? Or does your board have a full cryptographic module, securely storing keys and providing the functionality of high level cryptographic primitives?

### Process overview

1. Identify the module and the functions you want to replace. You can find the list of the replaceable functions for the ECP module in the `ecp_internal.h` header file in the `mbed-os/features/mbedtls/inc/mbedtls` directory. For example, if you have a full cryptographic module, then you probably want to replace functions in the modules. If you only have a couple of special instructions or a coprocessor that accelerates some part of the cryptographic function, then you may want to replace only the relevant functions in the module.

1. Implement the utility functions (only if you selected the ECP module):
    - these are functions that do not have a counterpart in the standard mbed TLS implementation and their only purpose is to facilitate the integration of the accelerated functions.
    - `mbedtls_internal_ecp_grp_capable`: implement it to tell mbed TLS if the cryptographic hardware can handle the group.
    - `mbedtls_internal_ecp_init` and `mbedtls_internal_ecp_free` are optional. Use them to optimize if you are replacing a function in the ECP module.
    - For more information about the utility functions read the subsection about the [ECP](#How-to-implement-ECP-module-functions) module.

1. Implement the selected functions with the help of your hardware accelerator. These functions have the same name as the ones they replace, but with the `_alt` postfix. We have [doxygen documentation for the original functions](https://tls.mbed.org/api/). The exception to the naming conventions is the ECP module, where an internal API is exposed to enable hardware acceleration. These functions too have a doxygen documentation.

1. Since mbed TLS is a static link library you also have to somehow notify the compiler/linker that the alternative implementations are present. To do this, you have to set the macros corresponding to the selected functions. You can read more on this in the [subsection about setting macros](#How-to-set-the-macros?).

### How to implement ECP module functions

mbed TLS supports only curves over prime fields and uses mostly curves of short Weierstrass form. The function `ecp_add_mixed_alt` and the functions having `_jac_` in their names are related to point arithmetic on curves in short Weierstrass form. The only Montgomery curve supported is Curve25519. To accelerate operations on this curve you have to replace the three functions with `_mxz_` in their name.

Hardware accelerators may support different kinds of elliptic curves. You may need to tell some of these accelerators what kind of curve operation it has to perform by setting some registers or calling some special instructions. If performing this takes significant amount of time or power, then you may not want mbed TLS to do this step unnecessarily. Unfortunately the replaceable functions in this module are relatively low level, and it may not be necessary to do this initialisation and de-initialisation in each of them.

To resolve this, you can move the setup of the hardware to the `mbedtls_internal_ecp_init` and `mbedtls_internal_ecp_free` functions and let mbed TLS call them whenever it is necessary. Please keep in mind that `mbedtls_internal_ecp_init` should return 0 upon a successful setup and `MBEDTLS_ERR_ECP_FEATURE_UNAVAILABLE` otherwise.

### How to set the macros for ECP function replacement

You will have to set some macros to notify mbed TLS and the compiler/linker about the presence of your functions.

1. You have to set a macro `MBEDTLS_ECP_INTERNAL_ALT` to turn function replacement in that module on.

1. Also each replaceable function has a corresponding macro `MBEDTLS_ECP_<Function Name Allcaps>_ALT`. You need to set this, too.

The best way to set these macros to add them to your target in `targets.json`.

For example, if you want to replace `ecp_double_jac`, then the macros of your target will look something like this:

```
"macros": ["MBEDTLS_ECP_INTERNAL_ALT","MBEDTLS_ECP_DOUBLE_JAC_ALT", etc.]
```

You can read more about how to add a macro for your target [here](../mbed_OS/Targets.md).

## Adding acceleration by replacing modules

Replacing the whole module is the harder way, because it usually takes much more effort than providing alternatives for a handful of functions. It is also less safe, not just because taking this road can cause complications during the maintenance period, but also because it can lead to increased security risks (For example, if the alternative module implementation contains the duplicate of some mbed TLS code, then keeping it up to date is an extra effort; not doing so may raise security risks).

To replace a module you have to:

- Implement the functionality of the whole module. Your implementation has to leave the function prototypes, and the name of any global type, variable or macro, unchanged.

- Provide a header file for your implementation. The filename must be `<Module Name>_alt.h`.

- Set the macro `MBEDTLS_<Module Name>_ALT` to notify mbed TLS and the compiler/linker about the replacement.You can read more on this in the [subsection about setting macros](#How-to-set-the-macros).


### Where do I find the default implementations?

The default implementation of the modules are usually in the file `<Module Name>.c`. The ECP module is split to two files: `ecp.c` and `ecp_curves.c`.
