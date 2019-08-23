<h1 id="watchdog-port">Watchdog</h1>

The Watchdog HAL API provides a low-level interface to the Independent Watchdog Timer of a target. Implementing the Watchdog API is not mandatory, but by implementing it, you can use the hardware watchdog timer to detect and recover from computer malfunctions.

Implement the ResetReason API when implementing the Watchdog API. The ResetReason API allows you to detect at boot time whether a watchdog caused the last reset.

## Assumptions

### Defined behavior

- Sleep and debug modes don't stop the watchdog timer from counting down.
- The function `hal_watchdog_init` is safe to call repeatedly. The function's implementation must not do anything if `hal_watchdog_init` has already initialized the hardware watchdog timer.
- `UINT32_MAX` milliseconds is the maximum allowed max_timeout `hal_watchdog_get_platform_features()` returns; minimum timeout is 1 ms.
- The watchdog should trigger at or after the timeout value.
- The watchdog should trigger before twice the timeout value.

### Undefined behavior

- Calling any function other than `hal_watchdog_init` or `hal_watchdog_get_platform_features` before you have initialized the watchdog.

### Notes

- A software reset may not stop the watchdog timer; the behavior is platform specific.

## Dependency

Hardware Independent Watchdog support.

## Implementing Watchdog

You can find the API and specification for the Watchdog API in its HAL API reference:

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/group__hal__watchdog.html)

To enable Watchdog support in Mbed OS, add the `WATCHDOG` label in the `device_has` option of the target's section in the `targets.json` file.

## Testing

The Mbed OS HAL provides a set of conformance tests for Watchdog. You can use these tests to validate the correctness of your implementation. To run the Watchdog HAL tests use the following command:

```
mbed test -t <toolchain> -m <target> -n "tests-mbed_hal-watchdog*"
```

For more details, please see:

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/group__hal__watchdog__tests.html)
