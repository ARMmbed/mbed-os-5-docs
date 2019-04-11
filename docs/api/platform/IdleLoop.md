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

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/group__rtos___idle.html)

## Example

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/SleepManager_Example_1/)](https://os.mbed.com/teams/mbed_example/code/SleepManager_Example_1/file/e85412b4147e/main.cpp)

## Related content

- [DeepSleepLock API reference](deepsleeplock.html).
- [Power management API reference](power-management.html).
- [Office Hours video about low power, tickless and sleep](https://www.youtube.com/watch?v=OFfOlBaegdg).
