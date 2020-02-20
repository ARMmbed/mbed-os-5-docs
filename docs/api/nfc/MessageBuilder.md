# MessageBuilder

Mbed OS provides this API to construct NDEF messages, the common data format exchange for NFC messages. The class `mbed::nfc::ndef::MessageBuilder` builds an NDEF message into a user-provided buffer. `URI`, `Text` and `Mime` types can be serialized in the builder with the help of the member function `append_as_record`.

## MessageBuilder class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1nfc_1_1ndef_1_1_message_builder.html)

## MessageBuilder example

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

## Related content

- [MessageParser](messageparser.html) API reference.
- [SimpleMessageParser](simplemessageparser.html) API reference.
- [NFC architecture](../reference/nfc-technology.html).
