# SimpleMessageParser

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1nfc_1_1ndef_1_1common_1_1_simple_message_parser.png)<span>SimpleMessageParser class hierarchy</span></span>

The SimpleMessageParser class is a more integrated parser than the MessageParser class. Like MessageParser, SimpleMessageParser parses data and sends parsing events to its delegate. However, SimpleMessageParser also includes subparsers for well-known NFC types records, such as Text, URI or Mime records, and produces usable objects out of the box. User defined parsers can be injected at runtime to extend the capabilities of the SimpleMessageParser.

## SimpleMessageParser class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1nfc_1_1ndef_1_1common_1_1_simple_message_parser.html)

## SimpleMessageParser example

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

An application can extend capabilities of `SimpleMessageParser` by adding new record parsers (`mbed::nfc::ndef::RecordParser`) at runtime.

## Related content

- [MessageParser](messageparser.html) API reference.
- [MessageBuilder](messagebuilder.html) API reference.
- [NFC architecture](../reference/nfc-technology.html).
