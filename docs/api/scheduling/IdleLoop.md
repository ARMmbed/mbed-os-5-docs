# Idle loop

Idle loop is a background system thread, which scheduler executes when no other threads are ready to run. That may happen when your application is waiting for an event to happen. By default, the idle loop invokes sleep manager to enter a sleep mode. You can overwrite this behavior by providing a different handler:

```c++ TODO
void new_idle_loop()
{
    // do nothing
}

void main()
{
    rtos_attach_idle_hook(&new_idle_loop);
}
```

## Function reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.13/mbed-os-api-doxy/group__rtos___idle.html)

## Example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-SleepManager_Example_1/tree/v6/13)](https://github.com/ARMmbed/mbed-os-snippet-SleepManager_Example_1/blobl/v6/13/main.cpp)

## Related content

- [DeepSleepLock API reference](deepsleeplock.html).
- [Power management API reference](power-management-sleep.html).
