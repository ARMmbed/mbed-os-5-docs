# mbed TLS Porting Guide

This document explains how to port [mbed TLS](https://github.com/ARMmbed/mbedtls) to a new mbed target board.

<span class="notes">**Note:** This part is critical for the security of your product and you should consult a cryptography expert while considering the choices and implementing them.</span>

## 1. Why mbed TLS needs entropy

Almost every cryptographic protocol requires random values that no one should be able to predict. A striking example is their use as session keys: it is easy to see that if an adversary can predict the session key, then he can decrypt the whole session. Even if the adversary can't predict it exactly, just with a relatively high probability, he can still recover the contents of the session. For example, if the adversary has a 0.00001% chance of predicting the 256 bit AES session key, then he can break it as easily as if we had used a 23 bit key (that is - very easily).

Creating session keys is only one use for random values; they have far more complicated applications. And although in these more complex use cases the connection between the predictability of the values and the security of the protocol is not so obvious, it is no less crucial.

## 2. Which entropy source to choose

- If you have a target with a True Random Number Generator (TRNG), then follow Section 3 to allow mbed TLS to use it.

- If you have a target without a TRNG, but with a non-volatile storage, then read Section 4 for instructions on making mbed TLS use a random seed as entropy. This seed should be separately initialized with a true random number for each device.

- If you just want to test mbed TLS on your target without implementing either of the above, and having no security at all is acceptable, then go to Section 5.

## 3. How to provide mbed TLS entropy from a hardware entropy source

mbed TLS distinguishes between strong and weak entropy sources. Of the sources registered by default, two are strong: /dev/urandom and Windows CryptoAPI. However, these resources are not available on many embedded platforms, and the default behavior of mbed TLS is to refuse to work if there are no strong sources present. To get around this, mbed TLS assumes that any hardware entropy source you register (as explained in this guide) is strong. It is very important that you add a strong source if you add a hardware entropy source yourself. For example, an integrated circuit extracting statistically random data from two oscillators of unknown frequencies and independent phases is strong, while anything derived from a real time clock is weak.

The preferred way to provide a custom entropy source:

1. Implement the `mbedtls_hardware_poll` function to let it access the device's entropy source.
2. Set the appropriate macros for your target in `hal/targets.json`.

The next two sections explain how to do this.

## How to implement the hardware poll

The `mbedtls_hardware_poll` function is declared in `entropy_poll.h`:

```C
int mbedtls_hardware_poll( void *data,
                           unsigned char *output, size_t len, size_t *olen );
```

The implementation of this function needs to be in the HAL.

### Parameters

- ``void *data``: A pointer to a structure containing the context to your entropy source. This parameter is `NULL` when the function is called by the framework. If you want to change this behavior, then please follow this [knowledge base article](https://tls.mbed.org/kb/how-to/add-entropy-sources-to-entropy-pool).

- ``unsigned char *output``: A pointer to the output buffer. The function should write the entropy it collected to the buffer; mbed TLS then uses this data as entropy. Please consult your board's manual and write only the strongest entropy possible in this buffer. 

	**Warning:** Although it is possible to fill this buffer without a strong hardware entropy source, we strongly advise against it, because it will nullify any security provided by mbed TLS.

- ``size_t len``: The length of the output buffer. The function shouldn't write more data than this to the output buffer under any circumstances.

- ``size_t *olen``: The length of the data written into the output buffer. It tells the caller how much entropy has been collected and how many bytes of the output buffer it can use. It should always reflect the exact amount of entropy collected; setting it higher than the actual number of bytes collected is a serious security risk.

### Setting the macros

To register your `mbedtls_hardware_poll` function with the mbed TLS entropy framework, you have to add `MBEDTLS_ENTROPY_HARDWARE_ALT` to your macros in `targets.json`:

```
"macros": ["MBEDTLS_ENTROPY_HARDWARE_ALT", etc.]
```

You can read more about how to add a macro for your target [here](../mbed_OS/Targets.md).

<span class="notes">**Note:** You should define the `MBEDTLS_NO_PLATFORM_ENTROPY` macro on any platform that does not support standards like /dev/urandom or Windows CryptoAPI.</span>

## 4. How to implement the Non-Volatile seed entropy source

If a hardware platform does not have a hardware entropy source to leverage into the entropy pool, alternatives have to be considered. As said before, a strong entropy source is crucial for security of cryptographic and TLS operations. For platforms that support non-volatile memory, an option is to use the NV seed entropy source that is provided with mbed TLS.

This makes mbed TLS use a fixed amount of entropy as a seed and update this seed each time it runs. To make this option a relatively strong compromise, the seed should be initialized separately for each device with true random data.

### Enabling NV seed entropy source support

To enable the NV seed entropy source, you have to add `MBEDTLS_ENTROPY_NV_SEED` to your macros in `targets.json`:

```
"macros": ["MBEDTLS_ENTROPY_NV_SEED", etc.],
```

This makes sure the entropy pool knows it can use the NV seed entropy source. 

You can read more about how to add a macro for your target [here](../mbed_OS/Targets.md).

By default the platform adaptation functions write/read a seed file called *seedfile*. If you have a system that does not support regular POSIX file operations (mbed OS does not support them by default), the default platform-adaptation functions will not be useful to you and you will need to provide platform-adaptation functions (see next section).

### 5. Providing platform-adaptation functions

The NV seed entropy source needs to know how to retrieve and store the seed in non-volatile memory. So in order to make the NV seed entropy source work, two platform-layer functions need to be provided.

The relevant read/write functions have the following prototypes:

```C
int (*mbedtls_nv_seed_read)( unsigned char *buf, size_t buf_len );
int (*mbedtls_nv_seed_write)( unsigned char *buf, size_t buf_len );
```

Where `buf` is a pointer to the buffer to read/write a seed, and `buf_len` is the length of that seed.

There are three methods for setting those functions pointers (similar to all platform adaptation functions in mbed TLS):

* `MBEDTLS_PLATFORM_NV_SEED_ALT`. By enabling this macro, the `mbedtls_platform_set_nv_seed(nv_seed_read_func *, nv_seed_write_func*)` function becomes available and lets you set the pointers at run-time.
* `MBEDTLS_PLATFORM_STD_NV_SEED_READ` and `MBEDTLS_PLATFORM_STD_NV_SEED_WRITE` (requires `MBEDTLS_PLATFORM_NV_SEED_ALT`). By setting these two macros to the relevant function names, the default read/write functions are replaced at compile-time and you still have the option to replace them at run-time as well.
* `MBEDTLS_PLATFORM_NV_SEED_READ_MACRO` and `MBEDTLS_PLATFORM_NV_SEED_WRITE_MACRO`. By setting these two macros to the relevant functions names, the read/write functions are replaced at compile-time.

## How to test without entropy sources

Both of the above options are secure if done properly, and depending on the platform may need more or less development work. In some cases it may be necessary to test mbed TLS on boards without entropy. For these kind of scenarios mbed TLS provides a compile time switch to enable testing without entropy sources.

### Setting the macros

This option is very dangerous, because compiling with it results in a build that is not secure! You have to let mbed TLS know that you are using it deliberately and you are aware of the consequences. That is why you have to turn off any entropy sources explicitly first.

Since it is a very dangerous option and no one should use it in production, we recommend to limit its scope as much as possible; you should apply these settings to the application specific config file, instead of the target related configuration as we did it above. You can read more about how to add a macro for your application [here](config_system.md).

To turn the unsafe testing mode on:

1. Make sure that the macros `MBEDTLS_HAVEGE_C`, `MBEDTLS_ENTROPY_HARDWARE_ALT`, `MBEDTLS_ENTROPY_NV_SEED` are not defined.
2. Add `MBEDTLS_NO_DEFAULT_ENTROPY_SOURCES` and `MBEDTLS_TEST_NULL_ENTROPY` to the macros in your `mbed_app.json`.
```
"macros": ["MBEDTLS_NO_DEFAULT_ENTROPY_SOURCES","MBEDTLS_TEST_NULL_ENTROPY", etc.]
```

### Warning!
_**The `MBEDTLS_TEST_NULL_ENTROPY` option nullifies any security provided by mbed TLS! It is there exclusively for testing purposes and should never be used in production. It cannot be stressed enough: a library built with this option does not provide any security whatsoever!**_

