## Platform service

The Platform service introduces System Reset and [PSA Lifecycle](./lifecycle/psa_lifecycle.md) APIs.

The System Reset API allows Nonsecure Processing environment to request a system reset.
[Trusted Base System Architecture for M (TBSA-M)](https://pages.arm.com/psa-resources-tbsa-m.html) specification defines that power state should be managed by SPE.
System reset will be carried out by SPE once all critical task are finished.

### Platform service class reference

[![View code](https://www.mbed.com/embed/?type=library)](../mbed-os-api-doxy/lifecycle_8h.html)

### Example
