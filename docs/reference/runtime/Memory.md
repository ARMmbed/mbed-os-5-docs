## Memory

This is a basic overview of the memory model in Mbed OS.

```
+---------------------+   Last Address of RAM
| Scheduler/ISR Stack |
+---------------------+
|          ^          |
|          |          |
|                     |
|      Heap Cont.     |
|---------------------|
| User thread n stack |
|---------------------|
| User thread 2 stack |
|---------------------|
| User thread 1 stack |
|---------------------|
|          ^          |
|          |          |
|                     |
|        Heap         |
+---------------------+
|                     |
| ZI: Global data     |
|                     |
+---------------------+
| ZI: Idle Stack      |
+---------------------+
| ZI: Timer Stack     |
+---------------------+
| ZI: Main Stack      |
+---------------------+
|                     |
| ZI: Global data     |
|                     |
+---------------------+
| RW: Vector Table    |
+=====================+   First Address of RAM
|                     |   Last address of flash
|                     |
|     Application     |
|                     |
|                     |
+---------------------+
|                     |
| Optional bootloader |
|                     |
+---------------------+   First address of flash

```

There are, at least, two kinds of memory in the system: flash and RAM.

### RAM

Inside RAM we can distinguish two logical types: static and dynamic memory. Each of them is used in different ways:
* Static (zero initialized)
  * Vector table
  * Global data
  * Static data
  * Stacks for default threads (main, timer, idle, scheduler/ISR)
* Dynamic
  * Heap (dynamic data)
  * Stacks for user threads. Mbed OS will dynamically allocate memory on heap for user thread's stacks.

Stack checking is turned on for all threads, and the kernel will error if an overflow condition is detected.

### Flash

Flash is a read only memory (ROM) that contains:
* Application code
* Application data
* Optional bootloader
