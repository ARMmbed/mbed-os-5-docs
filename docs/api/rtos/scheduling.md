# Scheduling APIs

## RTOS APIs

The RTOS APIs handle creation and destruction of threads in Arm Mbed OS, as well as mechanisms for safe interthread communication. Threads are a core component of Mbed OS (even your `main` function starts in a thread of its own), so understanding how to work with them is an important part of developing applications for Mbed OS.

- [Thread](thread.html): The class that allows defining, creating and controlling parallel tasks.
- [ThisThread](thisthread.html): The class with which you can control the current thread.
- [Mutex](mutex.html): The class used to synchronize the execution of threads.
- [Semaphore](semaphore.html): The class that manages thread access to a pool of shared resources of a certain type.
- [Queue](queue.html): The class that allows you to queue pointers to data from producer threads to consumer threads.
- [MemoryPool](memorypool.html): This class that you can use to define and manage fixed-size memory pools
- [Mail](mail.html): The API that provides a queue combined with a memory pool for allocating messages.
- [EventFlags](eventflags.html): An event channel that provides a generic way of notifying other threads about conditions or events. You can call some EventFlags functions from ISR context, and each EventFlags object can support up to 31 flags.
- [ConditionVariable](conditionvariable.html): The ConditionVariable class provides a mechanism to safely wait for or signal a single state change. You cannot call ConditionVariable functions from ISR context.
- [Kernel](kernel-interface-functions.html): Kernel namespace implements functions to control or read RTOS information, such as tick count.

## Event handling APIs

If you are using the bare metal profile, the only APIs of the RTOS group you can use are those that do not rely on the RTX:

- [Event](event.html): The queue to store events, extract them and execute them later.
- [EventQueue](eventqueue.html): The class that provides a flexible queue for scheduling events.
- [UserAllocatedEvent](userallocatedevent.html): The class that provides APIs to create and configure static events

Note that you can also use these APIs while using the full, RTOS-based profile.
