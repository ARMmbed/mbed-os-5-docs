### Configuring Arm Mbed OS

#### Thread memory model

All threads in Mbed OS share a global heap. By default, memory for thread stacks is dynamically allocated from the global heap. User spawned thread stacks can be allocated from other memory areas. The size of the global heap depends on the compiler. The heap size is static when compiling with IAR, and it is different for each target in Mbed OS. You can find it in the IAR linker configuration files nested inside target directories. For example, you can find the linker configuration file for a K66F [here](https://github.com/ARMmbed/mbed-os/blob/master/targets/TARGET_Freescale/TARGET_MCUXpresso_MCUS/TARGET_K66F/device/TOOLCHAIN_IAR/MK66FN2M0xxx18.icf#L49-L51). For the GCC and ARM compilers, the heap size is dynamic based on RAM usage.

#### Default threads

By default, there are four threads running after boot: the ISR/scheduler thread, the idle thread, the timer thread and the main application thread. Combined, the idle thread, timer thread and ISR/scheduler thread consume 2 kilobytes of RAM. The user cannot modify these. You can expand or reduce the size of the main application thread stack by using the Mbed configuration system.

#### Configuring the main thread stack

The default stack size of the main application thread is 4 kilobytes. This memory is dynamically allocated from the global heap. You can configure the stack size of the main thread by using the [Mbed config system](https://docs.mbed.com/docs/mbed-os-handbook/en/latest/advanced/config_system/). To reduce the stack size from 4K to 2K, create an `mbed_app.json` file for your project with the following content:

```JSON
{
    "config": {
        "main-stack-size": {
            "value": 2000
        }
    }
}
```

#### Configuring user spawned thread stacks

The default stack size of a user spawned thread is 4 kilobytes. You can configure the stack size of user spawned threads by using the [Mbed config system](https://docs.mbed.com/docs/mbed-os-handbook/en/latest/advanced/config_system/) or passing in the [Thread constructor](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/group__rtos.html#gab9f45e13f619a725b87c1e43c14cf158). You can reduce the default stack size for user spawned threads from 4K to 2K in the following two ways:

1. Create an `mbed_app.json` file for your project with the following content:

    ```JSON
    {
        "config": {
            "thread-stack-size": {
                "value": 2000
            }
        }
    }
    ```

2. Construct the thread like this in your application:

    `Thread thread(osPriorityNormal, 2000);`

By default, the memory for the thread's stack is dynamically allocated from the global heap, though you can change it in the [Thread constructor](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/group__rtos.html#gab9f45e13f619a725b87c1e43c14cf158). Here is an example application that uses memory allocated from the main thread's stack for the newly spawned thread stack:

```
int main() {
    uint32_t stack_on_main_stack[128 / sizeof(uint32_t)]; // 128 bytes
    Thread thread(osPriorityNormal, sizeof(stack_on_main_stack), stack_on_main_stack);
}
```

