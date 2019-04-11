<h1 id="NFC-port">NFC EEPROM driver porting guide</h1>

NFC EEPROM provides low level operations needed to create an NFC TAG. The device usually allows one device at a time to read and write into a shared memory through one of two channels. One is the radio channel that external devices interacting with the device use. The other is wired to the MCU. Either device needs to obtain a session before performing its operations. The session is released as the last step or through a timeout.

## Class hierarchy

The `NFCTarget` uses an implementation of `NFCEEPROMDriver` as the backend that delivers the fundamental operations needed to access and modify the memory containing the NDEF messages. The target implementation of `NFCTarget` creates the instance of the class.

Your implementation inherits from `NFCEEPROMDriver` and implements all the public methods therein.

## Required methods

`NFCEEPROMDriver` defines the following pure virtual methods.

These must return synchronously:

- `void reset()`.
- `size_t read_max_size()`.

These must return their results through calling methods in the `Delegate`:

- `void start_session(bool force = false)`.
- `void end_session()`.
- `void read_bytes(uint32_t address, uint8_t* bytes, size_t count)`.
- `void write_bytes(uint32_t address, const uint8_t* bytes, size_t count)`.
- `void write_size(size_t count)`.
- `void read_size()`.
- `void erase_bytes(uint32_t address, size_t size)`.

### Implementing `reset`

`reset` is called during initialization and may be called repeatedly. This must be safe to be called at any time and should return when the device is ready for operation.

### Implementing `read_max_size`

This must synchronously return the (effective) size of the EEPROM memory available to NDEF messages (not including the memory required by other files or headers).

### Implementing `start_session` and `end_session`

`start_session` and `end_session` open and close the communication with the device. `start_session` has an extra parameter that indicates the session should be started even if it would kill the RF session in the process. Otherwise, the `open_session` triggers the `on_session_opened` with the parameter set to false (failure) if an RF session is already opened.

### Implementing `read_bytes` and `write_bytes`

Both methods contain the `address`, which is to be used as the starting offset in the file. This starts at the beginning of the body of the file where NDEF messages may be written. You must account for any headers in the offset and size calculations. The `count` parameters are the maximum sizes of the operations, but the operation may return less than the requested counts.

The events `on_bytes_read` and `on_bytes_written` must return the number of bytes successfully read or written in case the maximum size of the operation the device allows is smaller than the request operation. It's up to the caller to call these methods multiple times with appropriate offsets as required.

### Implementing `read_size` and `write_size`

`read_size` and `write_size` read and write the limits the write and read operations use. Writing or reading beyond the set size must be truncated to the current size.

### Implementing `erase_bytes`

This is the equivalent of calling `write_bytes` with a buffer filled with `0`. Like `write_bytes`, it must return the number of bytes successfully set to `0`.

## Asynchronous operation

Depending on your hardware, you may support synchronous or asynchronous operation.

We designed the `NFCEEPROMDriver` with asynchronous operation, and the results of long operations are communicated through events. You must use these events, even if your implementation is synchronous.

In asynchronous implementations, you may use an `EventQueue` to schedule processing caused by interrupts. The `NFCTarget` has set up your event queue, which you can get by calling:

`EventQueue* event_queue()`

You may initiate your event processing by calling `call()` on the event queue.

For example:

If your event management occurs in a function called `manage_event`, you should call:

`event_queue()->call(&manage_event);`

The `EventQueue` also accepts passed in parameters and objects for nonstatic method calls. Please see the `EventQueue` documentation for details on calling functions on the queue.
    
### Communicating events back to the NFCTarget

All events call methods in the `Delegate` class object that has been set by the `NFCTarget`. Delegate is accessible through:
`Delegate* delegate()`

It implements the following methods:

- `void on_session_started(bool success)`
- `void on_session_ended(bool success)`
- `void on_bytes_read(size_t count)`
- `void on_bytes_written(size_t count)`
- `void on_size_written(bool success)`
- `void on_size_read(bool success, size_t size)`
- `void on_bytes_erased(size_t count)`

You must use these to communicate the results of all asynchronous calls.

## Testing

A macro `NFCEEPROM` is required for the test to build. The module containing your driver should contain `mbed_lib.json`. Add a configuration option for the build system to convert into a macro. Your `mbed_lib.json` could look like this:

```javascript
{
    "name": "MBED_NFC_<name of your driver>",
    "config": {
        "nfceeprom": {
            "macro_name": "NFCEEPROM",
            "value": true,
            "help": "Device supports NFC EEPROM"
        }
    }
}
```

Run the tests with:

`mbed test -m [mcu] -t [toolchain] -n tests-nfc-eeprom*`.
