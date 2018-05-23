## DNS Resolver

The DNS resolver provides an interface to do DNS host name resolutions.

### Usage

The DNS resolver supports both blocking and asynchronous DNS host name resolutions.

To make a DNS host name resolution:

1. Instantiate and connect a network interface.
1. Call the `gethostbyname()` function to resolve address.

To make an asynchronous DNS host name resolution:

1. Create a callback function for asynchronous host name resolution.
1. Instantiate and connect network interface.
1. Call the `gethostbyname_async()` with callback function to resolve address.

The callback returns the result of the DNS operation. If `gethostbyname_async()` returns a failure, the callback is not called. If the result is a success (the IP address was found from cache), the callback is called before the `gethostbyname_async()` function returns.

To cancel an asynchronous host name resolution:

1. Store the unique ID that the `gethostbyname_async()` call returns.
1. Call the `gethostbyname_async_cancel()` with a unique ID to cancel the asynchronous address resolution.

When you cancel the translation, the callback is not called.

Asynchronous host name resolution callback restrictions:

Callback is called from thread context. If the callback takes more than 10ms to execute, it might prevent underlying thread processing. Do not make calls to network operations due to stack size limitations; the callback should not perform expensive operations, such as socket recv/send calls or blocking operations.

The following code demonstrates steps to make an asynchronous DNS host name resolution:

```
#include "mbed.h"
#include "nsapi_types.h"
#include "EthernetInterface.h"
#include "SocketAddress.h"
#include "Semaphore.h"

rtos::Semaphore callback_semaphore;
SocketAddress address;
nsapi_error_t result;

// Callback for asynchronous host name resolution
void hostbyname_callback(nsapi_error_t res, SocketAddress *addr)
{
    // Store result and release semaphore
    result = res;
    address = *addr;
    callback_semaphore.release();
}

int main()
{
    // Initialise network interface
    EthernetInterface eth;
    eth.connect();

    // Initiate asynchronous DNS host name resolution
    eth.gethostbyname_async("www.mbed.com", hostbyname_callback);

    // Wait for callback semaphore
    callback_semaphore.wait();

    // Print result
    printf("Result %s, Address %s\r\n", result == NSAPI_ERROR_OK ? "OK" : "FAIL",
        result == NSAPI_ERROR_OK ? address.get_ip_address() : "NONE");

    // Disconnect network interface
    eth.disconnect();
}

```

### DNS resolver class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_dns.html)

### Troubleshooting information

Network interface `gethostbyname()` and `gethostbyname_async()` failure causes:

- `NSAPI_ERROR_DNS_FAILURE` indicates that DNS failed to complete successfully. Check the host name and network connection.
- `NSAPI_ERROR_NO_MEMORY` indicates that there was not enough memory on heap to make an address resolution.

### Related content

- [Network socket](/docs/development/reference/network-socket.html) API overview.
