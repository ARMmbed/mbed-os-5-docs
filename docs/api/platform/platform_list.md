# Platform APIs

## Time

- [RTC](../apis/time-apis.html): Mechanism to set the current time of the hardware Real-Time Clock (RTC).
- [Ticker](../apis/ticker.html): Set up a recurring interrupt.
- [Time](../apis/time.html): A group of functions in the standard library of the C programming language implementing date and time manipulation operations.
- [Timer](../apis/timer.html): Create, start, stop and read a stopwatch-like timer for measuring precise times.
- [Wait](../apis/wait.html): `wait_us` and `wait_ns` functions that provide precise wait capabilities.

## Power

- [DeepSleepLock](../apis/power-apis.html): Provides an RAII object for disabling sleep.
- [LowPowerTicker](../apis/lowpowerticker.html): Similar to the Ticker class but operates in deep sleep mode and has less resolution.
- [LowPowerTimeout](../apis/lowpowertimeout.html): Set up an interrupt to call a function after a specified delay.
- [LowPowerTimer](../apis/lowpowertimer.html): Similar to the Timer class but operates in deep sleep mode.
- [Power management (sleep)](../apis/power-management-sleep.html): Invokes sleep manager, which selects the most appropriate sleep mode.

## Memory

- [mbed_mem_trace (Memory tracing)](../apis/memory-apis.html): A set of functions that you can use to study the runtime memory allocation pattern of your software.
- [mpug_mgmt (MPU management)](../apis/mpu-management.html): Functions that allow libraries and applications to turn off the automatic memory protections of Mbed OS.
- [MemoryPool](../apis/memorypool.html): Define and manage fixed-size memory pools.
- [mbed_stats (Mbed statistics)](../apis/mbed-statistics.html): Set of functions that capture the memory and thread statistics at runtime.

## Other Platform APIs

- [Assert](../apis/other-platform-apis.html): A set of macros that evaluate an expression and print an error message if the expression evaluates to false.
- [ATCmdParser](../apis/atcmdparser.html): Parser and serializer for AT commands, which communicate with devices such as a modem, phone or Wi-Fi module.
- [Callback](../apis/callback.html): A user provided function that a user may pass to an API. The callback allows the API to execute the user’s code in its own context.
- [CircularBuffer](../apis/circularbuffer.html): Push and pop data from a buffer.
- [CriticalSectionLock](../apis/criticalsectionlock.html): Access a resource without interruption.
- [Debug](../apis/debug.html): Set of functions that you can use to output debug messages to STDIO at runtime.
- [Error handling](../apis/error-handling.html): A platform service that provides error status definitions and APIs for error construction, reporting and retrieving previously reported errors.
- [FileHandle](../apis/filehandle.html): An abstract class representing a device that supports file-like operations, such as read and write.
- [NonCopyable](../apis/noncopyable.html): Inherit from this class whenever another class is a resource or owns a resource (lock/hardware/file) that should or could not be copied.
- [PlatformMutex](../apis/platformmutex.html): Synchronize the execution of threads for drivers.
- [Poll](../apis/poll.html): A set of functions that perform timed waits on one or more file handles.
- [ScopedRamExecutionLock](../apis/scopedramexecutionlock.html): Enable execution from RAM.
- [ScopedRomWriteLock](../apis/scopedromwritelock.html): Enable writing to ROM.
- [SharedPtr (Shared pointer)](../apis/shared-pointer.html): A "smart" pointer that retains ownership of an object by using reference counting across all smart pointers referencing that object.
- [Span](../apis/span.html): A nonowning view to a sequence of contiguous elements.
