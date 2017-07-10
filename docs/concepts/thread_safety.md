# Thread and Interrupt Safety in mbed OS 5

## About this document

This document introduces the [mbed OS RTOS](#rtos) and [thread safety mechanisms](#thread-safety), then discusses [porting them](#considerations-when-porting) to a new target.

## RTOS

One of the major improvements introduced in mbed OS 5 is a new programming model based on a real time operating system (RTOS). Some earlier versions of mbed have had optional support for an RTOS. In version 5, RTOS support is a standard feature of the platform, so developers can take advantage of a more flexible programming model based on multiple threads.

As with any multithreaded environment, mbed developers need to use various synchronization primitives to ensure their code doesn’t include race conditions or other concurrency problems. They also need to understand what thread-safety guarantees the mbed OS 5 APIs provide when they use them. This is particularly important for code that runs in response to a hardware interrupt service routine (ISR), which needs to be carefully designed so as not to compromise the thread safety of the whole system.

The mbed OS library contains internal synchronization to provide various levels of thread safety. This document describes the mechanisms mbed OS 5 provides to build thread safe applications.  

## Thread and interrupt safety

### Synchronization levels

Different components within mbed OS 5 provide different levels of synchronization:

1. **Interrupt safe** - safe for use from multiple threads and interrupts; operation is done atomically or in a [critical section](#critical-sections). The behavior is well defined when used from both interrupts and threads.
2. **Thread safe** - safe for use from multiple threads; operation is protected by an RTOS primitive and can be used from multiple threads, but will cause problems if used from an interrupt service routine.
3. **Not protected** - operation does not protect against concurrent access and needs to be synchronized externally. If you call from multiple threads without some other form of synchronization, data can become corrupted and behavior is undefined.

<span class="tips">**Tip:** The API reference indicates the level of synchronization of each function.</span>

![](images/mbed-OS-5-protection.png "Showing the relationship between interrupt-safe, thread-safe and not-protected")

### Standard libraries

All supported toolchains are thread safe when using the full version of their standard library:


* Multi-threading support:
    * GCC Newlib - **GNU** ARM Embedded Toolchain
    * IAR Standard Library - **IAR** toolchain
    * ARMCC Standard Library - **ARM** toolchain
* Single thread support only:
    * Newlib Nano - **GNU** ARM Embeded Toolchain
    * Micro ARMCC - **uARM** toolchain


<span class="notes">**Note:** GCC and ARMCC provide smaller variants of their libraries. These smaller versions are not thread safe, and projects using them should always use only one thread.</span>

### Drivers

Most drivers are **thread safe** but may not be **interrupt safe**. Always check the relevant handbook page or doxygen for more specific details on the driver being used.

<span class="tips">**Note:** It is important that you first read the [section on synchronization levels](#synchronization-levels) above.</span>


Drivers that are **interrupt safe**:

- DigitalIn, DigitalOut, DigitalInOut.
- InterruptIn.
- PortIn, PortOut, PortInOut.
- PwmOut.
- Ticker, TimerEvent, Timeout.
- Timer.

Drivers that are **not protected**:

- SPISlave
- I2CSlave

### HAL C API

The HAL C API is the porting layer of mbed OS 5 and is not thread safe. Developers should not typically use this API directly, instead using the higher-level drivers and libraries. If you program directly to the HAL C API, it is your responsibility to synchronize operations with an appropriate mechanism, such as a mutex.

### Synchronization mechanisms

#### Mutex

The mbed RTOS C++ API provides the ``mutex`` class, which is one of the simplest primitives used to make code **thread safe**. Using a mutex is the recommended way of protecting an object's data, and most of the common mbed APIs are made thread safe through the use of mutexes.

However, there are times when a simple mutex is not an appropriate mechanism for achieving thread safety. In particular, mutexes should not be used within interrupt service routines (ISRs). The correct way to work with ISRs is not to let them do any real processing when responding to an interrupt. Instead, interrupts should send an event or message to a thread; the interrupt then completes, the thread is rescheduled and, subsequently, it is the thread that will perform the processing. This allows the thread to acquire the mutex safely when it needs it for processing.

The RTOS provides several mechanisms to move interrupt processing onto a thread. These include, but are not limited to:


 * [Signals](https://developer.mbed.org/users/mbed_official/code/mbed-rtos/docs/4c105b8d7cae/classrtos_1_1Thread.html)
 * [Queue](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/Queue_8h_source.html)
 * [Mail](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/Mail_8h_source.html)


**Warning:** In mbed OS 5, if you attempt to use a mutex from within an interrupt, nothing happens; attempts to lock a mutex will succeed immediately, regardless of whether the lock is actually free. In other words, if you acquire a mutex lock in an interrupt, you can break the thread safety mechanisms and introduce race conditions into an otherwise safe piece of code. Future versions of mbed OS will provide warnings and ultimately prevent this from happening.

For more information see [rtos/Mutex.h](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/Mutex_8h_source.html).

#### Atomics

mbed OS provides atomic functions to make code **interrupt safe**. If you must modify an object or data structure from interrupts, you can use these atomic functions to synchronize the access.

For more information see [platform/critical.h](https://github.com/ARMmbed/mbed-os/blob/master/platform/critical.h).

#### Critical sections

Critical sections disable interrupts to provide uninterrupted access to a resource, so you can use critical sections to make code **interrupt safe**.  However, you should avoid using critical sections if you can, because they must execute quickly, or they will cause system instability.

**Warnings**:

- Do not perform time consuming operations inside critical sections. This will negatively affect the timing of the entire system, because all interrupts are disabled during critical sections.
- Do not invoke any standard lib or RTOS functions within a critical section; it could result in a hard fault because RTOS performs SVC calls.

For more information see [platform/critical.h](https://github.com/ARMmbed/mbed-os/blob/master/platform/critical.h).

### Major mbed OS libraries

- Network Socket API - **Thread safe**: public calls are protected by a mutex.
- Nanostack - **Not protected**:  in general, we recommend that mbed developers use our 6LoWPAN stack through the Network Socket API. If you wish to use Nanostack directly, you need to be aware of how it uses threads. The core of Nanostack runs on a tasklet mechanism, scheduled on a single underlying OS thread. Developers who wish to call directly to Nanostack must create their own tasklet and make Nanostack calls from there. Because there is only one OS thread servicing all tasklets, there is no need for further synchronization between tasklets. [See the 6LoWPAN documentation](https://docs.mbed.com/docs/arm-ipv66lowpan-stack/en/latest/08_API_events/index.html).
- mbed-tls - **Not protected**: function calls are safe from any thread as long as the objects they operate on are properly protected - see the [documentation](https://tls.mbed.org/kb/development/thread-safety-and-multi-threading).
- mbed client - **Thread safe**: public calls are protected by a mutex.
- BLE - **Not protected**: the expected use case for BLE is to run on one thread and serialize all events to that thread. This is analogous to the way Nanostack uses a thread. We provide a number of examples that showcase how to use BLE in a thread-safe way, including the Eddystone Service found [here](https://github.com/ARMmbed/ble-examples-morpheus/blob/mbed_cli_update/BLE_EddystoneService/source/main.cpp).

### Additional considerations when writing thread-safe code

Synchronization will not provide protection when deleting an object; when the object is deleted, the mutex protecting it is deleted as well. This means that when an object is deleted, you must make sure that all other threads are done using it.

You need to synchronize access to hardware from two objects using the same pins. For example, if two instances of Serial are created on the same pins, writing to both of the objects at the same time could cause instabilities.

## Considerations when porting

Porting new platforms to mbed OS 5 is nearly the same as it is in mbed 2. In general, drivers that operate below the C HAL layer don't need synchronization mechansims because this is already provided at a higher level. The only exceptions to this are the functions ``port_read``, ``port_write``, ``gpio_read`` and ``gpio_write``, which are expected to use processor-specific ``set`` and ``clear`` registers rather than performing a read-modify-write sequence. See an example of this [here](https://github.com/mbedmicro/mbed/blob/52e93aebd083b679a8fe7b0e47039f138fa8c224/hal/targets/hal/TARGET_Freescale/TARGET_KSDK2_MCUS/TARGET_K64F/drivers/fsl_gpio.h#L135).

## Further reading

For more information, see [the CMSIS-RTOS tutorial](http://www2.keil.com/mdk5/cmsis/rtx/).
