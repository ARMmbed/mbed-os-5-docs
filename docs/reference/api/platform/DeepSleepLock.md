## DeepSleepLock

The `DeepSleepLock` class provides an RAII object for disabling sleep. You can prevent an application from entering deep sleep by creating an instance of the `DeepSleepLock` class. While the DeepSleepLock instance exists it prevents deep sleep.

<span class="notes">**Note:** Drivers that don't work in deep sleep mode automatically prevent deep sleep mode, so DeepSleepLock does not need to protect them.</span>

### DeepSleepLock class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/classmbed_1_1_deep_sleep_lock.html)

### Example

This example shows how you can lock deep sleep to decrease interrupt latency at the expense of increased power consumption.

[![View code](https://os.mbed.com/teams/mbed_example/code/DeepSleepLock_Example_1/)](https://os.mbed.com/teams/mbed_example/code/DeepSleepLock_Example_1/file/66aac0656e71/main.cpp)
