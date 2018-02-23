## Security Manager

Security Manager deals with authentication and encryption for the link. This is provided through the process of pairing and optionally bonding. Bonding is achieved by saving the pairing information to be reused on subsequent re-connections.

The process of pairing may produce a set of keys to be used during current or later connections, these are handled by the Security Manager and include the Long Term Encryption Key (LTK), the Identity Resolving Key (IRK) and the Connection Signature Resolving Key (CSRK). The LTK is used to encrypt subsequent connections. IRK is used to identify peers who use random resolvable addresses. CSRK is used to sign and authenticate signed data.

The pairing process may provide Man in the Middle protection (MITM). This is achieved through various means, including out of band communication, depending on the capabilities of the local and peer device.

The Security Manager will store the keys, if possible permanently, to speed up security requests on subsequent connections.

Security requests may come explicitly from the user application or implicitly from the GATT server based on attribute requirements.

### Security Manager class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/v5.7/mbed-os-api-doxy/class_securitymanager.html)

### Security Manager example

The Security Manager example shows its basic usage. It demonstrates both a central and a peripheral connecting and performing basic pairing and setting up link security.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-SM/)](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-SM)