## DeviceKey

DeviceKey is a mechanism that implements key derivation from a root of trust key. The DeviceKey mechanism generates symmetric keys that security features need. You can use these keys for encryption, authentication and more. The DeviceKey API allows key derivation without exposing the actual root of trust, to reduce the possibility of accidental exposure of the root of trust outside the device.

We have implemented DeviceKey according to NIST SP 800-108, section "KDF in Counter Mode", with AES-CMAC as the pseudorandom function.

### Root of Trust

The root of trust key, which DeviceKey uses to derive additional keys, is generated using the hardware random generator if it exists, or using a key injected to the device in the production process.

The characteristics required by this root of trust are:

- It must be unique per device.
- It must be difficult to guess.
- It must be at least 128 bits.
- It must be kept secret.

The DeviceKey feature keeps the root of trust key in internal storage, using the NVStore component. Internal storage provides protection from external physical attacks to the device.

The root of trust is generated at the first use of DeviceKey if the true random number generator is available in the device. If no true random number generator is available, you must pass the injected root of trust key to the DeviceKey before you call the key derivation API.

### Key derivation API

`generate_derived_key`: This API generates a new key based on an array of data ([salt](https://en.wikipedia.org/wiki/Salt_(cryptography)) the caller provides. A single salt value always generates the same key, so if you need a new key, you must use a new salt value. The salt can be have any value - array, string and so on. 

The generated keys can be 128 or 256 bits in length.

#### Root of Trust Injection API

`device_inject_root_of_trust`: You must call this API once in the lifecycle of the device, before any call to key derivation, if the device does not support true random number generator (`DEVICE_TRNG` is not defined).

#### Using DeviceKey 

DeviceKey is a singleton class, meaning that the system can have only a single instance of it.

To instantiate DeviceKey, you need to call its `get_instance` member function as following:

```c++
    DeviceKey &deviceKey = DeviceKey::get_instance();
```

#### Testing DeviceKey

Run the DeviceKey functionality test with the `mbed` command as following:

``` 
    mbed test -n features-device_key-tests-device_key-functionality
```

### DeviceKey API class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/v5.9/mbed-os-api-doxy/classmbed_1_1_device_key.html)

### DeviceKey example

```
/*
* Copyright (c) 2018 ARM Limited. All rights reserved.
* SPDX-License-Identifier: Apache-2.0
* Licensed under the Apache License, Version 2.0 (the License); you may
* not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
* http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an AS IS BASIS, WITHOUT
* WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*/

#include "mbed.h"
#include "DeviceKey.h"

//print a unsigned char buffer in hex format
void print_buffer(unsigned char *buf, size_t size)
{
    for (size_t i = 0; i < size; i++) {
        printf("%02X", buf[i]);
    }
}

//Injection of a dummy key when there is no TRNG
int inject_rot_key()
{
    uint32_t key[DEVICE_KEY_16BYTE / sizeof(uint32_t)];

    memset(key, 0, DEVICE_KEY_16BYTE);
    memcpy(key, "ABCDEF1234567890", DEVICE_KEY_16BYTE);
    int size = DEVICE_KEY_16BYTE;
    DeviceKey& devkey = DeviceKey::get_instance();
    return devkey.device_inject_root_of_trust(key, size);
}

// Entry point for the example
int main()
{
    unsigned char derive_key1 [DEVICE_KEY_32BYTE];
    unsigned char derive_key2 [DEVICE_KEY_32BYTE];
    unsigned char salt1[] = "SALT1 ----- SALT1 ------ SALT1";
    unsigned char salt2[] = "SALT2 ----- SALT2 ------ SALT2";
    int ret = DEVICEKEY_SUCCESS;

    printf("\n--- Mbed OS DeviceKey example ---\n");

    //DeviceKey is a singleton
    DeviceKey& devkey = DeviceKey::get_instance();

#if not defined(DEVICE_TRNG)

    //If TRNG is not available it is a must to inject the ROT before the first call to derive key method.
    printf("\n--- No TRNG support for this device. injecting ROT. ---\n");
    ret = inject_rot_key();
    if (DEVICEKEY_SUCCESS != ret && DEVICEKEY_ALREADY_EXIST != ret) {
        printf("\n--- Error, injection of ROT key has failed with status %d ---\n", ret);
        return -1;
    }

    if ( DEVICEKEY_ALREADY_EXIST == ret ) {
        printf("\n--- ROT Key already exists in the persistent memory. ---\n", ret);
    } else {
        printf("\n--- ROT Key injected and stored in persistent memory. ---\n", ret);
    }

#endif

    printf("\n--- Using the following salt for key derivation: %s ---\n", salt1);

    //16 byte key derivation.
    printf("--- First call to derive key, requesting derived key of 16 byte ---\n");
    ret = devkey.generate_derived_key(salt1, sizeof(salt1), derive_key1, DEVICE_KEY_16BYTE);
    if (DEVICEKEY_SUCCESS != ret) {
        printf("\n--- Error, derive key failed with error code %d ---\n", ret);
        return -1;
    }

    printf("--- Derived key1 is: \n");
    print_buffer(derive_key1, DEVICE_KEY_16BYTE);
    printf("\n");

    //16 byte key derivation with the same salt should result with the same derived key.
    printf("\n--- Second call to derive key with the same salt. ---\n");
    ret = devkey.generate_derived_key(salt1, sizeof(salt1), derive_key2, DEVICE_KEY_16BYTE);
    if (DEVICEKEY_SUCCESS != ret) {
        printf("\n--- Error, derive key failed with error code %d ---\n", ret);
        return -1;
    }

    printf("--- Derived key2 should be equal to key1 from the first call. key2 is: \n");
    print_buffer(derive_key2, DEVICE_KEY_16BYTE);
    printf("\n");

    if (memcmp(derive_key1, derive_key2, DEVICE_KEY_16BYTE) != 0) {
        printf("--- Error, first key and second key do not match ---\n");
        return -1;
    } else {
        printf("--- Keys match ---\n");
    }

    printf("\n--- Using the following salt for key derivation %s ---\n", salt2);

    //16 byte key derivation with the different salt should result with new derived key.
    ret = devkey.generate_derived_key(salt2, sizeof(salt2), derive_key1, DEVICE_KEY_16BYTE);
    if (DEVICEKEY_SUCCESS != ret) {
        printf("\n--- Error, derive key failed with error code %d ---\n", ret);
        return -1;
    }

    printf("--- Third call to derive key with the different salt should result with a new derived key1: \n");
    print_buffer(derive_key1, DEVICE_KEY_16BYTE);
    printf("\n");

    if (memcmp(derive_key1, derive_key2, DEVICE_KEY_16BYTE) == 0) {
        printf("--- Error, first key and second key do not match ---\n");
        return -1;
    } else {
        printf("--- Keys not match ---\n");
    }

    //32 byte key derivation.
    printf("\n--- 32 byte key derivation example. ---\n");
    ret = devkey.generate_derived_key(salt2, sizeof(salt2), derive_key2, DEVICE_KEY_32BYTE);
    if (DEVICEKEY_SUCCESS != ret) {
        printf("\n--- Error, derive key failed with error code %d ---\n", ret);
        return -1;
    }

    printf("--- 32 byte derived key is: \n");
    print_buffer(derive_key2, DEVICE_KEY_32BYTE);
    printf("\n");

    printf("\n--- Mbed OS DeviceKey example done. ---\n");

    return 0;
}
```

