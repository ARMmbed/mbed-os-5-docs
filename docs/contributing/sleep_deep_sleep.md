# Sleep HAL API

mbed OS defines two sleep modes for HAL:

- Sleep
- Deep sleep

Each target should document in their implementation:

- The target's mode description for each mode (how target's mode map to mbed OS sleep modes)
- Wake-up latency for each mode
- Wake-up sources for each mode

## Sleep

The core system clock is disabled, both the low and high precision clocks are enabled, RAM is retained.

1. Wake-up sources - any interrupt source should be able to wake-up the MCU
1. Latency - should wake-up within 10 us

## Deep sleep

The core system clock is disabled. The low precision clocks are enabled, RAM is retained.

1. Wake-up sources - RTC, low power ticker or GPIO should be able to wake-up the MCU
1. Latency - should wake-up within 10 ms

The deep sleep latency (10 ms) was chosen as the higher limit of the boards we support. Most of targets have wake-up latency for deep sleep within few microseconds, but often additional time is needed for reinitializing clocks or other configuration necessary to restore previous state.

## Implementing the Sleep API

There are two functions that target needs to implement to support sleep, their prototypes are located in [hal/sleep_api.h]():

- Sleep

```c++
void hal_sleep(void);
```

- Deep sleep

```c++
void hal_deepsleep(void);
```

To enable sleep support in mbed OS `SLEEP` label needs to be added in `device_has` option of target's section in `targets.json` file.

## Testing

The [sleep HAL API test suite]() validates:
- Sleep wake-up sources
- Sleep wake-up latency
