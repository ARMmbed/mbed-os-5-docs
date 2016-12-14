# mbed TLS Porting Guide

This document explains how to port [mbed TLS](https://github.com/ARMmbed/mbedtls) to a new mbed development board.

<span class="notes">**Note:** This part is critical for the security of your product, and you should consult a cryptography expert while considering the choices and implementing them.</span>

## 1. Why mbed TLS needs entropy

Almost every cryptographic protocol requires random values that no one should be able to predict. A striking example is their use as session keys: It is easy to see that if an adversary can predict the session key, then he can decrypt the whole session. Even if the adversary can't predict it exactly, just with a relatively high probability, he can still recover the contents of the session. For example, if the adversary has a 0.00001% chance of predicting the 256 bit AES session key, then he can break it as easily as if we had used a 23 bit key (that is - very easily).

Creating session keys is only one use for random values; they have far more complicated applications. In these more complex use cases, the connection between the predictability of the values and the security of the protocol is not as obvious, but it is still crucial.

## 2. Which entropy source to choose

- If you have a target with a True Random Number Generator (TRNG), then follow Section 3 to allow mbed TLS to use it.

- If you have a target without a TRNG, but with a non-volatile (NV) storage, then read Section 4 for instructions on making mbed TLS use a random seed as entropy. This seed should be separately initialized with a true random number for each device at manufacturing time.

- If you just want to test mbed TLS on your target without implementing either of the above, and having no security at all is acceptable, then go to Section 5.

## 3. How to provide mbed TLS entropy from a hardware entropy source

### 3.1 What kind of a source can be added

It is important that you only add a TRNG as described in this section. For the purposes of this document a device is considered a TRNG only if:

- It is dedicated to generating entropy to be used in cryptographic applications.

- Careful consideration has been given to how much the data generated is subject to adversarial manipulation.

- A thorough engineering study has been made to determine how much entropy it can actually provide.

For example, an integrated circuit extracting statistically random data from two oscillators of unknown frequencies and independent phases is considered a TRNG, but anything derived from a real time clock is NOT.

### 3.2 How to add an entropy source

mbed TLS distinguishes between strong and weak entropy sources. Of the sources registered by default, two are strong: /dev/urandom and Windows CryptoAPI. However, these resources are not available on many embedded platforms, and the default behaviour of mbed TLS is to refuse to work if there are no strong sources present. To get around this, mbed TLS assumes that the hardware entropy source you register (as explained in this section) is a TRNG and thus treats it as strong.

The preferred way to provide a custom entropy source:

1. Implement the functions declared in `hal/trng_api.h` to let mbed TLS access the device's entropy source.
2. Indicate that your target has an entropy source in `targets/targets.json`, by adding `TRNG` to your device's `device_has` section.

The next two sections explain how to do this.

## How to implement the TRNG API

The implementation of this interface has to be located in the mbed OS directory specific to your target. The name of this directory is of the form `targets/.../TARGET_<target name>`. For example, in the case of K64F targets, it is `targets/TARGET_Freescale/TARGET_KSDK2_MCUS/TARGET_MCU_K64F/`.

### Data structure

You have to define a structure `trng_s` that holds all the information needed to operate the peripheral and describe its state.

### Initialization and release

To enable initializing and releasing the peripheral, you must implement the following functions:

```C
void trng_init(trng_t *obj);
void trng_free(trng_t *obj);
```

### The entropy collector function

The function `trng_get_bytes()` serves as the primary interface to the entropy source. It is expected to load the collected entropy to the buffer and is declared as follows:

```C
int trng_get_bytes(trng_t *obj, uint8_t *output, size_t length, size_t *output_length);
```

- ``trng_t *obj``: `trng_t` is an alias to `trng_s`, and it is the caller's responsibility to initialize it before passing it to this function and release it (with the help of `trng_init()` and `trng_free()`, respectively) when it is not required anymore.

- ``uint8_t *output``: a pointer to the output buffer. The function should write the entropy it collected to the buffer; mbed TLS then uses this data as entropy. Please consult your board's manual, and write only the strongest entropy possible in this buffer.

    **Warning:** Although it is possible to fill this buffer without a strong hardware entropy source, we strongly advise against it because it will nullify any security provided by mbed TLS.

- ``size_t length``: the length of the output buffer. The function shouldn't write more data than this to the output buffer under any circumstances.

- ``size_t *output_length``: the length of the data written into the output buffer. It tells the caller how much entropy has been collected and how many bytes of the output buffer it can use. It should always reflect the exact amount of entropy collected; setting it higher than the actual number of bytes collected is a serious security risk.


### Indicating the presence of a TRNG

To indicate that the target has an entropy source, you have to add `TRNG` to the capabilities of the target in `targets/targets.json`:

```
"device_has": ["TRNG", etc.]
```

## 4. How to implement the non-volatile seed entropy source

If a hardware platform does not have a hardware entropy source to leverage into the entropy pool, alternatives have to be considered. As stated above, a strong entropy source is crucial for security of cryptographic and TLS operations. For platforms that support non-volatile memory, an option is to use the NV seed entropy source that is provided with mbed TLS.

This makes mbed TLS use a fixed amount of entropy as a seed and update this seed each time entropy is gathered with an mbed TLS entropy collector for the first time. In a simple case it means that the seed is updated after reset at the start of the first TLS connection.

<span class="notes">**Note:** To make this option a relatively strong compromize, the seed should be initialized separately for each device with true random data at manufacturing time. It has to be true random data, something dependant on, for example the serial number is **not** secure. </span>

### Enabling NV seed entropy source support

To enable the NV seed entropy source, you have to add `MBEDTLS_ENTROPY_NV_SEED` to your macros in `targets.json`:

```
"macros": ["MBEDTLS_ENTROPY_NV_SEED", etc.],
```

This ensures the entropy pool knows it can use the NV seed entropy source.

You can read more about how to add a macro for your target [here](mbed_targets.md).

By default the platform adaptation functions write/read a seed file called *seedfile*. If you have a system that does not support regular POSIX file operations (mbed OS does not support them by default), the default platform-adaptation functions will not be useful to you, and you will need to provide platform-adaptation functions (see next section).

### 5. Providing platform-adaptation functions

The NV seed entropy source needs to know how to retrieve and store the seed in non-volatile memory. So in order to make the NV seed entropy source work, two platform-layer functions need to be provided.

The relevant read/write functions have the following prototypes:

```C
int (*mbedtls_nv_seed_read)( unsigned char *buf, size_t buf_len );
int (*mbedtls_nv_seed_write)( unsigned char *buf, size_t buf_len );
```

Where `buf` is a pointer to the buffer to read/write a seed, and `buf_len` is the length of that seed.

There are three methods for setting those functions pointers (similar to all platform adaptation functions in mbed TLS):

* `MBEDTLS_PLATFORM_NV_SEED_ALT`. By enabling this macro, the `mbedtls_platform_set_nv_seed(nv_seed_read_func *, nv_seed_write_func*)` function becomes available and lets you set the pointers at runtime.
* `MBEDTLS_PLATFORM_STD_NV_SEED_READ` and `MBEDTLS_PLATFORM_STD_NV_SEED_WRITE` (requires `MBEDTLS_PLATFORM_NV_SEED_ALT`). By setting these two macros to the relevant function names, the default read/write functions are replaced at compile-time, and you still have the option to replace them at runtime as well.
* `MBEDTLS_PLATFORM_NV_SEED_READ_MACRO` and `MBEDTLS_PLATFORM_NV_SEED_WRITE_MACRO`. By setting these two macros to the relevant functions names, the read/write functions are replaced at compile-time.

## How to test without entropy sources

Both of the above options are secure if done properly, and depending on the platform may need more or less development work. In some cases it may be necessary to test mbed TLS on boards without entropy. For these kinds of scenarios, mbed TLS provides a compile time switch to enable testing without entropy sources.

### Setting the macros

This option is very dangerous because compiling with it results in a build that is not secure! You have to let mbed TLS know that you are using it deliberately and you are aware of the consequences. That is why you have to turn off any entropy sources explicitly first.

Because it is a very dangerous option and no one should use it in production, we recommend you limit its scope as much as possible; you should apply these settings to the application specific configuration file, instead of the target related configuration as we did it above. You can read more about how to add a macro for your application [here](config_system.md).

To turn the unsafe testing mode on:

1. Make sure that the macros `MBEDTLS_HAVEGE_C`, `MBEDTLS_ENTROPY_HARDWARE_ALT`, `MBEDTLS_ENTROPY_NV_SEED` are not defined.
2. Add `MBEDTLS_NO_DEFAULT_ENTROPY_SOURCES` and `MBEDTLS_TEST_NULL_ENTROPY` to the macros in your `mbed_app.json`.
```
"macros": ["MBEDTLS_NO_DEFAULT_ENTROPY_SOURCES","MBEDTLS_TEST_NULL_ENTROPY", etc.]
```

### Warning!
_**The `MBEDTLS_TEST_NULL_ENTROPY` option nullifies any security provided by mbed TLS! It is there exclusively for testing purposes and should never be used in production. It cannot be stressed enough: a library built with this option does not provide any security whatsoever!**_
