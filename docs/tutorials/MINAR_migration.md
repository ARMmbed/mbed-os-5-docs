<h2 id="minar-migration">Migrating from MINAR (Arm Mbed OS 3)</h2>

If you're looking to migrate your Arm Mbed application from Mbed OS 3 to Arm Mbed OS 5, one of the first things you're likely to notice is that [MINAR](https://github.com/ARMmbed/minar) (the event schduler in Mbed OS 3) does not exist in Mbed OS 5. This might be inconvenient, but there are different strategies that you can apply to port your Mbed OS 3 application to Mbed OS 5. This document presents some of these strategies from the MINAR perspective.

### Why isn't MINAR included in Mbed OS 5?

The answer to this question has to do with one of the fundamental differences between Mbed OS 3 and Mbed OS 5: the RTOS. Mbed OS 5 has [a built-in RTOS](https://github.com/ARMmbed/mbed-os/tree/master/rtos) that is enabled by default (your application's `main()` function executes in the context of an RTOS thread). The immediate benefit of using an RTOS is you can organize your program into parallel *threads* of execution, each with its own context. The RTOS will switch between these threads very quickly, so that they'll appear to execute in parallel (see [this article about round-robin scheduling](http://www.keil.com/support/man/docs/rlarm/rlarm_ar_rrobmt.htm) for more details). The part of the RTOS that switches between threads is called **scheduler**. There are other things that the scheduler takes care of:

- It keeps a list of **inactive threads**. These are threads that can't resume execution until a specific event happens (for example, data from an external peripheral becomes available, or a wait period has passed). Inactive threads are not scheduled for execution.
- It provides **timers**. Timers can be used to execute code periodically, or after a delay.
- When there are no active threads, it runs the **idle thread**. One common use for the idle thread is to put the MCU to sleep until an interrupt that can activate one of the threads occurs.

MINAR can take care of 2 and 3 above, but not 1, because MINAR doesn't have threads. This is an important difference between code that runs in an RTOS environment and code that runs in a simple, nonthreaded event scheduler. To illustrate the difference further, consider this simplified piece of code that declares a network socket and reads data from it:

```
Socket s;
char buffer[1024];

s.read(buffer, 1024);
printf("Read: %s\n", buffer);
```

If this code is executed in a system without an RTOS, the `read` call above has to wait in a busy waiting loop until data is available. While this busy waiting loop is executing, other code can't execute (with the possible exception of interrupt handlers). This wastes both processing cycles and power.

If this code is executed in a system with an RTOS, the `read` call will mark its calling thread as inactive, so the scheduler can switch to another thread (including the idle thread if there are no other active threads). When data becomes available, the thread will automatically be resumed, and will execute the `printf` call. This way, in a properly designed system with an RTOS, processing cycles and power are not wasted anymore. This looks like the perfect approach, but it introduces some problems:

- Each thread needs (at least) its own stack space, so applications running under an RTOS need more memory.
- The scheduler can preempt (interrupt) the running code at any time. This means that threads accessing shared data need to be **synchronized**. Thread synchronization is a complex topic, and reasoning about the behaviour of a multithreaded application can be quite difficult.

The MINAR approach sits somewhere between the two scenarios above. MINAR doesn't have threads, but it runs an infinite **event loop** that reads and dispatches **events** (code to be executed). Because it doesn't have threads, it requires a different style of programming, called "asynchronous programming". In short, that means that every blocking operation needs to provide a *completion callback*. In "asynchronous style", the above code would look like this (remember, we're simplifying things a lot):

```
Socket s;
char buffer[1024];

void read_done_cb() {
    printf("Read: %s\n", buffer);
}

// The 'read' operation will call 'read_done_cb' when data becomes available.
// This uses the MINAR event loop under the hood.
s.read(buffer, 1024, read_done_cb);
```

A MINAR application might use less memory than an RTOS one (because it doesn't have threads) and could be easier to understand in terms of synchronization, because MINAR doesn't preempt code. Unfortunately, this comes with its own set of problems:

- The code needs to be split into a completion function (such as `read_done_cb` above) whenever it hits a blocking operation. It can be difficult to understand and maintain code written in this manner.
- The asynchronous style of programming is relatively rare in the embedded programming world, but RTOS-based systems are quite common.
- The lack of preemption in MINAR can become problematic in some cases. For example, if a complex encryption function executes, it'll take a long time to run. During this time, other code in the system won't execute (with the possible exception of interrupt handlers). An RTOS would periodically preempt the thread running the encryption function, and give other threads in the system a chance to execute.

Because of the disadvantages above, and because the Mbed OS 5 RTOS covers a large part of the functionality present in MINAR, Mbed OS no longer uses MINAR. If you have been working with Mbed OS 3 and MINAR, we have created porting solutions for a smooth transition to Mbed OS 5. The next sections present these solutions.

### First things first: there's a "main" again

MINAR required that your application entry point be a function called `app_start`. In Mbed OS 5, this requirement doesn't exist. Your application entry point must be called `main`, as usual.

### Porting strategy 1: forget about asynchronous programming

If you don't like asynchronous programming, or if you wrote your code in asynchronous style just because you needed to use MINAR, you might want to forget about asynchronous programming completely and provide "regular" I/O functions (that is, functions that don't need completion callbacks). Your code will probably become simpler to understand and easier to maintain by doing this, but you might have to rewrite a large part of it. It's difficult to offer generic guidelines here; the way to change the code will depend a lot on the specific  application.

### Porting strategy 2: use the optional Mbed OS 5 event loop

To help ease porting MINAR applications, and to provide support for asynchronous style programming, Mbed OS 5 provides an optional event loop. See the main documentation for the [event loop](../reference/api-references.html#events/) for more information. In short, the Mbed OS 5 event loop implementation consists of an [EventQueue class](https://github.com/ARMmbed/mbed-os/blob/master/events/EventQueue.h) that implements the storage for the events and has a `dispatch` function. There are differences between MINAR and `EventQueue`:

- MINAR and the Mbed OS 5 event loop have incompatible APIs.
- Both MINAR and `EventQueue` work with *events* (objects that are placed in the event queue). However, the interface and implementations of events in MINAR and Mbed OS 5 are different, and that's also true for the APIs that use them. Look at [the Callback class](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_callback_3_01_r_07_a0_00_01_a1_00_01_a2_00_01_a3_00_01_a4_08_4.html), [the Event class](https://github.com/ARMmbed/mbed-os/blob/master/events/Event.h) and [the EventQueue class](https://github.com/ARMmbed/mbed-os/blob/master/events/EventQueue.h) for more details about the Mbed OS 5 implementation.
- In Mbed OS 3, the startup code automatically starts the event loop's `dispatch` function. In Mbed OS 5, the event loop is optional, so the programmer must initialize and start it manually. The event loop documentation has more information on this topic.
- MINAR runs on top of a hardware timer, but `EventQueue::dispatch` runs (typically) in its own RTOS thread.
- Mbed OS 5 can have as many event loops as needed, each running in its own thread.
- You can stop `EventQueue` if needed.

Even if you choose to use the Mbed OS 5 event loop, the RTOS is always present, so you need to consider all the RTOS-specific issues (such as synchronization).

If you want to keep the asynchronous aspect of your Mbed OS 3 application, the best way to proceed is to read the [documentation of the Mbed OS event loop](../reference/api-references.html#events) and rewrite your application using the new APIs. Here are some rough API compatibility guides:

- You can replace the MINAR function `postCallback` with `EventQueue::call`.
- You can replace the MINAR function `delay` with `EventQueue::call_in`.
- You can replace the MINAR function `period` with `EventQueue::call_every`.
- You can replace the MINAR function `cancelCallback` with `EventQueue::cancel`.

It should be clear by now that the above suggested replacements are **not** direct replacements: you can't simply change the name of the called function and expect the code to work because the APIs are not compatible. You need to understand how the event loop in Mbed OS 5 works first, then proceed to rewrite parts of your code, keeping the above suggestions in mind.

### Conclusion

Although it's possible to use asynchronous (event based) programming with Mbed OS 5, you might want to take advantage of the Mbed OS 5 RTOS instead. The RTOS will automatically preempt a thread that runs a blocking operation (for example a `read` operation on a socket), so you don't need a completion callback for the operation. If you give up on callbacks, you can write code that "flows" in a traditional, linear fashion. Generally speaking, this will make the code easier to understand and maintain.

If you still want or need to have event based code, take a look at [the EventQueue class](https://github.com/ARMmbed/mbed-os/blob/master/events/EventQueue.h), but keep in mind that even if you're using EventQueue, the RTOS is still there, so you'll have to think carefully about synchronizing access to your data.
