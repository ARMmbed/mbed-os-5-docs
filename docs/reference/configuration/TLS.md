# Configuring Mbed TLS
Configuration of Mbed TLS can either be done using the traditional method, by creating a header file with the appropriate `#defines`, or using the Mbed OS configuration system.

## Using the Mbed OS Configuration System
### Ciphersuites
A ciphersuite is a set of algorithms that the two parties in a TLS connection agree will be used for communication. Each server has a set of ciphersuites that it supports, and clients connecting to that server needs to support at least one of those ciphersuites.

A ciphersuite generally consists of four separate parts:
- The key exchange algorithm
- The signature algorithm
- The encryption algorithm
- The Message Authentication Code (MAC) algorithm

Not all ciphersuites contain all of the elements (for example, many RSA ciphersuites do not list a signature algorithm as it is the same as the key-exchange algorithm).

The configuration of Mbed TLS in Mbed OS is based upon selecting the ciphersuites that need to be supported by the device. This is usually determined by which ciphersuites are supported by whatever systems the device will be connecting to.

When configuring Mbed TLS in Mbed OS, the ciphersuites use the following naming convention:

\<Key Exchange Algorithm\>-\<Signature Algorithm\>-with-\<Encryption Algorithm\>-\<MAC Algorithm\>

For example, the name ecdhe-ecdsa-with-aes-128-gcm-sha256 means:
- The key exchange algorithm is ECDHE - Elliptic-Curve Diffie-Helmann Ephemeral
- The Signature algorithm is ECDSA - Elliptic-Curve Digital Signature Algorithm
- The encryption algorithm is AES_128_GCM -128-bit key Advanced Encryption Standard in Galois-Counter Mode
- The MAC algorithm is SHA256

In ciphersuites where the key exchange algorithm is the same as the signature algorithm, the algorithm will only be listed once. So, for example, rsa-with-aes-256-gcm-sha384 means:
- The key exchange and signature algorithm is RSA
- The encryption algorithm is 256-bit AES-GCM
- The MAC algorithm is SHA384

In Pre-Shared Key ciphersuites (PSK), there is no key exchange algorithm (as the key is already established before the connection is started) or a signature algorithm. In these cases, those two algorithm names are replaced with "psk". Thus, psk-with-aes-256-gcm-sha384 means:
- The key exchange algorithm is PSK - Pre-Shared Key
- The encryption algorithm is 256-bit AES-GCM
- The MAC algorithm is SHA384

The default configuration specified in the `features/mbedtls/mbed_lib.json` file is quite expansive as to allow users to connect to a wide range of services without having to configure things themselves.

When configuring MbedTLS on Mbed OS, developers should add the Mbed TLS ciphersuites that the device will need to support in the `target_overrides` section of their `mbed_app.json` file. Thus, to add the ecdhe-ecdsa-with-aes-128-gcm-sha256 option, they should include:
```
"mbedtls.ecdhe-ecdsa-with-aes-128-gcm-sha256": 1
```
in their `target_overrides` section. Developer should include as many ciphersuites as they deem necessary, keeping in mind that the more they add, the larger the binary footprint of MbedTLS will be on their device.

### Configuration Paramaters

The following list can be found locally by running `mbed compile --config -v --prefix mbedtls`.

```
Configuration parameters
------------------------
Name: mbedtls.app-config-file
    Description: Use an application provided config file instead of any other MBEDTLS configuration options
    Defined by: library:mbedtls
    No value set
Name: mbedtls.ecdh-ecdsa-with-aes-128-cbc-sha256
    Description: Include support for the TLS-ECDH-ECDSA-WITH-AES-128-CBC-SHA256 ciphersuite
    Defined by: library:mbedtls
    No value set
Name: mbedtls.ecdh-ecdsa-with-aes-128-gcm-sha256
    Description: Include support for the TLS-ECDH-ECDSA-WITH-AES-128-GCM-SHA256 ciphersuite
    Defined by: library:mbedtls
    No value set
Name: mbedtls.ecdh-ecdsa-with-aes-256-cbc-sha384
    Description: Include support for the TLS-ECDH-ECDSA-WITH-AES-256-CBC-SHA384 ciphersuite
    Defined by: library:mbedtls
    No value set
Name: mbedtls.ecdh-ecdsa-with-aes-256-gcm-sha384
    Description: Include support for the TLS-ECDH-ECDSA-WITH-AES-256-GCM-SHA384 ciphersuite
    Defined by: library:mbedtls
    No value set
Name: mbedtls.ecdh-rsa-with-aes-128-cbc-sha256
    Description: Include support for TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256 ciphersuite
    Defined by: library:mbedtls
    No value set
Name: mbedtls.ecdh-rsa-with-aes-128-gcm-sha256
    Description: Include support for the TLS-ECDH-RSA-WITH-AES-128-GCM-SHA256 ciphersuite
    Defined by: library:mbedtls
    No value set
Name: mbedtls.ecdh-rsa-with-aes-256-cbc-sha384
    Description: Include support for the TLS-ECDH-RSA-WITH-AES-256-CBC-SHA384 ciphersuite
    Defined by: library:mbedtls
    No value set
Name: mbedtls.ecdh-rsa-with-aes-256-gcm-sha384
    Description: Include support for the TLS-ECDH-RSA-WITH-AES-256-GCM-SHA384 ciphersuite
    Defined by: library:mbedtls
    No value set
Name: mbedtls.ecdhe-ecdsa-with-aes-128-cbc-sha256
    Description: Include support for the TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256 ciphersuite
    Defined by: library:mbedtls
    No value set
Name: mbedtls.ecdhe-ecdsa-with-aes-128-gcm-sha256
    Description: Include support for the TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256 ciphersuites
    Defined by: library:mbedtls
    Macro name: MBED_CONF_MBEDTLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
    Value: 1 (set by library:mbedtls)
Name: mbedtls.ecdhe-ecdsa-with-aes-256-cbc-sha384
    Description: Include support for the TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384 ciphersuite
    Defined by: library:mbedtls
    No value set
Name: mbedtls.ecdhe-ecdsa-with-aes-256-gcm-sha384
    Description: Include support for the TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384 ciphersuite
    Defined by: library:mbedtls
    Macro name: MBED_CONF_MBEDTLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
    Value: 1 (set by library:mbedtls)
Name: mbedtls.ecdhe-ecdsa-with-aes-ccm
    Description: Include support for the TLS-ECDHE-ECDSA-WITH-AES-*-CCM* ciphersuites
    Defined by: library:mbedtls
    No value set
Name: mbedtls.ecdhe-rsa-with-aes-128-cbc-sha256
    Description: Include support for the TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256 ciphersuite
    Defined by: library:mbedtls
    No value set
Name: mbedtls.ecdhe-rsa-with-aes-128-gcm-sha256
    Description: Include support for TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256 ciphersuite
    Defined by: library:mbedtls
    No value set
Name: mbedtls.ecdhe-rsa-with-aes-256-cbc-sha384
    Description: Include support for the TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384 ciphersuite
    Defined by: library:mbedtls
    Macro name: MBED_CONF_MBEDTLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384
    Value: 1 (set by library:mbedtls)
Name: mbedtls.ecdhe-rsa-with-aes-256-gcm-sha384
    Description: Include support for the TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384 ciphersuite
    Defined by: library:mbedtls
    No value set
Name: mbedtls.pelion-client
    Description: Include support needed to connect to Pelion Cloud
    Defined by: library:mbedtls
    Macro name: MBED_CONF_MBEDTLS_PELION_CLIENT
    Value: 1 (set by library:mbedtls)
Name: mbedtls.pelion-mini-client
    Description: Include support needed to connect to Pelion Cloud as a mini client
    Defined by: library:mbedtls
    No value set
Name: mbedtls.psk-with-aes-128-cbc-sha256
    Description: Include support for the TLS-PSK-WITH-AES-128-CBC-SHA256 ciphersuite
    Defined by: library:mbedtls
    No value set
Name: mbedtls.psk-with-aes-128-gcm-sha256
    Description: Include support for the TLS-PSK-WITH-AES-128-GCM-SHA256 ciphersuite
    Defined by: library:mbedtls
    No value set
Name: mbedtls.psk-with-aes-256-cbc-sha384
    Description: Include support for the TLS-PSK-WITH-AES-256-CBC-SHA384 ciphersuite
    Defined by: library:mbedtls
    No value set
Name: mbedtls.psk-with-aes-256-gcm-sha384
    Description: Include support for the TLS-PSK-WITH-AES-256-GCM-SHA384 ciphersuite
    Defined by: library:mbedtls
    No value set
Name: mbedtls.psk-with-aes-ccm
    Description: Include support for the TLS-PSK-WITH-AES-*-CCM* ciphersuites
    Defined by: library:mbedtls
    No value set
Name: mbedtls.rsa-with-aes-128-cbc-sha256
    Description: Include support for the TLS-RSA-WITH-AES-128-CBC-SHA256 cipersuite
    Defined by: library:mbedtls
    No value set
Name: mbedtls.rsa-with-aes-128-gcm-sha256
    Description: Include support for the TLS-RSA-WITH-AES-128-GCM-SHA256 ciphersuite
    Defined by: library:mbedtls
    No value set
Name: mbedtls.rsa-with-aes-256-cbc-sha256
    Description: Include support for the TLS-RSA-WITH-AES-256-CBC-SHA256 cipersuite
    Defined by: library:mbedtls
    No value set
Name: mbedtls.rsa-with-aes-256-gcm-sha384
    Description: Include support for the TLS-RSA-WITH-AES-256-GCM-SHA384 ciphersuite
    Defined by: library:mbedtls
    No value set
```

### Pelion Client
As a shortcut, the configuration system supports an option, `mbedtls.pelion-client`, that enables the ciphersuites required by the Pelion Cloud Service. To allow a device to connect to Pelion, developers need only enable this option.

## Traditional MbedTLS Method
Since the options in the `mbed_lib.json` file are not complete enough to handle all configuration options, users may still opt to use the MbedTLS configuration mechanism built in to the library. This involves creating a custom configuration header file. For instructions on how to do this, please refer to https://tls.mbed.org/kb/compiling-and-building/how-do-i-configure-mbedtls.

Once the header file is created, the user needs to specify the path to that file in a `mbedtls.app-config-file` entry in their `mbed_app.json` file. Entries in this file will supersede any other Mbed TLS selections made in the `mbed_app.json` file. Thus, if, in their custom header file,  a developer `#undefs` something needed for a selected ciphersuite, they will encounter either a build-time or run-time error.
