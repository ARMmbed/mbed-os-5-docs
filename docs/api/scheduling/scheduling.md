# Scheduling APIs

## RTOS APIs

The RTOS APIs handle creation and destruction of threads in Arm Mbed OS, as well as mechanisms for safe interthread communication. Threads are a core component of Mbed OS (even your `main` function starts in a thread of its own), so understanding how to work with them is an important part of developing applications for Mbed OS.

- [ConditionVariable](../apis/rtos-apis.html): The ConditionVariable class provides a mechanism to safely wait for or signal a single state change. You cannot call ConditionVariable functions from ISR context.
- [EventFlags](../apis/eventflags.html): An event channel that provides a generic way of notifying other threads about conditions or events. You can call some EventFlags functions from ISR context, and each EventFlags object can support up to 31 flags.
- [IdleLoop](../apis/idle-loop.html): Background system thread, executed when no other threads are ready to run.
- [Kernel interface functions](../apis/kernel-interface-functions.html): Kernel namespace implements functions to control or read RTOS information, such as tick count.
- [Mail](../apis/mail.html): The API that provides a queue combined with a memory pool for allocating messages.
- [Mutex](../apis/mutex.html): The class used to synchronize the execution of threads.
- [Queue](../apis/queue.html): The class that allows you to queue pointers to data from producer threads to consumer threads.
- [Semaphore](../apis/semaphore.html): The class that manages thread access to a pool of shared resources of a certain type.
- [ThisThread](../apis/thisthread.html): The class with which you can control the current thread.
- [Thread](../apis/thread.html): The class that allows defining, creating and controlling parallel tasks.

## Event handling APIs

If you are using the bare metal profile, the only APIs of the RTOS group you can use are those that do not rely on the RTX:

- [Event](../apis/event-handling-apis.html): The queue to store events, extract them and execute them later.
- [EventQueue](../apis/eventqueue.html): The class that provides a flexible queue for scheduling events.
- [UserAllocatedEvent](../apis/userallocatedevent.html): The class that provides APIs to create and configure static events

Note that you can also use these APIs while using the full, RTOS-based profile.
