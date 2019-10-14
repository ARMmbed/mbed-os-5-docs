# SocketStats

Use the SocketStats class to read the network socket statistics. When statistics are enabled, you can create the SocketStats class object with the `InternetSocket` class by using the `nsapi.socket-stats-enabled` configuration option.

The `SocketStats` class provides the static function `mbed_stats_socket_get_each` to get the network socket information for all sockets both currently in use and closed. Using this function, you can know how many sockets are open, destination IP addresses, the amount of data sent and received in bytes, the type of socket and the timestamp of recent "socket state" changes recorded in `last_change_tick`.

Socket statistics are stored in an internal data buffer and maintained for closed sockets, as well. If the internal data buffer is full, the socket closed with the oldest timestamp will be overwritten. You can configure the maximum amount of sockets statistics stored by using the `nsapi.socket-stats-max-count` configuration option.

## SocketStats class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/class_socket_stats.html)

## SocketStats example

Here is an example to collect socket statistics.

[![View Example](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-socket-stats)](https://github.com/ARMmbed/mbed-os-example-socket-stats/blob/mbed-os-5.14/main.cpp)

## Related content

- [IP networking architecture](../reference/ip-networking.html).
