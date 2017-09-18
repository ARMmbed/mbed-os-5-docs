## Configuration

TODO: intro how config is used and how to identify it (rules of use)
TODO: content below is partially runtime, partially rtos

The Arm Mbed configuration system customizes the compile time configuration of Mbed components: targets, libraries and applications.

Mbed OS provides some default memory configurations for thread memory allocation. You may want to modify these configurations to better suit your project. You can read about the default configurations and how you can modify them below. 

#### Configuring the main thread stack

The default stack size of the main application thread is 4 kilobytes. This memory is dynamically allocated from the global heap. You can configure the stack size of the main thread by using the [Mbed config system](/docs/v5.4/porting/the-arm-mbed-configuration-system.html). To reduce the stack size from 4K to 2K, create an `mbed_app.json` file for your project with the following content:

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

The default stack size of a user spawned thread is 4 kilobytes. You can configure the stack size of user spawned threads by using the [Mbed config system](/docs/v5.4/porting/the-arm-mbed-configuration-system.html) or passing in the [Thread constructor](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.6/api/group__rtos.html#gab9f45e13f619a725b87c1e43c14cf158). You can reduce the default stack size for user spawned threads from 4K to 2K in the following two ways:

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

By default, mbed OS dynamically allocates the memory for the thread's stack from the global heap, though you can change it in the [Thread constructor](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.6/api/group__rtos.html#gab9f45e13f619a725b87c1e43c14cf158). Here is an example application that uses memory allocated from the main thread's stack for the newly spawned thread stack:

```
int main() {
    uint32_t stack_on_main_stack[128 / sizeof(uint32_t)]; // 128 bytes
    Thread thread(osPriorityNormal, sizeof(stack_on_main_stack), stack_on_main_stack);
}
```

