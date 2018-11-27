## SocketStats

Use the SocketStats class to read the network socket statistics. SocketStats Class object is created by "InternetSocket" class when statistics are enabled by `nsapi.socket-stats-enable` config option.

The `SocketStats` class provides the static function `mbed_stats_socket_get_each` to get the network socket information for all sockets both currently in use and closed. Using this function you can know how many sockets are open, destination IP addresses, the amount of data sent and received in bytes, the type of socket and the timestamp of recent "socket state" changes recorded in `last_change_tick`.

Socket Statistics are stored in intenal data buffer and maintained for closed sockets as well. In case internal data buffer is full, socket closed with oldest timestamp will be over-written. Maximum amount of sockets statistics stored can be configured by `nsapi.socket-stats-max-count` config option.

### SocketStats class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_socket_stats.html)

### SocketStats example

Here is an example to collect socket statistics.

[![View Example](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/tree/master/SocketStats)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/SocketStats/main.cpp)

### Related content

- [IP networking architecture](/docs/development/reference/ip-networking.html).
