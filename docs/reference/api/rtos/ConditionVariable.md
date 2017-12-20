## ConditionVariable

The ConditionVariable class provides a mechanism to safely wait for or signal state changes. A common scenario when writing multithreaded code is to protect shared resources with a mutex and then release that mutex to wait for a change of that data. If you do not do this carefully, this can lead to a race condition in the code. A condition variable provides a safe solution to this problem by handling the wait for a state change, along with releasing and acquiring the mutex automatically during this waiting period.

### ConditionVariable class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/v5.7/mbed-os-api-doxy/classrtos_1_1_condition_variable.html)

### ConditionVariable example

Below is an example of ConditionVariable usage, where one thread is generating events every 1s, and the second thread is waiting for the events and executing an action.

```
#include "mbed.h"

Mutex mutex;
ConditionVariable cond(mutex);

// These variables are protected by locking mutex
uint32_t count = 0;
bool done = false;

void worker_thread()
{
    mutex.lock();
    do {
        printf("Worker: Count %lu\r\n", count);

        // Wait for a condition to change
        cond.wait();

    } while (!done);
    printf("Worker: Exiting\r\n");
    mutex.unlock();
}

int main() {
    Thread thread;
    thread.start(worker_thread);

    for (int i = 0; i < 5; i++) {

        mutex.lock();
        // Change count and signal this
        count++;
        printf("Main: Set count to %lu\r\n", count);
        cond.notify_all();
        mutex.unlock();

        wait(1.0);
    }

    mutex.lock();
    // Change done and signal this
    done = true;
    printf("Main: Set done\r\n");
    cond.notify_all();
    mutex.unlock();

    thread.join();
}
```
