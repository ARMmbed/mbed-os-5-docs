## NFC

Near-Field Communication (NFC) is a short-range radio technology. Mbed OS supports NFC card emulation through a controller or NFC EEPROM:

- [NFCController](nfccontroller.html) API reference.
- [NFCEEPROM](nfc-eeprom.html) API reference.

### NDEF APIs

The common data format for an NFC message is an NDEF message. An NDEF message is a collection of separate NDEF records. Each of these records is defined by a type, such as URI, Mime and Text, that identifies a payload and what the record contains.

Mbed OS provides NDEF APIs to construct and parse NDEF messages:

- [MessageParser](messageparser.html).
- [SimpleMessageParser](simplemessageparser.html).
- [MessageBuilder](messagebuilder.html).

#### Related content

- [NFC architecture](/docs/development/reference/nfc-technology.html).
