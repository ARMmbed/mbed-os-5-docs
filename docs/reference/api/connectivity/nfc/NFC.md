##   NFC
###  Introduction

NFC stands for Near-Field Communication and is a short-range radio technology.
It is used to enable use cases such as contactless payments, access control or device pairing.

![N Mark][n_mark]

More details on NFC can be found on the [NFC Forum's website](https://nfc-forum.org/what-is-nfc/) or on [Wikipedia](https://en.wikipedia.org/wiki/Near-field_communication).

### NFC Support in Mbed OS
Historically NFC encompasses multiple protocols.
NFC support in Mbed OS is based on the specifications published by the [NFC Forum](https://nfc-forum.org/our-work/specifications-and-application-documents/specifications/nfc-forum-technical-specifications/).

NFC offers three modes:
1. NFC card emulation
2. NFC reader/writer
3. NFC peer to peer

At present Mbed OS supports the card emulation mode, either through the use of a controller or NFC EEPROM.

Currently NFC support is available for the NXP PN512 transceiver.
In terms of NFC EEPROMs, a driver for the ST M24SR EEPROM series is available - we also provide a [porting guide](https://os.mbed.com/contributing/connectivity/NFCEEPROMDriver.html) to add support for other NFC EEPROMs.

We also provide APIs to decode and encode NDEF messages. A NDEF message is a standardized encoding that can be understood by most NFC devices such as Android & iOS smartphones.

A NDEF message can be read from and written to an NFC EEPROM. A NFC initiator can access the message through the NFC interface exposed by the EEPROM.

The NFC Forum defines 5 Tag specifications which define how to transmit and receive NDEF messages on top of various NFC technologies.

When using a controller, the [Type 4 Tag platform](https://nfc-forum.org/our-work/specifications-and-application-documents/specifications/tag-type-technical-specifications/) can be implemented by the Mbed OS NFC Framework. This means that NDEF messages can be generated dynamically before each read and parsed after each write from the initiator.

### Should I use a NFC controller or NFC EEPROM?

These components address different use cases and two factors need to be taken into account: cost and functionality.

Most NFC controllers implement many modes of NFC and offer the most flexibility, however they are typically more expensive than NFC EEPROMs.

NFC controllers typically support a large subset (if not all) of NFC Forum functionality, can either act as initiators or target and are driven by an external stack. In Mbed OS, this means that you can generate NDEF messages "on demand" when these are read by the initiator.

NFC EEPROMs behave like simple NFC tags which memory can either be addressed through a wired (such as I2C) or NFC air interface. One benefit is that these work autonomously from a microcontroller. Some of them can also use the NFC field as a power source if they are powered off at the time.

### Getting Started with NFC and example

NFC examples are available on [Github](https://github.com/ARMmbed/mbed-os-example-nfc) and demonstrate various ways of creating NFC tags that can be read and written using a phone.

![An Explore-NFC board attached to a Nucleo board][explorenfc_nucleo]

### API

There are two entrypoints for the API, depending on whether a NFC Controller or EEPROM is being used.

In both cases, these require to be initialized with a driver instance, an event queue and a scratch buffer for NDEF messages.

```cpp
#include "stdint.h"

#include "NFC.h"
#include "events/EventQueue.h"
#include "nfc/controllers/PN512Driver.h"
#include "nfc/controllers/PN512SPITransportDriver.h"

static uint8_t ndef_buffer[1024] = {0};

int main() {
    mbed::nfc::PN512SPITransportDriver pn512_transport(D11, D12, D13, D10, A1, A0);
    mbed::nfc::PN512Driver pn512_driver(&pn512_transport);
    events::EventQueue queue;
    mbed::nfc::NFCController nfc(&pn512_driver, &queue, ndef_buffer, sizeof(ndef_buffer));

    ...
}
```

Events are handled through a delegates mechanism throughout the API.

For instance, a delegate for a NFC controller can look similar to this:

```cpp
struct NFCDelegate : mbed::nfc::NFCController::Delegate {
    virtual void on_discovery_terminated(nfc_discovery_terminated_reason_t reason) {
        printf("Discovery terminated:\r\n");
        if(reason != nfc_discovery_terminated_completed) {
            nfc_ptr->start_discovery(); // Error, restart discovery
        }
    }
    virtual void on_nfc_initiator_discovered(const SharedPtr< mbed::nfc::NFCRemoteInitiator> &nfc_initiator) {
        printf("Remote inititator detected\r\n");
        nfc_initiator->set_delegate(nfc_initiator_delegate_ptr);
        nfc_initiator->connect(); // Connect to the initiator
    }
};
```


#### NFC Controller

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/FIXME)

#### NFC EEPROM

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/FIXME)


####    NDEF API

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/FIXME)


### Design

A detailed design document is available [within the Mbed OS source tree](https://github.com/ARMmbed/mbed-os/docs/design-documents/nfc/nfc_design.md). It details the rationale behind the API design.

[explorenfc_nucleo]: explorenfc_nucleo.jpg
[n_mark]: n_mark.png