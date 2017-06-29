## Task management APIs

The task management APIs handle creation and destruction of threads in mbed OS 5, as well as mechanisms for safe interthread communication. Threads are a core component of mbed OS 5 (even your `main` function starts in a thread of its own), so understanding how to work with them is an important part of developing applications for mbed OS 5. Pay particular attention to the [interrupt service routines](rtos.md#interrupt-service-routines) section, which contains important information about how the task management APIs can be used from an interrupt handler.

* [RTOS](#rtos-overview): The CMSIS-RTOS core.
* [Event Loop](#the-event-loop): The queue to store events, extract them and excute them later.
* [Ticker](Ticker.md): Set up a recurring interrupt.
* [Time](Time.md): The C date and time functions.
* [Timeout](TimeOut.md): Raise interrupt after certain time.
* [Timer](Timer.md): Measuring small times.
* [Wait](wait.md): NOP-type wait capabilities.

### Task management methods

[A document comparing ticker, time, timeout, wait and others.]
