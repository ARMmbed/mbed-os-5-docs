### Creating a compatible communication API

The Network-Socket-API (NSAPI) provides a TCP/UDP API on top of any IP based network interface. The NSAPI makes it easy to write applications and libraries that use TCP/UDP Sockets without regard to the type of IP connectivity. In addition to providing the TCP/UDP API, the NSAPI also includes virtual base classes for the different IP interface types.

#### Class hierarchy 

All network-socket API implementations inherit from two classes: a [NetworkStack](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.2/api/classNetworkStack.html) and a communication specific subclass of [NetworkInterface](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.4/api/classNetworkInterface.html). 

##### NetworkInterface Class

The current NetworkInterface subclasses are [CellularInterface](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.4/api/classCellularInterface.html), [EthernetInterface](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.4/api/classEthernetInterface.html), [MeshInterface](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.4/api/classMeshInterface.html), and [WiFiInterface](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.4/api/classWiFiInterface.html). Your communication interface is a subclass of one of these, as well as the NetworkStack. For example, the [ESP8266Interface](https://github.com/ARMmbed/esp8266-driver) inheritance structure looks like this: 

![Class](/img/esp-class.png)

There are three [pure virtual methods](https://en.wikipedia.org/wiki/Virtual_function#Abstract_classes_and_pure_virtual_functions) in the NetworkInterface class. 
* [`connect()`](https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/NetworkInterface.h#L99) - to connect the interface to the network.
* [`disconnect()`](https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/NetworkInterface.h#L105) - to disconnect the interface from the network.
* [`get_stack()`](https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/NetworkInterface.h#L144) - to return the underlying NetworkStack object.

Each subclass has distinct pure virtual methods. Visit their class references (linked above) to determine those that must be implemented.

##### NetworkStack class

`NetworkStack` provides a common interface that is shared between hardware that can connect to a network over IP. By implementing the NetworkStack, you can use a class as a target for instantiating network sockets.

NetworkStack requires that you implement the following functionalities:
* [Getting an IP address from the network](https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/NetworkStack.h#L45).
* [Opening a socket](https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/NetworkStack.h#L120).
* [Closing a socket](https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/NetworkStack.h#L130).
* [Accepting connections on a socket](https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/NetworkStack.h#L184).
* [Attaching a callback to a state change of a socket](https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/NetworkStack.h#L270).
* [Binding an address to a socket](https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/NetworkStack.h#L141).
* [Connecting a socket to a remote host](https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/NetworkStack.h#L164).
* [Listening for incoming connections](https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/NetworkStack.h#L153).
* [Receving data on a socket](https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/NetworkStack.h#L218).
* [Sending data on a socket](https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/NetworkStack.h#L201).

##### The `connect()` method

High level API calls to an implementation of a network-socket API are intended to be the **identical** across networking protocols. The only intended difference is the method used to connect to the network. For example, a Wi-Fi connection requires an SSID and password, a cellular connection requires an APN and Ethernet doesn't require any credentials. These differences are reflected only in the `connect` method syntax of the derived classes. The intended design allows the user to change out the connectivity of the app by adding a new library and changing the API call for connecting to the network. 

Let's demonstrate with the code used to send an HTTP request over ethernet: 

```C++
    EthernetInterface net;
    net.connect();

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
    net.connect();
```

To:

```C++
    ESP8266Interface net;
    net.connect("my_ssid", "my_password");
```

#### Case Study: ESP8266 Wi-Fi component

This example ports a driver for the ESP8266 Wi-Fi module to the NSAPI.

##### Required methods

Because ESP8266 is a Wi-Fi component, [`WiFiInterface`](https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/WiFiInterface.h) is the `NetworkworkInterface` parent class.

`WiFiInterface` defines the following pure virtual functions: 
1. `set_credentials(const char *ssid, const char *pass, nsapi_security_t security)`
2. `set_channel(uint8_t channel)`
3. `get_rssi()`
4. `connect(const char *ssid, const char *pass, nsapi_security_t security, uint8_t channel)`
5. `connect()`
6. `disconnect()`
7. `scan(WiFiAccessPoint *res, nsapi_size_t count)`

Additionally, `WiFiInterface` parent class `NetworkInterface` introduces `NetworkStack *get_stack()` as a pure virtual function. 

You must also use [`NetworkStack`](https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/NetworkStack.h) as a parent class of the interface. You've already explored the pure virtual methods [here](#NetworkStack-class).

##### Implementing `connect()`

We explained earlier that a Wi-Fi connection requires an SSID and password. So how can we implement a connect function that doesn't have these as a parameter?

You might have noticed that one of the `WiFiInterface` pure virtual functions is `set_credentials(const char *ssid, const char *pass, nsapi_security_t security)`. So, we implemented `set_credentials` to store the SSID and password in private class variables. So, when we call `connect()` with no SSID and password, it is assumed that `set_credentials` has been called. 

Let's think about how we might implement this of the `connect()` method. 

This is the first method that will need to interact with the Wi-Fi chip. We will need to do some configuration to get the chip in a state where we can open sockets, etc. We will need to send some [AT commands](https://www.espressif.com/sites/default/files/documentation/4a-esp8266_at_instruction_set_en.pdf) to the chip to accomplish this.

The AT commands we want to send are:

1. `AT+CWMODE=3` - This sets the Wi-Fi mode of the chip to 'station mode' and 'SoftAP mode', where it acts as a client connection to a Wi-Fi network, as well as a Wi-Fi access point.
2. `AT+CIPMUX=1` - This allows the chip to have multiple socket connections open at once
3. `AT+CWDHCP=1,1` - To enable DHCP
4. `AT+CWJAP=[ssid,password]` - To connect to the network
5. `AT+CIFSR` - To query our IP address, and ensure that the network assigned us one through DHCP

###### Sending AT Commands 

We've created an [AT command parser](https://github.com/ARMmbed/ATParser) to easily send AT commands and parse their responses. The AT command parser operates with a `BufferedSerial` object that provides software buffers and interrupt driven TX and RX for Serial.

`ESP8266Interface` utilizes an underlying interface called [`ESP8266`](https://github.com/ARMmbed/esp8266-driver/tree/master/ESP8266) to handle the communication with the Wi-Fi modem. `ESP8266` maintains an instance of AT command parser to handle communcation with the module. We have stored an instance of `ESP8266` in a private `ESP8266Interface` class variable `_esp`. In turn, `ESP8266` maintains an instance of AT command parser called `_parser`.

To send AT commands 1-2, we've made an `ESP8266` method called [`startup(int mode)`](https://github.com/ARMmbed/esp8266-driver/blob/master/ESP8266/ESP8266.cpp#L27). We will use the AT command parser's [`send`](https://github.com/ARMmbed/ATParser/blob/master/ATParser.h#L132) and [`recv`](https://github.com/ARMmbed/ATParser/blob/master/ATParser.h#L149) functions to accomplish this.

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

The parser's `send` function returns true if the command was succesully sent to the Wi-Fi chip. The `recv` function returns true if we receive the specified text. In the code example above, our success is determined by sending two commands and receiving the expected `OK` responses. 

###### Return values

So far, our connect method looks something like:

```C++
int ESP8266Interface::connect()
{
    if (!_esp.startup(3)) {
        return X;

```

What should we do if this `!_esp.startup(3)` evaluates to true? If it does, something went wrong when configuring the chip. So, we should return an error code. 

The NSAPI provides a set of error code return values for network operations. They are documented [here](https://github.com/ARMmbed/mbed-os/blob/master/features/netsocket/nsapi_types.h#L37-L54).

Looking through them, the most appropriate seems to be ` NSAPI_ERROR_DEVICE_ERROR  = -3012,     /*!< failure interfacing with the network processor */`. So let's replace `X` in our `return` statement with `NSAPI_ERROR_DEVICE_ERROR`.

###### Finishing up 

We implemented similar methods to `startup` in ESP8266 to send AT commands 3-5. Then we used them to determine the success of the `connect()` method. The completed implementation can be found [here](https://github.com/ARMmbed/esp8266-driver/blob/master/ESP8266Interface.cpp#L47-L68).  

##### Implementing `socket_open`

The `NetworkStack` parent class dictates that we implement the functionality of opening a socket. This is the method signature in our interface:

```C++
int ESP8266Interface::socket_open(void **handle, nsapi_protocol_t proto)
```

This is an interesting method, as it doesn't necessitate any AT commands. The purpose is to create a socket in software and store the information in the `handle` parameter for use in other socket operations.

The ESP8266 module can only handle 5 open sockets, so we want to ensure that we don't open a socket when there are none available. In our header file, we use this macro for convenience: `#define ESP8266_SOCKET_COUNT 5`. We are going to use a private class variable array to keep track of open sockets `bool _ids[ESP8266_SOCKET_COUNT]`. Our first order of business in `socket_open` is to iterate over `_ids` and look for an element in the array whose value is `false`.

So far, our method looks like this:
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

After we've determined that we have an open socket, we want to store some information in the `handle` parameter. We've created a `struct` to store information about the socket that will be necessary for network operations. This is it:
```C++
struct esp8266_socket {
    int id; // Socket ID number 
    nsapi_protocol_t proto; // TCP or UDP
    bool connected; // Is it connected to a server?
    SocketAddress addr; // The address that it is connected to
};
```

So, let's create one of these, store some information in it, then point the `handle` at it:

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

The `NetworkStack` parent class dictates that we implement the functionality of connecting a socket to a remote server. This is the method signature in our interface:

```C++
int ESP8266Interface::socket_connect(void *handle, const SocketAddress &addr)
```

In this case, the handle will be one that has been assigned in the [`socket_open`](https://github.com/ARMmbed/esp8266-driver/blob/master/ESP8266Interface.cpp#L137-L164) method. 

We can cast the void pointer to an `esp8266_socket` pointer.  We do this in the body of `socket_connect`: 

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

Focusing on this line: 
`!_esp.open(proto, socket->id, addr.get_ip_address(), addr.get_port()`. 

We access the socket ID and socket protocol from the members of `esp8266_socket`. We access the IP address and port of the server with the `SocketAddress addr` parameter. 

This method will send the AT command for opening a socket to the Wi-Fi module and is defined as follows:

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

In this instance, we use the AT command parser to send `AT+CIPSTART=[id],[TCP or UDP], [address]` to the module. We expect to receive a response of `OK`. We only return true if we succesfully send the command AND receive an `OK` response. 

##### Implementing `socket_attach`

The `NetworkStack` parent class dictates that you implement the functionality of registering a callback on state change of the socket. This is the method signature in the interface:

```C++
void ESP8266Interface::socket_attach(void *handle, void (*callback)(void *), void *data)
```

The specified callback is called on state changes, like when the socket can recv/send/accept successfully.

ESP8266 can have up to five open sockets. You need to keep track of all their callbacks. This [struct](https://github.com/ARMmbed/esp8266-driver/blob/master/ESP8266Interface.h#L269-L272) holds the callback as well as the data of these callbacks. It is stored as a private class variable `_cbs`:

```C++
struct {
    void (*callback)(void *);
    void *data;
} _cbs[ESP8266_SOCKET_COUNT];
```

The attach method is simple: 

```C++
void ESP8266Interface::socket_attach(void *handle, void (*callback)(void *), void *data)
{
    struct esp8266_socket *socket = (struct esp8266_socket *)handle;    
    _cbs[socket->id].callback = callback;
    _cbs[socket->id].data = data;
}
```

So, we store the information in our `_cbs` struct for use on state changes. This is the tricky part. When should these callbacks be called? We've defined a method: `event()` to call our socket callbacks. It looks like this: 

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

However, when should these events be triggered? We've used the `ESP8266` class object, `_esp` to attach a callback on a Serial RX event like so: `_esp.attach(this, &ESP8266Interface::event)`. Stepping into `_esp`'s attach function, we have: ` _serial.attach(func)`. Which attaches the a function to the underlying `BufferedSerial` RX event. So, whenever the radio receives something, we consider that a state change, and invoke any attach callbacks. A common use case is to attach `socket_recv` to a socket, so that the socket can receive data asynchronously without blocking.
