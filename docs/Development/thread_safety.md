#Thread Safety

The mbed library contains internal synchronization to provide various levels of thread safety.  This prevents race conditions and crashes due to concurrent access by multiple threads.  

##Levels of thread safety
1. Safe from thread and interrupt - Operation is done atomically or in a critical section.  The behavior is well defined when used from both interrupts and threads.
2. Safe from thread - Operation is protected by an RTOS primitive and can be used from multiple threads, but will cause problems if used from an interrupt.
3. Not thread safe - Operation does not protect against concurrent access and needs to be synchronized externally.  If called from multiple threads without synchronization the data being operated on can be corrupted.

Thread safety is built into both the standard library and the C++ API.  Calls to the standard library should be made only from thread context.  For details on the C++ API 

* Standard library - Safe for use only from threads.
* C++ API - Most drivers are safe for use from threads but not from interrupts.  Check the handbook page or doxygen for more specific details on the driver being used.    Below is a non-comprehensive list of the drivers which provide interrrupt safety in addition to thread safety.
** DigitialIn, DigitalOut, DigitalInOut
** InterruptIn
** PortIn, PortOut, PortInOut
** PwmOut
**Ticker, TimerEvent, Timeout
** Timer
* HAL C API - No synchronization provided.  Calls to this API must be protected by a critical section or a by an RTOS primitive such as a mutex.