## DeviceKey
DeviceKey is a mechanism that implements key derivation from a root of trust key.

### Description
The DeviceKey mechanism has been designed to generate symmetric keys needed by security features. These keys can be used for encryption, authentication and more. The Devicekey API allows key derivation without exposing the actual root of trust, to reduce the possibility of accidental exposure of the root of trust outside the device.
Devicekey is implemented according to NIST SP 800-108, section "KDF in Counter Mode", with AES-CMAC as the pseudorandom function.
### Root of Trust
The root of trust key, used by Devicekey to derive additional keys, is generated using the hardware random generator if it exists, or using a key injected to the device in the production process.
The characteristics required from this root of trust are:
1) It must be unique per device
2) It must be hard to guess
3) It must be at least 128 bits
4) Must be kept secret

The root of trust key is kept by the Devicekey feature in internal storage, using NVStore component. Internal storage provides protection from external physical attacks to the device.
The root of trust will be generated at the first usage of Devicekey if true random generator is available in the device. If no true random generator is available, the injected root of trust key must be passed to the Devicekey before the key derivation API is called.
## Key derivation API
device_key_derived_key: This API generates a new key based on a string (salt) provided by the caller. The same key will be generated for the same salt. Generated keys can be 128 or 256 bits in length.
### Root of Trust Injection API
device_inject_root_of_trust: This API must be called once in the lifecycle of the device, before any call to key derivation, if the device does not support True Random generator (DEVICE_TRNG is not defined).
### Using DeviceKey 
DeviceKey is a singleton class, meaning that the system can have only a single instance of it.
To instantiate DeviceKey, one needs to call its get_instance member function as following:
```c++
    DeviceKey &deviceKey = DeviceKey::get_instance();
```

### Testing DeviceKey
Run the DeviceKey functionality test with the `mbed` command as following:
``` 
    mbed test -n tests-mbed_drivers-device_key
```
