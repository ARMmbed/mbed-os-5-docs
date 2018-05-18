## SecurityManager

SecurityManager deals with authentication and encryption for the Bluetooth Low Energy link. The pairing and optionally bonding processes provide this. The SecurityManager achieves bonding by saving the pairing information and reusing it on subsequent reconnections. This saves time because the pairing does not have to be performed again.

The pairing process may produce a set of keys to be used during current or later connections. The SecurityManager handles these, and they include the Long Term Encryption Key (LTK), the Identity Resolving Key (IRK) and the Connection Signature Resolving Key (CSRK). The SecurityManager uses the LTK to encrypt subsequent connections without having to pair again. The Link Controller uses IRK to identify peers who use random resolvable addresses. The application uses CSRK to sign and authenticate signed data.

The pairing process may provide man-in-the-middle protection (MITM). The SecurityManager achieves this through various means, including out of band communication, depending on the capabilities of the local and peer device.

The SecurityManager stores the keys, permanently if possible, to speed security requests on subsequent connections.

Security requests may come explicitly from the user application or implicitly from the GATT server based on attribute requirements.
 
#### Paring

There are several ways to provide different levels of security during pairing depending on your requirements and the facilities provided by the application. The process starts with initialising the SecurityManager with default options for new connections. Some settings can later be changed per link or globally.

The important settings in the init() function are the MITM requirement and IO capabilities. Man in the Middle (MITM) protection prevents an attack where one device can impersonate another device by pairing with both devices at the same time. This protection is achieved by sharing some information between the devices through some independent channel. The IO capabilities of both devices dictate what algorithm is used. For details @see BLUETOOTH SPECIFICATION Version 5.0 | Vol 3, Part H - 2.3.5.1. You can change the IO capabilities after initialisation with setIoCapability(). This will take effect for all subsequent pairings.

#### Out of Band data used in pairing

Sharing this information through IO capabilities means user interaction which limits the degree of protection due to the limit of the amount of data that we can expect the user to transfer. Another solution is using OOB (out of band) communication to transfer this data instead which can send much more data making MITM attack even less likely to succeed. OOB data has to be exchanged by the application and provided to the SecurityManager. Use setOOBDataUsage() to indicate you want to use it. The same call also allows you to set whether or not the communication channel you are using to transmit the OOB data is itself secure against MITM protection - this will set the level of the link security achieved using pairing that uses this data.

The most secure pairing is provided by Secure Connections which relies on Elliptical Curve Cryptography. Support for Secure Connections is dependent on both the stack and controller on both sides supporting it. If either side doesn't support it Legacy Pairing will be used. This is an older standard of pairing. If higher security is required legacy pairing can be disabled by calling allowLegacyPairing(false);

#### Signing

Applications may require a level of security providing confidence that data transfers are coming from a trusted source. This can be achieved by encrypting the link which also provides added confidentiality. Encryption is a good choice when a device stays connected but introduces latency due to the need of encrypting the link if the device only connects periodically to transfer data. If confidentiality is not required data GATT server may allow writes to happen over an unencrypted link but authenticated by a signature present in each packet. This signature relies on having sent a signing key to the peer during pairing prior to sending any signed packets.

#### Persistence of Security information

SecurityManager stores all the data required for its operation on active links. Depending on resources available on the device it will also attempt to store data for disconnected devices which have bonded to be reused when reconnected. If the application has initialised a filesystem and the SecurityManager has been provided with a filepath during the init() call it may also provide data persistence across resets. This must be enabled by calling preserveBondingStateOnReset(). Persistence is not guaranteed and may fail if abnormally terminated. The SecurityManager may also fall back to a non-persistent implementation if the resources are too limited.

#### How to use

Call init() with your chosen settings before calling any other SecurityManager functions.

The SecurityManager communicates with your application through events. These will trigger calls in the EventHandler which you must provide by calling the setSecurityManagerEventHandler() function.

The most important process is pairing. This may be triggered manually by calling requestPairing() or may be called as a result of the application requiring encryption by calling setLinkEncryption() or as a result of the application requiring MITM protection through requestAuthentication().

All these can be implicitly called by using setLinkSecurity() to conveniently set the required security for the link. The SecurityManager will trigger all the process required to achieve the set security level. Security level can only be escalated. Asking the SecurityManager for a lower security level than the existing one will not fail but will result in a event informing the application through linkEncryptionResult() of the current level (which remains unchanged).

Depending on the IO capabilities and OOB usage settings different pairing algorithms will be chosen. They will produce appropriate events which must be handled by your EventHandler. If your event handler doesn't support all the calls you must not set IO capabilities or set OOB usage in such a way that would trigger them or else the pairing will fail (usually by timing out).

The simplest example is a pairing of a device with no IO capabilities and no OOB data available. With such limited pairing capabilities the "just works" method will be employed. This does not provide any MITM protection. The pairing (triggered implicitly or called explicitly) will result in an event being generated on the peer calling pairingRequest(). The event handler must make a decision (either in the application itself or based on user interaction) whether to accept the pairing and call accetPairing() or cancelPairing(). The result will be communicated on both peers through an event calling pairingResult() in the EventHandler.

### SecurityManager class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_security_manager.html)

### SecurityManager example

The SecurityManager example demonstrates both a central and a peripheral connecting, performing basic pairing and setting up link security.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-SM/)](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-SM/file/fcb1e0b995a9/source/main.cpp)
