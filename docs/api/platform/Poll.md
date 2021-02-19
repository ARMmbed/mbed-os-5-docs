# Poll

The `poll` functions perform timed waits on one or more [file handles](filehandle.html).

Mbed OS provides `poll()` in two forms:

- `int poll(struct pollfd fds[], nfds_t nfds, int timeout)` the standard POSIX form taking an array of integer file descriptors.
- `int mbed::poll(pollfh fhs[], unsigned nfhs, int timeout)`, the variant taking an array of `FileHandle *`.

See the POSIX specification of `poll` for full details of the API. Mbed OS provides the `POLLIN`, `POLLOUT`, `POLLERR` and `POLLHUP` event flags, but implementation depends on the device.

Note that the `poll` is not affected by the blocking or nonblocking setting of the individual file handles. The `timeout` argument always determines the wait behavior: 0 for immediate (nonblocking) return, -1 for wait forever or positive for a limited wait.

As per the POSIX specification, `poll` always indicates that ordinary files (as opposed to devices) are readable and writable.

## Poll reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/group__platform__poll.html)

## Poll example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Poll/tree/v6.8)](https://github.com/ARMmbed/mbed-os-snippet-Poll/blob/v6.8/main.cpp)

## Related content

- [FileHandle](filehandle.html).
