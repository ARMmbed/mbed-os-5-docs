# NFC EEPROM

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1nfc_1_1_n_f_c_e_e_p_r_o_m.png)<span>NFCEEPROM class hierarchy</span></span>

An NFC EEPROM can store NDEF messages. You can use a smartphone access the message through the NFC interface the EEPROM exposes.

To use an NFC EEPROM, you must initiate the instance with a driver instance, an event queue and a scratch buffer for NDEF messages.

## NFCEEPROM class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1nfc_1_1_n_f_c_e_e_p_r_o_m.html)

## NFCEEPROM example

```cpp TODO
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

### Related content

- [NFC architecture](../reference/nfc-technology.html).
