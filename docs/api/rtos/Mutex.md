# Mutex

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/classrtos_1_1_mutex.png)<span>Mutex class hierarchy</span></span>

A Mutex is used to synchronize the execution of threads, for example to protect the access to a shared resource.

The `Mutex` methods cannot be called from interrupt service routines (ISR). In the current version of Mbed OS, if you attempt to use a mutex from within an ISR, it will treat that as a fatal system error, and you will see an error like this:

```
++ MbedOS Error Info ++
Error Status: 0x80020115 Code: 277 Module: 2
Error Message: Mutex lock failed
Location: 0x80026B3
Error Value: 0xFFFFFFFA
Current Thread: Id: 0x20004F54 Entry: 0x8002ABF StackSize: 0x1000 StackMem: 0x20004F98 SP: 0x2004FEF8
For more info, visit: https://armmbed.github.io/mbedos-error/?error=0x80020115
-- MbedOS Error Info --
```

If synchronization is required in ISR, consider using semaphores.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/Mutex.png)</span>

<span class="notes">**Note:** Mbed OS uses the [PlatformMutex](platformmutex.html) class instead of the RTOS mutex for all drivers.</span>

## Mutex class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classrtos_1_1_mutex.html)

## Mutex example

Use Mutex to protect printf().

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/rtos_mutex/)](https://os.mbed.com/teams/mbed_example/code/rtos_mutex/file/6a34e5f81bba/main.cpp)

<span class="notes">**Note:** C standard library Mutexes<br>The Arm C standard library already has Mutexes in place to protect the access to `stdio`, so on the LPC1768 the above example is not necessary. On the other hand, the LPC11U24 does not provide default `stdio` Mutexes, making the above example a necessity.</br></span>

<span class="notes">**Note:** Because of the mutexes in the Arm C standard library, you cannot use `stdio` (`printf`, `putc`, `getc` and so on), `malloc` and `new` in ISR. </span>

## Related content

- [PlatformMutex](platformmutex.html) API reference.
