# Thread

<span class="images">![](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/classrtos_1_1_thread.png)<span>Thread class hierarchy</span></span>

The Thread class allows defining, creating and controlling parallel tasks.

<span class="notes">**Note:** The function `main` is a special thread function that is started at system initialization.</span>

## Memory considerations

All the internal thread data structures are part of the C++ class, but by default, the thread stack is allocated on the heap. Memory is allocated at the run time during the call to `start` method. If you don't want to use dynamic memory, you can provide your own static memory using the constructor parameters.

The default stack size is 4K. However, the application can override it by using the configuration system and setting the `THREAD_STACK_SIZE` option to the required size in `mbed_app.json`. For details, please see the [configuration documentation](../apis/scheduling-options-and-config.html).

<span class="notes">**Note:** The main thread stack size is specified as `rtos.main-thread-stack-size` in the configuration .json file. That defines the main thread for `mbed_rtos_start` in `mbed_rtos_rtx.c`.</span>

## Thread class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/classrtos_1_1_thread.html)

```C
/// Priority values.
typedef enum {
  osPriorityNone          =  0,         ///< No priority (not initialized).
  osPriorityIdle          =  1,         ///< Reserved for Idle thread.
  osPriorityLow           =  8,         ///< Priority: low
  osPriorityLow1          =  8+1,       ///< Priority: low + 1
  osPriorityLow2          =  8+2,       ///< Priority: low + 2
  osPriorityLow3          =  8+3,       ///< Priority: low + 3
  osPriorityLow4          =  8+4,       ///< Priority: low + 4
  osPriorityLow5          =  8+5,       ///< Priority: low + 5
  osPriorityLow6          =  8+6,       ///< Priority: low + 6
  osPriorityLow7          =  8+7,       ///< Priority: low + 7
  osPriorityBelowNormal   = 16,         ///< Priority: below normal
  osPriorityBelowNormal1  = 16+1,       ///< Priority: below normal + 1
  osPriorityBelowNormal2  = 16+2,       ///< Priority: below normal + 2
  osPriorityBelowNormal3  = 16+3,       ///< Priority: below normal + 3
  osPriorityBelowNormal4  = 16+4,       ///< Priority: below normal + 4
  osPriorityBelowNormal5  = 16+5,       ///< Priority: below normal + 5
  osPriorityBelowNormal6  = 16+6,       ///< Priority: below normal + 6
  osPriorityBelowNormal7  = 16+7,       ///< Priority: below normal + 7
  osPriorityNormal        = 24,         ///< Priority: normal
  osPriorityNormal1       = 24+1,       ///< Priority: normal + 1
  osPriorityNormal2       = 24+2,       ///< Priority: normal + 2
  osPriorityNormal3       = 24+3,       ///< Priority: normal + 3
  osPriorityNormal4       = 24+4,       ///< Priority: normal + 4
  osPriorityNormal5       = 24+5,       ///< Priority: normal + 5
  osPriorityNormal6       = 24+6,       ///< Priority: normal + 6
  osPriorityNormal7       = 24+7,       ///< Priority: normal + 7
  osPriorityAboveNormal   = 32,         ///< Priority: above normal
  osPriorityAboveNormal1  = 32+1,       ///< Priority: above normal + 1
  osPriorityAboveNormal2  = 32+2,       ///< Priority: above normal + 2
  osPriorityAboveNormal3  = 32+3,       ///< Priority: above normal + 3
  osPriorityAboveNormal4  = 32+4,       ///< Priority: above normal + 4
  osPriorityAboveNormal5  = 32+5,       ///< Priority: above normal + 5
  osPriorityAboveNormal6  = 32+6,       ///< Priority: above normal + 6
  osPriorityAboveNormal7  = 32+7,       ///< Priority: above normal + 7
  osPriorityHigh          = 40,         ///< Priority: high
  osPriorityHigh1         = 40+1,       ///< Priority: high + 1
  osPriorityHigh2         = 40+2,       ///< Priority: high + 2
  osPriorityHigh3         = 40+3,       ///< Priority: high + 3
  osPriorityHigh4         = 40+4,       ///< Priority: high + 4
  osPriorityHigh5         = 40+5,       ///< Priority: high + 5
  osPriorityHigh6         = 40+6,       ///< Priority: high + 6
  osPriorityHigh7         = 40+7,       ///< Priority: high + 7
  osPriorityRealtime      = 48,         ///< Priority: realtime
  osPriorityRealtime1     = 48+1,       ///< Priority: realtime + 1
  osPriorityRealtime2     = 48+2,       ///< Priority: realtime + 2
  osPriorityRealtime3     = 48+3,       ///< Priority: realtime + 3
  osPriorityRealtime4     = 48+4,       ///< Priority: realtime + 4
  osPriorityRealtime5     = 48+5,       ///< Priority: realtime + 5
  osPriorityRealtime6     = 48+6,       ///< Priority: realtime + 6
  osPriorityRealtime7     = 48+7,       ///< Priority: realtime + 7
  osPriorityISR           = 56,         ///< Reserved for ISR deferred thread.
  osPriorityError         = -1,         ///< System cannot determine priority or illegal priority.
  osPriorityReserved      = 0x7FFFFFFF  ///< Prevents enum down-size compiler optimization.
} osPriority_t;
```

## Thread example

The code below uses two separate threads to blink two LEDs. The first thread is automatically created and executes the `main` function; the second thread is created explicitly inside `main`.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Basic/tree/v6.0)](https://github.com/ARMmbed/mbed-os-snippet-Basic/blob/v6.0/main.cpp)

## Thread example with callbacks

The Callback API provides a convenient way to pass arguments to spawned threads.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Threading_with_callback/tree/v6.0)](https://github.com/ARMmbed/mbed-os-snippet-Threading_with_callback/blob/v6.0/main.cpp)

## Debugging tips

When debugging threads, check the full RTX state (ready, blocked and so on) for a deadlock (two things waiting for each other) or a missed signal leading to an event machine stall. You can confirm a deadlock if you see two threads in the "blocked" state each waiting for a resource that the other is supposed to signal.

To reduce deadlocks, proactively code in a safe way by never claiming a high-level mutex while holding a low-level one.

## Related content

- [Application flow control tutorial](../apis/scheduling-tutorials.html).
- [ThisThread API reference](../apis/thisthread.html).
