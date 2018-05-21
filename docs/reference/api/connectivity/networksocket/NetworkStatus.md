<h2 id="network-status">Network status</h2>

Purpose of this interface is to provide a way to inform about connection state changes asynchronously. This is accomplished
by providing a method to register a callback function to a socket. The callback gets triggered each time the network interface's state changes. 

### Usage


Possible network states the callback needs to be able to handle
 
```cpp
/** Enum of connection status types
 *
 *  Valid error codes have negative values.
 *
 *  @enum nsapi_connection_status
 */
 typedef enum nsapi_connection_status {
    NSAPI_STATUS_LOCAL_UP           = 0,        /*!< local IP address set */
    NSAPI_STATUS_GLOBAL_UP          = 1,        /*!< global IP address set */
    NSAPI_STATUS_DISCONNECTED       = 2,        /*!< no connection to network */
    NSAPI_STATUS_CONNECTING         = 3,        /*!< connecting to network */
    NSAPI_STATUS_ERROR_UNSUPPORTED  = NSAPI_ERROR_UNSUPPORTED
} nsapi_connection_status_t;
```

An interface which is to be monitored - ethernet used here only as an example

```cpp
EthernetInterface eth;
```

There is need to provide the callback function itself

```cpp
void status_callback(nsapi_event_t status, intptr_t param)
{
    printf("Connection status changed!\r\n");
    switch(param) {
        case NSAPI_STATUS_LOCAL_UP:
            printf("Local IP address set!\r\n");
            break;
        case NSAPI_STATUS_GLOBAL_UP:
            printf("Global IP address set!\r\n");
            break;
        case NSAPI_STATUS_DISCONNECTED:
            printf("No connection to network!\r\n");
            break;
        case NSAPI_STATUS_CONNECTING:
            printf("Connecting to network!\r\n");
            break;
        default:
            printf("Not supported");
            break;
    }
}
```

Now, the callback function is to be registered to the interface. The socket needs to be set in
non-blocking mode for the asynchronous behavior.  

```cpp
    eth.attach(&status_callback);
    eth.set_blocking(false);
```

### Example

How to register a status callback that gets triggered when connection state changes. It depends from a network interface 
if this functionality is provided.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/TCPSocket_ConnStateCb_Example/)](https://os.mbed.com/teams/mbed_example/code/TCPSocket_ConnStateCb_Example/file/8a8191e3d305/main.cpp)

### Related content

- [Network socket](/docs/development/reference/network-socket.html) API reference overview.
