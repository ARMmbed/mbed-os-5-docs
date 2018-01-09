### NetworkStack

The Network-Socket-API (NSAPI) provides a TCP/UDP API on top of any IP based network interface. With the NSAPI, you can write applications and libraries that use TCP/UDP Sockets without regard to the type of IP connectivity. In addition to providing the TCP/UDP API, the NSAPI includes virtual base classes for the different IP interface types.

#### Class hierarchy

All network-socket API implementations inherit from two classes: a [NetworkStack](https://os.mbed.com/docs/v5.7/mbed-os-api-doxy/class_network_stack.html) and a communication specific subclass of [NetworkInterface](https://os.mbed.com/docs/v5.7/mbed-os-api-doxy/class_network_interface.html).

##### NetworkInterface Class

The current NetworkInterface subclasses are [CellularInterface](https://os.mbed.com/docs/v5.7/mbed-os-api-doxy/class_cellular_interface.html), [EthernetInterface](https://os.mbed.com/docs/v5.7/mbed-os-api-doxy/class_eth_interface.html), [MeshInterface](https://os.mbed.com/docs/v5.7/mbed-os-api-doxy/class_mesh_interface.html) and [WiFiInterface](https://os.mbed.com/docs/v5.7/mbed-os-api-doxy/class_wi_fi_interface.html). Your communication interface is a subclass of one of these, as well as the NetworkStack. For example, the [ESP8266Interface](https://github.com/ARMmbed/esp8266-driver) inheritance structure looks like this:

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/esp-class.png)<span>Class</span></span>

There are three [pure virtual methods](https://en.wikipedia.org/wiki/Virtual_function#Abstract_classes_and_pure_virtual_functions) in the NetworkInterface class.
- [`connect()`](https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/NetworkInterface.h#L99) - to connect the interface to the network.
- [`disconnect()`](https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/NetworkInterface.h#L105) - to disconnect the interface from the network.
- [`get_stack()`](https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/NetworkInterface.h#L144) - to return the underlying NetworkStack object.

Each subclass has distinct pure virtual methods. Visit their class references (linked above) to determine those you must implement.

##### NetworkStack class

`NetworkStack` provides a common interface that hardware shares. By implementing the NetworkStack, you can use a class as a target for instantiating network sockets.

`NetworkStack` provides [these functions](https://os.mbed.com/docs/v5.7/mbed-os-api-doxy/class_network_stack.html). Look for the function signature like [`declarator virt-specifier(optional) = 0`](http://en.cppreference.com/w/cpp/language/abstract_class) to determine which functions are pure virtual and which you must override in your child class.

#### Errors

Many functions of `NetworkStack` and `NetworkInterface` have return types of `nsapi_error_t`, which is a type used to represent error codes. You can see a list of these return codes [here](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.4/api/group__netsocket.html#gac21eb8156cf9af198349069cdc7afeba). You can view the integer values the error macros in [this file](https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/nsapi_types.h). A negative error code indicates failure, while 0 indicates success.

##### The `connect()` method

High-level API calls to an implementation of a network-socket API are **identical** across networking protocols. The only difference is the interface object constructor and the method through which you connect to the network. For example, a Wi-Fi connection requires an SSID and password, a cellular connection requires an APN and Ethernet doesn't require any credentials. Only the `connect` method syntax of the derived classes reflects these differences. The intended design allows the user to change out the connectivity of the app by adding a new library and changing the API call for connecting to the network.

Below is a demonstration with the code that sends an HTTP request over Ethernet:

```C++
    EthernetInterface net;
    int return_code = net.connect();
    if (return_code < 0)
        printf("Error connecting to network %d\r\n", return_code);

    // Open a socket on the network interface, and create a TCP connection to api.ipify.org
    TCPSocket socket;
    socket.open(&net);
    socket.connect("api.ipify.org", 80);
    char *buffer = new char[256];

    // Send an HTTP request
    strcpy(buffer, "GET / HTTP/1.1\r\nHost: api.ipify.org\r\n\r\n");
    int scount = socket.send(buffer, strlen(buffer));

    // Recieve an HTTP response and print out the response line
    int rcount = socket.recv(buffer, 256);

    // Close the socket to return its memory and bring down the network interface
    socket.close();
    delete[] buffer;

    // Bring down the ethernet interface
    net.disconnect();
```

To change the connectivity to ESP8266 Wi-Fi, change these lines:

```C++
    EthernetInterface net;
    int return_code = net.connect();
```

To:

```C++
    ESP8266Interface net(TX_PIN, RX_PIN);
    int return_code = net.connect("my_ssid", "my_password");
```

#### Testing

When adding a new connectivity class, you can use `mbed test` to verify your implementation.

1. Make a new Mbed OS project: `mbed new [directory_name]`, where directory name is the name you'd like to use as your testing directory.
1. Move into that folder: `cd [directory_name]`.
1. Add your library to the project: `mbed add [driver URL]` or copy the driver files to this directory.
1. You need to create a JSON test configuration file using the following format:

    ```JSON
    {
        "config": {
            "header-file": {
                "help" : "String for including your driver header file",
                "value" : "\"EthernetInterface.h\""
            },
            "object-construction" : {
                "value" : "new EthernetInterface()"
            },
            "connect-statement" : {
                "help" : "Must use 'net' variable name",
                "value" : "((EthernetInterface *)net)->connect()"
            },
            "echo-server-addr" : {
                "help" : "IP address of echo server",
                "value" : "\"195.34.89.241\""
            },
            "echo-server-port" : {
                "help" : "Port of echo server",
                "value" : "7"
            },
            "tcp-echo-prefix" : {
                "help" : "Some servers send a prefix before echoed message",
                "value" : "\"u-blox AG TCP/UDP test service\\n\""
            }
        }
    }
    ```

    The configuration values you need to replace are `header-file`, `object-construction` and `connect-statement`.

    - `header-file` - Replace `EthernetInterface.h` with the correct header file of your class
    - `object-construction` - Replace `EthernetInterface()` with the syntax for your class' object construction.
    - `connect-statement` - Replace `EthernetInterface*` with a pointer type to your class and `connect()` to match your class' connect function signature.

1. Save the content as a new JSON file.
1. Run the following command to execute the tests:
    `mbed test -m [MCU] -t [toolchain] -n mbed-os-tests-netsocket* --test-config path/to/config.json`
1. Use `-vv` for very verbose to view detailed test output.

#### Case Study: ESP8266 Wi-Fi component

This example ports a driver for the ESP8266 Wi-Fi module to the NSAPI.

##### Required methods

Because ESP8266 is a Wi-Fi component, choose [`WiFiInterface`](https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/WiFiInterface.h) as the `NetworkworkInterface` parent class.

`WiFiInterface` defines the following pure virtual functions:

- `set_credentials(const char *ssid, const char *pass, nsapi_security_t security)`.
- `set_channel(uint8_t channel)`.
- `get_rssi()`.
- `connect(const char *ssid, const char *pass, nsapi_security_t security, uint8_t channel)`.
- `connect()`.
- `disconnect()`.
- `scan(WiFiAccessPoint *res, nsapi_size_t count)`.

Additionally, `WiFiInterface` parent class `NetworkInterface` introduces `NetworkStack *get_stack()` as a pure virtual function.

You must also use [`NetworkStack`](https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/NetworkStack.h) as a parent class of the interface. You've already explored the pure virtual methods [here](#NetworkStack-class).

##### Implementing `connect()`

Because a Wi-Fi connection requires an SSID and password, you need to implement a connect function that doesn't have these as a parameter.

One of the `WiFiInterface` pure virtual functions is `set_credentials(const char *ssid, const char *pass, nsapi_security_t security)`. Implement `set_credentials` to store the SSID and password in private class variables. When you call `connect()` with no SSID and password, it is assumed that `set_credentials` has been called.

The next step is to implement this with the `connect()` method.

This is the first method that needs to interact with the Wi-Fi chip. You need to do some configuration to get the chip in a state where you can open sockets. You need to send some [AT commands](https://www.espressif.com/sites/default/files/documentation/4a-esp8266_at_instruction_set_en.pdf) to the chip to accomplish this.

The AT commands you want to send are:

1. `AT+CWMODE=3` - This sets the Wi-Fi mode of the chip to 'station mode' and 'SoftAP mode', where it acts as a client connection to a Wi-Fi network, as well as a Wi-Fi access point.
2. `AT+CIPMUX=1` - This allows the chip to have multiple socket connections open at once.
3. `AT+CWDHCP=1,1` - To enable DHCP.
4. `AT+CWJAP=[ssid,password]` - To connect to the network.
5. `AT+CIFSR` - To query your IP address and ensure that the network assigned you one through DHCP.

###### Sending AT Commands

You can use the [AT command parser](https://github.com/ARMmbed/ATParser) to send AT commands and parse their responses. The AT command parser operates with a `BufferedSerial` object that provides software buffers and interrupt driven TX and RX for Serial.

`ESP8266Interface` uses an underlying interface called [`ESP8266`](https://github.com/ARMmbed/esp8266-driver/tree/master/ESP8266) to handle the communication with the Wi-Fi modem. `ESP8266` maintains an instance of AT command parser to handle communcation with the module. An instance of `ESP8266` is in a private `ESP8266Interface` class variable `_esp`. In turn, `ESP8266` maintains an instance of AT command parser called `_parser`.

To send AT commands 1-2, there is an `ESP8266` method called [`startup(int mode)`](https://github.com/ARMmbed/esp8266-driver/blob/master/ESP8266/ESP8266.cpp#L27). Use the AT command parser's [`send`](https://github.com/ARMmbed/ATParser/blob/master/ATParser.h#L132) and [`recv`](https://github.com/ARMmbed/ATParser/blob/master/ATParser.h#L149) functions to accomplish this.

The necessary code is:

```C++

bool ESP8266::startup(int mode)
{
    ...

    bool success =
        && _parser.send("AT+CWMODE=%d", mode)
        && _parser.recv("OK")
        && _parser.send("AT+CIPMUX=1")
        && _parser.recv("OK");

    ...

```

The parser's `send` function returns true if the command succesully sent to the Wi-Fi chip. The `recv` function returns true if you receive the specified text. In the code example above, sending two commands and receiving the expected `OK` responses determines success.

###### Return values

So far, our connect method looks something like:

```C++
int ESP8266Interface::connect()
{
    if (!_esp.startup(3)) {
        return X;

```

If this `!_esp.startup(3)` evaluates to true, something went wrong when configuring the chip, and you should return an error code.

The NSAPI provides a set of error code return values for network operations. They documentation is [here](https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/nsapi_types.h#L37-L54).

Of them, the most appropriate is `NSAPI_ERROR_DEVICE_ERROR`. So replace `X` in the `return` statement with `NSAPI_ERROR_DEVICE_ERROR`.

###### Finishing

You implemented similar methods to `startup` in ESP8266 to send AT commands 3-5. Then, you used them to determine the success of the `connect()` method. You can find the completed implementation [here](https://github.com/ARMmbed/esp8266-driver/blob/master/ESP8266Interface.cpp#L47-L68).  

##### Implementing `socket_open`

The `NetworkStack` parent class dictates that you implement the functionality of opening a socket. This is the method signature in the interface:

```C++
int ESP8266Interface::socket_open(void **handle, nsapi_protocol_t proto)
```

This method doesn't necessitate any AT commands. The purpose is to create a socket in software and store the information in the `handle` parameter for use in other socket operations.

The ESP8266 module can only handle 5 open sockets, so you want to ensure that you don't open a socket when none are available. In the header file, use this macro for convenience: `#define ESP8266_SOCKET_COUNT 5`. Use a private class variable array to keep track of open sockets `bool _ids[ESP8266_SOCKET_COUNT]`. In `socket_open`, first iterate over `_ids`, and look for an element in the array whose value is `false`.

So far, the method looks like this:

```C++
int ESP8266Interface::socket_open(void **handle, nsapi_protocol_t proto)
{
    // Look for an unused socket
    int id = -1;

    for (int i = 0; i < ESP8266_SOCKET_COUNT; i++) {
        if (!_ids[i]) {
            id = i;
            _ids[i] = true;
            break;
        }
    }

    if (id == -1) {
        return NSAPI_ERROR_NO_SOCKET;
    }

    ...
```

After you've determined that you have an open socket, you want to store some information in the `handle` parameter. We've created a `struct` to store information about the socket that will be necessary for network operations:

```C++
struct esp8266_socket {
    int id; // Socket ID number
    nsapi_protocol_t proto; // TCP or UDP
    bool connected; // Is it connected to a server?
    SocketAddress addr; // The address that it is connected to
};
```

Create one of these, store some information in it and then point the `handle` at it:

```C++
int ESP8266Interface::socket_open(void **handle, nsapi_protocol_t proto)
{
    ...
    struct esp8266_socket *socket = new struct esp8266_socket;
    if (!socket) {
        return NSAPI_ERROR_NO_SOCKET;
    }

    socket->id = id; // store the open ID we found above
    socket->proto = proto; // TCP or UDP as specified in parameter
    socket->connected = false; // default state not connected

    *handle = socket;
    return 0; // success
```

See the full implementation [here](https://github.com/ARMmbed/esp8266-driver/blob/master/ESP8266Interface.cpp#L137-L164).

##### Implementing `socket_connect`

The `NetworkStack` parent class dictates that you implement the functionality of connecting a socket to a remote server. This is the method signature in the interface:

```C++
int ESP8266Interface::socket_connect(void *handle, const SocketAddress &addr)
```

In this case, the handle is one that has been assigned in the [`socket_open`](https://github.com/ARMmbed/esp8266-driver/blob/master/ESP8266Interface.cpp#L137-L164) method.

You can cast the void pointer to an `esp8266_socket` pointer. Do this in the body of `socket_connect`:

```C++
int ESP8266Interface::socket_connect(void *handle, const SocketAddress &addr)
{
    struct esp8266_socket *socket = (struct esp8266_socket *)handle;
    _esp.setTimeout(ESP8266_MISC_TIMEOUT);

    const char *proto = (socket->proto == NSAPI_UDP) ? "UDP" : "TCP";
    if (!_esp.open(proto, socket->id, addr.get_ip_address(), addr.get_port())) {
        return NSAPI_ERROR_DEVICE_ERROR;
    }

    socket->connected = true;
    return 0;
}
```

Focus on this line:
`!_esp.open(proto, socket->id, addr.get_ip_address(), addr.get_port()`.

Access the socket ID and socket protocol from the members of `esp8266_socket`. Access the IP address and port of the server with the `SocketAddress addr` parameter.

This method sends the AT command for opening a socket to the Wi-Fi module and is defined as follows:

```C++
bool ESP8266::open(const char *type, int id, const char* addr, int port)
{
    //IDs only 0-4
    if(id > 4) {
        return false;
    }

    return _parser.send("AT+CIPSTART=%d,\"%s\",\"%s\",%d", id, type, addr, port)
        && _parser.recv("OK");
}
```

In this instance, use the AT command parser to send `AT+CIPSTART=[id],[TCP or UDP], [address]` to the module. Expect to receive a response of `OK`. Only return true if you succesfully send the command AND receive an `OK` response.

##### Implementing `socket_attach`

The `NetworkStack` parent class dictates that you implement the functionality of registering a callback on state change of the socket. This is the method signature in the interface:

```C++
void ESP8266Interface::socket_attach(void *handle, void (*callback)(void *), void *data)
```

Call the specified callback on state changes, such as when the socket can recv/send/accept successfully.

ESP8266 can have up to five open sockets. You need to keep track of all their callbacks. This [struct](https://github.com/ARMmbed/esp8266-driver/blob/master/ESP8266Interface.h#L269-L272) holds the callback as well as the data of these callbacks. It is stored as a private class variable `_cbs`:

```C++
struct {
    void (*callback)(void *);
    void *data;
} _cbs[ESP8266_SOCKET_COUNT];
```

The attach method is:

```C++
void ESP8266Interface::socket_attach(void *handle, void (*callback)(void *), void *data)
{
    struct esp8266_socket *socket = (struct esp8266_socket *)handle;    
    _cbs[socket->id].callback = callback;
    _cbs[socket->id].data = data;
}
```

Store the information in the `_cbs` struct for use on state changes. There is a method `event()` to call socket callbacks. It looks like this:

```C++
void ESP8266Interface::event() {
    for (int i = 0; i < ESP8266_SOCKET_COUNT; i++) {
        if (_cbs[i].callback) {
            _cbs[i].callback(_cbs[i].data);
        }
    }
}
```

Look for sockets that have callbacks. Then, call them with the specified data!

Know when to trigger these events. You've used the `ESP8266` class object, `_esp`, to attach a callback on a Serial RX event like so: `_esp.attach(this, &ESP8266Interface::event)`. The `_esp` attach function creates ` _serial.attach(func)`, which attaches the function to the underlying `UARTSerial` RX event. Whenever the radio receives something, consider that a state change, and invoke any attach callbacks. A common use case is to attach `socket_recv` to a socket, so the socket can receive data asynchronously without blocking.

#### Testing

- Make a new Mbed project - `mbed new esp8266-driver-test`.
- Move into project folder - `cd esp8266-driver-test`.
- Add ESP8266 driver - `mbed add esp8266-driver`.
- Make a configuration file called `esp8266_config.json` with the following contents:

```
{
    "config": {
        "header-file": {
            "help" : "String for including your driver header file",
            "value" : "\"ESP8266Interface.h\""
        },
        "object-construction" : {
            "value" : "new ESP8266Interface(D1, D0)"
        },
        "connect-statement" : {
            "help" : "Must use 'net' variable name",
            "value" : "((ESP8266Interface *)net)->connect(\"my_ssid\", \"my_password\")"
        },
        "echo-server-addr" : {
            "help" : "IP address of echo server",
            "value" : "\"195.34.89.241\""
        },
        "echo-server-port" : {
            "help" : "Port of echo server",
            "value" : "7"
        },
        "tcp-echo-prefix" : {
            "help" : "Some servers send a prefix before echoed message",
            "value" : "\"u-blox AG TCP/UDP test service\\n\""
        }
    }
}
```

- Run tests - `mbed test -m [mcu] -t [toolchain] -n mbed-os-tests-netsocket* --test-config esp8266_config.json`.
- View test results:

```shell
mbedgt: test suite report:
+--------------+---------------+--------------------------------------------+--------+--------------------+-------------+
| target       | platform_name | test suite                                 | result | elapsed_time (sec) | copy_method |
+--------------+---------------+--------------------------------------------+--------+--------------------+-------------+
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-connectivity       | OK     | 32.24              | shell       |
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-gethostbyname      | OK     | 24.01              | shell       |
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-ip_parsing         | OK     | 14.31              | shell       |
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-socket_sigio       | OK     | 29.23              | shell       |
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-tcp_echo           | OK     | 51.39              | shell       |
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-tcp_hello_world    | OK     | 21.03              | shell       |
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-udp_dtls_handshake | OK     | 19.65              | shell       |
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-udp_echo           | OK     | 23.22              | shell       |
+--------------+---------------+--------------------------------------------+--------+--------------------+-------------+
mbedgt: test suite results: 8 OK
mbedgt: test case report:
+--------------+---------------+--------------------------------------------+----------------------------------------+--------+--------+--------+--------------------+
| target       | platform_name | test suite                                 | test case                              | passed | failed | result | elapsed_time (sec) |
+--------------+---------------+--------------------------------------------+----------------------------------------+--------+--------+--------+--------------------+
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-connectivity       | Bringing the network up and down       | 1      | 0      | OK     | 7.61               |
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-connectivity       | Bringing the network up and down twice | 1      | 0      | OK     | 10.74              |
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-gethostbyname      | DNS literal                            | 1      | 0      | OK     | 0.09               |
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-gethostbyname      | DNS preference literal                 | 1      | 0      | OK     | 0.1                |
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-gethostbyname      | DNS preference query                   | 1      | 0      | OK     | 0.13               |
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-gethostbyname      | DNS query                              | 1      | 0      | OK     | 0.15               |
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-ip_parsing         | Hollowed IPv6 address                  | 1      | 0      | OK     | 0.06               |
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-ip_parsing         | Left-weighted IPv4 address             | 1      | 0      | OK     | 0.07               |
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-ip_parsing         | Left-weighted IPv6 address             | 1      | 0      | OK     | 0.06               |
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-ip_parsing         | Null IPv4 address                      | 1      | 0      | OK     | 0.04               |
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-ip_parsing         | Null IPv6 address                      | 1      | 0      | OK     | 0.05               |
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-ip_parsing         | Right-weighted IPv4 address            | 1      | 0      | OK     | 0.06               |
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-ip_parsing         | Right-weighted IPv6 address            | 1      | 0      | OK     | 0.06               |
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-ip_parsing         | Simple IPv4 address                    | 1      | 0      | OK     | 0.05               |
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-ip_parsing         | Simple IPv6 address                    | 1      | 0      | OK     | 0.04               |
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-socket_sigio       | Socket Attach Test                     | 1      | 0      | OK     | 2.04               |
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-socket_sigio       | Socket Detach Test                     | 1      | 0      | OK     | 6.26               |
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-socket_sigio       | Socket Reattach Test                   | 1      | 0      | OK     | 1.36               |
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-tcp_echo           | TCP echo                               | 1      | 0      | OK     | 6.24               |
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-tcp_hello_world    | TCP hello world                        | 1      | 0      | OK     | 7.34               |
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-udp_dtls_handshake | UDP DTLS handshake                     | 1      | 0      | OK     | 5.9                |
| K64F-GCC_ARM | K64F          | mbed-os-tests-netsocket-udp_echo           | UDP echo                               | 1      | 0      | OK     | 9.75               |
+--------------+---------------+--------------------------------------------+----------------------------------------+--------+--------+--------+--------------------+
mbedgt: test case results: 22 OK
mbedgt: completed in 217.24 sec
```
