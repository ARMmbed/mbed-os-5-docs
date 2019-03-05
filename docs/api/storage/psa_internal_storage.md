## PSA internal storage

PSA internal storage APIs enable software running in a secure environment to save data to and retrieve data from a PSA internal flash.

The PSA internal storage functionality varies depending on the target type:

* On a single core ARMv7-M target, PSA internal storage APIs call the default internal TDBStore instance allocated by the KVStore configuration. For more information, see [KVStore configuration](..reference/storage.html#kvstore-configuration).
* On PSA targets that implement Secure Partition Manager (SPM), PSA internal storage is implemented as a secure service. The service uses an access control list, which ensures that software executed in the Non-Secure Processing Environment (NSPE) cannot access entries created by the Secure Processing Environment (SPE).

### PSA internal storage class reference

[![View code](https://www.mbed.com/embed/?type=library)](../mbed-os-api-doxy/psa__prot__internal__storage_8h.html)

### Example

### Related content

* [API specification in Mbed OS](../apis/storage.html).

* [PSA secure storage](https://pages.arm.com/PSA-APIs).
