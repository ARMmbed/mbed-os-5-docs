# FileHandle

<span class="images">![](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/classmbed_1_1_file_handle.png)<span>FileHandle class hierarchy</span></span>

For general information on [files](file.html) and [filing systems](filesystem.html) in persistent storage, see their documentation. This chapter covers the abstract API, with an emphasis on devices.

`FileHandle` is an abstract class representing a device that supports file-like operations, such as `read` and `write`. This may be an actual `File` on a storage device provided by a `FileSystem` or a device such as `UARTSerial`.

The `FileHandle` abstraction represents an already-opened file or device, so it has no `open` method of its own - the opening may take the form of a call to another class that returns a `FileHandle`, such as `FileSystem::open`, or it may be implicit in the construction of an object such as `UARTSerial`.

The `FileHandle` abstraction permits stream-handling code to be device-independent, rather than tied to a specific device like a serial port. Examples of such code in Mbed OS are:

- The console input and output streams (`stdin` and `stdout`).
- The `ATCmdParser` helper.
- The PPP connection to lwIP.

Exactly which operations a `FileHandle` supports depends on the underlying device, and in turn restricts what applications it is suitable for. For example, a database application might require random-access and `seek`, but this may not be available on a limited file system, and certainly not on a stream device. Only a `File` on a full `FileSystem`, such as `FATFileSystem`, would generally implement the entire API. Specialized devices may have particular limitations or behavior, which limit their general utility. Devices that do not implement a particular call indicate it by an error return - often `ENOSYS`, but sometimes more specific errors, such as `ESPIPE` apply; please see the POSIX specifications for details.

## Relationship of FileHandle to other APIs

You can use a `FileHandle` directly, or you can use standard POSIX or C/C++ APIs to manipulate it. Stdio calls taking `FILE *stream` call the POSIX APIs taking `int fd`, which call methods on `FileHandle` objects.

![FileHandle callstack](../../images/filehandle_callstack2.jpg)

The `FileHandle` may be implicitly created by a higher layer, as in a call to `fopen`. In this case, the name lookup produces a `FileHandle` and POSIX file descriptor internally.

The three APIs provide different levels of capability:

API                            | C/C++                   | POSIX                  | Mbed
-------------------------------|-------------------------|------------------------|-----------------------------
Headers                        | stdio.h, iostream       | mbed_retarget.h        | FileHandle.h, mbed_poll.h
Main type                      | FILE *                  | int                    | FileHandle object
Blocking I/O                   | Yes (always)            | Yes (default)          | Yes (default)
Nonblocking I/O                | No                      | Yes                    | Yes
Poll                           | No                      | Yes (struct pollfd)    | Yes (struct pollfh)
Sigio                          | No                      | No                     | Yes
Disable input or output        | No                      | No                     | Yes
Device-specific extensions     | No                      | No                     | Possible using derived types
Newline conversion             | Yes (enabled with JSON) | No                     | No
Error indications              | EOF, ferror, set errno  | Return -1, set errno   | Return negative error code
Portability                    | High                    | Medium                 | Low

You can mix the APIs if you're careful, for example setting up a callback initially with `FileHandle::sigio` but performing all subsequent operations using POSIX.

<span class="notes">**Note:** `errno` is not thread-local on all toolchains. This may cause problems with error handling if multiple threads are using POSIX or C file APIs simultaneously.</span>

## Mapping between APIs

Calls are provided to attach already-opened lower levels to the higher levels:

- `int mbed_bind_to_fd(FileHandle *)` bind a FileHandle to a POSIX file descriptor.
- `FILE *fdopen(int fd, const char *mode)` bind a POSIX file descriptor to a stdio FILE.
- `FILE *fdopen(FileHandle *fh, const char *mode)` bind a FileHandle to a stdio FILE.

The only call provided to map from higher level to lower-level is:

- `FileHandle *mbed_file_handle(int fd)` obtain the FileHandle for a POSIX file descriptor

The standard POSIX function `int fileno(FILE *stream)` may be available to map from `FILE` to file descriptor, depending on the toolchain and C library in use - it is not usable in fully portable Mbed OS code.

It is not possible to map from `FILE` to lower levels. If code needs to access the lower levels, rather than use `fopen`, use a lower-level open call. Then, use `fdopen` to create the `FILE`.

The POSIX file descriptors for the console are available as `STDIN_FILENO`, `STDOUT_FILENO` and `STDERR_FILENO`, permitting operations such as `fsync(STDERR_FILENO)`, which would for example drain `UARTSerial`s output buffer.

## Redirecting the console

If a target has serial support, by default a serial port is used for the console. The pins and settings for the port selection come from target header files and JSON settings. This uses either an internal `DirectSerial` if unbuffered (for backwards compatibility) or `UARTSerial` if `platform.stdio-buffered-serial` is `true`.

The target can override this by providing `mbed::mbed_target_override_console` to specify an alternative `FileHandle`. For example, a target using SWO might have:

```
namespace mbed
{
    FileHandle *mbed_target_override_console(int)
    {
        // SerialWireOutput
        static SerialWireOutput swo;
        return &swo;
    }
}
```

Then any program using `printf` on that target sends its output over the SWO, rather than serial.

Because targets can redirect the console in this way, portable applications should not use constructs such as `Serial(CONSOLE_TX, CONSOLE_RX)`, assuming that this will access the console. Instead they should use `stdin`/`stdout`/`stderr` or `STDIN_FILENO`/`STDOUT_FILENO`/`STDERR_FILENO`.

```
    // Don't do:
    Serial serial(CONSOLE_TX, CONSOLE_RX);
    serial.printf("Hello!\r\n");

    // Do do:
    printf("Hello!\n");  // assume platform.stdio-convert-newlines is true
```

Beyond the target-specific override, an application can override the target's default behavior itself by providing `mbed::mbed_override_console`. Below are two examples that show how you can redirect the console to a debugger using semihosting or another application-specific serial port:

```
namespace mbed
{
    FileHandle *mbed_override_console(int fileno)
    {
        // Semihosting allows "virtual" console access through a debugger.
        static LocalFileSystem fs("host");
        if (fileno == STDIN_FILENO) {
            static FileHandle *in_terminal;
            static int in_open_result = fs.open(&in_terminal, ":tt", O_RDONLY);
            return in_terminal;
        } else {
            static FileHandle *out_terminal;
            static int out_open_result = fs.open(&out_terminal, ":tt", O_WRONLY);
            return out_terminal;
        }
    }
}
```

The application can redirect the console to a different serial port if you need the default port for another use:

```
namespace
{
    FileHandle *mbed_override_console(int)
    {
        static UARTSerial uart(PA_0, PA_1);
        return &uart;
    }
}
```

Alternatively, an application could use the standard C `freopen` function to redirect `stdout` to a named file or device while running. However there is no `fdreopen` analog to redirect to an unnamed device by file descriptor or `FileHandle` pointer.

### Suppressing console output

To always suppress output, you can provide an `mbed_override_console` that returns a sink class that discards output. (For UART console targets, you can simply set `target.console-uart` to `false` in your `mbed_app.json`.)

To temporarily suppress output, `mbed_override_console` can return a class that acts as a switchable mux between a sink and the real output.

More portably, you could ensure all your code uses your own `FILE *output_stream` rather than `stdout`, and you could dynamically change that between `stdout` and `fdopen(Sink)`. That then doesn't rely on "under C library" retargeting of `stdout`. Instead, you must switch streams at the application level.

## Polling and nonblocking

By default, `FileHandle`s conventionally block until a `read` or `write` operation completes. This is the only behavior supported by normal `File`s, and is expected by the C library's `stdio` functions.

Device-type `FileHandle`s, such as `UARTSerial`, are expected to also support nonblocking operation, which permits the `read` and `write` calls to return immediately when unable to transfer data. Please see the API reference pages of these functions for more information.

For a timed wait for data, or to monitor multiple `FileHandle`s, see [`poll`](poll.html)

## Event-driven I/O

If using nonblocking I/O, you probably want to know when to next attempt a `read` or `write` if they indicate no data is available. `FileHandle::sigio` lets you attach a `Callback`, which is called whenever the `FileHandle` becomes readable or writable.

Important notes on sigio:

- The sigio may be issued from interrupt context. You cannot portably issue `read` or `write` calls directly from this callback, so you should queue an [`Event`](event.html) or wake a thread to perform the `read` or `write`.
- The sigio callback is only guaranteed when a `FileHandle` _becomes_ readable or writable. If you do not fully drain the input or fully fill the output, no sigio may be generated. This is also important on start-up - don't wait for sigio before attempting to read or write for the first time, but only use it as a "try again" signal after seeing an `EAGAIN` error.
- Spurious sigios are permitted - you can't assume data will be available after a sigio.
- Given all the above, use of sigio normally implies use of nonblocking mode or possibly `poll`.

Ordinary files do not generate sigio callbacks because they are always readable and writable.

## Suspending a device

Having a device open through a `FileHandle` may cost power, especially if open for input. For example, for `UARTSerial` to be able to receive data, the system must not enter deep sleep, so deep sleep is prevented while the `UARTSerial` is active.

To permit power saving, you can close or destroy the `FileHandle`, or you can indicate that you do not currently require input or output by calling `FileHandle::enable_input` or `FileHandle::enable_output`. Disabling input or output effectively suspends the device in that direction, which can permit power saving.

This is particularly useful when an application does not require console input - it can indicate this by calling `mbed_file_handle(STDIN_FILENO)->enable_input(false)` once at the start of the program. This permits deep sleep when `platform.stdio-buffered-serial` is set to true.

## Stream-derived FileHandles

`Stream` is a legacy class that provides an abstract interface for streams similar to the `FileHandle` class. The difference is that the `Stream` API is built around the `getc` and `putc` set of functions, whereas `FileHandle` is built around `read` and `write`. This makes implementations simpler but limits what is possible with the API. Because of this, implementing the `FileHandle` API directly is suggested API for new device drivers.

Note that `FileHandle` implementations derived from `Stream`, such as `Serial`, have various limitations:

- `Stream` does not support nonblocking I/O, poll or sigio.
- `Stream` does not have correct `read` semantics for a device - it always waits for the entire input buffer to fill.
- `Stream` returns 0 from `isatty`, which can slightly confuse the C library (for example defeating newline conversion and causing buffering).

As such, you can only use `Stream`-based devices for blocking I/O, such as through the C library, so we don't recommend use of `Stream` to implement a `FileHandle` for more general use.

## FileHandle class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_file_handle.html)

## FileHandle using C library example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-FileHandle/tree/v6.7)](https://github.com/ARMmbed/mbed-os-snippet-FileHandle/blob/v6.7/main.cpp)

## FileHandle sigio example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-FileHandle_sigio/tree/v6.7)](https://github.com/ARMmbed/mbed-os-snippet-FileHandle_sigio/blob/v6.7/main.cpp)

## Related content

- [File](file.html).
- [FileSystem](filesystem.html).
- [Poll](poll.html).
- [Power management](../apis/power-management-sleep.html).
