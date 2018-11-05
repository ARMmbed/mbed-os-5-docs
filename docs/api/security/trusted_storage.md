<h2 id="blockdevice-port">PSA Internal Trusted Storage Reference API</h2>

## PSA Internal Trusted Storage

The PSA Internal Trusted Storage is a PSA Root of Trust Service which provides key (uid) value secure storage in internal flash for small data items.
The main use cases for PSA Internal Trusted Storage APIs are:
- Provide storage solution for persistent keys in PSA Crypto Service.
- Store rollback protection tokens for external application secure storage.
- Store persistent context in PSA Root of Trust services (i.e. epoch, device unique key, etc.)

 PSA Internal Trusted Storage stores data by a uid, a unique identifier for the data.

The API allows users to:
* Create a new or modify an existing uid/data pair
* Retrieve the value associated with a provided uid
* Retrieve the metadata about the provided uid
* Remove the provided uid and its associated data from the storage

The Internal Trusted Storage supports a "write once" feature which enforces that the data associated with a key will not be able to be modified or deleted.

**Note:** PSA Internal Trusted Storage is designed for the use of PSA Crypto Service. ARM recommends that applications use other storage stacks.

### Internal Trusted Storage API Reference

TODO: ADD A LINK TO DOXYGEN FILES

[![View code](https://www.mbed.com/embed/?type=library)](http://add-a-link-to-doxygen-file.html)

### Internal Trusted Storage Example

TODO: ADD A LINK TO DOXYGEN FILES

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-nvstore)](https://add-a-link-to-test-or-example-file.cpp)
