# Sleep

Implement the Sleep HAL API to enable your device to go into a low power state when you are not actively using it.

## Assumptions

### Defined behavior

There are two power-saving modes available in Mbed OS:

### Sleep

The core system clock is disabled. You can use both the low- and high-frequency clocks and retain RAM.

1. Wake-up sources - Any interrupt must wake up the MCU.
1. Latency - The MCU must wake up within 10 us.

#### Deep sleep

The core system clock is disabled. You can only enable the low-frequency clocks and retain RAM.

1. Wake-up sources - RTC, low power ticker or GPIO must wake up the MCU.
1. Latency - The MCU must wake up within 10 ms.

## Implementing the Sleep API

You can find the API and specification for the sleep API in the following header file:

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/group__hal__sleep.html)

To enable sleep support in Mbed OS, you need to add the `SLEEP` label in the `device_has` option of the target's section in the `targets.json` file.

## Targets that disable `systick` in sleep mode

If your target disables `systick` when entering sleep mode, the RTOS scheduler does not function correctly in the default configuration. You can fix this by either adding `SYSTICK_CLK_OFF_DURING_SLEEP` to `device_has`, which disables sleep when the RTOS is present, or by implementing tickless and adding `MBED_TICKLESS`.

## Testing

The Mbed OS HAL provides a set of conformance tests for Sleep. You can use these tests to validate the correctness of your implementation. To run the Sleep HAL tests, use the following command:

```
mbed test -t <toolchain> -m <target> -n "tests-mbed_hal-sleep*"
```

You can read more about the test cases:

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/group__hal__sleep__tests.html)
