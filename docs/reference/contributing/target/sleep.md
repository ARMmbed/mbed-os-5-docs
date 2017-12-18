### Sleep and deep sleep

Mbed OS defines two sleep modes for HAL:

- Sleep.
- Deep sleep.

Each target should document in their implementation:

- The target's mode description for each mode (how the target's mode maps to the Mbed OS sleep modes).
- Wake-up latency for each mode.
- Wake-up sources for each mode.

#### Sleep

The core system clock is disabled, both the low and high precision clocks are enabled and RAM is retained.

1. Wake-up sources - any interrupt source can wake up the MCU.
1. Latency - can wake up within 10 us.

#### Deep sleep

The core system clock is disabled. The low precision clocks are enabled, and RAM is retained.

1. Wake-up sources - RTC, low power ticker and GPIO can wake up the MCU.
1. Latency - can wake up within 10 ms.

The deep sleep latency (10 ms) is the higher limit of the boards we support. Most of targets have wake-up latency for deep sleep within a few microseconds, but often, reinitializing clocks and other configurations require additional time to restore previous state.

#### Implementing the Sleep API

There are two functions that the target needs to implement to support sleep, Their prototypes are in <a href="/docs/v5.7/mbed-os-api-doxy/sleep__api_8h_source.html" target="_blank">hal/sleep_api.h</a>:

- Sleep.

```c++
void hal_sleep(void);
```

- Deep sleep.

```c++
void hal_deepsleep(void);
```

To enable sleep support in Mbed OS, you need to add the `SLEEP` label in the `device_has` option of the target's section in the `targets.json` file.
