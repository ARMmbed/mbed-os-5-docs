# DeepSleepLock

The `DeepSleepLock` class provides an RAII object for disabling sleep. In other words, creating a DeepSleepLock object calls its constructor, which increments the deep sleep prevention lock. The DeepSleepLock object automatically releases the deep sleep prevention lock in its destructor when the object goes out of scope. Another way to look at this is when the DeepSleepLock object exists, it prevents deep sleep.

<span class="notes">**Note:** Drivers that don't work in deep sleep mode automatically prevent deep sleep mode, so DeepSleepLock does not need to protect them.</span>

## DeepSleepLock class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_deep_sleep_lock.html)

## Example

This example shows how you can lock deep sleep to decrease interrupt latency at the expense of increased power consumption.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/DeepSleepLock_Example_1/)](https://os.mbed.com/teams/mbed_example/code/DeepSleepLock_Example_1/file/66aac0656e71/main.cpp)

## Related content

- [Power management API references](power-management.html).
- [Office Hours video about low power, tickless and sleep](https://www.youtube.com/watch?v=OFfOlBaegdg).
