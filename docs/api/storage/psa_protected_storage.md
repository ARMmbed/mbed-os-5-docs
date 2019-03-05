## PSA protected storage

PSA protected storage APIs enable saving data to and retrieving data from PSA protected storage.

Unlike [PSA internal storage](../apis/psa_internal_storage.html), PSA protected storage always runs in the Non-Secure Processing Environment (NSPE) and redirects calls to the KVStore static API.

<span class="notes">**Note:** In general, we recommend using the [KVStore static API](../storage/KVStoreGlobalAPI.html) in the NSPE.</span>

### PSA protected storage class reference

[![View code](https://www.mbed.com/embed/?type=library)](../mbed-os-api-doxy/protected__storage_8h.html)

### Related content

* [API specification in Mbed OS](../apis/storage.html)

* [PSA Secure Storage](https://pages.arm.com/PSA-APIs).
