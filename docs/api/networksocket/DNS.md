# DNS Resolver

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/class_d_n_s.png)<span>DNS class hierarchy</span></span>

The DNS resolver provides an interface to do DNS host name resolutions. You can use DNS host name resolution to convert resource names to IP addresses. You can make DNS host name resolution after connecting the interface. You can use the returned IP address to make the socket connection.

### Usage

The DNS resolver supports both blocking and asynchronous DNS host name resolutions.

To make a DNS host name resolution:

1. Instantiate and connect a network interface.
1. Call the `gethostbyname()` function to resolve address.

To make an asynchronous DNS host name resolution:

1. Create a callback function for asynchronous host name resolution.
1. Instantiate and connect network interface.
1. Call the `gethostbyname_async()` with callback function to resolve address.

To cancel an asynchronous host name resolution:

1. Store the unique ID that the `gethostbyname_async()` call returns.
1. Call the `gethostbyname_async_cancel()` with a unique ID to cancel the asynchronous address resolution.

### Asynchronous operation

The DNS resolver has a cache for the host names and IP addresses. If the host name is found from the cache, the `gethostbyname_async()` function returns a success right away. The callback is called before the function returns.

If the address is not in the cache, `gethostbyname_async()` returns an unique ID for the operation. The callback is called after a response arrives from the DNS server on the network or a timeout occurs. You can use the unique ID to cancel the DNS host name resolution if needed.

If `gethostbyname_async()` returns a failure, the callback is not called.

When designing the callback function, take following considerations into account:

Callback is called from thread context. If the callback takes more than 10ms to execute, it might prevent underlying thread processing. Do not make calls to network operations due to stack size limitations; the callback should not perform expensive operations, such as socket recv/send calls or blocking operations.

## DNS resolver class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/class_d_n_s.html)

## DNS resolver example

This DNS resolver example makes asynchronous DNS host name resolution.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/DNS_GetHostbyNameAsync_Example/)](https://os.mbed.com/teams/mbed_example/code/DNS_GetHostbyNameAsync_Example/file/d0f7d306a900/main.cpp)

## Troubleshooting information

Network interface `gethostbyname()` and `gethostbyname_async()` failure causes:

- `NSAPI_ERROR_DNS_FAILURE` indicates that DNS failed to complete successfully. Check the host name and network connection.
- `NSAPI_ERROR_NO_MEMORY` indicates that there was not enough memory on heap to make an address resolution.

## Related content

- [Network socket](network-socket.html) API overview.
