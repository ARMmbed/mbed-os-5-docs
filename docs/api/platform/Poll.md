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

```
// Transfer bidirectional data between two ports, acting as a virtual link.
// poll() is used to monitor both ports for input.
#include "mbed.h"

// Pins for each port are specified using mbed_app.json. Assume no flow control.
// (If there were flow control, being blocked by it could break the implementation,
// as you would stop reading input in the opposite direction).
UARTSerial device1(MBED_CONF_APP_UART1_TX, MBED_CONF_APP_UART1_RX);
UARTSerial device2(MBED_CONF_APP_UART2_TX, MBED_CONF_APP_UART2_RX);

// Precondition: "in" is readable
static void copy_some(FileHandle *out, FileHandle *in)
{
    // To ensure performance, try to read multiple bytes at once,
    // but don't expect to read many in practice.
    char buffer[32];

    // Despite the FileHandle being in its default blocking mode,
    // read() must return immediately with between 1-32 bytes, as
    // you've already checked that `in` is ready with poll()
    ssize_t read = in->read(buffer, sizeof buffer);
    if (read <= 0) {
        error("Input error");
    }

    // Write everything out. Assuming output port is same speed as input,
    // and no flow control, this may block briefly but not significantly.
    ssize_t written = out->write(buffer, read);
    if (written < read) {
        error("Output error");
    }
}

int main()
{
    char buffer[32];
    pollfh fds[2];

    fds[0].fh = &device1;
    fds[0].events = POLLIN;
    fds[1].fh = &device2;
    fds[1].events = POLLIN;

    while (1) {
        // Block indefinitely until either of the 2 ports is readable (or has an error)
        poll(fds, 2, -1);

        // Transfer some data in either or both directions
        if (fds[0].revents) {
            copy_some(fds[1].fh, fds[0].fh);
        }
        if (fds[1].revents) {
            copy_some(fds[0].fh, fds[1].fh);
        }
    }
}
```

## Related content

- [FileHandle](filehandle.html).
