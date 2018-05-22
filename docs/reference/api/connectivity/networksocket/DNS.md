## DNS Resolver

The DNS resolver provides an interface to do DNS host name resolutions.

### Usage

The DNS resolver supports both blocking and asynchronous DNS host name resolutions.

To make a DNS host name resolution: 

1. Instantiate and connect network interface.
1. Call the `gethostbyname()` function to resolve address. 

To make an asynchronous DNS host name resolution:

1. Create callback function for asynchronous host name resolution. 
1. Instantiate and connect network interface.
1. Call the `gethostbyname_async()` with callback function to resolve address.

Result of the DNS operation is returned by the callback. If `gethostbyname_async()` returns failure, callback will not be called. In case result is success (IP address was found from cache), callback will be called before `gethostbyname_async()` function returns.

To cancel asynchronous host name resolution:

1. Store the unique ID returned by `gethostbyname_async()` call.
1. Call the `gethostbyname_async_cancel()` with unique ID to cancel the asynchronous address resolution.

When translation is cancelled, callback will not be called.

Asynchronous host name resolution callback restrictions:

Callback is called from thread context. It should not take more than 10ms to execute, otherwise it might prevent underlying thread processing. A portable user of the callback should not make calls to network operations due to stack size limitations. The callback should not perform expensive operations such as socket recv/send calls or blocking operations.

Following code demonstrates steps to make asynchronous DNS host name resolution:


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

- `NSAPI_ERROR_DNS_FAILURE` indicates that DNS failed to complete successfully. Check host name and network connection.
- `NSAPI_ERROR_NO_MEMORY` indicates that there was not enough memory on heap to make address resolution.

### Related content

- [Network socket](/docs/development/reference/network-socket.html) API overview.
