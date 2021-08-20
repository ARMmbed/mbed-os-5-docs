# DeviceKey

<span class="images">![](https://os.mbed.com/docs/mbed-os/v6.14/mbed-os-api-doxy/classmbed_1_1_device_key.png)<span>DeviceKey class hierarchy</span></span>

DeviceKey is a mechanism that implements key derivation from a root of trust key. The DeviceKey mechanism generates symmetric keys that security features need. You can use these keys for encryption, authentication and more. The DeviceKey API allows key derivation without exposing the actual root of trust, to reduce the possibility of accidental exposure of the root of trust outside the device.

We have implemented DeviceKey according to NIST SP 800-108, section "KDF in Counter Mode", with AES-CMAC as the pseudorandom function.

## Root of Trust

The root of trust key, which DeviceKey uses to derive additional keys, is generated using the hardware random generator if it exists, or using a key injected to the device in the production process.

The characteristics required by this root of trust are:

- It must be unique per device.
- It must be difficult to guess.
- It must be at least 128 bits.
- It must be kept secret.

The DeviceKey feature keeps the root of trust key in internal storage, using the KVStore component. Internal storage provides protection from external physical attacks to the device.

The root of trust must be created before its first use. Otherwise, the key derivation API fails.

## Key derivation API

`generate_derived_key`: This API generates a new key based on an array of data ([salt](https://en.wikipedia.org/wiki/Salt_(cryptography)) the caller provides. A single salt value always generates the same key, so if you need a new key, you must use a new salt value. The salt can have any value - array, string and so on.

The generated keys can be 128b or 256b in length.

### Root of Trust generation API

DeviceKey class needs root of trust ready to use before the derivation API's first call. There are two options to achieve this:

- Create a device key using a built-in random number generator.
- Manually fill the device key data array.

Both cases requires injecting this key data to the KVStore reserved area.

When `DEVICE_TRNG` is defined, the device supports a random number generator, and you may generate the key by calling `generate_root_of_trust()`. The call succeeds only if the key does not already exist. You can't change the existing key.

```c++ NOCI
int status = DeviceKey::get_instance().generate_root_of_trust();
if(status == DEVICEKEY_SUCCESS) {
    //success
} else {
   //error
}
```

If `DEVICE_TRNG` is not defined, the key buffer must be filled manually by calling `device_inject_root_of_trust()`. The example below shows an injection of a dummy key:

```c++ NOCI
uint32_t key[DEVICE_KEY_32BYTE / sizeof(uint32_t)];
memcpy(key, "12345678123456781234567812345678", DEVICE_KEY_32BYTE);
int size = DEVICE_KEY_32BYTE;

int status = DeviceKey::get_instance().device_inject_root_of_trust(key, size);
if(status == DEVICEKEY_SUCCESS) {
    //success
} else {
    //error
}
``` 

### Using DeviceKey

DeviceKey is a singleton class, meaning the system can have only a single instance of it.

To instantiate DeviceKey, call its `get_instance` member function:

```c++ TODO
    DeviceKey &deviceKey = DeviceKey::get_instance();
```

### Testing DeviceKey

Run the DeviceKey functionality test with the `mbed`:

```
    mbed test -n features-device_key-tests-device_key-functionality
```

## DeviceKey API class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.14/mbed-os-api-doxy/classmbed_1_1_device_key.html)

## DeviceKey example

[![View Example](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-DeviceKey/tree/v6.14)](https://github.com/ARMmbed/mbed-os-snippet-DeviceKey/blob/v6.14/main.cpp)
