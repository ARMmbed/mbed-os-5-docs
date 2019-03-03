## PSA Internal Storage

### Description

PSA internal storage APIs allows saving and retrieving data from PSA internal flash.

PSA internal storage implementation varies depending on the target type:
- on single core ARMv7-M target it PSA internal storage APIs are implemented by calling to "default" internal TDBStore instance.
- on PSA targets implementing SPM, PSA internal storage implemented as a secure service. PSA internal storage has access control list, 
  which makes sure that only the entries created from NSPE will be accessible to it.

### Specification

API specification in mbed-os specific context can be found here: [mbed-os/Storage](../../storage/storage.md) 

PSA specification can be found here [PSA Secure Storage](https://pages.arm.com/PSA-APIs)

### Doxygen

[![View code](https://www.mbed.com/embed/?type=library)](../mbed-os-api-doxy/psa__prot__internal__storage_8h.html)