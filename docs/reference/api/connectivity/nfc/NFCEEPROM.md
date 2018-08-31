## NFC EEPROM

An NFC EEPROM can store NDEF messages. You can use a smartphone access the message through the NFC interface the EEPROM exposes.

To use an NFC EEPROM, you must initiate the instance with a driver instance, an event queue and a scratch buffer for NDEF messages.

### NFC EEPROM class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/FIXME)

### NFC EEPROM example

```cpp
#include "stdint.h"

#include "NFC.h"
#include "events/EventQueue.h"
#include "m24sr_driver.h"

static uint8_t ndef_buffer[1024] = {0};

int main() {
    mbed::nfc::vendor::ST::M24srDriver m24sr_driver(p10, p11);
    events::EventQueue queue;
    mbed::nfc::NFCEEPROM nfc(&m24sr_driver, &queue, ndef_buffer);

    ...
    nfc.write_ndef_message();
}
```
