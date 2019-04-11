# Timer

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/classmbed_1_1_timer.png)<span>Timer class hierarchy</span></span>

Use the Timer interface to create, start, stop and read a timer for measuring precise times (better than millisecond precision).

You can independently create, start and stop any number of Timer objects.

## Warnings and notes

- Timers are based on 64-bit unsigned microsecond counters, but for backward compatibility, the `read_ms()` and `read_us()` methods only return 32-bit signed integers. This limits their range before wrapping to 49 days and 35 minutes respectively. Use `read_high_resolution_us()` to access the full range of over 500,000 years.
- While a Timer is running, deep sleep is blocked to maintain accurate timing. If you don't need microsecond precision, consider using the LowPowerTimer class instead because this does not block deep sleep mode.

## Timer class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/_timer_8h_source.html)

## Timer hello, world

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/Timer_HelloWorld/)](https://os.mbed.com/teams/mbed_example/code/Timer_HelloWorld/file/0d21eea06da7/main.cpp)

## Related content

- [Office Hours video about low power, tickless and sleep](https://youtu.be/OFfOlBaegdg?t=669).
