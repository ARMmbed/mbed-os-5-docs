### NDEF API

Mbed OS provides this API to construct and parse NDEF messages, which is the common data format exchange for NFC messages.

An NDEF message is a collection of separate NDEF records. Each of these records is defined by a type, such as URI, Mime and Text, that identifies a payload and what the record contains.

#### Parsing

The class `mbed::nfc::ndef::MessageParser` parses a buffer of data in input and produces parsing events that are forwarded to its delegate. To help you, we offer a more integrated parser (`mbed::nfc::ndef::common::SimpleMessageParser`) that parses well known NFC types records, such as Text, URI or Mime records, and produces usable objects out of the box.

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

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1nfc_1_1ndef_1_1_message_parser.html)

<span class="images">![](https://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/structmbed_1_1nfc_1_1ndef_1_1_message_parser_1_1_delegate.html)<span>SimpleMessageParser class hierarchy</span></span>

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1nfc_1_1ndef_1_1common_1_1_simple_message_parser.html)

#### Construction

The class `mbed::nfc::ndef::MessageBuilder` builds an NDEF message into a user-provided buffer. `URI`, `Text` and `Mime` types can be serialized in the builder with the help of the member function `append_as_record`.

```
#include "nfc/ndef/MessageBuilder.h"

using mbed::nfc::ndef::MessageBuilder;
using mbed::nfc::ndef::common::Text;
using mbed::nfc::ndef::common::URI;

size_t build_ndef_message(const Span<uint8_t> &buffer) {
    MessageBuilder builder(buffer);

    URI uri(URI::HTTPS_WWW, span_from_cstr("mbed.com"));
    Text text(Text::UTF8, span_from_cstr("en-US"), span_from_cstr("Mbed website"));

    uri.append_as_record(builder);
    text.append_as_record(builder, /* last record */ true);

    return builder.get_message().size();
}
```

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1nfc_1_1ndef_1_1_message_builder.html)
