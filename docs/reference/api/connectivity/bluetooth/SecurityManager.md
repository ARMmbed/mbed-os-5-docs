## SecurityManager

SecurityManager deals with authentication and encryption for the Bluetooth Low Energy link. The process of pairing and optionally bonding provides this. Bonding is achieved by the SecurityManager saving the pairing information to be reused by it on subsequent reconnections in order to save time by not having to perform pairing again.

The process of pairing may produce a set of keys to be used during current or later connections. These are handled by the SecurityManager and include the Long Term Encryption Key (LTK), the Identity Resolving Key (IRK) and the Connection Signature Resolving Key (CSRK). The LTK is used by the SecurityManager to encrypt subsequent connections without having to pair again. IRK is used by the Link Controller to identify peers who use random resolvable addresses. CSRK is used by the application to sign and authenticate signed data.

The pairing process may provide man-in-the-middle protection (MITM). The SecurityManager achieves this through various means, including out of band communication, depending on the capabilities of the local and peer device.

The SecurityManager stores the keys, permanently if possible, to speed security requests on subsequent connections.

Security requests may come explicitly from the user application or implicitly from the GATT server based on attribute requirements.

### SecurityManager class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/v5.7/mbed-os-api-doxy/class_security_manager.html)

### SecurityManager example

The SecurityManager example shows its basic use. It demonstrates both a central and a peripheral connecting and performing basic pairing and setting up link security.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-SM/)](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-SM)
