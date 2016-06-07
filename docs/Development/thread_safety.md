# Thread Safety

The mbed library contains internal synchronization to provide various levels of thread safety.  This prevents race conditions and crashes due to concurrent access by multiple threads.  

## Synchronization levels

There are three levels of synchronization which are documented on a per function basis.  These are:

1. **Interrupt safe** - safe from thread and interrupt, operation is done atomically or in a critical section.  The behavior is well defined when used from both interrupts and threads.
2. **Thread safe** - safe from thread, operation is protected by an RTOS primitive and can be used from multiple threads, but will cause problems if used from an interrupt.
3. **Not protected** - Operation does not protect against concurrent access and needs to be synchronized externally. If called from multiple threads without synchronization the data being operated on can be corrupted.

## Standard libraries

All supported toolchains are thread safe when using the full version of their standard library.  In addition, GCC and ARMCC provide smaller variants of their libraries. These smaller versions are not thread safe and projects using them should use one and only one thread.  A summary of the toolchains can be seen below.

Multi-threading support:

* GCC Newlib - toolchian **GCC**
* IAR Standard Library - toolchain **IAR**
* ARMCC Standard Library - toolchain **ARM**

Single thread use only:

* Newlib Nano - toolchain **GCC_ARM**
* Micro ARMCC - toolchain **uARM**

## Drivers

Most drivers **Thread Safe** but not safe for use in interrupts.  Some notable differences can be seen below.   Check the handbook page or doxygen for more specific details on the driver being used.

Drivers which are **Interrupt Safe**:

- DigitialIn, DigitalOut, DigitalInOut
- InterruptIn
- PortIn, PortOut, PortInOut
- PwmOut
- Ticker, TimerEvent, Timeout
- Timer
- rtc time

Drivers which are **Not Protected**

- SPISlave
- I2CSlave

## HAL C API

No synchronization provided. A caller must protect invocation of this API by a critical section or a by an RTOS primitive such as a mutex.

## Synchronization  mechanisms

### Mutex

RTOS C++ API provides the Mutex class which is used to make drivers **Thread Safe**.

For more information see ``rtos/rtos/Mutex.h``.

### Atomics

Atomic operations are provided by mbed which can be used to make code **Interrupt Safe**.  This is the preferred method of synchronization if code needs to be used both from threads and interrupts, since there is very low overhead and no latency decrease.

For more information see ``hal/api/critical.h``.

### Critical section

Critical sections can be used to make code **Interrupt Safe**.  Critical sections disable interrupts to provide uninterrupted access to a resource. A critical section must execute quickly, or it will cause system instability. Critical sections should be avoided when possible to avoid these undesirable side effects.

Warning: Do not perform time consuming operations inside critical sections.  This will negatively effect the timing of the entire system since all interrupts are disabled during critical sections.

Warning: Do not invoke any standard lib or RTOS functions within a critical section, it could result in a hard fault. Due to SVC calls that RTOS does. A critical section requires a code to be running in the privileged mode.

For more information see ``hal/api/critical.h``.
