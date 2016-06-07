# Thread Safety

The mbed library contains internal synchronization to provide various levels of thread safety.  This prevents race conditions and crashes due to concurrent access by multiple threads.  

## Synchronization levels

1. **Interrupt safe** - safe from thread and interrupt, operation is done atomically or in a critical section.  The behavior is well defined when used from both interrupts and threads.
2. **Thread safe** - safe from thread, operation is protected by an RTOS primitive and can be used from multiple threads, but will cause problems if used from an interrupt.
3. **Not protected** - Operation does not protect against concurrent access and needs to be synchronized externally. If called from multiple threads without synchronization the data being operated on can be corrupted.

Thread safety is built into both the standard library and the C++ API.  Calls to the standard library should be made only from thread context.

## Thread safety mechanism

### Critical section

Critical sections can be used to synchronize code used in both interrupts and threads.  Critical sections disable interrupts to provide uninterrupted access to a resource. A critical section must execute quickly, or it will cause system instability. Critical sections should be avoided when possible to avoid these undesirable side effects.

#### API

```
void core_util_critical_section_enter();
void core_util_critical_section_exit();
```

Note: Do not invoke any standard lib or RTOS functions within a critical section, it could result in a hard fault. Due to SVC calls that RTOS does. A critical section requires a code to be running in the privileged mode.

For more information see ``hal/api/critical.h``.

### Mutex, Semaphore

RTOS C++ API provides Mutex or Semaphores classes.

For more information see ``rtos/rtos/Mutex.h``, ``rtos/rtos/Semaphore.h``.

### Atomics

mbed provides atomic compare-and-swap, increment and decrement.

#### API
```
bool core_util_atomic_cas_u8(uint8_t *ptr, uint8_t *expectedCurrentValue, uint8_t desiredValue);
bool core_util_atomic_cas_u16(uint16_t *ptr, uint16_t *expectedCurrentValue, uint16_t desiredValue);
bool core_util_atomic_cas_u32(uint32_t *ptr, uint32_t *expectedCurrentValue, uint32_t desiredValue);
uint8_t core_util_atomic_incr_u8(uint8_t * valuePtr, uint8_t delta);
uint16_t core_util_atomic_incr_u16(uint16_t * valuePtr, uint16_t delta);
uint32_t core_util_atomic_incr_u32(uint32_t * valuePtr, uint32_t delta);
uint8_t core_util_atomic_decr_u8(uint8_t * valuePtr, uint8_t delta);
uint16_t core_util_atomic_decr_u16(uint16_t * valuePtr, uint16_t delta);
uint32_t core_util_atomic_decr_u32(uint32_t * valuePtr, uint32_t delta);
```

For more information see ``hal/api/critical.h``.

## Standard library

Safe for use only from threads. All supported toolchains but ``GCC_ARM``, ``uARM`` provide thread safety for their standard libs. To enable GCC_ARM to be thread safe, use ``-o thread_safety`` option for building, or use ``GCC`` toolchain which is thread-safe.

## Drivers

Most drivers are safe for use from threads but not from interrupts. Check the handbook page or doxygen for more specific details on the driver being used.

Below is a non-comprehensive list of the drivers which provide interrupt safety in addition to thread safety.

- DigitialIn, DigitalOut, DigitalInOut
- InterruptIn
- PortIn, PortOut, PortInOut
- PwmOut
- Ticker, TimerEvent, Timeout
- Timer
- rtc time

Unprotected drivers:

- SPISlave
- I2CSlave

## HAL C API

No synchronization provided. A caller must protect invokation of this API by a critical section or a by an RTOS primitive such as a mutex.
