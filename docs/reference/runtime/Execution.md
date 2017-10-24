## Execution

### Threads

Your application (`main` function) will start execution in the main thread, but it's not the only thread running in Mbed OS. There's a number of live system threads at any given time. They should be transparent from the user's point of view for most use cases. All threads that exist in the system by default:
* main - default thread that executes application's `main` function.
* idle - thread that's run by the scheduler when there's no other activity in the system (e.g. all other threads are waiting for some event). It's used to make sure the board is not burning empty processor cycles, but is put to sleep for as long as possible.
* timer - thread for handling system and user timer objects.

On top of the standard system threads, some drivers may utilize additional threads. User can create threads using [Thread class](docs/v5.6/reference/thread.html).

<span class="notes">**Note:** The main thread has 4kB of stack space by default, it can be configured by the application in mbed_app.json by defining MAIN_STACK_SIZE parameter.</span>

### Modes

There are two modes Mbed OS will execute in:
* Thread mode - default application mode, all user threads are executed in this mode. Using dedicated thread specific stack memory.
* Handler mode - interrupt mode, system code and interrupt handlers are executed in this mode. Using static system ISR stack memory.

#### Handler mode

All the ISR handlers will execute in this mode. You can use the same RTOS API in ISR handlers. The important difference between the modes is, code written for handler mode can't wait, it should execute as fast as possible and return to the thread mode. Therefore:

* You cannot use `Mutex`.
* Wait in ISR is not allowed; all the timeouts in method parameters have to be set to 0.

**ISR example**

This example uses a message from the queue to trigger an interrupt.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/rtos_isr/)](https://os.mbed.com/teams/mbed_example/code/rtos_isr/file/40078e697304/main.cpp)
