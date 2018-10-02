## NFC

Near-Field Communication (NFC) is a short-range radio technology. Mbed OS supports NFC card emulation through a controller or NFC EEPROM:

- [NFCController](nfccontroller.html) API reference.
- [NFCEEPROM](nfc-eeprom.html) API reference.

### NDEF APIs

The common data format for an NFC message is an NDEF message. An NDEF message is a collection of separate NDEF records. Each of these records is defined by a type, such as URI, Mime and Text, that identifies a payload and what the record contains.

Mbed OS provides NDEF APIs to construct and parse NDEF messages:

- [MessageParser]().
- [SimpleMessageParser]().
- [MessageBuilder]().

#### Parsing

The class `mbed::nfc::ndef::MessageParser` parses a buffer of data in input and produces parsing events that are forwarded to its delegate. To help you, we offer a more integrated parser (`mbed::nfc::ndef::common::SimpleMessageParser`) that parses well known NFC types records, such as Text, URI or Mime records, and produces usable objects out of the box.

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1nfc_1_1ndef_1_1_message_parser.html)

#### Related content

- [NFC architecture](/docs/development/reference/nfc-technology.html).
