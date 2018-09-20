## FileHandle

For general information on [files](file.html) and [filing systems](filesystem.html) in persistant storage, see the respective documentation. This chapter covers the abstract API, with an emphasis on devices, as they're less straightforward.

`FileHandle` is an abstract class representing a device that supports file-like operations such as `read` and `write`. This may be an actual `File` on a storage device provided by a `FileSystem`, or a device such as `UARTSerial`.

The `FileHandle` abstraction represents an already-opened file or device, so it has no `open` method of its own - the opening may take the form of a call to another class that returns a `FileHandle`, such as `FileSystem::open`, or it may be implicit in the construction of an object such as `UARTSerial`. 

The `FileHandle` abstraction permits stream-handling code to be device-independent. For example the console input and output streams used for C's `stdin` and `stdout` can be retargeted to something other than the default serial port via the `FileHandle` API, and `ATCmdParser` and the PPP connection to lwIP work on abstract `FileHandle` pointers.

Exactly which operations a `FileHandle` supports will depend on the underlying device, and will in turn restrict what applications it is suitable for. For example, a database application might require random-access and `seek`, but this may not be available on a limited filesystem, and certainly not on a stream device. Only a `File` on a full `FileSystem` such as `FATFileSystem` would generally implement the entire API. Specialised devices may have particular limitations or behavior, which they should document, and which would limit their general utility. Devices that do not implement a particular call indicate it by an error return - often `ENOSYS`, but sometimes more specific errors such as `ESPIPE` apply; see POSIX specifications for details.

### Relationship of FileHandle to other APIs

Mbed `FileHandle`s can be used directly, but they are often manipulated via POSIX or C/C++ APIs. The layering is that stdio calls taking `FILE *stream` call the POSIX APIs taking `int fd`, which call methods on `FileHandle` objects.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/filehandle_callstack.png)</span>

The `FileHandle` may be implicitly created by a higher layer, as in a call to `fopen`. In this case, the name lookup will produce a `FileHandle` and POSIX file descriptor internally.

The three APIs provide different levels of capability:

API                            | C/C++                   | POSIX                  | Mbed
-------------------------------|-------------------------|------------------------|-----------------------------
Headers                        | stdio.h, iostream       | mbed_retarget.h        | FileHandle.h, mbed_poll.h
Main type                      | FILE *                  | int                    | FileHandle object
Blocking I/O                   | Yes (always)            | Yes (default)          | Yes (default)
Non-blocking I/O               | No                      | Yes                    | Yes
Poll                           | No                      | Yes (struct pollfd)    | Yes (struct pollfh)
Sigio                          | No                      | No                     | Yes
Device-specific extensions     | No                      | No                     | Possible via derived types
Newline conversion             | Yes (enabled via JSON)  | No                     | No
Error indications              | EOF, ferror, set errno  | Return -1, set errno   | Return negative error code
Portability                    | High                    | Medium                 | Low

The APIs can be mixed with care, for example setting up a callback initially with `FileHandle::sigio`, but performing all subsequent operations using POSIX.

* Note: `errno` is not currently thread-local on all toolchains. This may cause problems with error handling if multiple threads are using POSIX or C file APIs simultaneously.
 
### Mapping between APIs

Calls are provided to attach already-opened lower levels to the higher levels:

* `int mbed_bind_to_fd(FileHandle *)` bind a FileHandle to a POSIX file descriptor
* `FILE *fdopen(int fd, const char *mode)` bind a POSIX file descriptor to a stdio FILE
* `FILE *fdopen(FileHandle *fh, const char *mode)` bind a FileHandle to a stdio FILE

There is currently no call to map from POSIX file descriptor to `FileHandle`; this may be added in future.

The standard POSIX function `int fileno(FILE *stream)` may be available to map from `FILE` to file descriptor, depending on the toolchain and C library in use - it is not useable in fully-portable Mbed OS code.

Given those limitations on mapping, if code needs to access the lower levels, a lower-level open call should be used, so the  lower-level handle is known, then that is bound to the higher level(s).

The POSIX file descriptors for the console are available as `STDIN_FILENO`, `STDOUT_FILENO` and `STDERR_FILENO`, permitting operations such as `fsync(STDERR_FILENO)`, which would for example drain `UARTSerial`s output buffer.

### Redirecting the console

If a target has serial support, by default a serial port is used for the console. The pins and settings for the port selection come from target header files and JSON settings. This uses either an internal `DirectSerial` if unbuffered (for backwards compatibility) or `UARTSerial` if `platform.stdio-buffered-serial` is `true`.

This can be overridden by the target providing `mbed::mbed_target_override_console` to specify an alternative `FileHandle`. For example, a target using SWO might have:

    namespace mbed
    {
        FileHandle *mbed_target_override_console(int)
        {
            static SerialWireOutput swo;
            return &swo;
        }
    }

Then any program using simple `printf` on that target will send its output over the SWO, rather than serial.

Because the console can be redirected in this way by targets, portable applications should not use constructs like `Serial(USBTX, USBRX)` assuming that this will access the console. Instead they should use `stdin`/`stdout`/`stderr` or `STDIN_FILENO`/`STDOUT_FILENO`/`STDERR_FILENO`.

    // Don't do:
    Serial serial(USBTX, USBRX);
    serial.printf("Hello!\r\n");
    
    // Do do:
    printf("Hello!\n");  // assume platform.stdio-convert-newlines is true


Beyond the target-specific override, an application can override the target's default behaviour itself by providing `mbed::mbed_override_console`. 

Alternatively, an application could use the standard C `freopen` function to redirect `stdout` to a named file or device while running. However there is no `fdreopen` analogue to redirect to an unnamed device by file descriptor or `FileHandle` pointer. 

### Polling and non-blocking

By default `FileHandle`s conventionally block until a `read` or `write` operation completes. This is the only behaviour supported by normal `File`s, and is expected by the C library's `stdio` functions.

Device-type `FileHandle`s such as `UARTSerial` are expected to also support non-blocking operation, which permits the `read` and `write` calls to return immediately when unable to transfer data. See reference of these functions for more information.

For a timed wait for data, or to monitor multiple `FileHandle`s, see [`poll`](poll.html)


### Event-driven I/O

If using non-blocking I/O, you will probably want to be know when to next attempt a `read` or `write` if they indicate no data is available. `FileHandle::sigio` lets you attach a `Callback` which will be called whenever the `FileHandle` becomes readable or writable.

Important notes on sigio:

* The sigio may be issued from interrupt context. You cannot portably issue `read` or `write` calls directly from this callback, so you should queue an [`Event`](event.html) or wake a thread to perform the `read` or `write`.
* The sigio callback is only guaranteed when a `FileHandle` _becomes_ readable or writable. So if you do not fully drain the input, or fully fill the output, no sigio may be generated. This is also important on start-up - don't wait for sigio before attempting to read/write for the first time, but only use it as a "try again" signal after seeing an `EAGAIN` error.
* Spurious sigios are permitted - you can't assume data will be available after a sigio.
* Given all the above, use of sigio normally implies use of non-blocking mode, or possibly `poll`. 

Ordinary files do not generate sigio callbacks, because they are always readable and writable, so never become readable or writable.

### Stream-derived FileHandles

`Stream` is a legacy class that provides an abstract interface for streams similar to the `FileHandle` class. The difference is that the `Stream` API is built around the `getc` and `putc` set of functions, whereas `FileHandle` is built around `read` and `write`. This makes implementations simpler but limits what is possible with the API. Because of this, implementing the `FileHandle` API directly is suggested API for new device drivers.

Note that `FileHandle` implementations derived from `Stream`, such as `Serial`, have various limitations:

* `Stream` does not support non-blocking I/O, poll or sigio.
* `Stream` does not have correct `read` semantics for a device - it always waits for the entire input buffer to be filled.
* `Stream` returns 0 from `isatty`, which can slightly confuse the C library (eg defeating newline conversion, and causing buffering).

As such, `Stream`-based devices can only be used for blocking I/O, such as through the C library, so use of `Stream` to implement a `FileHandle` for more general use is not recommended.
 
### FileHandle class reference
[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_file_handle.html)

### FileHandle via C library example

```
// Continuously monitor a serial device, and every time it outputs a
// character, send it to the console and toggle LED2. Can use the C library
// to access the device as only using blocking I/O.
//
// Note that the console is accessed via putchar - this will be accessing
// a FileHandle-based device under the surface, but the particular device can be
// target-dependent. This makes the program portable to different devices
// with different console types, with the only target-dependence being
// knowledge of which pins the serial device we're monitoring is attached to,
// which can be configured via JSON.

static DigitalOut led2(LED2);

// UARTSerial derives from FileHandle
static UARTSerial device(MBED_CONF_APP_DEVICE_TX, MBED_CONF_APP_DEVICE_RX);

int main()
{
    // Perform device-specific setup
    device.set_baud(19200);
    
    // Once set up, access via C library
    FILE *devin = fdopen(&device, "r");
    
    while (1) {
        putchar(fgetc(devin));
        led2 = !led2;
    }
}
```
// 
### FileHandle sigio example

```
// Main thread flashes LED1, while we monitor a serial-attached device
// in the background. Every time that device outputs a character, we echo
// it to the console and toggle LED2.
#include "mbed.h"

static DigitalOut led1(LED1);
static DigitalOut led2(LED2);

static UARTSerial device(MBED_CONF_APP_DEVICE_TX, MBED_CONF_APP_DEVICE_RX);

static void callback_ex()
{
    // always read until data is exhausted - we may not get another
    // sigio otherwise
    while (1) {
        char c;
        if (device.read(&c, 1) != 1) {
            break;
        }
        putchar(c);
        led2 = !led2;
    }
}

int main()
{
    // UARTSerial-specific method - all others are from FileHandle base class
    device.set_baud(19200);
    
    // Ensure that device.read() returns -EAGAIN when out of data
    device.set_blocking(false);
    
    // sigio callback is deferred to event queue, as we cannot in general
    // perform read() calls directly from the sigio() callback.
    device.sigio(mbed_event_queue()->event(callback_ex));

    while (1) {
        led1 = !led1;
        wait(0.5);
    }
}

```

### Related content

- [File](file.html).
- [FileSystem](filesystem.html).
- [poll](poll.html).
