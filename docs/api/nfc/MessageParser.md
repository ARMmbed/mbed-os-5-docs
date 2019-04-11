# MessageParser

The MessageParser class is an event-driven NDEF message parser. This class parses a buffer of data in input and produces parsing events. It then forwards these parsing events to its delegate.

## MessageParser class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1nfc_1_1ndef_1_1_message_parser.html)

## MessageParser example

```
void set_delegate(Delegate *delegate);
void parse(const Span<const uint8_t> &data_buffer);
```

## Related content

- [SimpleMessageParser](simplemessageparser.html) API reference.
- [MessageBuilder](messagebuilder.html) API reference.
- [NFC architecture](../reference/nfc-technology.html).
