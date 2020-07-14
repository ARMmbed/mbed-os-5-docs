# NFCController

<span class="images">![](https://os.mbed.com/docs/mbed-os/v6.2/mbed-os-api-doxy/classmbed_1_1nfc_1_1_n_f_c_controller.png)<span>NFCController class hierarchy</span></span>

Using an NFC controller with Mbed OS allows you to emulate NFC tags that a smartphone can read, as well as generate NDEF messages on demand.

To use an NFC controller, you must initiate the instance with a driver instance, an event queue and a scratch buffer for NDEF messages.

## NFCController class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.2/mbed-os-api-doxy/classmbed_1_1nfc_1_1_n_f_c_controller.html)

## NFCController example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-NFCController/tree/v6.0)](https://github.com/ARMmbed/mbed-os-snippet-NFCController/blob/v6.0/main.cpp)

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

## Related content

- [NFC architecture](../apis/nfc-technology.html).
