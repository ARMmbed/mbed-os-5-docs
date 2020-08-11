# SecurityManager

SecurityManager deals with authentication and encryption for the Bluetooth Low Energy link. The pairing and optionally bonding processes provide this. The SecurityManager achieves bonding by saving the pairing information and reusing it on subsequent reconnections. This saves time because the pairing does not have to be performed again.

The pairing process may produce a set of keys to be used during current or later connections. The SecurityManager handles these, and they include the Long Term Encryption Key (LTK), the Identity Resolving Key (IRK) and the Connection Signature Resolving Key (CSRK). The SecurityManager uses the LTK to encrypt subsequent connections without having to pair again. The Link Controller uses IRK to identify peers who use random resolvable addresses. The application uses CSRK to sign and authenticate signed data.

The pairing process may provide man-in-the-middle protection (MITM). The SecurityManager achieves this through various means, including out of band communication, depending on the capabilities of the local and peer device.

The SecurityManager stores the keys, permanently if possible, to speed security requests on subsequent connections.

Security requests may come explicitly from the user application or implicitly from the GATT server based on attribute requirements.

## Pairing

There are several ways to provide different levels of security during pairing depending on your requirements and the facilities the application provides. The process starts with initializing the SecurityManager with default options for new connections. You can later change some settings per link or globally.

The important settings in the `init()` function are the MITM requirement and IO capabilities. MITM protection prevents an attack where one device can impersonate another device by pairing with both devices at the same time. You can achieve this protection by sharing information between the devices through an independent channel. The IO capabilities of both devices dictate what algorithm is used. For details, see BLUETOOTH SPECIFICATION Version 5.0 | Vol 3, Part H - 2.3.5.1. You can change the IO capabilities after initialization with `setIoCapability()`. This takes effect for all subsequent pairings.

Secure Connections, which relies on elliptical curve cryptography, provides the most secure pairing. Support for Secure Connections depends on both the stack and controller on both sides supporting it. If either side doesn't support it, legacy pairing is used. This is an older standard of pairing. If you require higher security, you can disable legacy pairing by calling `allowLegacyPairing(false);`.

## Out of band (OOB) data used in pairing

Sharing this information through IO capabilities means user interaction, which limits the degree of protection due to the limit of the amount of data that you can expect to transfer. Another solution is using out of band (OOB) communication to transfer this data. OOB communication can send more data and make MITM attacks less likely to succeed. The application must exchange OOB data and provide it to the SecurityManager. Use `setOOBDataUsage()` to indicate you want to use it. With this same call, you can set whether the communication channel you are using to transmit the OOB data is itself secure against MITM protection - this sets the level of the link security achieved using pairing that uses this data.

## Signing

Applications may require a level of security providing confidence that data transfers are coming from a trusted source. You can achieve this by encrypting the link, which also provides added confidentiality. Encryption is a good choice when a device stays connected but introduces latency due to the need for encrypting the link if the device only connects periodically to transfer data. If you do not require confidentiality, the GATT server may allow writes to happen over an unencrypted link but authenticated by a signature present in each packet. This signature relies on having sent a signing key to the peer during pairing prior to sending any signed packets.

## Persistence of security information

SecurityManager stores all the data required for its operation on active links. Depending on resources available on the device, it also stores data for disconnected devices, which have bonded to be reused when reconnected. If the application has initialized a file system and the SecurityManager has received a file path during the `init()` call, SecurityManager may also provide data persistence across resets. You must enable this by calling `preserveBondingStateOnReset()`. Persistence may fail if abnormally terminated. SecurityManager may also fall back to a nonpersistent implementation if the resources are too limited.

## How to use

Call `init()` with your chosen settings before calling any other SecurityManager functions.

The SecurityManager communicates with your application through events. These trigger calls in the EventHandler that you must provide by calling the `setSecurityManagerEventHandler()` function.

The most important process is pairing. You may trigger this manually by calling `requestPairing()`. Pairing may also result from the application requiring encryption by calling `setLinkEncryption()` or the application requiring MITM protection through `requestAuthentication()`.

You can call all of these implicitly by using `setLinkSecurity()` to set the required security for the link. The SecurityManager triggers the process required to achieve the set security level. You can only escalate the security level; asking the SecurityManager for a lower security level than the existing one does not fail, but results in an event informing the application through `linkEncryptionResult()` of the current level (which remains unchanged).

The chosen pairing algorithms depend on the IO capabilities and OOB use settings. They produce appropriate events, which your EventHandler must handle. If your event handler doesn't support all the calls, you must not set IO capabilities or set OOB use in such a way that would trigger them, or else the pairing fails (usually by timing out).

The simplest example is a pairing of a device with no IO capabilities and no OOB data available. This does not provide any MITM protection. The pairing (triggered implicitly or called explicitly) results in the generation of an event on the peer calling `pairingRequest()`. The event handler must make a decision (either in the application itself or based on user interaction) whether to accept the pairing and call `acceptPairing()` or `cancelPairing()`. An event calling `pairingResult()` in the EventHandler communicates te result on both peers.

## SecurityManager class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/classble_1_1_security_manager.html)

## SecurityManager example

The SecurityManager example demonstrates both a central and a peripheral connecting, performing basic pairing and setting up link security.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-ble/blob/mbed-os-6.0.0/BLE_SM/source/)](https://github.com/ARMmbed/mbed-os-example-ble/blob/mbed-os-6.0.0/BLE_SM/source/main.cpp)
