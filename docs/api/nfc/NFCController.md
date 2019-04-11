# NFCController

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1nfc_1_1_n_f_c_controller.png)<span>NFCController class hierarchy</span></span>

Using an NFC controller with Mbed OS allows you to emulate NFC tags that a smartphone can read, as well as generate NDEF messages on demand.

To use an NFC controller, you must initiate the instance with a driver instance, an event queue and a scratch buffer for NDEF messages.

## NFCController class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1nfc_1_1_n_f_c_controller.html)

## NFCController example

```cpp TODO
#include "stdint.h"

#include "NFC.h"
#include "events/EventQueue.h"
#include "nfc/controllers/PN512Driver.h"
#include "nfc/controllers/PN512SPITransportDriver.h"

static uint8_t ndef_buffer[1024] = {0};

int main() {
    mbed::nfc::PN512SPITransportDriver pn512_transport(D11, D12, D13, D10, A1, A0);
    mbed::nfc::PN512Driver pn512_driver(&pn512_transport);
    events::EventQueue queue;
    mbed::nfc::NFCController nfc(&pn512_driver, &queue, ndef_buffer);

    ...
}
```

A delegate mechanism handles events throughout the API.

For instance, a delegate for a NFC controller can look similar to this:

```cpp TODO
struct NFCDelegate : mbed::nfc::NFCController::Delegate {
    virtual void on_discovery_terminated(nfc_discovery_terminated_reason_t reason) {
        printf("Discovery terminated:\r\n");
        if(reason != nfc_discovery_terminated_completed) {
            nfc_ptr->start_discovery(); // Error, restart discovery
        }
    }
    virtual void on_nfc_initiator_discovered(const SharedPtr< mbed::nfc::NFCRemoteInitiator> &nfc_initiator) {
        printf("Remote inititator detected\r\n");
        nfc_initiator->set_delegate(nfc_initiator_delegate_ptr);
        nfc_initiator->connect(); // Connect to the initiator
    }
};
```

### Related content

- [NFC architecture](../reference/nfc-technology.html).
