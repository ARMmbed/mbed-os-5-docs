# Memory model

This is a basic overview of the memory model.

Each thread of execution in the RTOS has a separate stack. When you use the RTOS, before explicitly initializing any additional thread, you will have four separate stacks:

* The stack of the Main Thread (executing the main function).
* The Idle Thread executed each time all the other threads are waiting for external or scheduled events. This is particularly useful for implementing energy saving strategies (like sleep).
* The Timer Thread that executes all the time-scheduled tasks (periodic and non-periodic).
* The stack of OS Scheduler itself (also used by the ISRs).

Stack checking is turned on for all threads and the kernel will error if an overflow condition is detected.

```
+-------------------+   Last Address of RAM
| Scheduler Stack   |
+-------------------+
|                   |   RAM
|                   |
|         ^         |
|         |         |
|    Heap Cont..    |
+-------------------+
| app thread n      |
|-------------------|
| app thread 2      |
|-------------------|
| app thread 1      |
|-------------------|
|         ^         |
|         |         |
|       Heap        |
+-------------------+
| ZI                |
+-------------------+
| ZI: OS drv stack  |
+-------------------+
| ZI: app thread 3  |
+-------------------+
| ZI: Idle Stack    |
+-------------------+
| ZI: Timer Stack   |
+-------------------+
| ZI: Main Stack    |
+-------------------+
| RW                |  
+===================+   First Address of RAM
|                   |
|                   |   Flash

```
