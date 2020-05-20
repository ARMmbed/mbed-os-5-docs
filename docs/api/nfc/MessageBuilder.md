# MessageBuilder

Mbed OS provides this API to construct NDEF messages, the common data format exchange for NFC messages. The class `mbed::nfc::ndef::MessageBuilder` builds an NDEF message into a user-provided buffer. `URI`, `Text` and `Mime` types can be serialized in the builder with the help of the member function `append_as_record`.

## MessageBuilder class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/classmbed_1_1nfc_1_1ndef_1_1_message_builder.html)

## MessageBuilder example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-MessageBuilder)](https://github.com/ARMmbed/mbed-os-snippet-MessageBuilder/blob/master/main.cpp)

## Related content

- [MessageParser](messageparser.html) API reference.
- [SimpleMessageParser](simplemessageparser.html) API reference.
- [NFC architecture](../apis/nfc-technology.html).
