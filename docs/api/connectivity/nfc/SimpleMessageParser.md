# SimpleMessageParser

<span class="images">![](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/classmbed_1_1nfc_1_1ndef_1_1common_1_1_simple_message_parser.png)<span>SimpleMessageParser class hierarchy</span></span>

The SimpleMessageParser class is a more integrated parser than the MessageParser class. Like MessageParser, SimpleMessageParser parses data and sends parsing events to its delegate. However, SimpleMessageParser also includes subparsers for well-known NFC types records, such as Text, URI or Mime records, and produces usable objects out of the box. User defined parsers can be injected at runtime to extend the capabilities of the SimpleMessageParser.

## SimpleMessageParser class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/classmbed_1_1nfc_1_1ndef_1_1common_1_1_simple_message_parser.html)

## SimpleMessageParser example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-SimpleMessageParser/tree/v6.9)](https://github.com/ARMmbed/mbed-os-snippet-SimpleMessageParser/blob/v6.9/main.cpp)

An application can extend capabilities of `SimpleMessageParser` by adding new record parsers (`mbed::nfc::ndef::RecordParser`) at runtime.

## Related content

- [MessageParser](messageparser.html) API reference.
- [MessageBuilder](messagebuilder.html) API reference.
- [NFC architecture](../apis/nfc-technology.html).
