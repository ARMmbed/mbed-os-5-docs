<h1 id="configuration-rtos">RTOS</h1>

**Thread memory model**

All threads in Mbed OS share a global heap. By default, Mbed OS dynamically allocates memory for thread stacks from the global heap. User spawned thread stacks can be allocated from other memory areas. The size of the global heap depends on the compiler; for the GCC and ARM compilers, the heap size is dynamic based on RAM usage.

**Default threads**

By default, there are four threads running after boot: the ISR/scheduler thread, the idle thread, the timer thread and the main application thread. Combined, the idle thread, timer thread and ISR/scheduler thread consume 2 kilobytes of RAM. The user cannot modify these. You can expand or reduce the size of the main application thread stack by using the Mbed configuration system.


This is the complete list of RTOS configuration parameters. To view all configuration parameters, run the `--config -v` command. Please see [the configuration system documentation](../program-setup/advanced-configuration.html) for details on how you may use or override these settings.

## RTOS configuration parameters

```
Configuration parameters
------------------------
Name: rtos-api.present
    Defined by: library:rtos-api
    Macro name: MBED_CONF_RTOS_API_PRESENT
    Value: 1 (set by library:rtos-api)
Name: rtos.evflags-num
    Description: Maximum number of CMSIS-RTOSv2 object-pool event flag objects that can be active at the same time
    Defined by: library:rtos
    No value set
Name: rtos.idle-thread-stack-size
    Description: The size of the idle thread's stack
    Defined by: library:rtos
    Macro name: MBED_CONF_RTOS_IDLE_THREAD_STACK_SIZE
    Value: 512 (set by library:rtos)
Name: rtos.idle-thread-stack-size-debug-extra
    Description: Additional size to add to the idle thread when code compilation optimization is disabled
    Defined by: library:rtos
    Macro name: MBED_CONF_RTOS_IDLE_THREAD_STACK_SIZE_DEBUG_EXTRA
    Value: 128 (set by library:rtos[STM])
Name: rtos.idle-thread-stack-size-tickless-extra
    Description: Additional size to add to the idle thread when a specific target or application implementation requires it or in case tickless is enabled and LPTICKER_DELAY_TICKS is used
    Defined by: library:rtos
    Macro name: MBED_CONF_RTOS_IDLE_THREAD_STACK_SIZE_TICKLESS_EXTRA
    Value: 256 (set by library:rtos)
Name: rtos.main-thread-stack-size
    Description: The size of the main thread's stack
    Defined by: library:rtos
    Macro name: MBED_CONF_RTOS_MAIN_THREAD_STACK_SIZE
    Value: 4096 (set by library:rtos)
Name: rtos.msgqueue-data-size
    Description: The total memory available for all CMSIS-RTOSv2 object-pool message queues combined
    Defined by: library:rtos
    No value set
Name: rtos.msgqueue-num
    Description: Maximum number of CMSIS-RTOSv2 object-pool message queues that can be active at the same time
    Defined by: library:rtos
    No value set
Name: rtos.mutex-num
    Description: Maximum number of CMSIS-RTOSv2 object-pool mutexes that can be active at the same time
    Defined by: library:rtos
    No value set
Name: rtos.present
    Defined by: library:rtos
    Macro name: MBED_CONF_RTOS_PRESENT
    Value: 1 (set by library:rtos)
Name: rtos.semaphore-num
    Description: Maximum number of CMSIS-RTOSv2 object-pool semaphores that can be active at the same time
    Defined by: library:rtos
    No value set
Name: rtos.thread-num
    Description: Maximum number of CMSIS-RTOSv2 object-pool threads that can be active at the same time
    Defined by: library:rtos
    No value set
Name: rtos.thread-stack-size
    Description: The default stack size of new threads
    Defined by: library:rtos
    Macro name: MBED_CONF_RTOS_THREAD_STACK_SIZE
    Value: 4096 (set by library:rtos)
Name: rtos.thread-user-stack-size
    Description: The total memory available for all CMSIS-RTOSv2 object-pool thread stacks combined
    Defined by: library:rtos
    No value set
Name: rtos.timer-num
    Description: Maximum number of CMSIS-RTOSv2 object-pool timers that can be active at the same time
    Defined by: library:rtos
    No value set
Name: rtos.timer-thread-stack-size
    Description: The size of the timer thread's stack
    Defined by: library:rtos
    Macro name: MBED_CONF_RTOS_TIMER_THREAD_STACK_SIZE
    Value: 768 (set by library:rtos)
```

## EventQueue configuration parameters

```
Configuration parameters
------------------------
Name: events.present
    Defined by: library:events
    Macro name: MBED_CONF_EVENTS_PRESENT
    Value: 1 (set by library:events)
Name: events.shared-dispatch-from-application
    Description: No thread created for shared event queue - application will call dispatch from another thread (eg dispatch_forever at end of main)
    Defined by: library:events
    No value set
Name: events.shared-eventsize
    Description: Event buffer size (bytes) for shared event queue
    Defined by: library:events
    Macro name: MBED_CONF_EVENTS_SHARED_EVENTSIZE
    Value: 768 (set by library:events)
Name: events.shared-highprio-eventsize
    Description: Event buffer size (bytes) for shared high-priority event queue
    Defined by: library:events
    Macro name: MBED_CONF_EVENTS_SHARED_HIGHPRIO_EVENTSIZE
    Value: 256 (set by library:events)
Name: events.shared-highprio-stacksize
    Description: Stack size (bytes) for shared high-priority event queue thread
    Defined by: library:events
    Macro name: MBED_CONF_EVENTS_SHARED_HIGHPRIO_STACKSIZE
    Value: 1024 (set by library:events)
Name: events.shared-stacksize
    Description: Stack size (bytes) for shared event queue thread
    Defined by: library:events
    Macro name: MBED_CONF_EVENTS_SHARED_STACKSIZE
    Value: 2048 (set by library:events)
Name: events.use-lowpower-timer-ticker
    Description: Enable use of low power timer and ticker classes in non-RTOS builds. May reduce the accuracy of the event queue. In RTOS builds, the RTOS tick count is used, and this configuration option has no effect.
    Defined by: library:events
    No value set
```
