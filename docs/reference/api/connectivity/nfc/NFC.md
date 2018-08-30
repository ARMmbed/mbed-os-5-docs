##   NFC

NFC stands for Near-Field Communication and is a short-range radio technology. You can use it to enable use cases such as contactless payments, access control or device pairing.

![N Mark][n_mark]

You can find more details on NFC about the [NFC Forum's website](https://nfc-forum.org/what-is-nfc/).

### NFC support in Mbed OS

Historically, NFC encompasses multiple protocols. NFC support in Mbed OS is based on the specifications the [NFC Forum](https://nfc-forum.org/our-work/specifications-and-application-documents/specifications/nfc-forum-technical-specifications/) publishes.

NFC offers three modes:

1. NFC card emulation.
1. NFC reader or writer.
1. NFC peer to peer.

Mbed OS supports the card emulation mode, either through the use of a controller or NFC EEPROM.

NFC support is available for the NXP PN512 transceiver. In terms of NFC EEPROMs, a driver for the ST M24SR EEPROM series is available - we also provide a [porting guide](https://os.mbed.com/contributing/connectivity/NFCEEPROMDriver.html) to add support for other NFC EEPROMs.

We also provide APIs to decode and encode NDEF messages. A NDEF message is a standardized encoding that most NFC devices, such as Android and iOS smartphones, can understand.

An NFC EEPROM can read from and write to a NDEF message. A NFC initiator can access the message through the NFC interface the EEPROM exposes.

The NFC Forum defines 5 Tag specifications, which define how to transmit and receive NDEF messages on top of various NFC technologies.

When using a controller, the Mbed OS NFC Framework can implement the [Type 4 Tag platform](https://nfc-forum.org/our-work/specifications-and-application-documents/specifications/tag-type-technical-specifications/). This means that the initiator can gnerate NDEF messages dynamically before each read and parse it after each write.

### NFC controllers and NFC EEPROMs

These components address different use cases, and you need to consider two factors: cost and functionality.

Most NFC controllers implement many modes of NFC and offer flexibility; however, they are typically more expensive than NFC EEPROMs.

NFC controllers typically support a large subset (if not all) of NFC Forum functionality, can act as either initiators or targets and are driven by an external stack. In Mbed OS, this means that you can generate NDEF messages "on demand" when the initiator reads them.

NFC EEPROMs behave like NFC tags whose memory can either be addressed through a wired (such as I2C) or NFC air interface. One benefit is that these work autonomously from a microcontroller. Some of them can also use the NFC field as a power source if they are powered off at the time.

### Getting started with NFC and example

NFC examples are available on [GitHub](https://github.com/ARMmbed/mbed-os-example-nfc) and demonstrate how to create NFC tags that you can be read from and write to using a phone.

![An Explore-NFC board attached to a Nucleo board][explorenfc_nucleo]

### API

There are two entrypoints for the API, depending on whether you are using a NFC Controller or EEPROM.

You must initiate either entry point with a driver instance, an event queue and a scratch buffer for NDEF messages.

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
    mbed::nfc::NFCController nfc(&pn512_driver, &queue, ndef_buffer);

    ...
}
```

A delegate mechanism handles events throughout the API.

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

#### NFC controller

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/FIXME)

#### NFC EEPROM

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/FIXME)

#### NDEF API

We provide API to construct and parse NDEF messages which is the common data format exchange for NFC messages.

A NDEF message is a collection of separate NDEF records where each of these records is defined by a type such as URI, Mime, Text that identifies what is contained in the record and a payload.

##### Parsing

The class `mbed::nfc::ndef::MessageParser` parse a buffer of data in input and produces parsing events that are forwarded to its delegate. To help developers we offer a more integrated parser (`mbed::nfc::ndef::common::SimpleMessageParser`) that parses well known NFC types records such as Text, URI or Mime records and produces usable objects out of the box.

```
#include "nfc/ndef/common/SimpleMessageParser.h"

using mbed::nfc::ndef::Record;
using mbed::nfc::ndef::RecordType;
using mbed::nfc::ndef::RecordID;
using mbed::nfc::ndef::MessageParser;
using mbed::nfc::ndef::common::Text;
using mbed::nfc::ndef::common::URI;
using mbed::nfc::ndef::common::Mime;

using mbed::nfc::ndef::common::SimpleMessageParser;

void parse_ndef_message(const Span<const uint8_t> &buffer) {
    SimpleMessageParser parser;
    struct : SimpleMessageParser::Delegate {
        virtual void on_parsing_started() {
            printf("parsing started\r\n");
        }

        virtual void on_text_parsed(const Text &text, const RecordID &) {
            printf("Text record parsed.\r\n");
            printf(
                "\tlanguage: %.*s\r\n",
                text.get_language_code().size(), text.get_language_code().data()
            );
            printf("\ttext: %.*s\r\n",  text.get_text().size(), text.get_text().data());
        }

        virtual void on_uri_parsed(const URI &uri, const RecordID &) {
            printf("URI parsed.\r\n");
            printf("\tid: %d\r\n", uri.get_id());
            printf("\tvalue: %.*s\r\n",  uri.get_uri_field().size(), uri.get_uri_field().data());
        }

        virtual void on_mime_parsed(const Mime &mime, const RecordID &) {
            printf("Mime object parsed.\r\n");
            printf("\ttype: %.*s\r\n", mime.get_mime_type().size(), mime.get_mime_type().data());
            printf("\tcontent size: %d\r\n", mime.get_mime_content().size());
        }

        virtual void on_unknown_record_parsed(const Record &record) {
            printf("Unknown record parsed.\r\n");
            printf(
                "\ttype: %d, type_value: %.*s\r\n",
                record.type.tnf, record.type.value.size(), record.type.value.data()
            );
            printf(
                "\tpayload size: %d, payload: %.*s\r\n",
                record.payload.size(), record.payload.size(), record.payload.data()
            );
        }

        virtual void on_parsing_terminated() {
            printf("parsing terminated\r\n");
        }

        virtual void on_parsing_error(MessageParser::error_t error) {
            printf("Parsing error: %d\r\n", error);
        }
    } delegate;

    parser.set_delegate(&delegate);
    parser.parse(buffer);
}
```

Application can extend capabilities of `SimpleMessageParser` by adding new record parsers (`mbed::nfc::ndef::RecordParser`) at runtime.

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/FIXME)

##### Construction

The class `mbed::nfc::ndef::MessageBuilder` build a NDEF message into a user provided buffer. `URI`, `Text` and `Mime` type can be serialized in the builder with the help of the member function `append_as_record`.

```
#include "nfc/ndef/MessageBuilder.h"

using mbed::nfc::ndef::MessageBuilder;
using mbed::nfc::ndef::common::Text;
using mbed::nfc::ndef::common::URI;

size_t build_ndef_message(const Span<uint8_t> &buffer) {
    MessageBuilder builder(buffer);

    URI uri(URI::HTTPS_WWW, span_from_cstr("mbed.com"));
    Text text(Text::UTF8, span_from_cstr("en-US"), span_from_cstr("mbed website"));

    uri.append_as_record(builder);
    text.append_as_record(builder, /* last record */ true);

    return builder.get_message().size();
}
```

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/FIXME)

### Design

A detailed design document is available [within the Mbed OS source tree](https://github.com/ARMmbed/mbed-os/docs/design-documents/nfc/nfc_design.md). It details the rationale behind the API design.

[explorenfc_nucleo]: explorenfc_nucleo.jpg
[n_mark]: n_mark.png
