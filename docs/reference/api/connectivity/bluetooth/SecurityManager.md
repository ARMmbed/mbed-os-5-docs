## SecurityManager

SecurityManager deals with authentication and encryption for the Bluetooth Low Energy link. The pairing and optionally bonding processes provide this. The SecurityManager achieves bonding by saving the pairing information and reusing it on subsequent reconnections. This saves time because the pairing does not have to be performed again.

The pairing process may produce a set of keys to be used during current or later connections. The SecurityManager includes the Long Term Encryption Key (LTK), the Identity Resolving Key (IRK) and the Connection Signature Resolving Key (CSRK). The SecurityManager uses the LTK to encrypt subsequent connections without having to pair again. The Link Controller uses IRK to identify peers who use random resolvable addresses. The application uses CSRK to sign and authenticate signed data.

The pairing process can provide man-in-the-middle protection (MITM). The SecurityManager achieves this through various means, including out of band communication, depending on the capabilities of the local and peer device.

The SecurityManager stores the keys, permanently if possible, to speed security requests on subsequent connections.

Security requests may come explicitly from the user application or implicitly from the GATT server based on attribute requirements.

### SecurityManager class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_security_manager.html)

### SecurityManager example

The SecurityManager example demonstrates both a central and a peripheral connecting, performing basic pairing, and setting up link security.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-SM/)](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-SM/file/fcb1e0b995a9/source/main.cpp)
