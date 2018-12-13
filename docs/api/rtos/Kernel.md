## Kernel interface functions

The Kernel namespace implements interfaces to attach a function to some kernel events and also to read the kernel tick count.

### Kernel namespace reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.11/mbed-os-api-doxy/namespacertos_1_1_kernel.html)

### `get_ms_count()` example

The function `get_ms_count()` can be used to read the current RTOS kernel millisecond tick count. The below code snippet demonstrates use of the `get_ms_count()` function to calculate the elapsed time:

```
void send_data()
{
    // 64-bit time doesn't wrap for half a billion years, at least
    uint64_t now = Kernel::get_ms_count();
    //do some operations
    // ...

    uint64_t later = Kernel::get_ms_count();

    //calculate millisecs elapsed
    uint64_t elapsed_ms = later - now;
}

```

### `attach_idle_hook()` example

The function `attach_idle_hook()` can be used to attach a function to be called by the RTOS idle task. The below code snippet demostrates the usage.

[![View Example](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-kernel-hooks)](https://github.com/ARMmbed/mbed-os-example-kernel-hooks/blob/master/main.cpp)

### `attach_thread_terminate_hook()` example

The function `attach_thread_terminate_hook()` can be used to attach a function to be called when a thread terminates.

[![View Example](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-kernel-hooks)](https://github.com/ARMmbed/mbed-os-example-kernel-hooks/blob/master/main.cpp)
