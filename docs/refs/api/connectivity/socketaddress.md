#### SocketAddress

Use the [SocketAddress](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.6/api/classSocketAddress.html) class to represent the IP address and port pair of a unique network endpoint. Most network functions are also overloaded to accept string representations of IP addresses, but SocketAddress can be used to avoid the overhead of parsing IP addresses during repeated network transactions, and can be passed around as a first class object.
