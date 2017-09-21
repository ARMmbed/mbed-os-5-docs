## MemoryPool

You can use the MemoryPool class to define and manage fixed-size memory pools.

### MemoryPool class reference

[![View code](https://www.mbed.com/embed/?type=library)](/docs/v5.4/mbed-os-api-doxy/classrtos_1_1_memory_pool.html)

### MemoryPool example

```
MemoryPool<message_t, 16> mpool;

message_t *message = mpool.alloc();

mpool.free(message);
```

### Queue and MemoryPool example

This example shows `Queue` and `MemoryPool` (see below) managing measurements.

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/rtos_queue/)](https://developer.mbed.org/teams/mbed_example/code/rtos_queue/file/0cb43a362538/main.cpp)
