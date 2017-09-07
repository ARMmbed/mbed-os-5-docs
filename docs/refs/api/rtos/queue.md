#### Queue and MemoryPool

##### Queue

A [`Queue`](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classrtos_1_1Queue.html) allows you to queue pointers to data from producer threads to consumer threads.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/queue.png)</span>

##### Queue class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classrtos_1_1Queue.html)

##### Queue class example

>>> c
```
Queue<message_t, 32> queue;

message_t *message;

queue.put(message);

osEvent evt = queue.get();
if (evt.status == osEventMessage) {
    message_t *message = (message_t*)evt.value.p;
```
>>>

##### MemoryPool

You can use the [MemoryPool](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classrtos_1_1MemoryPool.html) class to define and manage fixed-size memory pools.

##### MemoryPool class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classrtos_1_1MemoryPool.html)

##### MemoryPool class example

>>> c
```
MemoryPool<message_t, 16> mpool;

message_t *message = mpool.alloc();

mpool.free(message);
```
>>>

##### Queue and MemoryPool example

This example shows `Queue` and `MemoryPool` (see below) managing measurements.

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/rtos_queue/)](https://developer.mbed.org/teams/mbed_example/code/rtos_queue/file/0cb43a362538/main.cpp)
